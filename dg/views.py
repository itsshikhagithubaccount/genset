from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
from dg.forms import *


def home(request):
    return render(request, 'home/home.html')


def login(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')

            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'login.html', {'form': form, 'error': error})


def dashboard(request):
    return render(request, 'home/dashboard.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


# **********************************[city views]*************************************************************************


def city_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = CityForm()
        else:
            city = City.objects.get(pk=id)
            form = CityForm(instance=city)
        return render(request, "location/city_form.html", {'form': form})
    else:
        if id == 0:
            form = CityForm(request.POST)
        else:
            city = City.objects.get(pk=id)
            old_user = city.user
            form = CityForm(request.POST, instance=city)

        if form.is_valid() and id == 0:
            city = form.save(commit=False)
            messages.success(request, 'User request submitted successfully.')
            city.user = request.user
            city.created_on = datetime
            city.save()
        if form.is_valid() and id != 0:
            form.save(commit=False)
            messages.success(request, 'User request submitted successfully.')
            # city_name = request.POST['city_name']
            # if City.objects.filter(city_name=city_name).exists():
            #     messages.error(request, "city already exists")
            # return render(request,"location/city_form.html")
            city.user = old_user
            city.modified_user = request.user
            city.updated_on = datetime
            city.save()
            # messages.success(request,'successfully saved')
        return redirect('city_list')

        # if form.is_valid():
        #     if city_name in city_list:
        #         raise forms.ValidationError(city_name + "dublicate value ")
        #     else:
        #         return render(request, "location/city_form.html", {'error': True})
        #


def city_list(request):
    context = {'city_list': City.objects.all()}
    return render(request, 'location/city_list.html', context)


def city_delete(request, id):
    city = City.objects.get(pk=id)
    city.delete()
    return redirect('city_list')


# *******************************************[STATE VIEWS]*********************************************************************
def state_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = StateForm()
        else:
            state = State.objects.get(pk=id)
            form = StateForm(instance=state)
        return render(request, "location\state_form.html", {'form': form})
    else:
        if id == 0:
            form = StateForm(request.POST)
        else:
            state = State.objects.get(pk=id)
            old_user = state.user
            form = StateForm(request.POST, instance=state)
        if form.is_valid() and id == 0:
            state = form.save(commit=False)
            state.user = request.user
            state.created_on = datetime
            state.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            state = form.save(commit=False)
            state.user = old_user
            state.modified_user = request.user
            state.updated_on = datetime
            state.save()
            messages.success(request, 'successfully saved')
        return redirect('state_list')


def state_list(request):
    context = {'state_list': State.objects.all()}
    return render(request, 'location\state_list.html', context)


def state_delete(request, id):
    state = State.objects.get(pk=id)
    state.delete()
    return redirect('state_list')


# ************************************************[COUNTRY VIEW]*************************************************************

def country_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = CountryForm()
        else:
            country = Country.objects.get(pk=id)
            form = CountryForm(instance=country)
        return render(request, "location\country_form.html", {'form': form})
    else:
        if id == 0:
            form = CountryForm(request.POST)
        else:
            country = Country.objects.get(pk=id)
            old_user = country.user
            form = CountryForm(request.POST, instance=country)
        if form.is_valid() and id == 0:
            country = form.save(commit=False)
            country.user = request.user
            country.created_on = datetime
            country.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            country = form.save(commit=False)
            country.user = old_user
            country.modified_user = request.user
            country.updated_on = datetime
            country.save()
            messages.success(request, 'successfully saved')
        return redirect('country_list')


def country_list(request):
    context = {'country_list': Country.objects.all()}
    return render(request, 'location\country_list.html', context)


def country_delete(request, id):
    country = Country.objects.get(pk=id)
    country.delete()
    return redirect('country_list')


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, your profile is updated.')
            return redirect('profilehome')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'profiletemp\profile.html', context)


def profilehome(request):
    return render(request, 'profiletemp\profilehome.html')


def company_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = CompanyForm()
        else:
            company = Company.objects.get(pk=id)
            form = CompanyForm(instance=company)
        return render(request, "master\company_form.html", {'form': form})
    else:
        if id == 0:
            form = CompanyForm(request.POST)
        else:
            company = Company.objects.get(pk=id)
            old_user = company.user
            form = CompanyForm(request.POST, instance=company)
        if form.is_valid() and id == 0:
            company = form.save(commit=False)
            company.user = request.user
            company.created_on = datetime
            company.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            company = form.save(commit=False)
            company.user = old_user
            company.modified_user = request.user
            company.updated_on = datetime
            company.save()
            messages.success(request, 'successfully saved')
        return redirect('company_list')


def company_list(request):
    context = {'company_list': Company.objects.all()}
    return render(request, 'master\company_list.html', context)


def company_delete(request, id):
    company = Company.objects.get(pk=id)
    company.delete()
    return redirect('company_list')


# ***********************[ DISEL VIEWS ]********************************************************************************

def dm_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = DieselMasterForm()
        else:
            dieselmaster = DieselMaster.objects.get(pk=id)
            form = DieselMasterForm(instance=dieselmaster)
        return render(request, "master\dm_form.html", {'form': form})
    else:
        if id == 0:
            form = DieselMasterForm(request.POST)
        else:
            dieselmaster = DieselMaster.objects.get(pk=id)
            old_user = dieselmaster.user
            form = DieselMasterForm(request.POST, instance=dieselmaster)
        if form.is_valid() and id == 0:
            dieselmaster = form.save(commit=False)
            dieselmaster.user = request.user
            dieselmaster.created_on = datetime
            dieselmaster.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            dieselmaster = form.save(commit=False)
            dieselmaster.user = old_user
            dieselmaster.modified_user = request.user
            dieselmaster.updated_on = datetime
            dieselmaster.save()
            messages.success(request, 'successfully saved')
        return redirect('dm_list')


def dm_list(request):
    context = {'dm_list': DieselMaster.objects.all()}
    return render(request, 'master/dm_list.html', context)


def dm_delete(request, id):
    dieselmaster = DieselMaster.objects.get(pk=id)
    dieselmaster.delete()
    return redirect('dm_list')


def location_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = DieselLocationForm()
        else:
            location = DieselLocation.objects.get(pk=id)
            form = DieselLocationForm(instance=location)
        return render(request, "master\location_form.html", {'form': form})
    else:
        if id == 0:
            form = DieselLocationForm(request.POST)
        else:
            location = DieselLocation.objects.get(pk=id)
            old_user = location.user
            form = DieselLocationForm(request.POST, instance=location)
        if form.is_valid() and id == 0:
            location = form.save(commit=False)
            location.user = request.user
            location.created_on = datetime
            location.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            location = form.save(commit=False)
            location.user = old_user
            location.modified_user = request.user
            location.updated_on = datetime
            location.save()
            messages.success(request, 'successfully saved')
        return redirect('location_list')


def location_list(request):
    context = {'location_list': DieselLocation.objects.all()}
    return render(request, 'master\location_list.html', context)


def location_delete(request, id):
    location = DieselLocation.objects.get(pk=id)
    location.delete()
    return redirect('location_list')


def dg_template_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = DgTemplateForm()
        else:
            template = DgTemplate.objects.get(pk=id)
            form = DgTemplateForm(instance=template)
        return render(request, "dieseltemplates\dg_template_form.html", {'form': form})
    else:
        if id == 0:
            form = DgTemplateForm(request.POST)
        else:
            template = DgTemplate.objects.get(pk=id)
            old_user = template.user
            form = DgTemplateForm(request.POST, instance=template)
        if form.is_valid() and id == 0:
            template = form.save(commit=False)
            template.user = request.user
            template.created_on = datetime
            template.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            template = form.save(commit=False)
            template.user = old_user
            template.modified_user = request.user
            template.updated_on = datetime
            template.save()
            messages.success(request, 'successfully saved')
        return redirect('dg_template_list')


def dg_template_list(request):
    context = {'template_list': DgTemplate.objects.all()}
    return render(request, 'dieseltemplates\dg_template_list.html', context)


def dg_template_delete(request, id):
    template = DgTemplate.objects.get(pk=id)
    template.delete()
    return redirect('dg_template_list')


def bm_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = BatteryMasterForm()
        else:
            batterymaster = BatteryMaster.objects.get(pk=id)
            form = BatteryMasterForm(instance=batterymaster)
        return render(request, "master/bm_form.html", {'form': form})
    else:
        if id == 0:
            form = BatteryMasterForm(request.POST)
        else:
            batterymaster = BatteryMaster.objects.get(pk=id)
            old_user = batterymaster.user
            form = BatteryMasterForm(request.POST, instance=batterymaster)
        if form.is_valid() and id == 0:
            batterymaster = form.save(commit=False)
            batterymaster.user = request.user
            batterymaster.created_on = datetime
            batterymaster.save()
        if form.is_valid() and id != 0:
            batterymaster = form.save(commit=False)
            batterymaster.user = old_user
            batterymaster.modified_user = request.user
            batterymaster.updated_on = datetime
            batterymaster.save()
        return redirect('bm_list')


def bm_list(request):
    context = {'bm_list': BatteryMaster.objects.all()}
    return render(request, "master/bm_list.html", context)


def bm_delete(request, id):
    batterymaster = BatteryMaster.objects.get(pk=id)
    batterymaster.delete()
    return redirect('bm_list')


def condition_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = DgStateForm()
        else:
            condition = DgState.objects.get(pk=id)
            form = DgStateForm(instance=condition)
        return render(request, "dg_state/condition_form.html", {'form': form})
    else:
        if id == 0:
            form = DgStateForm(request.POST)
        else:
            condition = DgState.objects.get(pk=id)
            old_user = condition.user
            form = DgStateForm(request.POST, instance=condition)
        if form.is_valid() and id == 0:
            condition = form.save(commit=False)
            condition.user = request.user
            condition.created_on = datetime
            condition.save()
        if form.is_valid() and id != 0:
            condition = form.save(commit=False)
            condition.user = old_user
            condition.modified_user = request.user
            condition.updated_on = datetime
            condition.save()
        return redirect('condition_list')


def condition_list(request):
    context = {'condition_list': DgState.objects.all()}
    return render(request, "dg_state/condition_list.html", context)


def condition_delete(request, id):
    condition = DgState.objects.get(pk=id)
    condition.delete()
    return redirect('condition_list')


def dg_state_list(request):
    context = {'dg_state_list': DgState.objects.all()}
    return render(request, 'dg_state/condition_list.html', context)


def dg_state_delete(request, id):
    condition = DgState.objects.get(pk=id)
    condition.delete()
    return redirect('dg_state_list')


def external_tank_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = DgExternalTankDetailsForm()
        else:
            tank = DgExternalTankDetails.objects.get(pk=id)
            form = DgExternalTankDetailsForm(instance=tank)
        return render(request, "externaltank/external_tank_form.html", {'form': form})
    else:
        if id == 0:
            form = DgExternalTankDetailsForm(request.POST)
        else:
            tank = DgExternalTankDetails.objects.get(pk=id)
            old_user = tank.user
            form = DgExternalTankDetailsForm(request.POST, instance=tank)
        if form.is_valid() and id == 0:
            tank = form.save(commit=False)
            tank.user = request.user
            tank.created_on = datetime
            tank.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            tank = form.save(commit=False)
            tank.user = old_user
            tank.modified_user = request.user
            tank.updated_on = datetime
            tank.save()
            messages.success(request, 'successfully saved')
        return redirect('external_tank_list')


def external_tank_list(request):
    context = {'external_tank_list': DgExternalTankDetails.objects.all()}
    return render(request, 'externaltank/external_tank_list.html', context)


def external_tank_delete(request, id):
    tank = DgExternalTankDetails.objects.get(pk=id)
    tank.delete()
    return redirect('external_tank_list')


def fuel_level_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = FuelLevelMonitoringForm()
        else:
            fuel = FuelLevelMonitoring.objects.get(pk=id)
            form = FuelLevelMonitoringForm(instance=fuel)
        return render(request, "fuellevel/fuel_level_form.html", {'form': form})
    else:
        if id == 0:
            form = FuelLevelMonitoringForm(request.POST)
        else:
            fuel = FuelLevelMonitoring.objects.get(pk=id)
            old_user = fuel.user
            form = FuelLevelMonitoringForm(request.POST, instance=fuel)
        if form.is_valid() and id == 0:
            fuel = form.save(commit=False)
            fuel.user = request.user
            fuel.created_on = datetime
            fuel.save()
            messages.success(request, 'successfully saved')
        if form.is_valid() and id != 0:
            fuel = form.save(commit=False)
            fuel.user = old_user
            fuel.modified_user = request.user
            fuel.updated_on = datetime
            fuel.save()
            messages.success(request, 'successfully saved')
        return redirect('fuel_level_list')


def fuel_level_list(request):
    context = {'fuel_level_list': FuelLevelMonitoring.objects.all()}
    return render(request, "fuellevel/fuel_level_list.html", context)


def fuel_level_delete(request, id):
    fuel = FuelLevelMonitoring.objects.get(pk=id)
    fuel.delete()
    return redirect('fuel_level_list')


def battery_template_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = BatteryTemplateForm()
        else:
            template = BatteryTemplate.objects.get(pk=id)
            form = BatteryTemplateForm(instance=template)
        return render(request, "batterytemplate/battery_template_form.html", {'form': form})
    else:
        if id == 0:
            form = BatteryTemplateForm(request.POST)
        else:
            template = BatteryTemplate.objects.get(pk=id)
            old_user = template.user
            form = BatteryTemplateForm(request.POST, instance=template)
        if form.is_valid() and id == 0:
            template = form.save(commit=False)
            template.user = request.user
            template.created_on = datetime
            template.save()
        if form.is_valid() and id != 0:
            template = form.save(commit=False)
            template.user = old_user
            template.modified_user = request.user
            template.updated_on = datetime
            template.save()
        return redirect('battery_template_list')


def battery_template_list(request):
    context = {'battery_template_list': BatteryTemplate.objects.all()}
    return render(request, "batterytemplate/battery_template_list.html", context)


def battery_template_delete(request, id):
    template = BatteryTemplate.objects.get(pk=id)
    template.delete()
    return redirect('battery_template_list')


def maintenance_form(request, id=0):
    global old_user
    if request.method == "GET":
        if id == 0:
            form = MaintenanceMasterForm()
        else:
            maintenance = MaintenanceMaster.objects.get(pk=id)
            form = MaintenanceMasterForm(instance=maintenance)
        return render(request, "maintenance_form.html", {'form': form})
    else:
        if id == 0:
            form = MaintenanceMasterForm(request.POST)
        else:
            maintenance = MaintenanceMaster.objects.get(pk=id)
            old_user = maintenance.user
            form = MaintenanceMasterForm(request.POST, instance=maintenance)
        if form.is_valid() and id == 0:
            maintenance = form.save(commit=False)
            maintenance.user = request.user
            maintenance.created_on = datetime
            maintenance.save()
        if form.is_valid() and id != 0:
            maintenance = form.save(commit=False)
            maintenance.user = old_user
            maintenance.modified_user = request.user
            maintenance.updated_on = datetime
            maintenance.save()
        return redirect('maintenance_list')


def maintenance_list(request):
    context = {'maintenance_list': MaintenanceMaster.objects.all()}
    return render(request, "maintenance_list.html", context)


def maintenance_delete(request, id):
    maintenance = MaintenanceMaster.objects.get(pk=id)
    maintenance.delete()
    return redirect('maintenance_list')
