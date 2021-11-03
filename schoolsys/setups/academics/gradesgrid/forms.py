from django.forms import ModelForm

from setups.academics.gradesgrid.models import GradesGrid


class GradesGridForm(ModelForm):
    class Meta:
        model = GradesGrid
        fields = '__all__'