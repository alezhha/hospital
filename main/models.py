from django.db import models
from django.urls import reverse

# Create your models here.
class Hospital(models.Model):
    REGION = [
        # ("Bishkek", "Бишкекская"), 
        ("Osh", "Ошская"),
        ("Batken", "Баткенская"),
        ("Talas", "Таласская"),
        ("Naryn", "Нарынская"),
        ("IK", "Иссык-Кульская"),
        ("DjA", "Джалал-Абадская"),
        ("Chui", "Чуйская"),
    ]
    photo = models.ImageField(upload_to = 'main', null=True, blank=True)
    name = models.CharField('Название', max_length=255)
    region = models.CharField('Область', max_length=10, choices=REGION, default="Osh")
    ocpo = models.CharField("ОКПО", max_length=4, unique=True)
    gov = models.BooleanField("Государственное", default=False)
    doctor = models.OneToOneField("Doctor", on_delete=models.PROTECT, related_name="Врач", verbose_name="Врачи")
    maxn = models.IntegerField(verbose_name="Максимальное количество сотрудников", default=100)
    nurse = models.ForeignKey("Nurse", on_delete=models.CASCADE, verbose_name="Медсёстры")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Больница"
        verbose_name_plural = "Больницы"

class Nurse(models.Model):
    name = models.CharField("ФИО",max_length=100)
    pin = models.CharField("Пин",max_length=14)
    birthdate = models.DateField("Дата Рождения")
    phone = models.CharField("Номер Телефона",max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Медсестра"
        verbose_name_plural = "Медсестры"

    def get_absolute_url(self):
        return reverse("index")

class Maindoctor(models.Model):
    name = models.CharField("ФИО", max_length=255)
    pin = models.CharField("Пин", max_length=4)
    birthdate = models.DateField("Дата рождения")
    phone = models.CharField("Номер телефона", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Главрач"
        verbose_name_plural = "Главрачи"

class Doctor(models.Model):
    POSITION = [
        ("therapist", "Терапевт"),
        ("surgeon", "Хирург")
    ]
    position = models.CharField("Терапевт/Хирург", max_length=255, choices=POSITION, default="therapist")
    pin = models.CharField("Пин",max_length=14)
    name = models.CharField("ФИО",max_length=100)
    birthdate = models.DateField("Дата рождения")
    phone = models.CharField("Номер Телефона",max_length=10)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, related_name="Больница", verbose_name="Больница", default=1)
    nurse = models.ForeignKey("Nurse", on_delete=models.CASCADE, verbose_name="Медсестра")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def get_absolute_url(self):
        return reverse("index")

class Patient(models.Model):
    pin = models.CharField("Пин",max_length=14)
    name = models.CharField("ФИО",max_length=100)
    birthdate = models.DateField("Дата рождения")
    phone = models.CharField("Номер Телефона",max_length=10)
    hospital = models.ForeignKey("Hospital", on_delete=models.CASCADE, verbose_name="Больница")
    reason = models.CharField("Причина по которой в Больнице",max_length=255)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE, verbose_name="Врач")
    nurse = models.ForeignKey("Nurse", on_delete=models.CASCADE, verbose_name="Медсестра")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def get_absolute_url(self):
        return reverse("index")
