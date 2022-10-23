from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('predict/', include('predict.urls')),
    path('admin/', admin.site.urls),
    ]
