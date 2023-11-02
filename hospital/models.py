from django.db import models
from django.contrib.auth.models import User

# Create your models here.
departamentos = [
    ("Kinesiología", "Kinesiología"),
    ("Oftalmología", "Oftalmología"),
    ("Otorrinolaringología", "Otorrinolaringología")
]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20, null=True)
    departamento = models.CharField(
        max_length=50, choices=departamentos, default="Kinesiología"
    )
    estado = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.departamento)


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20, null=False)
    sintomas = models.CharField(max_length=100, null=False)
    asignadoDoctorId = models.PositiveIntegerField(null=True)
    admitirFecha = models.DateField(auto_now=True)
    estado = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + "(" + self.sintomas + ")"


class Cita(models.Model):
    pacienteID = models.PositiveIntegerField(null=True)
    doctorID = models.PositiveIntegerField(null=True)
    nombrePaciente = models.CharField(max_length=40, null=True)
    nombreMedico = models.CharField(max_length=40, null=True)
    fechaCita = models.DateField(auto_now=True)
    descripcion = models.TextField(max_length=500)
    estado = models.BooleanField(default=False)


class DetallesAltaPaciente(models.Model):
    idPaciente = models.PositiveIntegerField(null=True)
    nombrePaciente = models.CharField(max_length=40)
    nombreMedicoAsignado = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20, null=True)
    sintomas = models.CharField(max_length=100, null=True)

    fechaIngreso = models.DateField(null=False)
    fechaAlta = models.DateField(null=False)
    díasTranscurridos = models.PositiveIntegerField(null=False)

    honorariosMédico = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)
