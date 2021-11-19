from django.forms import ModelForm

from setups.accounts.accountmapping.models import AccountMapping



class AccountMappingForm(ModelForm):
    class Meta:
        model = AccountMapping
        fields = '__all__'