from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('registration/', registration),
    path('workers_tree/', workers_tree),
    path('workers_info/', workers_info),
    path('load_workers_level/', load_workers_level),
    path('sort/', sort_table)
]