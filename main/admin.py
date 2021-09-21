from django.contrib import admin
from .models import Hospital, Maindoctor, Doctor, Nurse, Patient

# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    list_display = ("name", "region")

admin.site.register(Hospital, HospitalAdmin)

class MainDoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "pin", "phone")

admin.site.register(Maindoctor, MainDoctorAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "pin", "position", "phone", "hospital", "nurse")

admin.site.register(Doctor, DoctorAdmin)

class NurseAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "pin", "phone")

admin.site.register(Nurse, NurseAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "pin", "phone", "hospital", "reason", "doctor", "nurse")

admin.site.register(Patient, PatientAdmin)