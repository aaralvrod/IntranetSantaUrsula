from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AreaForm
from .models import Area


@staff_member_required
def area_list(request):
    areas = Area.objects.select_related("headquarters", "manager").order_by("dept_name")
    return render(request, "areas/area_list.html", {"areas": areas})


@staff_member_required
def area_detail(request, pk):
    area = get_object_or_404(Area, pk=pk)
    return render(request, "areas/area_detail.html", {"area": area})


@staff_member_required
def area_create(request):
    if request.method == "POST":
        if (form := AreaForm(request.POST)).is_valid():
            form.save()
            return redirect("areas:area-list")
    else:
        form = AreaForm()
    return render(request, "areas/area_form.html", {"form": form})


@staff_member_required
def area_update(request, pk):
    area = get_object_or_404(Area, pk=pk)
    if request.method == "POST":
        if (form := AreaForm(request.POST, instance=area)).is_valid():
            form.save()
            return redirect("areas:area-detail", pk=pk)
    else:
        form = AreaForm(instance=area)
    return render(request, "areas/area_form.html", {"form": form, "area": area})


@staff_member_required
def area_delete(request, pk):
    area = get_object_or_404(Area, pk=pk)
    if request.method == "POST":
        area.delete()
        return redirect("areas:area-list")
    return render(request, "areas/area_confirm_delete.html", {"area": area})
