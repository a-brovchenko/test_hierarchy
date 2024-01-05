from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('registration/', registration),
    path('workers_tree/', workers_tree),
    path('workers_info/', workers_info),
]