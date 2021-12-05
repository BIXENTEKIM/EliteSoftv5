from django.forms import ModelForm

from setups.academics.departments.models import   Departments


class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'