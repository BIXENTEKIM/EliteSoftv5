from django.urls import path

from setups.academics.gradesgrid import views

urlpatterns = [
	path(r'', views.gradesgrid,name="gradesgrid"),
    path(r'createGradesgrid', views.createGradesgrid, name="createGradesgrid"),
    path(r'getGradesgrids', views.getGradesgrids, name="getGradesgrids"),
    path('editGradesgrid/<int:id>', views.editGradesgrid, name='editGradesgrid'),
    path('updateGradesgrid/<int:id>', views.updateGradesgrid, name='updateGradesgrid'),
    path('deleteGradesgrid/<int:id>', views.deleteGradesgrid, name='deleteGradesgrid'),
    path('searchDepartment', views.searchDepartment, name='searchDepartment'),
    # path('searchclasses', views.searchclasses, name='searchclasses')

]