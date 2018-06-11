from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('add/',views.AddView.as_view(),name='add'),
    path('delete/<int:pk>/',views.DeleteView.as_view(),name='delete'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
]
