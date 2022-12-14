from django.contrib import admin
from django.urls import path
from room.views import post_list
from room.views import post_retrieve
from room.views import post_create
from room.views import post_update
from room.views import post_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listings/',post_list),
    path('listings/<int:pk>/',post_retrieve),
    path('listings/create/',post_create),
    path('listings/<int:pk>/edit',post_update),
    path('listings/<int:pk>/delete',post_delete)
]
