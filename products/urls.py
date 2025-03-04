from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="index"),
  
    # path("category/", views.main, name="main"),
    # path("category/<int:category_id>",views.category,name="category"),
    # # path("<int:category_id>/", views.cat, name="cat"),
    # path("<int:product_id>/", views.detail, name="detail"),

    
]