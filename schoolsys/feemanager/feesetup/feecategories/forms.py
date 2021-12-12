from django.forms import ModelForm

from feemanager.feesetup.feecategories.models import  FeeCategories


class FeeCategoriesForm(ModelForm):
    class Meta:
        model = FeeCategories
        fields = '__all__'