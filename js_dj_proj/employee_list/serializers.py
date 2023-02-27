from rest_framework import serializers
from .models import *

class DepartmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['dep_name']

class TitlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        fields = ['tit_name']

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    emp_department = serializers.SlugRelatedField(
        read_only=True,
        slug_field='dep_name'
    )

    emp_title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='tit_name'
    )

    class Meta:
        model = Employee
        fields = ['name', 'second_name', 'last_name', 'number', 'emp_department', 'emp_title']