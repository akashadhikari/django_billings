from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.company_name

class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)
    selection = models.IntegerField(default=0)

    def __str__(self):
        return self.department_name