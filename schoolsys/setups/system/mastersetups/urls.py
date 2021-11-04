from django.urls import path

from setups.academics.mastersetups import views

urlpatterns = [
	path(r'', views.mastersetups,name="mastersetups"),
    path(r'createMasterSetups', views.createMasterSetups, name="createMasterSetups"),
    path(r'getMasterSetups', views.getMasterSetups, name="getMasterSetups"),
    path('editMasterSetups/<int:id>', views.editMasterSetups, name='editMasterSetups'),
    path('updateMasterSetups/<int:id>', views.updateMasterSetups, name='updateMasterSetups'),
    path('deleteMasterSetups/<int:id>', views.deleteMasterSetups, name='deleteMasterSetups'),
    # path('searchMasterSetups', views.searchMasterSetups, name='searchMasterSetups')

]