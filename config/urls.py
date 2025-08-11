from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Урлы для приложения cash_flow
    path('', include('cash_flow.urls', namespace='cash_flow')),
]
