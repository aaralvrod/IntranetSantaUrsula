from django.urls import path

from . import views

app_name = "areas"

urlpatterns = [
    path("", views.area_list, name="area-list"),
    path("<int:pk>/", views.area_detail, name="area-detail"),
    path("crear/", views.area_create, name="area-create"),
    path("<int:pk>/editar/", views.area_update, name="area-update"),
    path("<int:pk>/eliminar/", views.area_delete, name="area-delete"),
]
