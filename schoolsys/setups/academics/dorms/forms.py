from django.forms import ModelForm

from setups.academics.dorms.models import  SchoolDorms


class DormForm(ModelForm):
    class Meta:
        model = SchoolDorms
        fields = '__all__'