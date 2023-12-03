from .models import Notes
from .forms import NotesForm
from django.views.generic import CreateView,ListView,DetailView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

class NotesDeleteView(DeleteView):
    model= Notes
    success_url = '/notes/'
    template_name = 'notes/notes_delete.html'


class NotesCreateView(CreateView):
    model= Notes
    success_url = '/notes/'
    form_class = NotesForm


class NotesUpdateView(UpdateView):
    model= Notes
    success_url = '/notes/'
    form_class = NotesForm


class NotesListView( ListView):
    model = Notes
    context_object_name = "notes"
    login_url = '/admin'

    # def get_queryset(self):
    #     return self.request.user.notes.all()


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    



