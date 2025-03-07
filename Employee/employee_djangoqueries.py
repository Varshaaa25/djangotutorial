from django.db.models import ExpressionWrapper, Count, Value, DecimalField
from django.db.models import Sum,Count

# Employee app:
# ----------------------query1-----------------------------------------------------------------------------------------
# ------SQL QUERY-------------
# SELECT employee.e_id,employee.e_name,employee.e_email, department.d_name
# FROM department
# LEFT JOIN employee ON department.d_id = employee.d_id;

# ----DJANGO EQUIVALENT-------
from Employee.models import Employee,Department
employees=Employee.objects.select_related('department_id').values('id','name','email','department_id__name')
for employee in employees:
         print(employee)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------query2-----------------------------------------------------------------------------------------
# SELECT
# 	employee.e_id,
# 	employee.e_name,
# 	employee.e_email,
# 	department.d_name,
# 	concat(location.loc_city, '-', LOCATION.loc_state, '-', LOCATION.loc_country) AS city_state_country
# FROM
# 	employee
# 	JOIN department ON employee.d_id = department.d_id
# 	JOIN location ON LOCATION.loc_id = department.loc_id;

# ----DJANGO EQUIVALENT-------
from django.db.models import Value as V,F
from django.db.models.functions import Concat
results=Employee.objects.select_related('department__id','department__location_id').annotate(city_state_country=Concat(F('department_id__location_id__city'),V('_'),F('department_id__location_id__state'),V('_'),F('department_id__location_id__country'))).values('id','name','email','department_id__name','city_state_country')

for result in results:
	print(result)
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------query3---------------------------------------------------------------------------
# -- Get all contacts based on emp_name
# select contact.number from contact
# left join employee
# on contact.employee_id=employee.e_id
# where employee.e_name='Jeevan';

# ----DJANGO EQUIVALENT-------
contacts_result=Contact.objects.select_related('employee').filter(employee_id__name='Jeevan').values('number')
print(contacts_result)
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------query4---------
# -- Given a contact number find who it is associated with
# select employee.e_name
# from employee
# join contact
# on employee.e_id=contact.employee_id
# where contact.number=897546789;

# ----DJANGO EQUIVALENT-------
employee_result=Contact.objects.select_related('employee').filter(number=897546789).values('employee__name')
print(employee_result)

# ----------------------------------------------------------------------------------------------------------------------