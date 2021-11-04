from django.urls import path

from setups.academics.subjects import views

urlpatterns = [
	path(r'', views.subjects,name="subjects"),
    path(r'createSubject', views.createSubject, name="createSubject"),
    path(r'getSubjects', views.getSubjects, name="getSubjects"),
    path('editSubject/<int:id>', views.editSubject, name='editSubject'),
    path('updateSubject/<int:id>', views.updateSubject, name='updateSubject'),
    path('deleteSubject/<int:id>', views.deleteSubject, name='deleteSubject'),
    path('searchDepartment', views.searchDepartment, name='searchDepartment'),
    # path('searchclasses', views.searchclasses, name='searchclasses')

]