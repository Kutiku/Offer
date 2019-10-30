from django.db import models
from multiselectfield import MultiSelectField


class Tax(models.Model):
    TaxOffice = models.CharField(max_length=100, verbose_name="Vergi Dairesi")
    TaxNumber = models.CharField(max_length=11, verbose_name="Vergi Numarası")

    def __str__(self):
        return self.TaxOffice


class Department(models.Model):
    dep_name = models.CharField(max_length=100, primary_key=True, verbose_name="Dep Adı")

    def __str__(self):
        return self.dep_name

class Company(Tax):
    full_name = models.CharField(max_length=200, verbose_name="Şirketin Tam Adı")
    short_name = models.CharField(max_length=50, verbose_name="Şirketin Kısaltımı")
    bagla = models.ManyToManyField(Department, verbose_name="Dep Seçiniz")

    def __str__(self):
        return self.short_name

class Depp(models.Model):
    cek = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Departman")

class Staff(Depp):
    bagla = models.ForeignKey(Company, on_delete=models.CASCADE)
    staff_name = models.CharField(max_length=100, verbose_name="Çalışan Adı")
    rütbe = [
        ("stj", "Stajyer"),
        ("jun", "junior"),
        ("sen", "Senior")
    ]
    staff_rank = models.CharField(max_length=20, choices=rütbe, verbose_name="Rank")
    staff_pay = models.PositiveIntegerField(default=10)
    contact_person = models.BooleanField(default=False)

    def __str__(self):
        return self.staff_name


class Ability(models.Model):
    bagla = models.ForeignKey(Staff, on_delete=models.CASCADE)
    seviye = [
        ("blg", "Başlangıç"),
        ("ort", "Orta"),
        ("uz", "Uzman")
    ]

    yeteneği = [
        ("rea", "React"),
        ("pyt", "Python"),
        ("ren", "React Native")
    ]
    ability = models.CharField(max_length=100, choices=yeteneği, verbose_name="Yeteneği")
    seviyesi = models.CharField(max_length=100, choices=seviye)