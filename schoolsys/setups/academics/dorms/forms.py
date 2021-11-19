from django.forms import ModelForm

from setups.academics.dorms.models import  Dorms


class DormForm(ModelForm):
    class Meta:
        model = Dorms
        fields = '__all__'