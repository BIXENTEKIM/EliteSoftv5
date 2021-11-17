from django.urls import path

from setups.system.organisation import views

urlpatterns = [
    path(r'', views.organisation,name="organisation"),
    path('getOrganisations', views.getOrganisations, name='getOrganisations'),
    path('addOrganisation', views.addOrganisation, name='addOrganisation'),
    path('testProc', views.testProc, name='testProc'),
    path('editOrganisation/<int:id>', views.editOrganisation, name='editOrganisation'),
	path('updateOrganisation/<int:id>', views.updateOrganisation, name='updateOrganisation'),
	path('deleteOrganisation/<int:id>', views.deleteOrganisation, name='deleteOrganisation')

]