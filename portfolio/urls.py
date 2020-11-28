from django.contrib import admin
from django.urls import path
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='jobs/home'),
    path('earnings', jobs.views.earnings, name='/jobs/earnings')
]
