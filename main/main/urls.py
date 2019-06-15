from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
	url(r'^', include('apps.users.urls', namespace="users")),
	url(r'^admin/', admin.site.urls),
]
