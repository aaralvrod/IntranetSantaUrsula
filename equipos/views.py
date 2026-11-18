from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProveedorForm, EquipoForm, PrestamoForm, ScreenForm, PeripheralsForm, PrinterForm
from .models import Proveedor, Equipo, Prestamo, Screen, Peripherals, Printer


# Proveedores

@staff_member_required
def proveedor_list(request):
    proveedores = Proveedor.objects.order_by("name")
    return render(request, "equipos/proveedor_list.html", {"proveedores": proveedores})


@staff_member_required
def proveedor_detail(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, "equipos/proveedor_detail.html", {"proveedor": proveedor})


@staff_member_required
def proveedor_create(request):
    if request.method == "POST":
        if (form := ProveedorForm(request.POST)).is_valid():
            form.save()
            return redirect("equipos:proveedor-list")
    else:
        form = ProveedorForm()
    return render(request, "equipos/proveedor_form.html", {"form": form})


@staff_member_required
def proveedor_update(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        if (form := ProveedorForm(request.POST, instance=proveedor)).is_valid():
            form.save()
            return redirect("equipos:proveedor-detail", pk=pk)
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, "equipos/proveedor_form.html", {"form": form, "proveedor": proveedor})


@staff_member_required
def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == "POST":
        proveedor.delete()
        return redirect("equipos:proveedor-list")
    return render(request, "equipos/proveedor_confirm_delete.html", {"proveedor": proveedor})


# Equipo

@staff_member_required
def equipo_list(request):
    equipos = Equipo.objects.select_related("provider").order_by("serial_num")
    return render(request, "equipos/equipo_list.html", {"equipos": equipos})


@staff_member_required
def equipo_detail(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    return render(request, "equipos/equipo_detail.html", {"equipo": equipo})


@staff_member_required
def equipo_create(request):
    if request.method == "POST":
        if (form := EquipoForm(request.POST)).is_valid():
            form.save()
            return redirect("equipos:equipo-list")
    else:
        form = EquipoForm()
    return render(request, "equipos/equipo_form.html", {"form": form})


@staff_member_required
def equipo_update(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        if (form := EquipoForm(request.POST, instance=equipo)).is_valid():
            form.save()
            return redirect("equipos:equipo-detail", pk=pk)
    else:
        form = EquipoForm(instance=equipo)
    return render(request, "equipos/equipo_form.html", {"form": form, "equipo": equipo})


@staff_member_required
def equipo_delete(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        equipo.delete()
        return redirect("equipos:equipo-list")
    return render(request, "equipos/equipo_confirm_delete.html", {"equipo": equipo})


# Prestamos

@staff_member_required
def prestamo_list(request):
    prestamos = Prestamo.objects.select_related("equipment", "employee").order_by("-asignation_datetime")
    return render(request, "equipos/prestamo_list.html", {"prestamos": prestamos})


@staff_member_required
def prestamo_detail(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    return render(request, "equipos/prestamo_detail.html", {"prestamo": prestamo})


@staff_member_required
def prestamo_create(request):
    if request.method == "POST":
        if (form := PrestamoForm(request.POST)).is_valid():
            form.save()
            return redirect("equipos:prestamo-list")
    else:
        form = PrestamoForm()
    return render(request, "equipos/prestamo_form.html", {"form": form})


@staff_member_required
def prestamo_update(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == "POST":
        if (form := PrestamoForm(request.POST, instance=prestamo)).is_valid():
            form.save()
            return redirect("equipos:prestamo-detail", pk=pk)
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, "equipos/prestamo_form.html", {"form": form, "prestamo": prestamo})


@staff_member_required
def prestamo_delete(request, pk):
    prestamo = get_object_or_404(Prestamo, pk=pk)
    if request.method == "POST":
        prestamo.delete()
        return redirect("equipos:prestamo-list")
    return render(request, "equipos/prestamo_confirm_delete.html", {"prestamo": prestamo})


# Pantallas

@staff_member_required
def screen_list(request):
    screens = Screen.objects.select_related("equipment").order_by("serial_num")
    return render(request, "equipos/screen_list.html", {"screens": screens})


@staff_member_required
def screen_detail(request, pk):
    screen = get_object_or_404(Screen, pk=pk)
    return render(request, "equipos/screen_detail.html", {"screen": screen})


@staff_member_required
def screen_create(request):
    if request.method == "POST":
        if (form := ScreenForm(request.POST)).is_valid():
            form.save()
            return redirect("equipos:screen-list")
    else:
        form = ScreenForm()
    return render(request, "equipos/screen_form.html", {"form": form})


@staff_member_required
def screen_update(request, pk):
    screen = get_object_or_404(Screen, pk=pk)
    if request.method == "POST":
        if (form := ScreenForm(request.POST, instance=screen)).is_valid():
            form.save()
            return redirect("equipos:screen-detail", pk=pk)
    else:
        form = ScreenForm(instance=screen)
    return render(request, "equipos/screen_form.html", {"form": form, "screen": screen})


@staff_member_required
def screen_delete(request, pk):
    screen = get_object_or_404(Screen, pk=pk)
    if request.method == "POST":
        screen.delete()
        return redirect("equipos:screen-list")
    return render(request, "equipos/screen_confirm_delete.html", {"screen": screen})


# Perifericos

@staff_member_required
def peripherals_list(request):
    peripherals = Peripherals.objects.select_related("provider").order_by("type_peripheral")
    return render(request, "equipos/peripherals_list.html", {"peripherals": peripherals})


@staff_member_required
def peripherals_detail(request, pk):
    peripheral = get_object_or_404(Peripherals, pk=pk)
    return render(request, "equipos/peripherals_detail.html", {"peripheral": peripheral})


@staff_member_required
def peripherals_create(request):
    if request.method == "POST":
        if (form := PeripheralsForm(request.POST)).is_valid():
            form.save()
            return redirect("equipos:peripherals-list")
    else:
        form = PeripheralsForm()
    return render(request, "equipos/peripherals_form.html", {"form": form})


@staff_member_required
def peripherals_update(request, pk):
    peripheral = get_object_or_404(Peripherals, pk=pk)
    if request.method == "POST":
        if (form := PeripheralsForm(request.POST, instance=peripheral)).is_valid():
            form.save()
            return redirect("equipos:peripherals-detail", pk=pk)
    else:
        form = PeripheralsForm(instance=peripheral)
    return render(request, "equipos/peripherals_form.html", {"form": form, "peripheral": peripheral})


@staff_member_required
def peripherals_delete(request, pk):
    peripheral = get_object_or_404(Peripherals, pk=pk)
    if request.method == "POST":
        peripheral.delete()
        return redirect("equipos:peripherals-list")
    return render(request, "equipos/peripherals_confirm_delete.html", {"peripheral": peripheral})


# Impresoras 

@staff_member_required
def printer_list(request):
    printers = Printer.objects.select_related("area", "provider").order_by("ip")
    return render(request, "equipos/printer_list.html", {"printers": printers})


@staff_member_required
def printer_detail(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    return render(request, "equipos/printer_detail.html", {"printer": printer})


@staff_member_required
def printer_create(request):
    if request.method == "POST":
        if (form := PrinterForm(request.POST)).is_valid():
            form.save()
            return redirect("equipos:printer-list")
    else:
        form = PrinterForm()
    return render(request, "equipos/printer_form.html", {"form": form})


@staff_member_required
def printer_update(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == "POST":
        if (form := PrinterForm(request.POST, instance=printer)).is_valid():
            form.save()
            return redirect("equipos:printer-detail", pk=pk)
    else:
        form = PrinterForm(instance=printer)
    return render(request, "equipos/printer_form.html", {"form": form, "printer": printer})


@staff_member_required
def printer_delete(request, pk):
    printer = get_object_or_404(Printer, pk=pk)
    if request.method == "POST":
        printer.delete()
        return redirect("equipos:printer-list")
    return render(request, "equipos/printer_confirm_delete.html", {"printer": printer})
