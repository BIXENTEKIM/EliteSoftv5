from django.forms import ModelForm

from setups.academics.campuses.models import Campuses


class CampusForm(ModelForm):
    class Meta:
        model = Campuses
        fields = '__all__'