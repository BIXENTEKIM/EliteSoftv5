from django.urls import path

from setups.accounts.accountmapping import views

urlpatterns = [
    path(r'', views.accountmapping,name="accountmapping"),
    path('getAccountmapping', views.getAccountmapping, name='getAccountmapping'),
    path('createAccountmapping', views.createAccountmapping, name='createAccountmapping'),
    path('editAccountmapping/<int:id>', views.editAccountmapping, name='editAccountmapping'),
	path('updateAccountmapping/<int:id>', views.updateAccountmapping, name='updateAccountmapping'),
	path('deleteAccountmapping/<int:id>', views.deleteAccountmapping, name='deleteAccountmapping'),
    path('searchAccountMaster', views.searchAccountMaster, name='searchAccountMaster'),
    path('searchAccountMaster2', views.searchAccountMaster2, name='searchAccountMaster2')
]