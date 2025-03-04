from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from students.models import Student,Result,Sem
from django.db.models import Sum,Count
from django.db.models import ExpressionWrapper, FloatField

from .forms import ResultForm

def form(request):
    student_results=None
    if request.method=="POST":
        form = ResultForm(request.POST) #binding resultform with user inputed data so we can check for validation
        if form.is_valid():
            usn=form.cleaned_data['USN']
            sem=form.cleaned_data['SEMESTER']
            
            student_results=Result.objects.filter(student__usn=usn,semester__semester_number=sem).select_related('subject')
    
            total_marks=student_results.aggregate(Sum('marks'))['marks__sum']
            subject_count=student_results.count()
            
            if subject_count>0:
             percentage=total_marks/subject_count 
            else:
                percentage=0
          
            if not student_results.exists():
                student_results=None
            return render(request,'form_result.html',{
                    'usn':usn,
                    'sem':sem,
                    'student_results':student_results,
                    'percentage':round(percentage,2)

                })
    else:
        form=ResultForm()
    return render(request,'form.html',{'form':form})



def dropdown(request):
    USN=request.GET.get('usn',)
    SEMESTER=request.GET.get('sem',)
    
    student_list_all=Result.objects.order_by('student__usn').distinct('student__usn')
    sem_list=Sem.objects.all()
    student_list=Result.objects.all()

    student_results=Result.objects.filter(student__usn=USN,semester__semester_number=SEMESTER).select_related('subject')
    
    total_marks=student_results.aggregate(Sum('marks'))['marks__sum']
    subject_count=student_results.count()
            
    if subject_count>0:
        percentage=total_marks/subject_count 
    else:
        percentage=0

    if USN:
        student_list=student_list.filter(student__usn__icontains=USN)
    if SEMESTER:
        student_list=student_list.filter(semester__semester_number=SEMESTER)
    
    

    if student_list.exists():
        template = loader.get_template("student_dropdown.html")
        context = {
         "student_list_all": student_list_all,   
        "student_list": student_list,
        "sem_list":sem_list,
        'percentage':round(percentage,2)

        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("No matching students",status=404)

        




        
        
    















# def index(request):
#     student_list=Student.objects.all()
#     template = loader.get_template("student.html")
#     context = {
#         "student_list": student_list,
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     student_usn=request.GET.get('usn','')
#     student_sem=request.GET.get('sem','')

#     sem_list=Sem.objects.all()
#     student_list_all=Student.objects.all()
#     student_list=Student.objects.all()
    
#     if student_usn:
#         student_list=student_list.filter(usn__icontains=student_usn)


#     template = loader.get_template("student.html")
#     context = {
#         "sem_list":sem_list,
#         "student_list_all":student_list_all,
#         "student_list":student_list,
        
#     }
#     return HttpResponse(template.render(context, request))




# def detail(request, student_id):   
#     if Student.objects.filter(id=student_id).exists(): 
#         result_list=Student.objects.filter(id=student_id).annotate(t_percentage=ExpressionWrapper((Sum('result__marks') / Count('result__subject')),output_field=FloatField())).values('result__semester','t_percentage')
#         template = loader.get_template("results.html")
#         context = {
#         "result_list": result_list,
#         }

#         return HttpResponse(template.render(context, request))

#     else:
#         return HttpResponse('Does not exists')



