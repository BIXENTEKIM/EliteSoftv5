from django.urls import path

from setups.system.parameters import views

urlpatterns = [
	path(r'', views.parameters,name="parameters"),
    path(r'createParameter', views.createParameter, name="createParameter"),
    path(r'getParameters', views.getParameters, name="getParameters"),
    path('editParameter/<int:id>', views.editParameter, name='editParameter'),
    path('updateParameter/<int:id>', views.updateParameter, name='updateParameter'),
    path('deleteParameter/<int:id>', views.deleteParameter, name='deleteParameter'),
    # path('searchParameter', views.searchParameter, name='searchParameter')

]