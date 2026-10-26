from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path(
        'about/',
        views.about,
        kwargs={
            'company_name': 'FooBar',
            'company_phone': '88005553535'
        }
    ),
]