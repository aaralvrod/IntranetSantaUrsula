from django.urls import path

from . import views

app_name = "equipos"

urlpatterns = [
    path("proveedores/", views.proveedor_list, name="proveedor-list"),
    path("proveedores/<int:pk>/", views.proveedor_detail, name="proveedor-detail"),
    path("proveedores/crear/", views.proveedor_create, name="proveedor-create"),
    path("proveedores/<int:pk>/editar/", views.proveedor_update, name="proveedor-update"),
    path("proveedores/<int:pk>/eliminar/", views.proveedor_delete, name="proveedor-delete"),

    path("", views.equipo_list, name="equipo-list"),
    path("<int:pk>/", views.equipo_detail, name="equipo-detail"),
    path("crear/", views.equipo_create, name="equipo-create"),
    path("<int:pk>/editar/", views.equipo_update, name="equipo-update"),
    path("<int:pk>/eliminar/", views.equipo_delete, name="equipo-delete"),

    path("prestamos/", views.prestamo_list, name="prestamo-list"),
    path("prestamos/<int:pk>/", views.prestamo_detail, name="prestamo-detail"),
    path("prestamos/crear/", views.prestamo_create, name="prestamo-create"),
    path("prestamos/<int:pk>/editar/", views.prestamo_update, name="prestamo-update"),
    path("prestamos/<int:pk>/eliminar/", views.prestamo_delete, name="prestamo-delete"),

    path("pantallas/", views.screen_list, name="screen-list"),
    path("pantallas/<int:pk>/", views.screen_detail, name="screen-detail"),
    path("pantallas/crear/", views.screen_create, name="screen-create"),
    path("pantallas/<int:pk>/editar/", views.screen_update, name="screen-update"),
    path("pantallas/<int:pk>/eliminar/", views.screen_delete, name="screen-delete"),

    path("perifericos/", views.peripherals_list, name="peripherals-list"),
    path("perifericos/<int:pk>/", views.peripherals_detail, name="peripherals-detail"),
    path("perifericos/crear/", views.peripherals_create, name="peripherals-create"),
    path("perifericos/<int:pk>/editar/", views.peripherals_update, name="peripherals-update"),
    path("perifericos/<int:pk>/eliminar/", views.peripherals_delete, name="peripherals-delete"),

    path("impresoras/", views.printer_list, name="printer-list"),
    path("impresoras/<int:pk>/", views.printer_detail, name="printer-detail"),
    path("impresoras/crear/", views.printer_create, name="printer-create"),
    path("impresoras/<int:pk>/editar/", views.printer_update, name="printer-update"),
    path("impresoras/<int:pk>/eliminar/", views.printer_delete, name="printer-delete"),
]
