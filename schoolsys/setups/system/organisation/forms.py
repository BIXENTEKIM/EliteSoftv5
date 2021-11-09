from django.forms import ModelForm

from setups.system.organisation.models import Organisation


class OrganisationForm(ModelForm):
    class Meta:
        model = Organisation
        fields = '__all__'