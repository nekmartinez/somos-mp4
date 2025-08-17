
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pages.models import Page
from .forms import CommentForm
from .models import Comment

def inbox(request):
    comments = Comment.objects.select_related('author', 'page')[:50]
    return render(request, 'messaging/inbox.html', {'comments': comments})

@login_required
def add_comment(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.page = page
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comentario publicado.')
    return redirect('pages:page_detail', pk=page.pk)

@login_required
def add_reply(request, page_id, parent_id):
    page = get_object_or_404(Page, pk=page_id)
    parent = get_object_or_404(Comment, pk=parent_id, page=page)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.page = page
            reply.author = request.user
            reply.parent = parent
            reply.save()
            messages.success(request, 'Respuesta publicada.')
    return redirect('pages:page_detail', pk=page.pk)

@login_required
def toggle_like(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
            messages.info(request, 'Quitaste tu me gusta.')
        else:
            comment.likes.add(request.user)
            messages.success(request, 'Te gustó este comentario.')
    return redirect('pages:page_detail', pk=comment.page.pk)
