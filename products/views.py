from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from products.models import Product,Category


from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


# def index(request):
	
# 	category_list=Category.objects.all()
	

# 	p = Paginator(category_list, 3) # creating a paginator object
# 	# getting the desired page number from url
# 	page_number = request.GET.get('page',1)
# 	page_range = p.get_elided_page_range(number=page_number)
# 	try:
# 		page_obj = p.get_page(page_number) # returns the desired page object
# 	except PageNotAnInteger:
# 		# if page_number is not an integer then assign the first page
# 		page_obj = p.page(1)
# 	except EmptyPage:
# 		# if page is empty then return last page
# 		page_obj = p.page(p.num_pages)
# 	context = {
# 		'page_obj': page_obj,
		
		
# 		}
# 	# sending the page object to index.html
	# return render(request, 'products_list.html', context)


def index(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', '')
 
    if selected_category:
        products = Product.objects.filter(category__name=selected_category)  # Filter by category
    else:
        products = Product.objects.all()  # Show all products if no category is selected
 
    # Pagination: 3 products per page
    paginator = Paginator(products, 3)
    page_number = request.GET.get('page', 1)
    page_range = paginator.get_elided_page_range(number=page_number)
 
    try:
        page_obj = paginator.get_page(page_number)
    except:
        page_obj = paginator.get_page(1)  # Default to first page if error
 
    context = {
        'categories': categories,
        'selected_category': selected_category,
        'page_obj': page_obj,
        'page_range': page_range,
    }
    return render(request, 'products_list.html', context)





    
# def index(request):
#     product_list = Product.objects.all()
#     template = loader.get_template("products.html")
#     context = {
#         "product_list": product_list,
#     }
#     return HttpResponse(template.render(context, request))


# def detail(request, product_id):   
#     if Product.objects.filter(id=product_id).exists(): 
#         product=Product.objects.get(id=product_id)
#         response='Product details:%s' % product.name,', price:%s' %product.price,' , rating:%s' %product.rating, ', brand:%s '%product.brand.name
#         return HttpResponse(response)
#     else:
#         return HttpResponse('Does not exists')



    
# def category(request,category_id):
#     parent_cat= Category.objects.get(id=category_id)
#     category_list=Category.objects.all()
#     sub_categories=[]
#     for category in category_list:
#         if category.parent_category_id==parent_cat.id:
#              sub_categories.append(category.name)
      
#     template = loader.get_template("category.html")
#     context = {
#         "sub_categories": sub_categories,
#     }
#     return HttpResponse(template.render(context, request))

    
# def main(request):
#     category_list =Category.objects.all()
#     template = loader.get_template("main_category.html")
#     context = {
#         "category_list": category_list,
#     }
#     return HttpResponse(template.render(context, request))
