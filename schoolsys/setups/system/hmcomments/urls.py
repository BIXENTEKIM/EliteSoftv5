from django.urls import path

from setups.academics.hmcomments import views

urlpatterns = [
	path(r'', views.hmcomments,name="hmcomments"),
    path(r'createHMComments', views.createHMComments, name="createHMComments"),
    path(r'getHMComments', views.getHMComments, name="getHMComments"),
    path('editHMComments/<int:id>', views.editHMComments, name='editHMComments'),
    path('updateHMComments/<int:id>', views.updateHMComments, name='updateHMComments'),
    path('deleteHMComments/<int:id>', views.deleteHMComments, name='deleteHMComments'),
    # path('searchclasses', views.searchclasses, name='searchclasses')

]