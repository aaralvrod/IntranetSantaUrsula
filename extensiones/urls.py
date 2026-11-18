from django.urls import path

from . import views

app_name = "extensiones"

urlpatterns = [
    # ── ExtensionMovil ────────────────────────
    path("movil/", views.extension_movil_list, name="extension-movil-list"),
    path("movil/<int:pk>/", views.extension_movil_detail, name="extension-movil-detail"),
    path("movil/crear/", views.extension_movil_create, name="extension-movil-create"),
    path("movil/<int:pk>/editar/", views.extension_movil_update, name="extension-movil-update"),
    path("movil/<int:pk>/eliminar/", views.extension_movil_delete, name="extension-movil-delete"),

    # ── ExtensionFija ─────────────────────────
    path("fija/", views.extension_fija_list, name="extension-fija-list"),
    path("fija/<int:pk>/", views.extension_fija_detail, name="extension-fija-detail"),
    path("fija/crear/", views.extension_fija_create, name="extension-fija-create"),
    path("fija/<int:pk>/editar/", views.extension_fija_update, name="extension-fija-update"),
    path("fija/<int:pk>/eliminar/", views.extension_fija_delete, name="extension-fija-delete"),

    # ── MobileDevice ──────────────────────────
    path("dispositivos/", views.mobile_device_list, name="mobile-device-list"),
    path("dispositivos/<int:pk>/", views.mobile_device_detail, name="mobile-device-detail"),
    path("dispositivos/crear/", views.mobile_device_create, name="mobile-device-create"),
    path("dispositivos/<int:pk>/editar/", views.mobile_device_update, name="mobile-device-update"),
    path("dispositivos/<int:pk>/eliminar/", views.mobile_device_delete, name="mobile-device-delete"),
]
