from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from pages.views import home, about

urlpatterns = [

    path('', RedirectView.as_view(pattern_name='home', permanent=False)),

    path('admin/', admin.site.urls),

    path('home/', home, name='home'),
    path('about/', about, name='about'),

    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    path('notifications/', include(('messaging.urls', 'messaging'), namespace='notifications')),

    path('messaging/', RedirectView.as_view(url='/notifications/', permanent=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
