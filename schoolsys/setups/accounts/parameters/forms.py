from django.forms import ModelForm

from setups.system.parameters.models import  Parameters


class ParametersForm(ModelForm):
    class Meta:
        model = Parameters
        fields = '__all__'