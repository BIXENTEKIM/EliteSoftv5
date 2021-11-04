from django.urls import path,include

from setups import views

urlpatterns = [
	path(r'academicsetups', views.academics, name="academics"),
	path(r'academics/', include('setups.academics.urls')),
	path(r'systemsetups', views.system, name="system"),
	path(r'system/', include('setups.system.urls'))

	]