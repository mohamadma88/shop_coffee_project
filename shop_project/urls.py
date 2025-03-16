from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

        path('admin/', admin.site.urls),
        path('', include('home.urls')),
        path('product/', include('product.urls')),
        path('article/', include('article.urls')),
        path('contactus/', include('contactus.urls')),
        path('', include('account.urls')),
        path('cart/', include('cart.urls')),
        path('dashboard/', include('dashboard.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'home.views.page_404'
