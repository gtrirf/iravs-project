from django.shortcuts import render, redirect, get_object_or_404
from .models import Ideas, ReplyToIdea
from .forms import IdeasForm, ReplyToIdeaForm
from django.utils import timezone

def ideas_list_view(request):
    ideas = Ideas.objects.filter(replytoidea__isnull=False).distinct()
    form = IdeasForm()

    if request.method == 'POST':
        form = IdeasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideas_list')

    return render(request, 'ideas/ideas_list.html', {'ideas': ideas, 'form': form})

def reply_view(request, idea_id):
    idea = get_object_or_404(Ideas, id=idea_id)
    form = ReplyToIdeaForm()

    if request.method == 'POST':
        form = ReplyToIdeaForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.idea = idea
            reply.save()
            return redirect('ideas_list')

    return render(request, 'ideas/reply_form.html', {'form': form, 'idea': idea})
