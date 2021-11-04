from django.forms import ModelForm

from setups.academics.campuses.models import SchoolCampuses


class CampusForm(ModelForm):
    class Meta:
        model = SchoolCampuses
        fields = '__all__'