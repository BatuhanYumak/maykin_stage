from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotels/', views.hotel, name='hotel'),
    path('amsterdam/', views.amsterdam, name='ams'),
    path('antwerpen/', views.antwerpen, name='antw'),
    path('athene/', views.athene, name='ath'),
    path('bangkok/', views.bangkok, name='bak'),
    path('barcelona/', views.barcelona, name='bar'),
    path('berlijn/', views.berlijn, name='ber'),





    # path('antwerpen/', )
    # path('hotels/<int:hotel_id>', views.hotel_detail, name='hotel_detail'),
]


# urlpatterns(r'^$', 'index', name='index'),
# urlpatterns(r'^blog$', 'horel', name='blog'),