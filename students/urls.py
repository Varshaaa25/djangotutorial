from django.urls import path

from . import views

urlpatterns=[
    path("", views.form, name="form"),
    path("dropdown/",views.dropdown,name="dropdown"),
    # path("<int:student_id>/", views.detail, name="detail"),
]