from django.urls import path, include
from . import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view(), name='notes-list'),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name='detail-note'),
    path('notes/new', views.NotesCreateView.as_view(), name='new-note'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='delete-note'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='update-note'),   
]
