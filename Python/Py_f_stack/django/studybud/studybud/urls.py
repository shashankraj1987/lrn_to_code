from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls), 
    path('',include('base.urls'))  # This tells django to have the base.urls handle all the routing.
]
