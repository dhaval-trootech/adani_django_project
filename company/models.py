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
        return f"object({self.id}) Company - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='companyProduct')
    category = models.OneToOneField('Category', on_delete=models.CASCADE, related_name='categoryProduct')

    def __str__(self):
        return f"object({self.id}) Product - {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return f"object({self.id}) Category - {self.name}"


class Color(models.Model):
    color = models.CharField(max_length=255)
    category = models.ManyToManyField(Category, related_name='categoryColor')

    def __str__(self):
        return f"object({self.id}) Color - {self.color}"
