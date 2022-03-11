from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from wellenss_world_project import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Swagger Wellness-World",
      default_version='v1',
      description="developers Anton and Bektur",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/account/', include('applications.account.urls')),
    path('api/v1/category/', include('applications.food_time.urls')),
    path('api/v1/forum/', include('applications.forum.urls')),
    path('api/v1/food/', include('applications.foods.urls')),
    path('api/v1/comment/', include('applications.comments.urls')),

    path('swagger(.json|.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
