from rest_framework import viewsets

from .serializers import *
from .models import *

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentsSerializer

class EmployeeVuewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeesSerializer