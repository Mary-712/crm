from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [     
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('log',views.log,name='log'),
    path('new',views.new,name='new'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('archieve',views.archieve,name='archieve'),

    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
