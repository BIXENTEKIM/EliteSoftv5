from django.urls import path

from schoolsys.views import custom404
from usertype.usertype import views
handler404 = custom404
urlpatterns = [
	path(r'usertype', views.usertype, name="usertype"),
    path(r'createUsertype', views.createUsertype, name="createUsertype"),
    path(r'updateUsertype/<int:id>', views.updateUsertype, name="updateUsertype"),
    path(r'editUsertype/<int:id>', views.editUsertype, name="editUsertype"),
    path(r'deleteUsertype/<int:id>', views.deleteUsertype, name="deleteUsertype"),
    path(r'getUsertypes', views.getUsertypes, name="getUsertypes")

]