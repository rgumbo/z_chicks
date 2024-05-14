from django.shortcuts import render

from .filters import CustOrdersFilter, StoreOrderFilter,OrderItemFilter
#imports to be cleaned up

from django.http import HttpResponse
from django_globals import globals
import json
#import plotly.express  as px
from .tables import CustOrdersHTMxTable
#Imports for table
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView
#from .tables import TransHTMxTable
import django_tables2 as tables

#End imports for table

import datetime
import csv, io
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from django.db.models import Sum, F,Avg, Max, Min,Count,Q
from django.core.mail import EmailMessage

from django.views.generic import ListView, DetailView

from django.conf import settings
import csv,io
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Round

#from django.http import HttpResponse
import getpass
from os import environ, getcwd
from decimal import *
#end of imports to be cleaned up

# Create your views here.
from django.shortcuts import render
# Start Imports
from django.shortcuts import render
import datetime
import csv, io
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
from django.db.models import Sum, F,Avg, Max, Min,Count,Q
from django.core.mail import EmailMessage

from django.views.generic import ListView, DetailView

from django.conf import settings
import csv,io
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
import getpass
from os import environ, getcwd
from django.views.generic import ListView, DetailView
# from .filters import MemberFilter,EmailFilter,MembReturnsFilter

from .forms import QualificationForm,CountryForm,RegionForm,TownForm,DistrictForm,\
    WardForm,VillageForm,GradeForm,ContractTypeForm,MemberForm,EmployeeForm,\
    HoldingForm,HoldingInstanceForm,ActivityForm,NoteForm,ResourceForm,OutPutForm,CustOrdersForm, \
    RegionForm_e,TownForm_e,DistrictForm_e, WardForm_e,VillageForm_e, EmployeeForm_e , \
    PackTypeForm,CurrencyForm, StoreNameForm, StockLocForm, StockTypeForm, StockItemForm, CustomerForm,\
    StoreOrderForm, OrderItemForm,OrderItemEditForm,OrdRunForm,ContributionForm, BlogForm

from .models import Qualification,ContractType, Country,Region,Town,District,Grade, Ward,\
        Village,Grade,Member,Employee,Holding,HoldingInstance,Activity,Note,Resource,OutPut,CustOrders, \
        PackType,Currency, StoreName, StockLoc, StockType, StockItem, Customer, StoreOrder, OrderItem, \
        BlogPost, PostContribution

#Start Views

#Index Templates

def HomePageView(Request):
    template = 'chicks/homeindex.html'
    context = {}

    return render (Request, template, context)

def EmpHomeView(Request):
    template = 'chicks/emp_home.html'
    context = {}

    return render (Request, template, context)

def GeoHomeView(Request):
    template = 'chicks/geo_home.html'
    context = {}

    return render (Request, template, context)

def ParaHomeView(Request):
    template = 'chicks/para_home.html'
    context = {}

    return render (Request, template, context)

def TransHomeView(Request):
    template = 'chicks/trans_home.html'
    context = {}

    return render (Request, template, context)

def FarmProjHomeView(Request):
    template = 'chicks/farmproj.html'
    context = {}

    return render (Request, template, context)

def MyStoreView(Request):
    template = 'chicks/mystore1.html'
    context = {}

    return render (Request, template, context)

def StoreParamView(Request):
    template = 'chicks/storeparams.html'
    context = {}

    return render (Request, template, context)

def StoreTransView(Request):
    template = 'chicks/storestrans.html'
    context = {}

    return render (Request, template, context)

# home view for BenefitType. BenefitType are displayed in a list

# home view for Qualification. Qualification are displayed in a list
class QualificationIndexView(ListView):
    template_name = 'chicks/qualification/index.html'
    context_object_name = 'Qualification_list'

    def get_queryset(self):
        return Qualification.objects.all()

# Detail view (view Qualification detail)
class QualificationDetailView(DetailView):
    model = Qualification
    template_name = 'chicks/qualification/qualification-detail.html'

# New Qualification view (Create new Qualification)
def QualificationView(request):
    if request.method == 'POST':
        form = QualificationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('qualification')
    form = QualificationForm()
    return render(request, 'chicks/qualification/qualification.html', {'form': form})

# Edit a Qualification
def EditQualification(request, pk, template_name='chicks/qualification/edit.html'):
    qualification = get_object_or_404(Qualification, pk=pk)
    form = QualificationForm(request.POST or None, instance=qualification)
    if form.is_valid():
        form.save()
        return redirect('qualification')
    return render(request, template_name, {'form': form})

# Delete Qualification
def DeleteQualification(request, pk, template_name='chicks/qualification/confirm_delete.html'):
    qualification = get_object_or_404(Qualification, pk=pk)
    if request.method == 'POST':
        qualification.delete()
        return redirect('qualification')
    return render(request, template_name, {'object': qualification})

# home view for Country. Country are displayed in a list
class CountryIndexView(ListView):
    template_name = 'chicks/country/index.html'
    context_object_name = 'Country_list'

    def get_queryset(self):
        return Country.objects.all()

# Detail view (view Country detail)
class CountryDetailView(DetailView):
    model = Country
    template_name = 'chicks/country/country-detail.html'

# New Country view (Create new Country)
def CountryView(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('country')
    form = CountryForm()
    return render(request, 'chicks/country/custorders.html', {'form': form})

# Edit a Country
def EditCountry(request, pk, template_name='chicks/country/edit.html'):
    country = get_object_or_404(Country, pk=pk)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        form.save()
        return redirect('country')
    return render(request, template_name, {'form': form})

# Delete Country
def DeleteCountry(request, pk, template_name='chicks/country/confirm_delete.html'):
    country = get_object_or_404(Country, pk=pk)
    if request.method == 'POST':
        country.delete()
        return redirect('country')
    return render(request, template_name, {'object': country})

# home view for Region. Region are displayed in a list
class RegionIndexView(ListView):
    template_name = 'chicks/region/index.html'
    context_object_name = 'Region_list'

    def get_queryset(self):
        return Region.objects.filter(rg_co_code=self.kwargs['pk'])

# Detail view (view Region detail)
class RegionDetailView(DetailView):
    model = Region
    template_name = 'chicks/region/region-detail.html'

# New Region view (Create new Region)
def RegionView1(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('region')
    form = RegionForm()
    return render(request, 'chicks/region/region.html', {'form': form})

def RegionView(request, pk):
    country = Country.objects.get(pk=pk)

    new_region = None
    if request.method == 'POST':

        form = RegionForm(data=request.POST or None)

        if form.is_valid():
            # Create an Region object but don't save to database yet
            new_region = form.save(commit=False)
            new_region.rg_co_code = country
            new_region.save()
            messages.success(request, "Region created successfully")
        return redirect('country')
    else:
        form = RegionForm()
    return render(request,  'chicks/region/region.html', {'form': form})

# Edit a Region
def EditRegion(request, pk, template_name='chicks/region/edit.html'):
    region = get_object_or_404(Region, pk=pk)
    form = RegionForm_e(request.POST or None, instance=region)
    if form.is_valid():
        form.save()
        return redirect('region')
    return render(request, template_name, {'form': form})

# Delete Region
def DeleteRegion(request, pk, template_name='chicks/region/confirm_delete.html'):
    region = get_object_or_404(Region, pk=pk)
    if request.method == 'POST':
        region.delete()
        return redirect('region')
    return render(request, template_name, {'object': region})

# home view for Town. Town are displayed in a list
class TownIndexView(ListView):
    template_name = 'chicks/town/index.html'
    context_object_name = 'Town_list'

    def get_queryset(self):
        return Town.objects.filter(to_rg_code=self.kwargs['pk'])

  # Detail view (view Town detail)
class TownDetailView(DetailView):
    model = Town
    template_name = 'chicks/town/town-detail.html'

# New Town view (Create new Town)
def TownView1(request):
    if request.method == 'POST':
        form = TownForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('town')
    form = TownForm()
    return render(request, 'chicks/town/town.html', {'form': form})

def TownView(request, pk):
    region = Region.objects.get(pk=pk)

    new_town = None
    if request.method == 'POST':

        form = TownForm(data=request.POST or None)

        if form.is_valid():
            # Create a Town object but don't save to database yet
            new_town = form.save(commit=False)
            new_town.to_rg_code = region
            new_town.save()
            messages.success(request, "Town created successfully")
        return redirect('region')
    else:
        form = TownForm()
    return render(request, 'chicks/town/town.html', {'form': form})

# Edit a Town
def EditTown(request, pk, template_name='chicks/town/edit.html'):
    town = get_object_or_404(Town, pk=pk)
    form = TownForm_e(request.POST or None, instance=town)
    if form.is_valid():
        form.save()
        return redirect('town')
    return render(request, template_name, {'form': form})

# Delete Town
def DeleteTown(request, pk, template_name='chicks/town/confirm_delete.html'):
    town = get_object_or_404(Town, pk=pk)
    if request.method == 'POST':
        town.delete()
        return redirect('town')
    return render(request, template_name, {'object': town})

# home view for District. District are displayed in a list
class DistrictIndexView(ListView):
    template_name = 'chicks/district/index.html'
    context_object_name = 'District_list'

    def get_queryset(self):
        return District.objects.filter(dt_to_code=self.kwargs['pk'])

 # Detail view (view District detail)
class DistrictDetailView(DetailView):
    model = District
    template_name = 'chicks/district/district-detail.html'

# New District view (Create new District)
def DistrictView1(request):
    if request.method == 'POST':
        form = DistrictForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('district')
    form = DistrictForm()
    return render(request, 'chicks/district/district.html', {'form': form})

def DistrictView(request, pk):
    town = Town.objects.get(pk=pk)
    region = Region.objects.get(pk=town.to_rg_code_id)
    country = Country.objects.get(pk=region.rg_co_code_id)

    new_district = None
    if request.method == 'POST':

        form = DistrictForm(data=request.POST or None)

        if form.is_valid():
            # Create a District object but don't save to database yet
            new_district = form.save(commit=False)
            new_district.dt_to_code = town
            new_district.dt_rg_code = town.to_rg_code
            new_district.dt_co_code = country

            new_district.save()
            messages.success(request, "District created successfully")
        return redirect('town')
    else:
        form = DistrictForm()
    return render(request, 'chicks/district/district.html', {'form': form})

# Edit a District
def EditDistrict(request, pk, template_name='chicks/district/edit.html'):
    district = get_object_or_404(District, pk=pk)
    form = DistrictForm_e(request.POST or None, instance=district)
    if form.is_valid():
        form.save()
        return redirect('district')
    return render(request, template_name, {'form': form})

# Delete District
def DeleteDistrict(request, pk, template_name='chicks/district/confirm_delete.html'):
    district = get_object_or_404(District, pk=pk)
    if request.method == 'POST':
        district.delete()
        return redirect('district')
    return render(request, template_name, {'object': district})

# home view for Ward. Ward are displayed in a list
class WardIndexView(ListView):
    template_name = 'chicks/ward/index.html'
    context_object_name = 'Ward_list'

    def get_queryset(self):
        return Ward.objects.filter(wd_dt_code=self.kwargs['pk'])

# Detail view (view Ward detail)
class WardDetailView(DetailView):
    model = Ward
    template_name = 'chicks/ward/ward-detail.html'

# New Ward view (Create new Ward)
def WardView1(request, pk):
    if request.method == 'POST':
        form = WardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ward')
    form = WardForm()
    return render(request, 'chicks/ward/ward.html', {'form': form})

def WardView2(request):
    if request.method == 'POST':
        form = WardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('ward')
    form = WardForm()
    return render(request, 'chicks/ward/ward.html', {'form': form})

def WardView(request, pk):
    district = District.objects.get(pk=pk)

    new_ward = None
    if request.method == 'POST':

        form = WardForm(data=request.POST or None)

        if form.is_valid():
            # Create a Ward object but don't save to database yet
            new_ward = form.save(commit=False)
            new_ward.wd_dt_code = district
            new_ward.wd_rg_code = district.dt_rg_code
            new_ward.wd_to_code = district.dt_to_code

            new_ward.save()
            messages.success(request, "Ward created successfully")
        return redirect('district')
    else:
        form = WardForm()
    return render(request, 'chicks/ward/ward.html', {'form': form})

# Edit a Ward
def EditWard(request, pk, template_name='chicks/ward/edit.html'):
    ward = get_object_or_404(Ward, pk=pk)
    form = WardForm_e(request.POST or None, instance=ward)
    if form.is_valid():
        form.save()
        return redirect('ward')
    return render(request, template_name, {'form': form})

# Delete Ward
def DeleteWard(request, pk, template_name='chicks/ward/confirm_delete.html'):
    ward = get_object_or_404(Ward, pk=pk)
    if request.method == 'POST':
        ward.delete()
        return redirect('ward')
    return render(request, template_name, {'object': ward})

# home view for Village. Village are displayed in a list
class VillageIndexView(ListView):
    template_name = 'chicks/village/index.html'
    context_object_name = 'Village_list'

    def get_queryset(self):
        return Village.objects.filter(vg_wd_code=self.kwargs['pk'])

# Detail view (view Village detail)
class VillageDetailView(DetailView):
    model = Village
    template_name = 'chicks/village/village-detail.html'

# New Village view (Create new Village)
def VillageView1(request):
    if request.method == 'POST':
        form = VillageForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('village')
    form = VillageForm()
    return render(request, 'chicks/village/village.html', {'form': form})

def VillageView(request, pk):
    ward = Ward.objects.get(pk=pk)

    new_village = None
    if request.method == 'POST':

        form = VillageForm(data=request.POST or None)

        if form.is_valid():
            # Create a Village object but don't save to database yet
            new_village = form.save(commit=False)
            new_village.vg_wd_code = ward
            new_village.vg_rg_code = ward.wd_rg_code
            new_village.vg_to_code = ward.wd_to_code
            new_village.vg_dt_code = ward.wd_dt_code

            new_village.save()
            messages.success(request, "Village created successfully")
        return redirect('village')
    else:
        form = VillageForm()
    return render(request, 'chicks/village/village.html', {'form': form})

# Edit a Village
def EditVillage(request, pk, template_name='chicks/village/edit.html'):
    village = get_object_or_404(Village, pk=pk)
    form = VillageForm_e(request.POST or None, instance=village)
    if form.is_valid():
        form.save()
        return redirect('village')
    return render(request, template_name, {'form': form})

# Delete Village
def DeleteVillage(request, pk, template_name='chicks/village/confirm_delete.html'):
    village = get_object_or_404(Village, pk=pk)
    if request.method == 'POST':
        village.delete()
        return redirect('village')
    return render(request, template_name, {'object': village})

# home view for grade. grade are displayed in a list
class GradeIndexView(ListView):
    template_name = 'chicks/grade/index.html'
    context_object_name = 'Grade_list'

    def get_queryset(self):
        return Grade.objects.all()

# Detail view (view grade detail)
class GradeDetailView(DetailView):
    model = Grade
    template_name = 'chicks/grade/grade-detail.html'

# New grade view (Create new grade)
def GradeView(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('grade')
    form = GradeForm()
    return render(request, 'chicks/grade/grade.html', {'form': form})

# Edit a grade
def EditGrade(request, pk, template_name='chicks/grade/edit.html'):
    grade = get_object_or_404(Grade, pk=pk)
    form = GradeForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        return redirect('grade')
    return render(request, template_name, {'form': form})

# Delete grade
def DeleteGrade(request, pk, template_name='chicks/grade/confirm_delete.html'):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade')
    return render(request, template_name, {'object': grade})

# home view for ContractType. ContractType are displayed in a list
class ContractTypeIndexView(ListView):
    template_name = 'chicks/contracttype/index.html'
    context_object_name = 'ContractType_list'

    def get_queryset(self):
        return ContractType.objects.all()

# Detail view (view ContractType detail)
class ContractTypeDetailView(DetailView):
    model = ContractType
    template_name = 'chicks/contracttype/contracttype-detail.html'

# New ContractType view (Create new ContractType)
def ContractTypeView(request):
    if request.method == 'POST':
        form = ContractTypeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contracttype')
    form = ContractTypeForm()
    return render(request, 'chicks/contracttype/contracttype.html', {'form': form})

# Edit a ContractType
def EditContractType(request, pk, template_name='chicks/contracttype/edit.html'):
    contracttype = get_object_or_404(ContractType, pk=pk)
    form = ContractTypeForm(request.POST or None, instance=contracttype)
    if form.is_valid():
        form.save()
        return redirect('contracttype')
    return render(request, template_name, {'form': form})

# Delete ContractType
def DeleteContractType(request, pk, template_name='chicks/contracttype/confirm_delete.html'):
    contracttype = get_object_or_404(ContractType, pk=pk)
    if request.method == 'POST':
        contracttype.delete()
        return redirect('contracttype')
    return render(request, template_name, {'object': contracttype})

# home view for Member. Member are displayed in a list
class MemberIndexView(ListView):
    template_name = 'chicks/member/index.html'
    context_object_name = 'Member_list'

    def get_queryset(self):
        return Member.objects.all()

# Detail view (view Member detail)
class MemberDetailView(DetailView):
    model = Member
    template_name = 'chicks/member/member-detail.html'

# New Member view (Create new Member)
def MemberView(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('member')
    form = MemberForm()
    return render(request, 'chicks/member/member.html', {'form': form})

# Edit a Member
def EditMember(request, pk, template_name='chicks/member/edit.html'):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('member')
    return render(request, template_name, {'form': form})

# Delete Member
def DeleteMember(request, pk, template_name='chicks/member/confirm_delete.html'):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        Member.delete()
        return redirect('member')
    return render(request, template_name, {'object': member})

# home view for Employee. Employee are displayed in a list
class EmployeeIndexView(ListView):
    template_name = 'chicks/employee/index.html'
    context_object_name = 'Employee_list'

    def get_queryset(self):
        return Employee.objects.all()

# Detail view (view Employee detail)
class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'chicks/employee/employee-detail.html'

# New Employee view (Create new Employee)
def EmployeeView1(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee')
    form = EmployeeForm()
    return render(request, 'chicks/employee/employee.html', {'form': form})

def EmployeeView(request, pk):

    member = Member.objects.get(pk=pk)

    new_employee = None
    if request.method == 'POST':

        form = EmployeeForm(data=request.POST or None)

        if form.is_valid():
            # Create an employee Instance object but don't save to database yet
            new_employee = form.save(commit=False)
            new_employee.ee_ey_num = member

            new_employee.save()
            messages.success(request, "Employee Instance created successfully")
        return redirect('member')
    else:
        form = EmployeeForm
    return render(request, 'chicks/employee/employee.html', {'form': form})

# Edit a Employee
def EditEmployee(request, pk, template_name='chicks/employee/edit.html'):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm_e(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee')
    return render(request, template_name, {'form': form})

# Delete Employee
def DeleteEmployee(request, pk, template_name='chicks/employee/confirm_delete.html'):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee')
    return render(request, template_name, {'object': employee})

#Start Of Farming projects Views

# home view for Holding. Holding are displayed in a list

class HoldingIndexView(ListView):
    template_name = 'chicks/holding/index.html'
    context_object_name = 'Holding_list'

    def get_queryset(self):
        return Holding.objects.all()

# Detail view (view Holding detail)
class HoldingDetailView(DetailView):
    model = Holding
    template_name = 'chicks/holding/holding-detail.html'

# New Holding view (Create new Holding)
def HoldingView(request):
    if request.method == 'POST':
        form = HoldingForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('holding')
    form = HoldingForm()
    return render(request, 'chicks/holding/holding.html', {'form': form})

# Edit a Holding
def EditHolding(request, pk, template_name='chicks/holding/edit.html'):
    holding = get_object_or_404(Holding, pk=pk)
    form = HoldingForm(request.POST or None, instance=holding)
    if form.is_valid():
        form.save()
        return redirect('holding')
    return render(request, template_name, {'form': form})

# Delete Holding
def DeleteHolding(request, pk, template_name='chicks/holding/confirm_delete.html'):
    holding = get_object_or_404(Holding, pk=pk)
    if request.method == 'POST':
        holding.delete()
        return redirect('holding')
    return render(request, template_name, {'object': holding})

# home view for HoldingInstance. HoldingInstance are displayed in a list

class HoldingInstanceIndexView(ListView):
    template_name = 'chicks/holdinginstance/index.html'
    context_object_name = 'HoldingInstance_list'

    def get_queryset(self):
        return HoldingInstance.objects.filter(hi_hd_num=self.kwargs['pk']) #all()
        #return HoldingInstance.objects.all()

class HoldingInstanceIndexView_o(ListView):
    template_name = 'chicks/holdinginstance/index_o.html'
    context_object_name = 'HoldingInstance_list'

    def get_queryset(self):
        return HoldingInstance.objects.filter(hi_hd_num=self.kwargs['pk']) #all()
        #return HoldingInstance.objects.all()

# Detail view (view HoldingInstance detail)
class HoldingInstanceDetailView(DetailView):
    model = HoldingInstance
    template_name = 'chicks/holdinginstance/holdinginstance-detail.html'

# New HoldingInstance view (Create new HoldingInstance)
def HoldingInstanceView1(request):
    if request.method == 'POST':
        form = HoldingInstanceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('holdinginstance')
    form = HoldingInstanceForm()
    return render(request, 'chicks/holdinginstance/stockloc.html', {'form': form})

def HoldingInstanceView(request, pk):
    holding = Holding.objects.get(pk=pk)

    new_holdinginstance = None
    if request.method == 'POST':

        form = HoldingInstanceForm(data=request.POST or None)

        if form.is_valid():
            # Create a Holding Instance object but don't save to database yet
            new_holdinginstance = form.save(commit=False)
            new_holdinginstance.hi_hd_num = holding

            new_holdinginstance.save()

            l_ac_date = form.cleaned_data['hi_start_date']
            no_of_days = form.cleaned_data['hi_days']
            l_hi_code = form.cleaned_data['hi_code']


            print(l_ac_date)

            # Begin Iterating for the days the activities will run
            l_ac_date = form.cleaned_data['hi_start_date']
            no_of_days = form.cleaned_data['hi_days']
            #l_hi_code = form.cleaned_data['hi_code']

            #holdinginstance = HoldingInstance.objects.filter(hi_code=l_hi_code) #.first()
            holdinginstance = HoldingInstance.objects.get(hi_code=l_hi_code)

            l_ac_type = '7'
            l_ac_day = 0
            #l_ac_date = "24/03/26"
            l_ac_o_qty = 0
            l_ac_c_qty = 0
            l_ac_t_wqt = 0
            l_ac_a_wqt = 0
            l_ac_morlity = 0
            l_ac_e_cost = 0
            l_ac_desc = 'None'
            l_ac_status = '1'
            l_ac_remark = 'None'

            #no_of_days = 35
            cnt = 0

            while cnt <= no_of_days:
                c_activity = Activity()
                c_activity.ac_hi_num   =  holdinginstance
                c_activity.ac_type = l_ac_type
                c_activity.ac_day = l_ac_day
                c_activity.ac_date = l_ac_date
                c_activity.ac_o_qty = l_ac_o_qty
                c_activity.ac_c_qty = l_ac_c_qty
                c_activity.ac_t_wqt = l_ac_t_wqt
                c_activity.ac_a_wqt = l_ac_a_wqt
                c_activity.ac_morlity = l_ac_morlity
                c_activity.ac_e_cost = l_ac_e_cost
                c_activity.ac_desc = l_ac_desc
                c_activity.ac_status = l_ac_status
                c_activity.ac_remark = l_ac_remark

                c_activity.ac_pstart_date = l_ac_date
                c_activity.ac_pend_date = l_ac_date
                c_activity.ac_astart_date = l_ac_date
                c_activity.ac_aend_date = l_ac_date

                c_activity.save()

                l_ac_day = l_ac_day + 1
                cnt     = (cnt + 1)
                l_ac_date = l_ac_date + datetime.timedelta(days=1)
                print(l_ac_day)
                print(cnt)

            messages.success(request, "Holding Instance created successfully")
        return redirect('holding')
    else:
        form = HoldingInstanceForm()
    return render(request, 'chicks/holdinginstance/holdinginstance.html', {'form': form})

# Edit a HoldingInstance
def EditHoldingInstance(request, pk, template_name='chicks/holdinginstance/edit.html'):
    holdinginstance = get_object_or_404(Holding, pk=pk)
    form = HoldingInstanceForm(request.POST or None, instance=holdinginstance)
    if form.is_valid():
        form.save()
        return redirect('holdinginstance')
    return render(request, template_name, {'form': form})

# Delete HoldingInstance
def DeleteHoldingInstance(request, pk, template_name='chicks/holdinginstance/confirm_delete.html'):
    holdinginstance = get_object_or_404(HoldingInstance, pk=pk)
    if request.method == 'POST':
        holdinginstance.delete()
        return redirect('holdinginstance')
    return render(request, template_name, {'object': holdinginstance})

# home view for Activity. Activity are displayed in a list

class ActivityIndexView(ListView):
    template_name = 'chicks/activity/index.html'
    context_object_name = 'Activity_list'

    def get_queryset(self):
        return Activity.objects.filter(ac_hi_num=self.kwargs['pk']) #all()

def ActivityIndexView1(request, pk):

    Activity_list = Activity.objects.filter(ac_hi_num=pk) #all()
    template_name = 'chicks/activity/index.html'
    context = {'Ativity_list' : 'Activity_list'}

    return render(request, template_name, context)

class ActivityIndexView_r(ListView):
    template_name = 'chicks/activity/index_r.html'
    context_object_name = 'Activity_list'

    def get_queryset(self):
        return Activity.objects.filter(ac_hi_num=self.kwargs['pk'])  # all()

# Detail view (view Activity detail)
class ActivityDetailView(DetailView):
    model = Activity
    template_name = 'chicks/activity/activity-detail.html'

# New Activity view (Create new Activity)
def ActivityView1(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('activity')
    form = ActivityForm()
    return render(request, 'chicks/activity/activity.html', {'form': form})

def ActivityView(request, pk):
    holdinginstance = HoldingInstance.objects.get(pk=pk)

    new_activity = None
    if request.method == 'POST':

        form = ActivityForm(data=request.POST or None)

        if form.is_valid():
            # Create an Activity Instance object but don't save to database yet
            new_activity = form.save(commit=False)
            new_activity.ac_hi_num = holdinginstance

            new_activity.save()
            messages.success(request, "Activity Instance created successfully")
        return redirect('holdinginstance')
    else:
        form = ActivityForm()
    return render(request, 'chicks/activity/activity.html', {'form': form})

# Edit a Activity
def EditActivity(request, pk, template_name='chicks/activity/edit.html'):
    activity = get_object_or_404(Activity, pk=pk)
    form = ActivityForm(request.POST or None, instance=activity)
    if form.is_valid():
        form.save()
        #return render(request, template_name, {'form': form})#redirect('activity_r')
        return redirect('activity', pk)
    return render(request, template_name, {'form': form})

# Delete Activity
def DeleteActivity(request, pk, template_name='chicks/activity/confirm_delete.html'):
    activity = get_object_or_404(Activity, pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('activity')
    return render(request, template_name, {'object': activity})

# home view for Note. Notes are displayed in a list

class NoteIndexView(ListView):
    template_name = 'chicks/note/index.html'
    context_object_name = 'Note_list'

    def get_queryset(self):
        return Note.objects.filter(nt_ac_num=self.kwargs['pk'])  # all()

# Detail view (view Note detail)
class NoteDetailView(DetailView):
    model = Note
    template_name = 'chicks/note/note-detail.html'

# New Note view (Create new Note)
def NoteView1(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('holding')
    form = NoteForm()
    return render(request, 'chicks/note/note.html', {'form': form})

def NoteView(request, pk):
    activity = Activity.objects.get(pk=pk)

    new_note = None
    if request.method == 'POST':

        form = NoteForm(data=request.POST or None)

        if form.is_valid():
            # Create a Note Instance object but don't save to database yet
            new_note = form.save(commit=False)
            new_note.nt_ac_num = activity

            new_note.save()
            messages.success(request, "Note Instance created successfully")
        return redirect('activity_n', pk)
    else:
        form = NoteForm()
    return render(request,  'chicks/note/note.html', {'form': form})

# Edit a Note
def EditNote(request, pk, template_name='chicks/note/edit.html'):
    note = get_object_or_404(Note, pk=pk)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('activity_n',pk)
    return render(request, template_name, {'form': form})

# Delete Note
def DeleteNote(request, pk, template_name='chicks/note/confirm_delete.html'):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note')
    return render(request, template_name, {'object': note})

# home view for Resource. Resource are displayed in a list

class ResourceIndexView(ListView):
    template_name = 'chicks/resource/index.html'
    context_object_name = 'Resource_list'

    def get_queryset(self):
        return Resource.objects.filter(rs_ac_num=self.kwargs['pk'])  # all()
        #return Resource.objects.all()

# Detail view (view Resource detail)
class ResourceDetailView(DetailView):
    model = Resource
    template_name = 'chicks/resource/resource-detail.html'

# New Resource view (Create new Resource)
def ResourceView1(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('resource')
    form = ResourceForm()
    return render(request, 'chicks/resource/resource.html', {'form': form})

def ResourceView(request, pk):
    activity = Activity.objects.get(pk=pk)

    new_resource = None
    if request.method == 'POST':

        form = ResourceForm(data=request.POST or None)

        if form.is_valid():
            # Create a Resource Instance object but don't save to database yet
            new_resource = form.save(commit=False)
            new_resource.rs_ac_num = activity

            new_resource.save()
            messages.success(request, "Resource object created successfully")
        return redirect('holding')
    else:
        form = ResourceForm()
    return render(request,  'chicks/resource/resource.html', {'form': form})

# Edit a Resource
def EditResource(request, pk, template_name='chicks/resource/edit.html'):
    resource = get_object_or_404(Resource, pk=pk)
    form = ResourceForm(request.POST or None, instance=resource)
    if form.is_valid():
        form.save()
        return redirect('activity_r', pk)
    return render(request, template_name, {'form': form})

# Delete Resource
def DeleteResource(request, pk, template_name='chicks/resource/confirm_delete.html'):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        resource.delete()
        return redirect('resource')
    return render(request, template_name, {'object': resource})

# home view for OutPut. OutPut are displayed in a list

class OutPutIndexView(ListView):
    template_name = 'chicks/output/index.html'
    context_object_name = 'OutPut_list'

    def get_queryset(self):
        return OutPut.objects.all()

# Detail view (view OutPut detail)
class OutPutDetailView(DetailView):
    model = OutPut
    template_name = 'chicks/output/output-detail.html'

# New OutPut view (Create new OutPut)
def OutPutView1(request):
    if request.method == 'POST':
        form = OutPutForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('output')
    form = OutPutForm()
    return render(request, 'chicks/output/output.html', {'form': form})

def OutPutView(request, pk):
    holdinginstance = HoldingInstance.objects.get(pk=pk)

    new_output = None
    if request.method == 'POST':

        form = OutPutForm(data=request.POST or None)

        if form.is_valid():
            # Create an Output Instance object but don't save to database yet
            new_output = form.save(commit=False)
            new_output.op_hi_num = holdinginstance

            new_output.save()
            messages.success(request, "Output Instance created successfully")
        return redirect('holdinginstance', pk)
    else:
        form = OutPutForm()
    return render(request, 'chicks/output/output.html', {'form': form})

# Edit a OutPut
def EditOutPut(request, pk, template_name='chicks/output/edit.html'):
    output = get_object_or_404(OutPut, pk=pk)
    form = OutPutForm(request.POST or None, instance=output)
    if form.is_valid():
        form.save()
        return redirect('holdinginstance', pk)
    return render(request, template_name, {'form': form})

# Delete OutPut
def DeleteOutPut(request, pk, template_name='chicks/output/confirm_delete.html'):
    output = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        output.delete()
        return redirect('output')
    return render(request, template_name, {'object': output})

# home view for CustOrders. CustOrders are displayed in a list

class CustOrdersIndexView(ListView):
    template_name = 'chicks/custorders/index.html'
    context_object_name = 'CustOrders_list'

    def get_queryset(self):
        return CustOrders.objects.all()

# Detail view (view CustOrders detail)
class CustOrdersDetailView(DetailView):
    model = CustOrders
    template_name = 'chicks/custorders/custorders-detail.html'

# New CustOrders view (Create new CustOrders)
def CustOrdersView(request):
    if request.method == 'POST':
        form = CustOrdersForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('custorders')
    form = CustOrdersForm()
    return render(request, 'chicks/custorders/custorders.html', {'form': form})

# Edit a CustOrders
def EditCustOrders(request, pk, template_name='chicks/custorders/edit.html'):
    custorders = get_object_or_404(CustOrders, pk=pk)
    form = CustOrdersForm(request.POST or None, instance=custorders)
    if form.is_valid():
        form.save()
        return redirect('custorders')
    return render(request, template_name, {'form': form})

# Delete CustOrders
def DeleteCustOrders(request, pk, template_name='chicks/custorders/confirm_delete.html'):
    custorders = get_object_or_404(CustOrders, pk=pk)
    if request.method == 'POST':
        custorders.delete()
        return redirect('custorders')
    return render(request, template_name, {'object': custorders})

#Reports

def SpotFlashView(request):
        # global l_gr_num

    dataset = Activity.objects.values('ac_hi_num').annotate(
            tot_num=Max('ac_o_qty'), mort_sum=Sum('ac_morlity'), avail_sum=(Max('ac_o_qty') - Sum('ac_morlity')),\
            wgt_sum=Avg('ac_a_wqt')).order_by('ac_hi_num')

    batch = list()
    tot_series_data = list()
    mort_series_data = list()
    avail_series_data = list()
    wgt_series_data = list()

    for entry in dataset:
        batch.append('%s Batch' % entry['ac_hi_num'])

        tot = entry['tot_num']
        if tot is None:
            tot = 0
        tot = float(tot)

        print (tot)

        mort = entry['mort_sum']
        if mort is None:
            mort = 0
        mort = abs(float(mort))

        avail = entry['avail_sum']
        if avail is None:
            avail = 0
        avail = abs(float(avail))

        wgt = entry['wgt_sum']
        if wgt is None:
            wgt = 0
        wgt = abs(float(wgt))

        tot_series_data.append(tot)
        mort_series_data.append(mort)
        avail_series_data.append(avail)
        wgt_series_data.append(wgt)

    tot_series_data = {
        'name': 'Batch Size',
        'data': tot_series_data,
        'color': 'purple'
    }

    mort_series_data = {
        'name': 'Mortality',
        'data': mort_series_data,
        'color': 'red'
    }

    avail_series_data = {
            'name': 'Available',
            'data': avail_series_data,
            'color': 'green'
        }

    wgt_series_data = {
        'name': 'Weight',
        'data': wgt_series_data,
        'color': 'black'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Spot Flash'},
        'xAxis': {'Batch': batch},
        'series': [tot_series_data, mort_series_data, avail_series_data, wgt_series_data]
    }

    dump = json.dumps(chart, cls=DecimalEncoder)

    return render(request, 'chicks/reports/charts/s_flash.html', {'chart': dump})

def SpotFlashView1(request):

        # global l_gr_num

        dataset = Activity.objects.values('ac_hi_num__hi_code').annotate(
            tot_num=Max('ac_o_qty'), mort_sum=Sum('ac_morlity'), avail_sum=(Max('ac_o_qty') - Sum('ac_morlity')), \
            wgt_sum=Avg('ac_a_wqt')).order_by('ac_hi_num')

        return render(request, 'chicks/reports/charts/s_flash1.html', {'dataset': dataset})

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        #  if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

class CustOrdersHTMxTableView(SingleTableMixin, FilterView):
    table_class = CustOrdersHTMxTable
    queryset = CustOrders.objects.values('od_num','od_hi_num','od_Custname','od_phone','od_trans_date','od_item','od_unit','od_qty',
			'od_unit_p','ot_status','ot_paid')
    filterset_class = CustOrdersFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "chicks/CustOrders_table_partial.html"
        else:
            template_name = "chicks/CustOrders_table_htmx.html"

        return template_name

class TransHTMxTableView(SingleTableMixin, FilterView):
    #global l_gr_num
    #l_gr_num = 1

    table_class = CustOrdersHTMxTable
    queryset = CustOrders.objects.values('od_num','od_hi_num','od_Custname','od_phone','od_trans_date','od_item','od_unit','od_qty',
			'od_unit_p','ot_status','ot_paid')
    filterset_class = CustOrdersFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "chicks/cust_order_partial.html"
        else:
            template_name = "chicks/cust_order_htmx.html"

        return template_name

# This class will create the table just like how we create forms
class OrdersHTMxTable(tables.Table):
   class Meta:
        model = CustOrders
        fields = ('od_num','od_hi_num','od_Custname','od_phone','od_trans_date','od_item','od_unit','od_qty',
			'od_unit_p','ot_status','ot_paid')

   paginate_by = 20

# This View will render table
class OrdersHTMxTableView(tables.SingleTableView):
    global l_gr_num

    table_class = OrdersHTMxTable
    def get_queryset(self):
        return CustOrders.objects.values('od_num','od_hi_num','od_Custname','od_phone','od_trans_date','od_item','od_unit','od_qty',
			'od_unit_p','ot_status','ot_paid')

    template_name = "chicks/custorders.html"

def MyOrdersView(request):
        #global l_gr_num

        total = 0
        myorders = CustOrders.objects.values('od_num','od_hi_num__hi_code','od_Custname','od_phone',
                                    'od_trans_date','od_item','od_unit','od_qty','od_unit_p',
                                    'ot_status','ot_paid').annotate(tot=Sum(F('od_qty') * F('od_unit_p')))

        my_orders = CustOrdersFilter(request.GET, queryset=myorders)
        total_qty = my_orders.qs.aggregate(Totqty=Sum('od_qty'))
        total_val = my_orders.qs.aggregate(Totval=Sum('tot'))

        context = {'filter': my_orders, 'total_qty': total_qty, 'total_val': total_val}

        return render(request, 'chicks/reports/myorders.html', context)

#Stores management views start here

# home view for PackType. PackType are displayed in a list
class PackTypeIndexView(ListView):
    template_name = 'chicks/PackType/index.html'
    context_object_name = 'PackType_list'

    def get_queryset(self):
        return PackType.objects.all()

# Detail view (view PackType detail)
class PackTypeDetailView(DetailView):
    model = PackType
    template_name = 'chicks/PackType/PackType-detail.html'

# New PackType view (Create new PackType)
def PackTypeView(request):
    if request.method == 'POST':
        form = PackTypeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('packtype')
    form = PackTypeForm()
    return render(request, 'chicks/PackType/PackType.html', {'form': form})

# Edit a PackType
def EditPackType(request, pk, template_name='chicks/PackType/edit.html'):
    packtype = get_object_or_404(PackType, pk=pk)
    form = PackTypeForm(request.POST or None, instance=packtype)
    if form.is_valid():
        form.save()
        return redirect('packtype')
    return render(request, template_name, {'form': form})

# Delete PackType
def DeletePackType(request, pk, template_name='chicks/PackType/confirm_delete.html'):
    packtype = get_object_or_404(PackType, pk=pk)
    if request.method == 'POST':
        packtype.delete()
        return redirect('packtype')
    return render(request, template_name, {'object': packtype})

# home view for Currency. Currency are displayed in a list
class CurrencyIndexView(ListView):
    template_name = 'chicks/Currency/index.html'
    context_object_name = 'Currency_list'

    def get_queryset(self):
        return Currency.objects.all()

# Detail view (view Currency detail)
class CurrencyDetailView(DetailView):
    model = Currency
    template_name = 'chicks/Currency/Currency-detail.html'

# New Currency view (Create new Currency)
def CurrencyView(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('currency')
    form = CurrencyForm()
    return render(request, 'chicks/Currency/Currency.html', {'form': form})

# Edit a Currency
def EditCurrency(request, pk, template_name='chicks/Currency/edit.html'):
    currency = get_object_or_404(Currency, pk=pk)
    form = CurrencyForm(request.POST or None, instance=currency)
    if form.is_valid():
        form.save()
        return redirect('currency')
    return render(request, template_name, {'form': form})

# Delete Currency
def DeleteCurrency(request, pk, template_name='chicks/Currency/confirm_delete.html'):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('currency')
    return render(request, template_name, {'object': currency})

# home view for StoreName. StoreName are displayed in a list
class StoreNameIndexView(ListView):
    template_name = 'chicks/StoreName/index.html'
    context_object_name = 'StoreName_list'

    def get_queryset(self):
        return StoreName.objects.all()

class StoreName1IndexView(ListView):
    template_name = 'chicks/StoreName/index.html'
    context_object_name = 'StoreName_list'

    def get_queryset(self):
        return StoreName.objects.filter(sn_code=self.kwargs['pk'])

# Detail view (view StoreName detail)
class StoreNameDetailView(DetailView):
    model = StoreName
    template_name = 'chicks/StoreName/StoreName-detail.html'

# New StoreName view (Create new StoreName)
def StoreNameView(request):
    if request.method == 'POST':
        form = StoreNameForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('storename')
    form = StoreNameForm()
    return render(request, 'chicks/StoreName/StoreName.html', {'form': form})

def StoreNameView1(request, pk):

    new_storename = None
    if request.method == 'POST':

        form = StoreNameForm(data=request.POST or None)

        if form.is_valid():
            # Create a StoreName object but don't save to database yet
            new_storename = form.save(commit=False)

            new_storename.save()
            messages.success(request, "Store Name created successfully")
        return redirect('storename')
    else:
        form = StoreNameForm()
    return render(request, 'chicks/StoreName/StoreName.html', {'form': form})

# Edit a StoreName
def EditStoreName(request, pk, template_name='chicks/StoreName/edit.html'):
    storename = get_object_or_404(StoreName, pk=pk)
    form = StoreNameForm(request.POST or None, instance=StoreName)
    if form.is_valid():
        form.save()
        return redirect('storename')
    return render(request, template_name, {'form': form})

# Delete StoreName
def DeleteStoreName(request, pk, template_name='chicks/StoreName/confirm_delete.html'):
    storename = get_object_or_404(StoreName, pk=pk)
    if request.method == 'POST':
        storename.delete()
        return redirect('storename')
    return render(request, template_name, {'object': storename})

# home view for StockLoc. StockLoc are displayed in a list
class StockLocIndexView(ListView):
    template_name = 'chicks/StockLoc/index.html'
    context_object_name = 'StockLoc_list'

    def get_queryset(self):
        return StockLoc.objects.filter(sl_sn_code=self.kwargs['pk'])

class StockLocAllIndexView(ListView):
    template_name = 'chicks/StockLoc/index.html'
    context_object_name = 'StockLoc_list'

    def get_queryset(self):
        return StockLoc.objects.all()

# Detail view (view StockLoc detail)
class StockLocDetailView(DetailView):
    model = StockLoc
    template_name = 'chicks/StockLoc/StockLoc-detail.html'

# New StockLoc view (Create new StockLoc)
def StockLocView1(request):
    if request.method == 'POST':
        form = StockLocForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('stockloc')
    form = StockLocForm()
    return render(request, 'chicks/StockLoc/StockLoc.html', {'form': form})

def StockLocView(request, pk):
    storename = StoreName.objects.get(pk=pk)

    new_stockloc = None
    if request.method == 'POST':

        form = StockLocForm(data=request.POST or None)

        if form.is_valid():
            # Create a StockLoc object but don't save to database yet
            new_stockloc = form.save(commit=False)
            new_stockloc.sl_sn_code = storename

            new_stockloc.save()
            messages.success(request, "Stock Location created successfully")
        return redirect('storename1',pk)
    else:
        form = StockLocForm()
    return render(request, 'chicks/StockLoc/StockLoc.html', {'form': form})

# Edit a StockLoc
def EditStockLoc(request, pk, template_name='chicks/StockLoc/edit.html'):
    stockloc = get_object_or_404(StockLoc, pk=pk)
    form = StockLocForm(request.POST or None, instance=stockloc)
    if form.is_valid():
        form.save()
        return redirect('stockloc')
    return render(request, template_name, {'form': form})

# Delete StockLoc
def DeleteStockLoc(request, pk, template_name='chicks/StockLoc/confirm_delete.html'):
    stockloc = get_object_or_404(StockLoc, pk=pk)
    if request.method == 'POST':
        stockloc.delete()
        return redirect('stockloc')
    return render(request, template_name, {'object': stockloc})

# home view for StockType. StockType are displayed in a list
class StockTypeIndexView(ListView):
    template_name = 'chicks/StockType/index.html'
    context_object_name = 'StockType_list'

    def get_queryset(self):
        return StockType.objects.filter(st_sl_code=self.kwargs['pk'])

# Detail view (view StockType detail)
class StockTypeDetailView(DetailView):
    model = StockType
    template_name = 'chicks/StockType/StockType-detail.html'

# New StockType view (Create new StockType)
def StockTypeView1(request):
    if request.method == 'POST':
        form = StockTypeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('StockType')
    form = StockTypeForm()
    return render(request, 'chicks/StockType/StockType.html', {'form': form})

def StockTypeView(request, pk):
    stockloc = StockLoc.objects.get(pk=pk)

    new_stocktype = None
    if request.method == 'POST':

        form = StockTypeForm(data=request.POST or None)

        if form.is_valid():
            # Create a StockType object but don't save to database yet
            new_stocktype = form.save(commit=False)
            new_stocktype.st_sl_code = stockloc
            new_stocktype.st_sn_code = stockloc.sl_sn_code

            new_stocktype.save()
            messages.success(request, "Stock Type created successfully")
        return redirect('stockloc',pk)
    else:
        form = StockTypeForm()
    return render(request, 'chicks/StockType/StockType.html', {'form': form})

# Edit a StockType
def EditStockType(request, pk, template_name='chicks/StockType/edit.html'):
    stocktype = get_object_or_404(StockType, pk=pk)
    form = StockTypeForm(request.POST or None, instance=stocktype)
    if form.is_valid():
        form.save()
        return redirect('stockloc',pk)
    return render(request, template_name, {'form': form})

# Delete StockType
def DeleteStockType(request, pk, template_name='chicks/StockType/confirm_delete.html'):
    stocktype = get_object_or_404(StockType, pk=pk)
    if request.method == 'POST':
        stocktype.delete()
        return redirect('stockloc',pk)
    return render(request, template_name, {'object': stocktype})

# home view for StockItem. StockItem are displayed in a list
class StockItemIndexView(ListView):
    template_name = 'chicks/StockItem/index.html'
    context_object_name = 'StockItem_list'

    def get_queryset(self):
        return StockItem.objects.filter(si_st_code=self.kwargs['pk'])

# Detail view (view StockItem detail)
class StockItemDetailView(DetailView):
    model = StockItem
    template_name = 'chicks/StockItem/StockItem-detail.html'

# New StockItem view (Create new StockItem)
def StockItemView1(request):
    if request.method == 'POST':
        form = StockItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('stockitem')
    form = StockItemForm()
    return render(request, 'chicks/StockItem/StockItem.html', {'form': form})

def StockItemView(request, pk):
    stocktype = StockType.objects.get(pk=pk)

    new_stockitem = None
    if request.method == 'POST':

        form = StockItemForm(data=request.POST or None)

        if form.is_valid():
            # Create a StockItem object but don't save to database yet
            new_stockitem = form.save(commit=False)
            new_stockitem.si_st_code = stocktype
            new_stockitem.si_sn_code = stocktype.st_sn_code

            new_stockitem.save()
            messages.success(request, "Stock Item created successfully")
        return redirect('stocktype',pk)
    else:
        form = StockItemForm()
    return render(request, 'chicks/StockItem/StockItem.html', {'form': form})

# Edit a StockItem
def EditStockItem(request, pk, template_name='chicks/StockItem/edit.html'):
    stockitem = get_object_or_404(StockItem, pk=pk)
    form = StockItemForm(request.POST or None, instance=stockitem)
    if form.is_valid():
        form.save()
        return redirect('stocktype',pk)
    return render(request, template_name, {'form': form})

# Delete StockItem
def DeleteStockItem(request, pk, template_name='chicks/StockItem/confirm_delete.html'):
    stockitem = get_object_or_404(StockItem, pk=pk)
    if request.method == 'POST':
        stockitem.delete()
        return redirect('stocktype',pk)
    return render(request, template_name, {'object': stockitem})

# home view for Customer. Customer are displayed in a list
class CustomerIndexView(ListView):
    template_name = 'chicks/Customer/index.html'
    context_object_name = 'Customer_list'

    def get_queryset(self):
        return Customer.objects.filter(cs_sn_code=self.kwargs['pk'])

class CustomerAllIndexView(ListView):
    template_name = 'chicks/Customer/index.html'
    context_object_name = 'Customer_list'

    def get_queryset(self):
        return Customer.objects.all()

# Detail view (view Customer detail)
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'chicks/Customer/Customer-detail.html'

# New Customer view (Create new Customer)
def CustomerView1(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customer')
    form = CustomerForm()
    return render(request, 'chicks/Customer/Customer.html', {'form': form})

def CustomerView(request, pk):
    storename = StoreName.objects.get(pk=pk)

    new_customer = None
    if request.method == 'POST':

        form = CustomerForm(data=request.POST or None)

        if form.is_valid():
            # Create a Customer object but don't save to database yet
            new_customer = form.save(commit=False)
            new_customer.cs_sn_code = storename

            new_customer.save()
            messages.success(request, "Customer created successfully")
        return redirect('storename1',pk)
    else:
        form = CustomerForm()
    return render(request, 'chicks/Customer/Customer.html', {'form': form})

# Edit a Customer
def EditCustomer(request, pk, template_name='chicks/Customer/edit.html'):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=customer)
    if form.is_valid():
        form.save()
        return redirect('customer')
    return render(request, template_name, {'form': form})

# Delete Customer
def DeleteCustomer(request, pk, template_name='chicks/Customer/confirm_delete.html'):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('Customer')
    return render(request, template_name, {'object': customer})

# home view for StoreOrders. StoreOrders are displayed in a list
class StoreOrderIndexView(ListView):
    template_name = 'chicks/StoreOrders/index.html'
    context_object_name = 'StoreOrders_list'

    def get_queryset(self):
        return StoreOrder.objects.filter(so_cs_num=self.kwargs['pk'])

# Detail view (view StoreOrders detail)
class StoreOrderDetailView(DetailView):
    model = StoreOrder
    template_name = 'chicks/StoreOrders/StoreOrders-detail.html'

# New StoreOrders views (Create new StoreOrders)
def StoreOrderView(request):
    if request.method == 'POST':
        form = StoreOrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('storeorderall')
    form = StoreOrderForm()
    return render(request, 'chicks/StoreOrders/storeorder.html', {'form': form})

def StoreOrderPView(request, pk):
    customer = Customer.objects.get(pk=pk)

    new_storeorder = None
    if request.method == 'POST':

        form = StoreOrderForm(data=request.POST or None)

        if form.is_valid():
            # Create a StoreOrders object but don't save to database yet
            new_storeorder = form.save(commit=False)
            new_storeorder.so_cs_num = customer
            new_storeorder.so_type = customer.cs_type
            new_storeorder.so_sn_code = customer.cs_sn_code
            new_storeorder.so_p_s = 'P'

            new_storeorder.save()
            messages.success(request, "Store Order created successfully")
        return redirect('storeorder', pk)
    else:
        form = StoreOrderForm()
    return render(request, 'chicks/StoreOrders/storeorder.html', {'form': form})

def StoreOrderSView(request, pk):
    customer = Customer.objects.get(pk=pk)

    new_storeorder = None
    if request.method == 'POST':

        form = StoreOrderForm(data=request.POST or None)

        if form.is_valid():
            # Create a StoreOrders object but don't save to database yet
            new_storeorder = form.save(commit=False)
            new_storeorder.so_cs_num = customer
            new_storeorder.so_type = customer.cs_type
            new_storeorder.so_sn_code = customer.cs_sn_code
            new_storeorder.so_p_s = 'S'

            new_storeorder.save()
            messages.success(request, "Store Order created successfully")
        return redirect('storeorder', pk)
    else:
        form = StoreOrderForm()
    return render(request, 'chicks/StoreOrders/storeorder.html', {'form': form})

# Edit a StoreOrders
def EditStoreOrder(request, pk, template_name='chicks/StoreOrders/edit.html'):
    storeorder = get_object_or_404(StoreOrder, pk=pk)
    form = StoreOrderForm(request.POST or None, instance=storeorder)
    if form.is_valid():
        form.save()
        return redirect('storeorder')
    return render(request, template_name, {'form': form})

# Delete StoreOrders
def DeleteStoreOrder(request, pk, template_name='chicks/StoreOrders/confirm_delete.html'):
    storeorder = get_object_or_404(StoreOrder, pk=pk)
    if request.method == 'POST':
        storeorder.delete()
        return redirect('storeorder')
    return render(request, template_name, {'object': storeorder})

# home view for OrderItem. OrderItem are displayed in a list
class OrderItemIndexView(ListView):
    template_name = 'chicks/OrderItem/index.html'
    context_object_name = 'OrderItem_list'

    def get_queryset(self):
        return OrderItem.objects.filter(oi_so_num=self.kwargs['pk'])

# Detail view (view OrderItem detail)
class OrderItemDetailView(DetailView):
    model = OrderItem
    template_name = 'chicks/OrderItem/OrderItem-detail.html'

# New OrderItem view (Create new OrderItem)
def OrderItemView1(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('orderitem')
    form = OrderItemForm()
    return render(request, 'chicks/OrderItem/OrderItem.html', {'form': form})

def OrderItemView(request, pk,so_p_s):
    storeorder = StoreOrder.objects.get(pk=pk)
    orderupdte = StoreOrder.objects.filter(pk=pk)
    l_p_s = so_p_s #'S'
    new_orderitem = None
    if request.method == 'POST':
        form1 = OrderItemForm(data=request.POST or None)
        form = OrderItemForm(data=request.POST or None)
        if form.is_valid():
            l_cu_id = form.cleaned_data['oi_cu_id']
            l_si_code = form.cleaned_data['oi_si_code']
            l_qty = form.cleaned_data['oi_ord_qty']
            currency = Currency.objects.get(cu_name=l_cu_id)
            l_rate = currency.cu_rate

            l_avail_qty = 0
            stockitem = StockItem.objects.filter(si_name=l_si_code)  # all()
            for stock in stockitem:
                l_price_b = stock.si_price_b
                l_price_1 = stock.si_price_1
                l_price_2 = stock.si_price_2
                l_avail_qty = stock.si_qty
                l_acost = stock.si_avg_cost
                l_tax = stock.si_tax
                l_disc = stock.si_disc

        # l_new_qty = (l_avail_qty - l_qty)

            if currency.cu_base == 'Y':  # l_base
                l_price = l_price_b
                l_tamnt = (l_price_b * l_qty)
                l_bamnt = (l_price_b * l_qty)
                l_new_avg = (((l_avail_qty * l_acost) + l_bamnt) / l_price_b)

            if currency.cu_base == '1':  # l_base
                l_price = l_price_1
                l_tamnt = (l_price_1 * l_qty)
                l_bamnt = ((l_price_1 * l_rate) * l_qty)
                l_new_avg = (((l_avail_qty * l_acost) + l_bamnt) / l_price_b)

            if currency.cu_base == '2':  # l_base
                l_price = l_price_2
                l_tamnt = (l_price_2 * l_qty)
                l_bamnt = ((l_price_2 * l_rate) * l_qty)

            l_new_avg = (((l_avail_qty * l_acost) + l_bamnt) / l_price_b)

            if l_p_s == 'S':
                l_new_qty = (l_avail_qty - l_qty)
                l_new_avg = l_acost

            if l_p_s == 'P':
                l_new_qty = (l_avail_qty + l_qty)

            l_disc_amnt = (l_tamnt * (l_disc / 100))
            l_tax_amnt = (l_tamnt * (l_tax / 100))

            l_amnt_due = ((l_tamnt - l_disc_amnt) + l_tax_amnt)

        # Create a OrderItem object but don't save to database yet
            new_orderitem = form.save(commit=False)
            new_orderitem.oi_so_num = storeorder

            new_orderitem.oi_uprice = l_price_b
            new_orderitem.oi_ucost = l_acost
            new_orderitem.oi_trans_amnt = l_tamnt
            new_orderitem.oi_base_amnt = l_bamnt

            new_orderitem.oi_disc = l_disc
            new_orderitem.oi_tax = l_tax

            new_orderitem.oi_disc_amnt = l_disc_amnt
            new_orderitem.oi_tax_amnt = l_tax_amnt

            new_orderitem.oi_tot_amnt = l_amnt_due
            new_orderitem.oi_so_p_s = l_p_s  # l_rate'oi_so_p_s'

            new_orderitem.save()

            stockitem.update(si_qty=l_new_qty, si_avg_cost=l_new_avg)
            orderupdte.update(so_trans_amnt=l_tamnt, so_base_amnt=l_bamnt, so_tax_amnt=l_tax_amnt,
                          so_disc_amnt=l_disc_amnt, so_tot_amnt=l_amnt_due)

            messages.success(request, "Order Item created successfully")
        return  redirect('orderitem', pk)

    else:
            form = OrderItemForm()
    return render(request, 'chicks/OrderItem/OrderItem.html', {'form': form})

def OrderItemOiView(request, pk,oi_so_p_s):
    storeorder = StoreOrder.objects.get(pk=pk)
    orderupdte = StoreOrder.objects.filter(pk=pk)
    l_p_s = oi_so_p_s #'S'
    new_orderitem = None
    if request.method == 'POST':
        form1 = OrderItemForm(data=request.POST or None)
        form = OrderItemForm(data=request.POST or None)
        if form.is_valid():
            l_cu_id = form.cleaned_data['oi_cu_id']
            l_si_code = form.cleaned_data['oi_si_code']
            l_qty = form.cleaned_data['oi_ord_qty']
            currency = Currency.objects.get(cu_name=l_cu_id)
            l_rate = currency.cu_rate

            l_avail_qty = 0
            stockitem = StockItem.objects.filter(si_name=l_si_code)  # all()
            for stock in stockitem:
                l_price_b = stock.si_price_b
                l_price_1 = stock.si_price_1
                l_price_2 = stock.si_price_2
                l_avail_qty = stock.si_qty
                l_acost = stock.si_avg_cost
                l_tax = stock.si_tax
                l_disc = stock.si_disc

            l_new_qty = 0

            if currency.cu_base == 'Y':  # l_base
                l_price = l_price_b
                l_tamnt = (l_price_b * l_qty)
                l_bamnt = (l_price_b * l_qty)
                l_new_avg = (((l_avail_qty * l_acost) + l_bamnt) / l_price_b)

            if currency.cu_base == '1':  # l_base
                l_price = l_price_1
                l_tamnt = (l_price_1 * l_qty)
                l_bamnt = ((l_price_1 * l_rate) * l_qty)
                l_new_avg = (((l_avail_qty * l_acost) + l_bamnt) / l_price_b)

            if currency.cu_base == '2':  # l_base
                l_price = l_price_2
                l_tamnt = (l_price_2 * l_qty)
                l_bamnt = ((l_price_2 * l_rate) * l_qty)

            l_new_avg = (((l_avail_qty * l_acost) + l_bamnt) / l_price_b)

            if l_p_s == 'S':
                l_new_qty = (l_avail_qty - l_qty)
                l_new_avg = l_acost

            if l_p_s == 'P':
                l_new_qty = (l_avail_qty + l_qty)

            l_disc_amnt = (l_tamnt * (l_disc / 100))
            l_tax_amnt = (l_tamnt * (l_tax / 100))

            l_amnt_due = ((l_tamnt - l_disc_amnt) + l_tax_amnt)

        # Create a OrderItem object but don't save to database yet
            new_orderitem = form.save(commit=False)
            new_orderitem.oi_so_num = storeorder

            new_orderitem.oi_uprice = l_price_b
            new_orderitem.oi_ucost = l_acost
            new_orderitem.oi_trans_amnt = l_tamnt
            new_orderitem.oi_base_amnt = l_bamnt

            new_orderitem.oi_disc = l_disc
            new_orderitem.oi_tax = l_tax

            new_orderitem.oi_disc_amnt = l_disc_amnt
            new_orderitem.oi_tax_amnt = l_tax_amnt

            new_orderitem.oi_tot_amnt = l_amnt_due
            new_orderitem.oi_so_p_s = l_p_s  # l_rate'oi_so_p_s'

            new_orderitem.save()

            stockitem.update(si_qty=l_new_qty, si_avg_cost=l_new_avg)
            orderupdte.update(so_trans_amnt=l_tamnt, so_base_amnt=l_bamnt, so_tax_amnt=l_tax_amnt,
                          so_disc_amnt=l_disc_amnt, so_tot_amnt=l_amnt_due)

            messages.success(request, "Order Item created successfully")
        return  redirect('orderitem', pk)

    else:
            form = OrderItemForm()
    return render(request, 'chicks/OrderItem/OrderItem.html', {'form': form})

# Edit a OrderItem
def EditOrderItem(request, pk, template_name='chicks/OrderItem/edit.html'):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    form = OrderItemEditForm(request.POST or None, instance=orderitem)
    if form.is_valid():
        form.save()
        return redirect('orderitem')
    return render(request, template_name, {'form': form})

# Delete OrderItem
def DeleteOrderItem(request, pk, template_name='chicks/OrderItem/confirm_delete.html'):
    orderitem = get_object_or_404(OrderItem, pk=pk)
    if request.method == 'POST':
        orderitem.delete()
        return redirect('orderitem')
    return render(request, template_name, {'object': orderitem})

#Stores Reports

def OrderItemRepView(request):
        # global l_gr_num

        total = 0
        storders = OrderItem.objects.values('oi_si_code__si_name','oi_so_num').annotate(tot_amnt=Sum(F('oi_trans_amnt')),tot_qty=Sum(F('oi_ord_qty')) )

        st_orders= OrderItemFilter(request.GET, queryset=storders)
        total_qty = st_orders.qs.aggregate(Totqty=Sum('tot_qty'))
        total_val = st_orders.qs.aggregate(Totval=Sum('tot_amnt'))

        context = {'filter': st_orders, 'total_qty': total_qty, 'total_val': total_val}

        return render(request, 'chicks/storereports/orderitem.html', context)

def StoreOrderSalesView(request):
    # global l_gr_num

    total = 0
    storders = StoreOrder.objects.filter(so_p_s='S').values('so_ord_date', 'so_sn_code__sn_name').annotate(base_amnt=Sum(F('so_base_amnt')),
            tax_amnt=Sum(F('so_tax_amnt')),\
            disc_amnt=Sum(F('so_disc_amnt')),
            due_amnt=Sum(F('so_tot_amnt')))

    st_orders = StoreOrderFilter(request.GET, queryset=storders)
    total_base = st_orders.qs.aggregate(TotBase=Sum('base_amnt'))
    total_tax = st_orders.qs.aggregate(TotTax=Sum('tax_amnt'))
    total_disc = st_orders.qs.aggregate(TotDisc=Sum('disc_amnt'))
    total_due = st_orders.qs.aggregate(DueAmnt=Sum('due_amnt'))

    context = {'filter': st_orders, 'total_base': total_base, 'total_tax': total_tax, 'total_disc': total_disc, 'total_due': total_due}

    return render(request, 'chicks/storereports/storeoder.html', context)

def StoreOrderPurView(request):
    # global l_gr_num

    total = 0
    storders = StoreOrder.objects.filter(so_p_s='P').values('so_ord_date', 'so_sn_code__sn_name').annotate(base_amnt=Sum(F('so_base_amnt')),
            tax_amnt=Sum(F('so_tax_amnt')),\
            disc_amnt=Sum(F('so_disc_amnt')),
            due_amnt=Sum(F('so_tot_amnt')))

    st_orders = StoreOrderFilter(request.GET, queryset=storders)
    total_base = st_orders.qs.aggregate(TotBase=Sum('base_amnt'))
    total_tax = st_orders.qs.aggregate(TotTax=Sum('tax_amnt'))
    total_disc = st_orders.qs.aggregate(TotDisc=Sum('disc_amnt'))
    total_due = st_orders.qs.aggregate(DueAmnt=Sum('due_amnt'))

    context = {'filter': st_orders, 'total_base': total_base, 'total_tax': total_tax, 'total_disc': total_disc, 'total_due': total_due}

    return render(request, 'chicks/storereports/storeoder.html', context)

def StoreSalesFlash1View(request):
        # global l_gr_num

        dataset = StoreOrder.objects.filter(so_p_s='P').values('so_sn_code__sn_name').annotate(
            base_amnt=Sum(F('so_base_amnt')), tax_amnt=Sum(F('so_tax_amnt')), disc_amnt=Sum(F('so_disc_amnt')), \
            due_amnt=Sum(F('so_tot_amnt')))

        return render(request, 'chicks/storereports/salesflash1.html', {'dataset': dataset})

def StoreSalesFlashView(request):
    # global l_gr_num

    dataset = StoreOrder.objects.filter(so_p_s='P').values('so_sn_code__sn_name').annotate(
        base_amnt=Sum(F('so_base_amnt')), tax_amnt=Sum(F('so_tax_amnt')), disc_amnt=Sum(F('so_disc_amnt')), \
        due_amnt=Sum(F('so_tot_amnt')))

    batch = list()
    base_series_data = list()
    tax_series_data = list()
    disc_series_data = list()
    due_series_data = list()

    for entry in dataset:
        batch.append('%s batch' % entry['so_sn_code__sn_name'])

        base = entry['base_amnt']
        if base is None:
            base = 0
        base = float(base)

        print(base)

        tax = entry['tax_amnt']
        if tax is None:
            tax = 0
        tax = abs(float(tax))

        disc = entry['disc_amnt']
        if disc is None:
            disc = 0
        disc = abs(float(disc))

        due = entry['due_amnt']
        if due is None:
            due = 0
        due = abs(float(due))

        base_series_data.append(base)
        tax_series_data.append(tax)
        disc_series_data.append(disc)
        due_series_data.append(due)

    base_series_data = {
        'name': 'Gross Amount',
        'data': base_series_data,
        'color': 'purple'
    }

    tax_series_data = {
        'name': 'Tax',
        'data': tax_series_data,
        'color': 'orange'
    }

    disc_series_data = {
        'name': 'Discount',
        'data': disc_series_data,
        'color': 'red'
    }

    due_series_data = {
        'name': 'Net',
        'data': due_series_data,
        'color': 'green'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Sales Flash'},
        #'xAxis': {'Batch': batch},
        'xAxis': {'categories': batch},
        'series': [base_series_data, tax_series_data, disc_series_data, due_series_data]
    }

    dump = json.dumps(chart, cls=DecimalEncoder)

    return render(request, 'chicks/storereports/salesflash.html', {'chart': dump})

def MonthlySalesFlash1View(request):
        # global l_gr_num

        dataset = StoreOrder.objects.filter(so_p_s='P').values('so_ord_date__month').annotate(
            base_amnt=Sum(F('so_base_amnt')), tax_amnt=Sum(F('so_tax_amnt')), disc_amnt=Sum(F('so_disc_amnt')), \
            due_amnt=Sum(F('so_tot_amnt')))

        return render(request, 'chicks/storereports/salesflash2.html', {'dataset': dataset})

def MonthlySalesFlashView(request):
    # global l_gr_num

    dataset = StoreOrder.objects.filter(so_p_s='P').values('so_ord_date__month').annotate(
        base_amnt=Sum(F('so_base_amnt')), tax_amnt=Sum(F('so_tax_amnt')), disc_amnt=Sum(F('so_disc_amnt')), \
        due_amnt=Sum(F('so_tot_amnt')))

    batch = list()
    base_series_data = list()
    tax_series_data = list()
    disc_series_data = list()
    due_series_data = list()


    for entry in dataset:
        batch.append('%s batch' % entry['so_ord_date__month'])

        base = entry['base_amnt']
        if base is None:
            base = 0
        base = float(base)

        print(base)

        tax = entry['tax_amnt']
        if tax is None:
            tax = 0
        tax = abs(float(tax))

        disc = entry['disc_amnt']
        if disc is None:
            disc = 0
        disc = abs(float(disc))

        due = entry['due_amnt']
        if due is None:
            due = 0
        due = abs(float(due))

        base_series_data.append(base)
        tax_series_data.append(tax)
        disc_series_data.append(disc)
        due_series_data.append(due)

    base_series_data = {
        'name': 'Gross Amount',
        'data': base_series_data,
        'color': 'purple'
    }

    tax_series_data = {
        'name': 'Tax',
        'data': tax_series_data,
        'color': 'orange'
    }

    disc_series_data = {
        'name': 'Discount',
        'data': disc_series_data,
        'color': 'red'
    }

    due_series_data = {
        'name': 'Net',
        'data': due_series_data,
        'color': 'green'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Sales Flash'},
        #'xAxis': {'Batch': batch},
        'xAxis': {'categories': batch},
        'series': [base_series_data, tax_series_data, disc_series_data, due_series_data]
    }

    dump = json.dumps(chart, cls=DecimalEncoder)

    return render(request, 'chicks/storereports/salesflash.html', {'chart': dump})

def StoreFlashView(request):
    # global l_gr_num

    dataset = Activity.objects.values('ac_hi_num__hi_code').annotate(
        tot_num=Max('ac_o_qty'), mort_sum=Sum('ac_morlity'), avail_sum=(Max('ac_o_qty') - Sum('ac_morlity')), \
        wgt_sum=Avg('ac_a_wqt')).order_by('ac_hi_num')

    batch = list()
    tot_series_data = list()
    mort_series_data = list()
    avail_series_data = list()
    wgt_series_data = list()

    for entry in dataset:
        batch.append('%s batch' % entry['ac_hi_num__hi_code'])

        tot = entry['tot_num']
        if tot is None:
            tot = 0
        tot = float(tot)

        print(tot)

        mort = entry['mort_sum']
        if mort is None:
            mort = 0
        mort = abs(float(mort))

        avail = entry['avail_sum']
        if avail is None:
            avail = 0
        avail = abs(float(avail))

        wgt = entry['wgt_sum']
        if wgt is None:
            wgt = 0
        wgt = abs(float(wgt))

        tot_series_data.append(tot)
        mort_series_data.append(mort)
        avail_series_data.append(avail)
        wgt_series_data.append(wgt)

    tot_series_data = {
        'name': 'Batch Size',
        'data': tot_series_data,
        'color': 'purple'
    }

    mort_series_data = {
        'name': 'Mortality',
        'data': mort_series_data,
        'color': 'red'
    }

    avail_series_data = {
        'name': 'Available',
        'data': avail_series_data,
        'color': 'green'
    }

    wgt_series_data = {
        'name': 'Weight',
        'data': wgt_series_data,
        'color': 'black'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Spot Flash'},
        # 'xAxis': {'Batch': batch},
        'xAxis': {'categories': batch},
        'series': [tot_series_data, mort_series_data, avail_series_data, wgt_series_data]
    }

    dump = json.dumps(chart, cls=DecimalEncoder)

    return render(request, 'chicks/reports/charts/s_flash.html', {'chart': dump})

#Start Commspace Views

class PostList(generic.ListView):

    queryset = BlogPost.objects.filter(bp_status='P').order_by('-ad_date_c')
    template_name = 'chicks/commspace/index.html'

    context_object_name = 'post_list'
    paginate_by = 20

class PostListAdmin(generic.ListView):

    queryset = BlogPost.objects.exclude(bp_status='P').order_by('-ad_date_c')
    template_name = 'chicks/commspace/index.html'

    context_object_name = 'post_list'
    paginate_by = 20

class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'chicks/commspace/post_detail.html'

@login_required
def Post_Detail(request, slug):

    c_user = request.user
    print(c_user)

    template_name = 'chicks/commspace/post_detail.html'
    post = get_object_or_404(BlogPost, slug=slug)

    if request.user.username in ("reg","xx"):
        contributions = post.contributions.all()
        #print(c_user)
    else:
        contributions = post.contributions.filter(pc_active=True)
        print(request.user.username)

    new_contribution = None
    # Contribution posted
    if request.method == 'POST':
        contribution_form = ContributionForm(data=request.POST)

        if contribution_form.is_valid():

            # Create Contribution object but don't save to database yet
            new_contribution = contribution_form.save(commit=False)
            # Assign the current post to the Contribution
            new_contribution.pc_bp_num = post
            # Save the comment to the database
            new_contribution.save()
    else:
        contribution_form = ContributionForm()

    return render(request, template_name, {'post': post,
                                           'contributions': contributions,
                                           'new_contribution': new_contribution,
                                           'contribution_form': contribution_form})
@login_required
def post_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user_c = request.user
            post.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = BlogForm()
    return render(request, 'chicks/commspace/post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user_a = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = BlogForm(instance=post)
    return render(request, 'chicks/commspace/post_edit.html', {'form': form,'post': post})

@login_required
def post_remove(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.delete()
    return redirect('bloghome')

@login_required
def cont_approve(request, pk):
    contribution = get_object_or_404(PostContribution, pk=pk)
    contribution.approve_contributions()
    return redirect('bloghome')

@login_required
def cont_remove(request, pk):
    contribution = get_object_or_404(PostContribution, pk=pk)
    contribution.delete()
    return redirect('bloghome')
