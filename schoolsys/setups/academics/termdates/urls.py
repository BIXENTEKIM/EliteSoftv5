from django.urls import path

from setups.academics.termdates import views

urlpatterns = [
	path(r'', views.termdates,name="termdates"),
    path(r'createtermdates', views.createtermdates, name="createtermdates"),
    path(r'gettermdates', views.gettermdates, name="gettermdates"),
    path('edittermdates/<int:id>', views.edittermdates, name='edittermdates'),
    path('updatetermdates/<int:id>', views.updatetermdates, name='updatetermdates'),
    path('deletetermdates/<int:id>', views.deletetermdates, name='deletetermdates'),
    path('searchclasses', views.searchclasses, name='searchclasses')

]