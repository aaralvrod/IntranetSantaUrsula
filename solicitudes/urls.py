from django.urls import path

from . import views

app_name = "solicitudes"

urlpatterns = [
    # Solicitudes
    path("", views.request_list, name="request-list"),
    path("<int:pk>/", views.request_detail, name="request-detail"),
    path("crear/", views.request_create, name="request-create"),
    path("<int:pk>/editar/", views.request_update, name="request-update"),
    path("<int:pk>/eliminar/", views.request_delete, name="request-delete"),

    # Llaves
    path("llaves/", views.key_list, name="key-list"),
    path("llaves/<int:pk>/", views.key_detail, name="key-detail"),
    path("llaves/crear/", views.key_create, name="key-create"),
    path("llaves/<int:pk>/editar/", views.key_update, name="key-update"),
    path("llaves/<int:pk>/eliminar/", views.key_delete, name="key-delete"),

    # Vehículos
    path("vehiculos/", views.vehicle_list, name="vehicle-list"),
    path("vehiculos/<int:pk>/", views.vehicle_detail, name="vehicle-detail"),
    path("vehiculos/crear/", views.vehicle_create, name="vehicle-create"),
    path("vehiculos/<int:pk>/editar/", views.vehicle_update, name="vehicle-update"),
    path("vehiculos/<int:pk>/eliminar/", views.vehicle_delete, name="vehicle-delete"),

    # Lugares
    path("lugares/", views.place_list, name="place-list"),
    path("lugares/<int:pk>/", views.place_detail, name="place-detail"),
    path("lugares/crear/", views.place_create, name="place-create"),
    path("lugares/<int:pk>/editar/", views.place_update, name="place-update"),
    path("lugares/<int:pk>/eliminar/", views.place_delete, name="place-delete"),
]
