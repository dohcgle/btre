from django.db import models
from datetime import datetime
from django.urls import reverse


class Realtor(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name = "Realtor"
        verbose_name_plural = "Realtors"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Realtor_detail", kwargs={"pk": self.pk})
