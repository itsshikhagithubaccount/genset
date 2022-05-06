from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email" # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()


#********************************[ADD CITY MODEL]**********************************************************************


class City(models.Model):
    # city_name = models.CharField(max_length=100,unique=True,null=False)
    city_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user', related_name='modified_user',
                             blank=True,null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user_city',
                                      related_name='modified_user_city', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table= "dg_city"

#******************************************[ADD STATE MODEL]*************************************************************

class State(models.Model):
    state_name = models.CharField(max_length=100,unique=True, blank=False,null=False)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_userr', related_name='modified_userr',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user_state',
                                      related_name='modified_user_state', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.state_name


#************************************[ADD COUNTRY MODEL]******************************************************************
class Country(models.Model):
    country_name = models.CharField(max_length=100,unique=True, blank=False)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_userrr', related_name='modified_user_countryy',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user_country',
                                      related_name='modified_user_country', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.country_name

#*************************************[ADD PROFILE MODEL ]****************************************************************

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='John Doe (Default)', max_length=200, null=True)
    bio = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_img = models.ImageField(default='media/2.png', upload_to='media', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"



#*************************************[ADD COMPANY MODEL ]****************************************************************

class Company(models.Model):
   company_name = models.CharField(max_length=20, null=True,blank=True)
   city = models.ForeignKey('City',on_delete=models.CASCADE)
   state = models.ForeignKey('State', on_delete=models.CASCADE)
   country = models.ForeignKey('Country', on_delete=models.CASCADE)
   user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_us', related_name='modified_user_companyy',
                            blank=True, null=True)
   modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user_company',
                                     related_name='modified_user_company', blank=True, null=True)
   created_on = models.DateTimeField(auto_now_add=True, null=True)
   updated_on = models.DateTimeField(auto_now=True, null=True)

   def __str__(self):
       return self.company_name

#*********************************************[ADD DISEL MASTER MODEL]*************************************************


class DieselMaster(models.Model):
    dg_name = models.CharField(max_length=49)
    dg_model = models.CharField(max_length=40, blank=True, null=True)
    dg_make = models.CharField(max_length=45, blank=True, null=True)
    dg_voltage = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    dg_power = models.CharField(max_length=45, blank=True, null=True)
    attendant_id = models.IntegerField(blank=True, null=True)
    diesel_template = models.ForeignKey('DgTemplate', on_delete=models.CASCADE)
    diesel_location = models.ForeignKey('DieselLocation', on_delete=models.CASCADE)
    diesel_attend_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_diesel_master',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user_diesel',
                                      related_name='modified_user_diesel_master', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.dg_name

#*************************************[ADD DISEL LOCATION MODEL]**********************************************************

class DieselLocation(models.Model):
    location_name = models.CharField(max_length=45, blank=True, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    gps_coordinate = models.CharField(max_length=45, blank=True, null=True)
    longitude_latitude = models.CharField(max_length=45, blank=True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_location',
                             blank=True, null=True)

    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user_location',
                                      related_name='modified_user_diesel_location', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.location_name

#*************************************[ADD DISEL TEMPLATE MODEL]**********************************************************



class DgTemplate(models.Model):
    dg_template_name = models.CharField(max_length=45, blank=True, null=True)
    dg_rating = models.IntegerField(blank=True, null=True)
    dg_rated_kw = models.IntegerField(blank=True, null=True)
    dg_rated_current_amp = models.IntegerField(blank=True, null=True)
    dg_size = models.IntegerField(blank=True,null=True)
    dg_weight_kg = models.IntegerField(blank=True, null=True)
    engine_bhp = models.IntegerField(blank=True, null=True)
    engine_cylinder = models.IntegerField(blank=True, null=True)
    engine_rpm = models.IntegerField(blank=True, null=True)
    engine_bore_mm_field = models.IntegerField(db_column='engine_bore(mm)', blank=True, null=True)
    engine_stroke_mm_field = models.IntegerField(db_column='engine_stroke(mm)', blank=True, null=True)
    engine_displacement_ltr_field = models.IntegerField(db_column='engine_displacement(ltr)', blank=True, null=True)
    engine_compression_ratio = models.IntegerField(blank=True, null=True)
    engine_sfc_gsm_hr_field = models.IntegerField(db_column='engine_sfc(gsm_bhp_hr)', blank=True, null=True)
    engine_governor = models.IntegerField(blank=True, null=True)
    engine_class_of_governing = models.IntegerField(blank=True, null=True)
    engine_aspiration = models.IntegerField(blank=True, null=True)
    engine_air_filter = models.IntegerField(blank=True, null=True)
    engine_type_of_oil = models.CharField(max_length=45, blank=True, null=True)
    engine_oil_sump_capacity_ltr = models.IntegerField(blank=True, null=True)
    engine_fuel = models.IntegerField(blank=True, null=True)
    engine_lube_oil_consumption_gms_bhp_hr = models.IntegerField(blank=True, null=True)
    cooling_bare_radiator_coolant_ltr = models.IntegerField(blank=True, null=True)
    cooling_coolant_capacity_with_engine_jacket_ltr = models.IntegerField(blank=True, null=True)
    cooling_engine_dry_weight_kgs = models.IntegerField(blank=True, null=True)
    cooling_electric_starting_system = models.IntegerField(blank=True, null=True)
    alternator_model = models.CharField(max_length=45, blank=True, null=True)
    alternator_kva = models.IntegerField(blank=True, null=True)
    alternator_voltage = models.IntegerField(blank=True, null=True)
    alternator_no_of_phases = models.IntegerField(blank=True,null=True)
    alternator_power_factor = models.IntegerField(blank=True, null=True)
    alternator_speed_rpm_frequency = models.IntegerField(blank=True, null=True)
    alternator_voltage_regulation = models.IntegerField(blank=True, null=True)
    alternator_enclosure = models.CharField(max_length=45,blank=True, null=True)
    alternator_insulation = models.CharField(max_length=45, blank=True, null=True)
    alternator_weight_of_acg_kgs = models.CharField(max_length=45, blank=True, null=True)
    battery_type = models.CharField(max_length=45, blank=True, null=True)
    battery_rating_ah = models.IntegerField(blank=True, null=True)
    battery_quantity_nos = models.IntegerField(blank=True, null=True)
    battery_charging_facility = models.IntegerField(blank=True, null=True)
    battery_metering = models.IntegerField(blank=True, null=True)
    exhaust_silencer_type = models.CharField(max_length=45, blank=True, null=True)
    exhaust_location = models.CharField(max_length=44, blank=True, null=True)
    exhaust_pipe_size_in_mm = models.IntegerField(blank=True, null=True)
    fuel_tank_type = models.CharField(max_length=45, blank=True, null=True)
    fuel_tank_capacity_ltr = models.IntegerField(blank=True, null=True)
    canopy_type = models.CharField(max_length=45, blank=True, null=True)
    canopy_sheet_metal = models.CharField(max_length=45, blank=True, null=True)
    canopy_draft = models.CharField(max_length=45, blank=True, null=True)
    canopy_insulation = models.CharField(max_length=45, blank=True, null=True)
    canopy_noise_level_al_1m = models.CharField(max_length=45, blank=True, null=True)
    other_base_frame = models.CharField(max_length=45,blank=True, null=True)
    other_avm_qty_nos = models.IntegerField(blank=True, null=True)
    other_emergency_stop = models.CharField(max_length=45, blank=True, null=True)
    other_internal_lights = models.CharField(max_length=45, blank=True, null=True)
    control_panel_dg_parameter_monitoring_display = models.CharField(max_length=45, blank=True, null=True)
    control_panel_engine_parameter_monitoring_display = models.CharField(max_length=45, blank=True, null=True)
    control_panel_functions = models.CharField(max_length=45, blank=True, null=True)
    control_panel_protection = models.CharField(max_length=45, blank=True, null=True)
    control_panel_safeties = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_dgstate', blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_dgstate', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.dg_template_name


#**************************************[DIESEL STATE MODEL]****************************************************************
class DgState(models.Model):
    dg_master = models.ForeignKey('DieselMaster', on_delete=models.CASCADE)
    battery_master = models.ForeignKey('BatteryMaster', on_delete=models.CASCADE)
    dg_externaltank_master = models.ForeignKey('DgExternalTankDetails', on_delete=models.CASCADE)
    fuel_level = models.ForeignKey('FuelLevelMonitoring', on_delete=models.CASCADE)
    dg_start_time = models.CharField(max_length=45,blank=True, null=True)
    dg_off_time = models.CharField(max_length=45,blank=True, null=True)
    dg_master_name = models.CharField(max_length=45, blank=True, null=True)
    battery_master_name = models.CharField(max_length=45, blank=True, null=True)
    dg_externaltank_name = models.CharField(max_length=45, blank=True, null=True)
    fuel_level_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User,models.DO_NOTHING, db_column='user',related_name='created_user_dg_state', blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_dg_state', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.dg_master


#****************************************************[EXTERNAL TANK MODEL ]*************************************************
class DgExternalTankDetails(models.Model):
    dg_master = models.ForeignKey('DieselMaster', on_delete=models.CASCADE)
    external_tank_current_level = models.IntegerField(blank=True, null=True)
    external_tank_reading_timestamp = models.IntegerField(blank=True, null=True)
    dg_master_name = models.CharField(max_length=45, blank=True, null=True)
    dg_external_tank_name = models.CharField(max_length=45, blank=True, null=True)
    external_tank_capacity = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_external_tank',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_external_tank', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
#****************************[FUEL LEVEL MONITORING MODEL]****************************************************************

class FuelLevelMonitoring(models.Model):
    dg_master = models.ForeignKey('DieselMaster', on_delete=models.CASCADE)
    dg_name = models.CharField(max_length=45, blank=True, null=True)
    fuel_current_level = models.IntegerField(blank=True, null=True)
    monitoring_time = models.CharField(max_length=45,blank=True, null=True)
    diesel_on_time = models.CharField(max_length=45,blank=True, null=True)
    diesel_off_time = models.CharField(max_length=45,blank=True, null=True)
    fuel_level_name = models.CharField(max_length=45,blank=True, null=True)
    user = models.ForeignKey(User,  models.DO_NOTHING, db_column='user', related_name='created_user_fuel_level',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_fuel_level',blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
#*********************************************[BATTERY MASTER MODEL]***********************************************************



class BatteryMaster(models.Model):
    battery_master_id = models.AutoField(primary_key=True)
    battery_template = models.ForeignKey('BatteryTemplate', on_delete=models.CASCADE)
    battery_current_voltage = models.CharField(max_length=45, blank=True, null=True)
    battery_reading_timestamp = models.DateTimeField(blank=True, null=True)
    battery_template_name = models.CharField(max_length=45, blank=True, null=True)
    battery_name = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_battery_master',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_battery_master', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.battery_name

#*********************************[BATERY TEMPLATE]*************************************************************************


class BatteryTemplate(models.Model):
    battery_template_name = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)
    rating_ah = models.CharField(max_length=45, blank=True, null=True)
    quantity_nos = models.IntegerField(blank=True, null=True)
    charging_facility = models.IntegerField( blank=True, null=True)
    make = models.CharField(max_length=45, blank=True, null=True)
    battery_metering = models.CharField(max_length=45, blank=True, null=True)
    battery_current_voltage = models.CharField(max_length=45, blank=True, null=True)
    battery_reading_timestamp = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=45, blank=True, null=True)
    others = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_bt',blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_bt', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.battery_template_name

#*****************************************************[ADD MAINTENCE TEMPLATE ]***************************************************


class MaintenanceMaster(models.Model):
    dg_master = models.ForeignKey('DieselMaster',on_delete=models.CASCADE)
    dg_type = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    historical_cost = models.CharField(max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user')
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_maintenance', blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.dg_type

#*****************************************[ADD MaintenanceAuditTrial MODEL ]*****************************************


class MaintenanceAuditTrial(models.Model):
    maintenance_master = models.ForeignKey('MaintenanceMaster', on_delete=models.CASCADE)
    dg_master = models.ForeignKey('DieselMaster', on_delete=models.CASCADE)
    maintenance_master_name = models.CharField(max_length=45, blank=True, null=True)
    dg_name = models.CharField(max_length=45, blank=True, null=True)
    dg_number = models.IntegerField()
    dg_type = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=45, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', related_name='created_user_audit',
                             blank=True, null=True)
    modified_user = models.ForeignKey(User, models.DO_NOTHING, db_column='modified_user',
                                      related_name='modified_user_audit', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.maintenance_master