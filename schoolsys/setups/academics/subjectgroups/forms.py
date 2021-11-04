from django.forms import ModelForm

from setups.academics.subjectgroups.models import SubjectGroups


class SubjectGroupsForm(ModelForm):
    class Meta:
        model = SubjectGroups
        fields = '__all__'