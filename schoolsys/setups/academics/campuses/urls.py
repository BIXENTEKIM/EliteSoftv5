from django.urls import path

from setups.academics.campuses import views

urlpatterns = [
	path(r'', views.campuses,name="campuses"),
    path(r'createCampus', views.createCampus, name="createCampus"),
    path(r'getCampuses', views.getCampuses, name="getCampuses"),
    path('editCampus/<int:id>', views.editCampus, name='editCampus'),
    path('updateCampus/<int:id>', views.updateCampus, name='updateCampus'),
    path('deleteCampus/<int:id>', views.deleteCampus, name='deleteCampus'),
    path('searchCounty', views.searchCounty, name='searchCounty')

]