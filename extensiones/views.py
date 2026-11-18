from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ExtensionFijaForm, ExtensionMovilForm, MobileDeviceForm
from .models import ExtensionFija, ExtensionMovil, MobileDevice


@staff_member_required
def extension_movil_list(request):
    extensiones = ExtensionMovil.objects.select_related("employee").order_by("extension")
    return render(request, "extensiones/extensionmovil_list.html", {"extensiones": extensiones})


@staff_member_required
def extension_movil_detail(request, pk):
    extension = get_object_or_404(ExtensionMovil, pk=pk)
    return render(request, "extensiones/extensionmovil_detail.html", {"extension": extension})


@staff_member_required
def extension_movil_create(request):
    if request.method == "POST":
        if (form := ExtensionMovilForm(request.POST)).is_valid():
            form.save()
            return redirect("extensiones:extension-movil-list")
    else:
        form = ExtensionMovilForm()
    return render(request, "extensiones/extensionmovil_form.html", {"form": form})


@staff_member_required
def extension_movil_update(request, pk):
    extension = get_object_or_404(ExtensionMovil, pk=pk)
    if request.method == "POST":
        if (form := ExtensionMovilForm(request.POST, instance=extension)).is_valid():
            form.save()
            return redirect("extensiones:extension-movil-detail", pk=pk)
    else:
        form = ExtensionMovilForm(instance=extension)
    return render(request, "extensiones/extensionmovil_form.html", {"form": form, "extension": extension})


@staff_member_required
def extension_movil_delete(request, pk):
    extension = get_object_or_404(ExtensionMovil, pk=pk)
    if request.method == "POST":
        extension.delete()
        return redirect("extensiones:extension-movil-list")
    return render(request, "extensiones/extensionmovil_confirm_delete.html", {"extension": extension})


@staff_member_required
def extension_fija_list(request):
    extensiones = ExtensionFija.objects.select_related("employee", "area").order_by("extension")
    return render(request, "extensiones/extensionfija_list.html", {"extensiones": extensiones})


@staff_member_required
def extension_fija_detail(request, pk):
    extension = get_object_or_404(ExtensionFija, pk=pk)
    return render(request, "extensiones/extensionfija_detail.html", {"extension": extension})


@staff_member_required
def extension_fija_create(request):
    if request.method == "POST":
        if (form := ExtensionFijaForm(request.POST)).is_valid():
            form.save()
            return redirect("extensiones:extension-fija-list")
    else:
        form = ExtensionFijaForm()
    return render(request, "extensiones/extensionfija_form.html", {"form": form})


@staff_member_required
def extension_fija_update(request, pk):
    extension = get_object_or_404(ExtensionFija, pk=pk)
    if request.method == "POST":
        if (form := ExtensionFijaForm(request.POST, instance=extension)).is_valid():
            form.save()
            return redirect("extensiones:extension-fija-detail", pk=pk)
    else:
        form = ExtensionFijaForm(instance=extension)
    return render(request, "extensiones/extensionfija_form.html", {"form": form, "extension": extension})


@staff_member_required
def extension_fija_delete(request, pk):
    extension = get_object_or_404(ExtensionFija, pk=pk)
    if request.method == "POST":
        extension.delete()
        return redirect("extensiones:extension-fija-list")
    return render(request, "extensiones/extensionfija_confirm_delete.html", {"extension": extension})


@staff_member_required
def mobile_device_list(request):
    devices = MobileDevice.objects.select_related("mobile_extension").order_by("brand", "model")
    return render(request, "extensiones/mobiledevice_list.html", {"devices": devices})


@staff_member_required
def mobile_device_detail(request, pk):
    device = get_object_or_404(MobileDevice, pk=pk)
    return render(request, "extensiones/mobiledevice_detail.html", {"device": device})


@staff_member_required
def mobile_device_create(request):
    if request.method == "POST":
        if (form := MobileDeviceForm(request.POST)).is_valid():
            form.save()
            return redirect("extensiones:mobile-device-list")
    else:
        form = MobileDeviceForm()
    return render(request, "extensiones/mobiledevice_form.html", {"form": form})


@staff_member_required
def mobile_device_update(request, pk):
    device = get_object_or_404(MobileDevice, pk=pk)
    if request.method == "POST":
        if (form := MobileDeviceForm(request.POST, instance=device)).is_valid():
            form.save()
            return redirect("extensiones:mobile-device-detail", pk=pk)
    else:
        form = MobileDeviceForm(instance=device)
    return render(request, "extensiones/mobiledevice_form.html", {"form": form, "device": device})


@staff_member_required
def mobile_device_delete(request, pk):
    device = get_object_or_404(MobileDevice, pk=pk)
    if request.method == "POST":
        device.delete()
        return redirect("extensiones:mobile-device-list")
    return render(request, "extensiones/mobiledevice_confirm_delete.html", {"device": device})
