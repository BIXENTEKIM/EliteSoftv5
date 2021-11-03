from django.forms import ModelForm

from setups.academics.departments.models import  SchoolDepartments


class DepartmentForm(ModelForm):
    class Meta:
        model = SchoolDepartments
        fields = '__all__'