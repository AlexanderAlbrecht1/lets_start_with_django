
from django.urls import path
from .views import start_page_view, test_page, single_gadget_view

urlpatterns = [
    path( '', start_page_view),
    path('test', test_page),
    path('single_gadget', single_gadget_view)
]