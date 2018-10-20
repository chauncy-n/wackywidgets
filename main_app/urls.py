from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='base'),
    path('<int:pk>/delete', views.WidgetDelete.as_view(), name="widgets_delete"),
]