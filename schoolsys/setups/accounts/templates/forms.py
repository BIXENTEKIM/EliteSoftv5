from django.forms import ModelForm

from setups.system.templates.models import  Templates


class TemplatesForm(ModelForm):
    class Meta:
        model = Templates
        fields = '__all__'