from django import forms
from django.contrib.auth.forms import UserCreationForm
from rest_framework.exceptions import ValidationError

from dg.models import *
from .models import Profile
from django.forms.widgets import FileInput
from django.forms.models import ModelForm

class LogInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")




class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = "__all__"
        labels = {
            'city_name': 'City Name',
        }

    def __init__(self, *args, **kwargs):
        super(CityForm, self).__init__(*args, **kwargs)
        self.fields['city_name'].required = True

#
# def clean(self):
#     """
#     Override the default clean method to check whether this course has
#     been already inputted.
#     """
#     cleaned_data = self.cleaned_data
#
#     city_name = cleaned_data.get('city_name')
#
#     city = City.objects.filter(city_name='city_name')
#     if self.instance:
#         city = city.exclude(pk=self.instance.pk)
#     if city.exists():
#         ms = u"City name: %s has already exist." % city_name
#         raise ValidationError(ms)
#     else:
#         return self.cleaned_data


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = "__all__"
        labels = {
            'state_name': 'State Name',
            'state_id': 'State Id'


        }

    def __init__(self, *args, **kwargs):
        super(StateForm, self).__init__(*args, **kwargs)
        self.fields['state_name'].required = True


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"
        labels = {
            'country_name': 'Country Name'
 }

    def __init__(self, *args, **kwargs):
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['country_name'].required = True


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'profile_img': FileInput(),
        }




class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        labels = {
                'company_name': 'Company Name',

        }

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].required = False
        self.fields['city'].empty_label = "select"
        self.fields['state'].empty_label = "select"
        self.fields['country'].empty_label = "select"




class DieselMasterForm(forms.ModelForm):
    class Meta:
        model = DieselMaster
        fields = "__all__"
        labels = {
            'dg_name ': 'Dg Name',
            'dg_model': 'Dg Model',
            'dg_make': 'Dg Make',
            'dg_voltage': 'Dg Voltage',
            'dg_power': 'Dg Power',
            'attendant_id': 'Attendant Id',
            'diesel_template': 'Diesel Template',
            'diesel_location': 'Diesel Location',
            'diesel_attend_name': 'Diesel Attend Name',


        }

    def __init__(self, *args, **kwargs):
        super(DieselMasterForm, self).__init__(*args, **kwargs)
        self.fields['dg_name'].required = False
        self.fields['diesel_template'].empty_label = "select"
        self.fields['diesel_location'].empty_label = "select"


class DieselLocationForm(forms.ModelForm):
    class Meta:
        model = DieselLocation
        fields = "__all__"
        labels = {
            'location_name': 'Location Name',
            'company': 'Company',
            'gps_coordinate': 'Gps Coordinate',
            'longitude_latitude': 'Longitude Latitude',

        }

    def __init__(self, *args, **kwargs):
        super(DieselLocationForm, self).__init__(*args, **kwargs)
        self.fields['company'].empty_label = "select"
        self.fields['city'].empty_label = "select"
        self.fields['state'].empty_label = "select"


class DgTemplateForm(forms.ModelForm):
    class Meta:
        model = DgTemplate
        fields = "__all__"
        labels={
            'dg_template_name': 'Dg Template Name',
            'dg_rating': 'Dg Rating',
            'dg_rated_kw': 'Dg Rated Kw',
            'dg_rated_current_amp': 'Dg Rated Current Amp',
            'dg_size': 'Dg Size',
            'dg_weight_kg': 'Dg Weight Kg',
            'engine_bhp':'Engine Bhp',
            'engine_cylinder': 'Engine Cylinder',
            'engine_rpm': 'Engine Rpm',
            'engine_bore_mm_field': 'Engine Bore mm Field',
            'engine_stroke_mm_field': 'Engine Stroke mm Field',
            'engine_displacement_ltr_field': 'Engine Displacement Ltr Field',
            'engine_compression_ratio': 'Engine Compression Ratio',
            'engine_sfc_gsm_hr_field': 'Engine Sfc Gsm Hr Field',
            'engine_governor': 'Engine Governor',
            'engine_class_of_governing': 'Engine Class Of Governing',
            'engine_aspiration': 'Engine Aspiration',
            'engine_air_filter': 'Engine Air Filter',
            'engine_type_of_oil': 'Engine Type Of Oil',
            'engine_oil_sump_capacity_ltr': 'Engine Oil Sump Capacity Ltr',
            'engine_fuel': 'Engine Fuel',
            'engine_lube_oil_consumption_gms_bhp_hr':'Engine Lube Oil Consumption Gms Bhp Hr',
            'cooling_bare_radiator_coolant_ltr': 'Cooling Bare Radiator Coolant Ltr',
            'cooling_coolant_capacity_with_engine_jacket_ltr': 'Cooling Coolant Capacity With Engine Jacket Ltr',


        }

    def __init__(self, *args, **kwargs):
        super(DgTemplateForm, self).__init__(*args, **kwargs)



class BatteryMasterForm(forms.ModelForm):
    class Meta:
        model = BatteryMaster
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BatteryMasterForm, self).__init__(*args, **kwargs)


class DgStateForm(forms.ModelForm):
    class Meta:
        model = DgState
        fields = "__all__"
        labels = {
            'dg_start_time': 'Dg Start Time',
            'dg_off_time': 'Dg Off Time',
            'dg_master_name': 'Dg Master Name',
            'battery_master_name': 'Battery Master Name',
            'dg_externaltank_name': 'Dg Externaltank Name',
            'fuel_level_name': 'Fuel Level Name',

        }

    def __init__(self, *args, **kwargs):
        super(DgStateForm, self).__init__(*args, **kwargs)
        self.fields['dg_master'].empty_label = "select"
        self.fields['battery_master'].empty_label = "select"
        self.fields['dg_externaltank_master'].empty_label = "select"
        self.fields['fuel_level'].empty_label = "select"


class DgExternalTankDetailsForm(forms.ModelForm):
    class Meta:
        model = DgExternalTankDetails
        fields = "__all__"
        labels = {
            'external_tank_current_level': 'External Tank Current Level',
            'external_tank_reading_timestamp': 'External Tank Reading Timestamp',
            'dg_master_name': 'Dg Master Name',
            'dg_external_tank_name': 'Dg External Tank Name',
            ' external_tank_capacity': ' External Tank Capacity',

        }

    def __init__(self, *args, **kwargs):
        super(DgExternalTankDetailsForm, self).__init__(*args, **kwargs)
        self.fields['dg_master'].empty_label = "select"


class FuelLevelMonitoringForm(forms.ModelForm):
    class Meta:
        model = FuelLevelMonitoring
        fields = "__all__"
        labels = {
            'dg_name': 'Dg Name',
            'fuel_current_level': 'Fuel Current Level',
            'monitoring_time': ' Monitoring Time',
            'diesel_on_time': 'Diesel On Time',
            'diesel_off_time': 'Diesel Off Time',
            'fuel_level_name': 'Fuel Level Name',

        }

    def __init__(self, *args, **kwargs):
        super(FuelLevelMonitoringForm, self).__init__(*args, **kwargs)
        self.fields['dg_master'].empty_label = "select"


class BatteryTemplateForm(forms.ModelForm):
    class Meta:
        model = BatteryTemplate
        fields = "__all__"
        labels = {
            'battery_template_name': 'Battery Template Name',
            'type': 'Type',
            'rating_ah': 'Rating Ah',
            'quantity_nos': 'Quantity Nos',
            'charging_facility': 'Charging Facility',
            'make': ' Make',
            'battery_metering': 'Battery Metering',
            'battery_current_voltage': 'Battery Current Voltage',
            'battery_reading_timestamp': 'Battery Reading Timestamp',
            'model': 'Model',

        }

    def __init__(self, *args, **kwargs):
        super(BatteryTemplateForm, self).__init__(*args, **kwargs)


class BatteryTemplateForm(forms.ModelForm):
    class Meta:
        model = BatteryTemplate
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BatteryTemplateForm, self).__init__(*args, **kwargs)


class MaintenanceMasterForm(forms.ModelForm):
    class Meta:
        model = MaintenanceMaster
        fields = "__all__"
        labels = {
            'dg_type': 'Dg Type',
            'category': 'Category',
            'historical_cost': 'Historical Cost',

        }

    def __init__(self, *args, **kwargs):
        super(MaintenanceMasterForm, self).__init__(*args, **kwargs)
        self.fields['dg_master'].empty_label = "select"




class MaintenanceAuditTrialForm(forms.ModelForm):
    class Meta:
        model = MaintenanceAuditTrial
        fields = "__all__"
        labels = {
            'maintenance_master_name': 'Maintenance Master Name',
            'dg_name': 'Dg Name',
            'dg_number': 'Dg Number',
            ' dg_type' : ' Dg Type',
            'category' : 'Category',
            'class_field': 'Class Field',
        }

    def __init__(self, *args, **kwargs):
        super(MaintenanceAuditTrialForm, self).__init__(*args, **kwargs)