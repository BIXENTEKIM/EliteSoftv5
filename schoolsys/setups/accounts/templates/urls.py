from django.urls import path

from setups.system.templates import views

urlpatterns = [
	path(r'', views.templates,name="templates"),
    path(r'createTemplate', views.createTemplate, name="createTemplate"),
    path(r'getTemplates', views.getTemplates, name="getTemplates"),
    path('editTemplate/<int:id>', views.editTemplate, name='editTemplate'),
    path('updateTemplate/<int:id>', views.updateTemplate, name='updateTemplate'),
    path('deleteTemplate/<int:id>', views.deleteTemplate, name='deleteTemplate'),
    # path('searchParameter', views.searchParameter, name='searchParameter')

]