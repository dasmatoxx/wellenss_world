from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from wellenss_world_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('category/', include('applications.food_time.urls')),
    path('forum/', include('applications.forum.urls')),
    path('food/', include('applications.foods.urls')),
    path('comment/', include('applications.comments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
