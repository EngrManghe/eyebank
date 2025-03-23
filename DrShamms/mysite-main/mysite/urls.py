import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from mysite.views import custom_logout_view  # Import the custom logout view
from django.conf import settings
from django.conf.urls.static import static

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('hello/', include('hello.urls')),
    path('accounts/logout/', custom_logout_view, name='logout'),  # Use custom logout view
    path('accounts/', include('django.contrib.auth.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('ads/', include('ads.urls')),
    path("change-password/", auth_views.PasswordChangeView.as_view()),                                                                    
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
    path('', TemplateView.as_view(template_name='home/main.html')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)