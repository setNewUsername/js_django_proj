from django.db import models

class Department(models.Model):
    dep_name = models.CharField(max_length=40)

    def __str__(self):
        return self.dep_name

class Title(models.Model):
    tit_name = models.CharField(max_length=40)

    def __str__(self):
        return self.tit_name

class Employee(models.Model):
    name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    number = models.IntegerField(default=000)
    picture = models.CharField(default='none', max_length=40)

    emp_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    emp_title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.second_name + ' ' + self.second_name + ' ' + self.last_name}"
