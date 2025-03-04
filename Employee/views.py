from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Employee.models import Employee


def index(request):
    employee_name=request.GET.get('name','')
    employee_designation=request.GET.get('designation','')
    employee_experience=request.GET.get('experience','')
    

    employee_list_all = Employee.objects.all()
    employee_list = Employee.objects.all()

    if employee_name:
        employee_list=employee_list.filter(name__icontains=employee_name)
    if employee_designation:
        employee_list=employee_list.filter(designation__icontains=employee_designation).order_by('designation').distinct('designation')
    if employee_experience:
        employee_list=employee_list.filter(experience=employee_experience)
    
    if employee_list.exists():
        template = loader.get_template("index.html")
        context = {
        "employee_list": employee_list,
        "employee_list_all": employee_list_all,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("No matching employees",status=404)
    


def detail(request,employee_id):
    if Employee.objects.filter(id=employee_id).exists():
        employee=Employee.objects.get(id=employee_id)
        template = loader.get_template("profile.html")
        context={
            "employee":employee
        }       
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse('Does not exists') 



    
# def detail(request, employee_id):   
#     if Employee.objects.filter(id=employee_id).exists(): 
#         emp=Employee.objects.get(id=employee_id)
#         response='Employee details:%s' % emp.name,', salary:%s' %emp.salary,' , designation:%s'%emp.designation
#         return HttpResponse(response)
#     else:
#         return HttpResponse('Does not exists')   
    



    







































    
# def index(request):
#     employee_list = Employee.objects.all()
#     template = loader.get_template("index.html")
#     context = {
#         "employee_list": employee_list,
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, employee_id):   
#     if Employee.objects.filter(id=employee_id).exists(): 
#         # emp_name=Employee.objects.filter(id=employee_id).values('name')[0]['name']
#         emp=Employee.objects.get(id=employee_id)
#         response='Employee details:%s' % emp.name,', salary:%s' %emp.salary,' , designation:%s'%emp.designation
#         return HttpResponse(response)
#     else:
#         return HttpResponse('Does not exists')





