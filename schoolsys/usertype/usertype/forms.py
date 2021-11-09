from django.forms import ModelForm

from useradmin.users.models import UserType


class UsertypeForm(ModelForm):
    class Meta:
        model = UserType
        fields = '__all__'