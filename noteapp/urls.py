from django.urls import path
from . import views
app_name = "noteapp"
urlpatterns = [
    path('note-add/',views.NoteCreateView.as_view(),name="note-add"),
    path('note/<int:pk>/',views.NoteDetailView.as_view(),name="note-detail"),
    path('note/<int:pk>/update/',views.NoteUpdateView.as_view(),name="note-update"),
    path('note/<int:pk>/delete/',views.NoteDeleteView.as_view(),name="note-delete"),
    path('note-list',views.NoteListView.as_view(),name="note-list"),
]