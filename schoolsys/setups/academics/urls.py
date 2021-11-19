from django.urls import path, include

urlpatterns = [
	path(r'classes/', include('setups.academics.classes.urls')),
	path(r'termdates/', include('setups.academics.termdates.urls')),
	path(r'dorms/', include('setups.academics.dorms.urls')),
	path(r'departments/', include('setups.academics.departments.urls')),
	path(r'subjects/', include('setups.academics.subjects.urls')),
	path(r'campuses/', include('setups.academics.campuses.urls')),
	path(r'gradesgrid/', include('setups.academics.gradesgrid.urls')),
	path(r'mastersetups/', include('setups.academics.mastersetups.urls')),
	path(r'hmcomments/', include('setups.academics.hmcomments.urls')),
	path(r'subjectgroups/', include('setups.academics.subjectgroups.urls'))
]