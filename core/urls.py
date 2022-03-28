from django.urls import path
from .views import link_list, link_detail, link_create, link_update


urlpatterns = [
    path('', link_list),   # /havolalar/
    path('<int:havola_idisi>', link_detail),  # havolalar/10
    path('/create', link_create),    # havolalar/create
    path('<int:link_id>/update', link_update)  # localhost:8000/havolalar/54987/update
]
