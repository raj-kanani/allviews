from django.urls import path
from .import views


urlpatterns = [
     path('student/', views.StuListView.as_view(), name='student'),
     path('student1/<int:pk>/', views.StuDetailView.as_view(), name='students'),
     path('contact/', views.ContactFormView.as_view(), name='contact'),
     path('create/', views.StudentCreateView.as_view(), name='create'),
     path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
     path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),


 ]