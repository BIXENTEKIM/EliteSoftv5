from django.forms import ModelForm

from setups.academics.subjects.models import  Subjects


class SubjectForm(ModelForm):
    class Meta:
        model =  Subjects
        fields = '__all__'