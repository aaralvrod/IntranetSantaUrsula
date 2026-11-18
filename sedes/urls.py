from django.urls import path

from . import views

app_name = "sedes"

urlpatterns = [
    # Sede
    path("", views.sede_list, name="sede-list"),
    path("<int:pk>/", views.sede_detail, name="sede-detail"),
    path("crear/", views.sede_create, name="sede-create"),
    path("<int:pk>/editar/", views.sede_update, name="sede-update"),
    path("<int:pk>/eliminar/", views.sede_delete, name="sede-delete"),

    # Piso
    path("plantas/", views.floor_list, name="floor-list"),
    path("plantas/<int:pk>/", views.floor_detail, name="floor-detail"),
    path("plantas/crear/", views.floor_create, name="floor-create"),
    path("plantas/<int:pk>/editar/", views.floor_update, name="floor-update"),
    path("plantas/<int:pk>/eliminar/", views.floor_delete, name="floor-delete"),

    # Telecomunicaciones
    path("telecomunicaciones/", views.telecom_list, name="telecom-list"),
    path("telecomunicaciones/<int:pk>/", views.telecom_detail, name="telecom-detail"),
    path("telecomunicaciones/crear/", views.telecom_create, name="telecom-create"),
    path("telecomunicaciones/<int:pk>/editar/", views.telecom_update, name="telecom-update"),
    path("telecomunicaciones/<int:pk>/eliminar/", views.telecom_delete, name="telecom-delete"),
]
