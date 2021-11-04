from django.forms import ModelForm

from setups.academics.subjects.models import SchoolSubjects


class SubjectForm(ModelForm):
    class Meta:
        model = SchoolSubjects
        fields = '__all__'