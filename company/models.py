from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    established_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='userCompany')

    class Meta:
        db_table = 'adani_companies'
        verbose_name_plural = 'companies'

    def __str__(self):
        return f"{self.name.upper()}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companyProduct')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='categoryProduct')
    color = models.ForeignKey('color', on_delete=models.CASCADE, related_name='colorProduct')

    def __str__(self):
        return f"{self.name.upper()}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='categoryParent')

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"{self.name.upper()}"


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name.upper()}"
