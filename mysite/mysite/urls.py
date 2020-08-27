from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todaysdoing/', include('todaysdoing.urls')),
    path('admin/', admin.site.urls),
]
