
from django.urls import path
from .views import start_page_view, test_page, single_gadget_view, single_gadget_slug_view

urlpatterns = [
    path( '', start_page_view),
    path('test', test_page),
    path('single_gadget/<int:gadget_id>', single_gadget_view),
    path('single_gadget/<slug:gadget_slug>', single_gadget_slug_view)
]