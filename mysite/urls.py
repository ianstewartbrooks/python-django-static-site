from django.contrib import admin
from django.urls import path, include

# add include to the above import so we can add our urls
# from our apps eg pages (like below)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
