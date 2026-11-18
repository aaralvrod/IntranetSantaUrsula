from django.urls import path

from . import views

app_name = "empleados"

urlpatterns = [
    path("", views.employee_list, name="employee-list"),
    path("<int:pk>/", views.employee_detail, name="employee-detail"),
    path("crear/", views.employee_create, name="employee-create"),
    path("<int:pk>/editar/", views.employee_update, name="employee-update"),
    path("<int:pk>/eliminar/", views.employee_delete, name="employee-delete"),
    path("vacaciones/", views.vacationdays_list, name="vacationdays-list"),
    path("vacaciones/<int:pk>/", views.vacationdays_detail, name="vacationdays-detail"),
    path("vacaciones/crear/", views.vacationdays_create, name="vacationdays-create"),
    path("vacaciones/<int:pk>/editar/", views.vacationdays_update, name="vacationdays-update"),
    path("vacaciones/<int:pk>/eliminar/", views.vacationdays_delete, name="vacationdays-delete"),
]
