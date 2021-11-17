from django.urls import path

from setups.accounts.accountmaster import views

urlpatterns = [
    path(r'', views.accountmaster,name="accountmaster"),
    path('getAccountmaster', views.getAccountmaster, name='getAccountmaster'),
    path('createAccountmaster', views.createAccountmaster, name='createAccountmaster'),
    path('editAccountmaster/<int:id>', views.editAccountmaster, name='editAccountmaster'),
	path('updateAccountmaster/<int:id>', views.updateAccountmaster, name='updateAccountmaster'),
	path('deleteAccountmaster/<int:id>', views.deleteAccountmaster, name='deleteAccountmaster'),
    path('searchAccountMain', views.searchAccountMain, name='searchAccountMain'),
    path('searchAccountGroup', views.searchAccountGroup, name='searchAccountGroup')
]