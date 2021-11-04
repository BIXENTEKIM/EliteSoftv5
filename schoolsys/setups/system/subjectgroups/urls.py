from django.urls import path

from setups.academics.subjectgroups import views

urlpatterns = [
	path(r'', views.subjectgroups,name="subjectgroups"),
    path(r'createSubjectGroup', views.createSubjectGroup, name="createSubjectGroup"),
    path(r'getSubjectGroups', views.getSubjectGroups, name="getSubjectGroups"),
    path('editSubjectGroup/<int:id>', views.editSubjectGroup, name='editSubjectGroup'),
    path('updateSubjectGroup/<int:id>', views.updateSubjectGroup, name='updateSubjectGroup'),
    path('deleteSubjectGroup/<int:id>', views.deleteSubjectGroup, name='deleteSubjectGroup'),
    path('searchSubject', views.searchSubject, name='searchSubject'),
    # path('searchclasses', views.searchclasses, name='searchclasses')

]