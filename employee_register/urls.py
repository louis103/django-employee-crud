from django.urls import include,path
from .views import employee_form,employee_delete,employee_list

urlpatterns = [
   path('', employee_form, name="employee_form"),
   path('list/', employee_list, name='employee_list'),
   path('<int:id>/',employee_form, name="employee_update"),
   path('delete/<int:id>/', employee_delete,name="employee_delete"),
]
