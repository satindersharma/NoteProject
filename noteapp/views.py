from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, View, FormView
from django.views.generic import DetailView, TemplateView, UpdateView, ListView, DeleteView
from .models import Note
from .forms import NoteForm
from django.urls import reverse, reverse_lazy
# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    '''
    default home view
    '''


    template_name = 'home.html'

    def get_context_data(self,*args,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['objects_list'] = Note.objects.all()
        return context


class NoteCreateView(LoginRequiredMixin,CreateView):
    '''
    Note Create View
    '''
    model = Note
    template_name = 'note_form.html'
    form_class = NoteForm

    def get_success_url(self):
        if self.object is not None:
            obj = self.object
        else:
            obj = self.get_object()
        return obj.get_detail_url()

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDetailView(LoginRequiredMixin,DetailView):
    
    model = Note
    template_name = 'note_detail.html'



class NoteUpdateView(LoginRequiredMixin,UpdateView):
    '''
    Note Update View
    '''
    model = Note
    template_name = 'note_form.html'

    form_class = NoteForm

    def get_success_url(self):
        if self.object is not None:
            obj = self.object
        else:
            obj = self.get_object()
        return obj.get_detail_url()

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin,DeleteView):
    '''
    Note Delete View
    '''
    model = Note
    template_name = 'note_delete_confirm.html'
    success_url = reverse_lazy('noteapp:note-list')



class NoteListView(LoginRequiredMixin,ListView):
    model = Note
    template_name = 'note_page.html'