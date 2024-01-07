from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('registration/', registration),
    path('workers_tree/', workers_tree),
    path('workers_info/', workers_info),
    path('load_workers_level/', load_workers_level),
    path('sort/', sort_table),
    path('workers_info/create_worker/', create_worker),
    path('workers_info/delete_worker/', delete_user),
    path('workers_info/update_worker/', update_worker),
]