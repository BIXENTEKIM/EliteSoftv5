from django.urls import path

from setups.academics.dorms import views

urlpatterns = [
	path(r'', views.dorms,name="dorms"),
    path(r'createDorm', views.createDorm, name="createDorm"),
    path(r'getDorms', views.getDorms, name="getDorms"),
    path('editDorm/<int:id>', views.editDorm, name='editDorm'),
    path('updateDorm/<int:id>', views.updateDorm, name='updateDorm'),
    path('deleteDorm/<int:id>', views.deleteDorm, name='deleteDorm'),
    path('searchDorm', views.searchDorm, name='searchDorm')

]