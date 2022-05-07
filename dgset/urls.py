"""dgset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from dg.views import *
from django.conf.urls.static import static

from dgset import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', signup, name='register'),

#******************************************************[PASSWORD ALL URLS]******************************************************

    path('change-password',
         auth_views.PasswordChangeView.as_view(template_name='password/change-password.html', success_url='/'),
         name='change-password'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'),
         name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_done.html'),
         name='password_reset_complete'),

#***************************************[add city URLS]************************************************************************

    path('city_form.html/', city_form, name='city_form'),
    path('city_list/', city_list, name='city_list'),
    path('city_form/<int:id>/', city_form, name='city_update'),
    path('delete/<int:id>/', city_delete, name='city_delete'),

#*********************************************[add state urls]*****************************************************************

    path('state_list/', state_list, name='state_list'),
    path('state_form/', state_form, name='state_form'),
    path('state_form/<int:id>/', state_form, name='state_update'),
    path('state_delete/<int:id>/', state_delete, name='state_delete'),

#*******************************************[ADD COUNTRY URLS]******************************************************************

    path('country_list/', country_list, name='country_list'),
    path('country_form/', country_form, name='country_form'),
    path('country_form/<int:id>/', country_form, name='country_update'),
    path('country_delete/<int:id>/', country_delete, name='country_delete'),
#***********************************[profile url]*******************************************************************************

    path('profile/', profile, name='profile'),
    path('profilehome/', profilehome, name='profilehome'),

#****************************************************[COMPANY URLS ]******************************************************


    path('company_list/', company_list, name='company_list'),
    path('company_form/', company_form, name='company_form'),
    path('company_form/<int:id>/', company_form, name='company_update'),
    path('company_delete/<int:id>/', company_delete, name='company_delete'),


#************************************[DIESEL URL]*********************************************************************

    path('dm_list/', dm_list, name='dm_list'),
    path('dm_form/', dm_form, name='dm_form'),
    path('dg_form/<int:id>/', dm_form, name='dm_update'),
    path('dm_delete/<int:id>/', dm_delete, name='dm_delete'),

    path('location_list/', location_list, name='location_list'),
    path('location_form/', location_form, name='location_form'),
    path('location_form/<int:id>/', location_form, name='location_update'),
    path('location_delete/<int:id>/', location_delete, name='location_delete'),

    path('dg_template_list/', dg_template_list, name='dg_template_list'),
    path('dg_template_form/', dg_template_form, name='dg_template_form'),
    path('dg_template_form/<int:id>/', dg_template_form, name='dg_template_update'),
    path('dg_template_delete/<int:id>/', dg_template_delete, name='dg_template_delete'),

    path('bm_form/', bm_form, name='bm_form'),
    path('bm_form/<int:id>/', bm_form, name='bm_update'),
    path('bm_delete/<int:id>/', bm_delete, name='bm_delete'),
    path('bm_list/', bm_list, name='bm_list'),

    path('condition_form/', condition_form, name='condition_form'),
    path('condition_form/<int:id>/', condition_form, name='condition_update'),
    path('condition_delete/<int:id>/', condition_delete, name='condition_delete'),
    path('condition_list/', condition_list, name='condition_list'),

    path('external_tank_list/', external_tank_list, name='external_tank_list'),
    path('external_tank_form/', external_tank_form, name='external_tank_form'),
    path('external_tank_form/<int:id>/', external_tank_form, name='external_tank_update'),
    path('external_tank_delete/<int:id>/', external_tank_delete, name='external_tank_delete'),

    path('fuel_level_list/', fuel_level_list, name='fuel_level_list'),
    path('fuel_level_form/', fuel_level_form, name='fuel_level_form'),
    path('fuel_level_form/<int:id>/', fuel_level_form, name='fuel_level_update'),
    path('fuel_level_delete/<int:id>/', fuel_level_delete, name='fuel_level_delete'),

    path('battery_template_form/', battery_template_form, name='battery_template_form'),
    path('battery_template_form/<int:id>/', battery_template_form, name='battery_template_update'),
    path('battery_template_delete/<int:id>/', battery_template_delete, name='battery_template_delete'),
    path('battery_template_list/', battery_template_list, name='battery_template_list'),

#************************************[ADD MAINTENCE URL ]********************************************************************

    path('maintenance_form.html/', maintenance_form, name='maintenance_form'),
    path('maintenance_form.html/<int:id>/', maintenance_form, name='maintenance_update'),
    path('maintenance_delete/<int:id>/', maintenance_delete, name='maintenance_delete'),
    path('maintenance_list.html/', maintenance_list, name='maintenance_list'),

#***************************************************[ ]*********************************************************************

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
