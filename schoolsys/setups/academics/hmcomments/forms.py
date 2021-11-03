from django.forms import ModelForm

from setups.academics.hmcomments.models import HMComments


class HMCommentsForm(ModelForm):
    class Meta:
        model = HMComments
        fields = '__all__'