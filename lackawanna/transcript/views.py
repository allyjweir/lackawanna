from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.http import HttpResponse
from django.contrib import messages


from braces.views import LoginRequiredMixin

from .models import Transcript

class TranscriptListView(LoginRequiredMixin, ListView):
    model = Transcript


class TranscriptCreateView(LoginRequiredMixin, CreateView):
    model = Transcript
    fields = ('owner', 'transcript', 'name', 'description',)
    success_url = reverse_lazy('transcript:list')


class TranscriptUpdateView(LoginRequiredMixin, UpdateView):
    model = Transcript
    fields = ('owner', 'transcript', 'name', 'description',)
    success_url = reverse_lazy('transcript:list')


class TranscriptDeleteView(LoginRequiredMixin, DeleteView):
    model = Transcript
    success_url = reverse_lazy('transcript:delete_confirmed')
    success_message = "Transcript was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TranscriptDeleteView, self).delete(request, *args, **kwargs)


class TranscriptDetailView(LoginRequiredMixin, DetailView):
    template_name = 'transcript/transcript_detail.html'
    model = Transcript

    def get_context_data(self, **kwargs):
        context = super(TranscriptDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
