from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from orders.views import stripe_webhook_view
from products.views import IndexView, ProductsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('webhook/stripe', stripe_webhook_view, name='stripe_webhook'),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)