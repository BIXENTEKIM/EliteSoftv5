from django.forms import ModelForm

from setups.academics.mastersetups.models import  MasterSetups


class MasterSetupsForm(ModelForm):
    class Meta:
        model = MasterSetups
        fields = '__all__'