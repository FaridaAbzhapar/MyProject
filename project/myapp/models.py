from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Faculty(models.Model):
    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = "Факультеттер"

    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Position(models.Model):
    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = "Позициялар"

    p_name = models.CharField(max_length=100)

    def __str__(self):
        return self.p_name


class Role(models.Model):
    TORAGA = 1
    SENIOR_SECRETARY = 2
    SECRETARY = 3
    EMPLOYEE = 4
    ADMIN = 5
    ROLE_CHOICES = (
        (TORAGA, 'toraga'),
        (SENIOR_SECRETARY, 'senior_secretary'),
        (SECRETARY, 'secretary'),
        (EMPLOYEE, 'employee'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Employee(AbstractBaseUser):
    class Meta:
        verbose_name = 'Колдонуучу'
        verbose_name_plural = "Колдонуучулар"

    fio = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.IntegerField()

    def __str__(self):
        return self.fio


class Protocol(models.Model):
    p_number = models.IntegerField()


class Theme(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    toktom = models.TextField(null=True, blank=True)
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE)

# Create your models here.
