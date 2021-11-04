from django.urls import path

from setups.academics.departments import views

urlpatterns = [
	path(r'', views.departments,name="departments"),
    path(r'createDepartment', views.createDepartment, name="createDepartment"),
    path(r'getDepartments', views.getDepartments, name="getDepartments"),
    path('editDepartment/<int:id>', views.editDepartment, name='editDepartment'),
    path('updateDepartment/<int:id>', views.updateDepartment, name='updateDepartment'),
    path('deleteDepartment/<int:id>', views.deleteDepartment, name='deleteDepartment'),
    path('searchDepartment', views.searchDepartment, name='searchDepartment')

]