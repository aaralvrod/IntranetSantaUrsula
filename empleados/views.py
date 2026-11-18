from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EmployeeCreateForm, EmployeeUpdateForm, VacationDaysForm
from .models import Employee, VacationDays


@staff_member_required
def employee_list(request):
    employees = Employee.objects.order_by("last_name", "first_name")
    paginator = Paginator(employees, 25)
    page_obj = paginator.get_page(request.GET.get("page"))
    return render(request, "empleados/employee_list.html", {"page_obj": page_obj})


@staff_member_required
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, "empleados/employee_detail.html", {"employee": employee})


@staff_member_required
def employee_create(request):
    if request.method == 'POST':
        if (form := EmployeeCreateForm(request.POST)).is_valid():
            form.save()
            return redirect('empleados:employee-list')
    else:
        form = EmployeeCreateForm()
    return render(request, 'empleados/employee_form.html', {'form': form})


@staff_member_required
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        if (form := EmployeeUpdateForm(request.POST, instance=employee)).is_valid():
            form.save()
            return redirect('empleados:employee-list')
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, 'empleados/employee_form.html', {'form': form, 'employee': employee})


@staff_member_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("empleados:employee-list")
    return render(request, "empleados/employee_confirm_delete.html", {"employee": employee})


@staff_member_required
def vacationdays_list(request):
    qs = VacationDays.objects.order_by("start_date")
    employee_pk = request.GET.get("employee")
    if employee_pk:
        qs = qs.filter(employee__pk=employee_pk)
    return render(request, "empleados/vacationdays_list.html", {"vacation_days": qs})


@staff_member_required
def vacationdays_detail(request, pk):
    vacation = get_object_or_404(VacationDays, pk=pk)
    return render(request, "empleados/vacationdays_detail.html", {"vacation": vacation})


@staff_member_required
def vacationdays_create(request):
    if request.method == 'POST':
        if (form := VacationDaysForm(request.POST)).is_valid():
            form.save()
            return redirect('empleados:vacationdays-list')
    else:
        form = VacationDaysForm()
    return render(request, 'empleados/vacationdays_form.html', {'form': form})


@staff_member_required
def vacationdays_update(request, pk):
    vacation = get_object_or_404(VacationDays, pk=pk)
    if request.method == 'POST':
        if (form := VacationDaysForm(request.POST, instance=vacation)).is_valid():
            form.save()
            return redirect('empleados:vacationdays-list')
    else:
        form = VacationDaysForm(instance=vacation)
    return render(request, 'empleados/vacationdays_form.html', {'form': form, 'vacation': vacation})


@staff_member_required
def vacationdays_delete(request, pk):
    vacation = get_object_or_404(VacationDays, pk=pk)
    if request.method == "POST":
        vacation.delete()
        return redirect("empleados:vacationdays-list")
    return render(request, "empleados/vacationdays_confirm_delete.html", {"vacation": vacation})
