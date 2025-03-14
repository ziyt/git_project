from django.contrib import admin
from django.urls import path
from .views import home, elephant_info, lion_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('elephant/', elephant_info, name='elephant_info'),
    path('lion/', lion_info, name='lion_info'),
]
