from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=125, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Notebook(models.Model):
    name = models.CharField(max_length=125)
    brand = models.CharField(max_length=125)
    number = models.CharField(max_length=13, unique=True)
    group = models.ForeignKey(Brand, related_name="notebook_group", on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Notebook"
        verbose_name_plural = "Notebooks"
        ordering = ["name", "brand"]

    def __str__(self):
        return f"{self.name} {self.brand}"


