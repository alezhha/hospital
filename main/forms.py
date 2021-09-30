from django import forms
from .models import Maindoctor, Patient, Doctor, Nurse

class AddPatient(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class AddNurse(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = "__all__"

class AddMaindoctor(forms.ModelForm):
    class Meta:
        model = Maindoctor
        fields = "__all__"

class AddDoctor(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
