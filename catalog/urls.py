from django.urls import path, re_path

from catalog import views

app_name = 'catalog'
urlpatterns = [
    path('', views.item_list, name='item-list'),
    re_path(r'^(?P<pk>[1-9]\d*)/$', views.item_detail, name='item-detail'),
]
