from django.urls import path

from . import views

app_name = 'trial'

urlpatterns = [
    path('', views.index, name='index'),
    path('document/create/', views.doc_create, name='doc_create'),
    path('document/result/<int:document_id>/', views.doc_result, name='doc_result'),
]