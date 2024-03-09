from django.contrib import admin
from django.urls import path, include

admin_urlpatterns = [
    path('admin/', admin.site.urls),

]

apps_urlpatterns = [
    path('', include('index.urls', namespace='index')),
    path('stock/', include('stock.urls', namespace='stock')),
    path('portfolio/', include('portfolio.urls', namespace='portfolio')),
    path('transactions/', include('transactions.urls', namespace='transactions')),
]

urlpatterns = admin_urlpatterns + apps_urlpatterns