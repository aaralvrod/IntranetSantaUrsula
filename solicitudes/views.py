from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RequestForm, KeyForm, VehicleForm, PlaceForm
from .models import Request, Key, Vehicle, Place


# Solicitudes

@staff_member_required
def request_list(request):
    solicitudes = Request.objects.select_related("id_key", "id_vehicle", "id_place", "id_employee")
    return render(request, "solicitudes/request_list.html", {"solicitudes": solicitudes})


@staff_member_required
def request_detail(request, pk):
    solicitud = get_object_or_404(Request, pk=pk)
    return render(request, "solicitudes/request_detail.html", {"solicitud": solicitud})


@staff_member_required
def request_create(request):
    if request.method == "POST":
        if (form := RequestForm(request.POST)).is_valid():
            form.save()
            return redirect("solicitudes:request-list")
    else:
        form = RequestForm()
    return render(request, "solicitudes/request_form.html", {"form": form})


@staff_member_required
def request_update(request, pk):
    solicitud = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        if (form := RequestForm(request.POST, instance=solicitud)).is_valid():
            form.save()
            return redirect("solicitudes:request-detail", pk=pk)
    else:
        form = RequestForm(instance=solicitud)
    return render(request, "solicitudes/request_form.html", {"form": form, "solicitud": solicitud})


@staff_member_required
def request_delete(request, pk):
    solicitud = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        solicitud.delete()
        return redirect("solicitudes:request-list")
    return render(request, "solicitudes/request_confirm_delete.html", {"solicitud": solicitud})


# Llaves

@staff_member_required
def key_list(request):
    keys = Key.objects.order_by("name")
    return render(request, "solicitudes/key_list.html", {"keys": keys})


@staff_member_required
def key_detail(request, pk):
    key = get_object_or_404(Key, pk=pk)
    return render(request, "solicitudes/key_detail.html", {"key": key})


@staff_member_required
def key_create(request):
    if request.method == "POST":
        if (form := KeyForm(request.POST)).is_valid():
            form.save()
            return redirect("solicitudes:key-list")
    else:
        form = KeyForm()
    return render(request, "solicitudes/key_form.html", {"form": form})


@staff_member_required
def key_update(request, pk):
    key = get_object_or_404(Key, pk=pk)
    if request.method == "POST":
        if (form := KeyForm(request.POST, instance=key)).is_valid():
            form.save()
            return redirect("solicitudes:key-detail", pk=pk)
    else:
        form = KeyForm(instance=key)
    return render(request, "solicitudes/key_form.html", {"form": form, "key": key})


@staff_member_required
def key_delete(request, pk):
    key = get_object_or_404(Key, pk=pk)
    if request.method == "POST":
        key.delete()
        return redirect("solicitudes:key-list")
    return render(request, "solicitudes/key_confirm_delete.html", {"key": key})


# Vehículos

@staff_member_required
def vehicle_list(request):
    vehicles = Vehicle.objects.order_by("plate")
    return render(request, "solicitudes/vehicle_list.html", {"vehicles": vehicles})


@staff_member_required
def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, "solicitudes/vehicle_detail.html", {"vehicle": vehicle})


@staff_member_required
def vehicle_create(request):
    if request.method == "POST":
        if (form := VehicleForm(request.POST)).is_valid():
            form.save()
            return redirect("solicitudes:vehicle-list")
    else:
        form = VehicleForm()
    return render(request, "solicitudes/vehicle_form.html", {"form": form})


@staff_member_required
def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        if (form := VehicleForm(request.POST, instance=vehicle)).is_valid():
            form.save()
            return redirect("solicitudes:vehicle-detail", pk=pk)
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, "solicitudes/vehicle_form.html", {"form": form, "vehicle": vehicle})


@staff_member_required
def vehicle_delete(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        vehicle.delete()
        return redirect("solicitudes:vehicle-list")
    return render(request, "solicitudes/vehicle_confirm_delete.html", {"vehicle": vehicle})


# Lugares

@staff_member_required
def place_list(request):
    places = Place.objects.order_by("name")
    return render(request, "solicitudes/place_list.html", {"places": places})


@staff_member_required
def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, "solicitudes/place_detail.html", {"place": place})


@staff_member_required
def place_create(request):
    if request.method == "POST":
        if (form := PlaceForm(request.POST)).is_valid():
            form.save()
            return redirect("solicitudes:place-list")
    else:
        form = PlaceForm()
    return render(request, "solicitudes/place_form.html", {"form": form})


@staff_member_required
def place_update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        if (form := PlaceForm(request.POST, instance=place)).is_valid():
            form.save()
            return redirect("solicitudes:place-detail", pk=pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, "solicitudes/place_form.html", {"form": form, "place": place})


@staff_member_required
def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        place.delete()
        return redirect("solicitudes:place-list")
    return render(request, "solicitudes/place_confirm_delete.html", {"place": place})
