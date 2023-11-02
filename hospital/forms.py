from django import forms
from django.contrib.auth.models import User
from . import models


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
        widgets = {"password": forms.PasswordInput()}


class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
        widgets = {"password": forms.PasswordInput()}


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ["direccion", "telefono", "departamento", "estado"]


class PacienteUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
        widgets = {"password": forms.PasswordInput()}


class PacienteForm(forms.ModelForm):
    assignedDoctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(estado=True),
        empty_label="Nombre y Departamento",
        to_field_name="user_id",
    )

    class Meta:
        model = models.Paciente
        fields = ["direccion", "telefono", "estado", "sintomas"]


class CitaForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(estado=True),
        empty_label="Nombre y Departamento del Doctor",
        to_field_name="user_id",
    )
    pacienteID = forms.ModelChoiceField(
        queryset=models.Paciente.objects.all().filter(estado=True),
        empty_label="Nombre del Paciente y Sintomas",
        to_field_name="user_id",
    )

    class Meta:
        model = models.Cita
        fields = ["descripcion", "estado"]


class PacienteCitaForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(estado=True),
        empty_label="Nombre y Departamento del Doctor",
        to_field_name="user_id",
    )

    class Meta:
        model = models.Cita
        fields = ["descripcion", "estado"]
