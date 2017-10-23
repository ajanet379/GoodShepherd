from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Sum


now = timezone.now()
def home(request):
    return render(request, 'portfolio/home.html',
                 {'portfolio': home})


@login_required
def client_list(request):
    clients = Client.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/client_list.html',
                 {'clients': clients})


@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
       # update
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
           client = form.save(commit=False)
           client.updated_date = timezone.now()
           client.save()
           clients = Client.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/client_list.html',
                         {'clients': clients})
    else:
       # edit
       form = ClientForm(instance=client)
       return render(request, 'portfolio/client_edit.html', {'form': form})


@login_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('portfolio:client_list')

@login_required
def client_new(request):
   if request.method == "POST":
       form = ClientForm(request.POST)
       if form.is_valid():
           client = form.save(commit=False)
           client.created_date = timezone.now()
           client.save()
           clients = Client.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/client_list.html',
                         {'clients': clients})
   else:
       form = ClientForm()
       # print("Else")
   return render(request, 'portfolio/client_new.html', {'form': form})



@login_required
def employee_list(request):
    employees = Employee.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/employee_list.html', {'employees': employees})


@login_required
def employee_new(request):
   if request.method == "POST":
       form = EmployeeForm(request.POST)
       if form.is_valid():
           employee = form.save(commit=False)
           employee.created_date = timezone.now()
           employee.save()
           employees = Employee.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/employee_list.html',
                         {'employees': employees})
   else:
       form = EmployeeForm()
       # print("Else")
   return render(request, 'portfolio/employee_new.html', {'form': form})



@login_required
def employee_edit(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
       # update
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.updated_date = timezone.now()
            employee.save()
            employees = Client.objects.filter(created_date__lte=timezone.now())
            return render(request, 'portfolio/client_list.html',
                         {'employees': employees})
    else:
               # edit
            form = EmployeeForm(instance=employee)
            return render(request, 'portfolio/employee_edit.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    employees = Employee.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/employee_list.html', {'employees': employees})

@login_required
def item_list(request):
    items = Item.objects.filter(expired_date__lte=timezone.now())
    return render(request, 'portfolio/item_list.html', {'items': items})

@login_required
def item_new(request):
   if request.method == "POST":
       form = ItemForm(request.POST)
       if form.is_valid():
           item = form.save(commit=False)
           item.created_date = timezone.now()
           item.save()
           items = Employee.objects.filter(expired_date__lte=timezone.now())
           return render(request, 'portfolio/item_list.html',
                         {'items': items})
   else:
       form = ItemForm()
       # print("Else")
   return render(request, 'portfolio/item_new.html', {'form': form})


@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
       form = ItemForm(request.POST, instance=item)
       if form.is_valid():
           item = form.save()
           # investment.customer = investment.id
           item.updated_date = timezone.now()
           item.save()
           items = Item.objects.filter(expired_date__lte=timezone.now())
           return render(request, 'portfolio/item_list.html',
                         {'items': items})
    else:
       # print("else")
       form = ItemForm(instance=item)
       return render(request, 'portfolio/item_edit.html', {'form': form})

@login_required
def item_delete(request,pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    items = Item.objects.filter(expired_date__lte=timezone.now())
    return render(request, 'portfolio/item_list.html', {'items': items})

@login_required
def donor_list(request):
    donors = Donor.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/donor_list.html', {'donors': donors})

@login_required
def donor_new(request):
   if request.method == "POST":
       form = DonorForm(request.POST)
       if form.is_valid():
           donor = form.save(commit=False)
           donor.created_date = timezone.now()
           donor.save()
           donors = Donor.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/donor_list.html',
                         {'donors': donors})
   else:
       form = DonorForm()
       # print("Else")
   return render(request, 'portfolio/donor_new.html', {'form': form})


@login_required
def donor_edit(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    if request.method == "POST":
       form = DonorForm(request.POST, instance=donor)
       if form.is_valid():
           donor = form.save()
           # fund.customer = fund.id
           donor.updated_date = timezone.now()
           donor.save()
           donors = Donor.objects.filter(created_date__lte=timezone.now())
           return render(request, 'portfolio/donor_list.html', {'donors': donors})
    else:
       # print("else")
       form = DonorForm(instance=donor)
       return render(request, 'portfolio/donor_edit.html', {'form': form})

@login_required
def donor_delete(request,pk):
    donor = get_object_or_404(Donor, pk=pk)
    donor.delete()
    donors = Donor.objects.filter(created_date__lte=timezone.now())
    return render(request, 'portfolio/donor_list.html', {'donors': donors})
