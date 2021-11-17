from django.forms import ModelForm

from setups.accounts.accountmaster.models import AccountTypes
from setups.accounts.accountmaster.models import AccountGroups
from setups.accounts.accountmaster.models import AccountMain
from setups.accounts.accountmaster.models import AccountMaster


class AccountTypesForm(ModelForm):
    class Meta:
        model = AccountTypes
        fields = '__all__'

class AccountGroupsForm(ModelForm):
    class Meta:
        model = AccountGroups
        fields = '__all__'

class AccountMainForm(ModelForm):
    class Meta:
        model = AccountMain
        fields = '__all__'

class AccountMasterForm(ModelForm):
    class Meta:
        model = AccountMaster
        fields = '__all__'