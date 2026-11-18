from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SedeForm, FloorForm, TelecommunicationsForm
from .models import Sede, Floor, Telecommunications


# Sedes

@staff_member_required
def sede_list(request):
    sedes = Sede.objects.order_by("name")
    return render(request, "sedes/sede_list.html", {"sedes": sedes})


@staff_member_required
def sede_detail(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    return render(request, "sedes/sede_detail.html", {"sede": sede})


@staff_member_required
def sede_create(request):
    if request.method == "POST":
        if (form := SedeForm(request.POST)).is_valid():
            form.save()
            return redirect("sedes:sede-list")
    else:
        form = SedeForm()
    return render(request, "sedes/sede_form.html", {"form": form})


@staff_member_required
def sede_update(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == "POST":
        if (form := SedeForm(request.POST, instance=sede)).is_valid():
            form.save()
            return redirect("sedes:sede-detail", pk=pk)
    else:
        form = SedeForm(instance=sede)
    return render(request, "sedes/sede_form.html", {"form": form, "sede": sede})


@staff_member_required
def sede_delete(request, pk):
    sede = get_object_or_404(Sede, pk=pk)
    if request.method == "POST":
        sede.delete()
        return redirect("sedes:sede-list")
    return render(request, "sedes/sede_confirm_delete.html", {"sede": sede})


# Piso

@staff_member_required
def floor_list(request):
    floors = Floor.objects.order_by("floor_num")
    return render(request, "sedes/floor_list.html", {"floors": floors})


@staff_member_required
def floor_detail(request, pk):
    floor = get_object_or_404(Floor, pk=pk)
    return render(request, "sedes/floor_detail.html", {"floor": floor})


@staff_member_required
def floor_create(request):
    if request.method == "POST":
        if (form := FloorForm(request.POST)).is_valid():
            form.save()
            return redirect("sedes:floor-list")
    else:
        form = FloorForm()
    return render(request, "sedes/floor_form.html", {"form": form})


@staff_member_required
def floor_update(request, pk):
    floor = get_object_or_404(Floor, pk=pk)
    if request.method == "POST":
        if (form := FloorForm(request.POST, instance=floor)).is_valid():
            form.save()
            return redirect("sedes:floor-detail", pk=pk)
    else:
        form = FloorForm(instance=floor)
    return render(request, "sedes/floor_form.html", {"form": form, "floor": floor})


@staff_member_required
def floor_delete(request, pk):
    floor = get_object_or_404(Floor, pk=pk)
    if request.method == "POST":
        floor.delete()
        return redirect("sedes:floor-list")
    return render(request, "sedes/floor_confirm_delete.html", {"floor": floor})


# Telecomunicaciones

@staff_member_required
def telecom_list(request):
    telecoms = Telecommunications.objects.select_related("headquarters").order_by("serial_num")
    return render(request, "sedes/telecom_list.html", {"telecoms": telecoms})


@staff_member_required
def telecom_detail(request, pk):
    telecom = get_object_or_404(Telecommunications, pk=pk)
    return render(request, "sedes/telecom_detail.html", {"telecom": telecom})


@staff_member_required
def telecom_create(request):
    if request.method == "POST":
        if (form := TelecommunicationsForm(request.POST)).is_valid():
            form.save()
            return redirect("sedes:telecom-list")
    else:
        form = TelecommunicationsForm()
    return render(request, "sedes/telecom_form.html", {"form": form})


@staff_member_required
def telecom_update(request, pk):
    telecom = get_object_or_404(Telecommunications, pk=pk)
    if request.method == "POST":
        if (form := TelecommunicationsForm(request.POST, instance=telecom)).is_valid():
            form.save()
            return redirect("sedes:telecom-detail", pk=pk)
    else:
        form = TelecommunicationsForm(instance=telecom)
    return render(request, "sedes/telecom_form.html", {"form": form, "telecom": telecom})


@staff_member_required
def telecom_delete(request, pk):
    telecom = get_object_or_404(Telecommunications, pk=pk)
    if request.method == "POST":
        telecom.delete()
        return redirect("sedes:telecom-list")
    return render(request, "sedes/telecom_confirm_delete.html", {"telecom": telecom})
