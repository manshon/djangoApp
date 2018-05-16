from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage

from .models import Board, Tag, Comment
from .forms import BoardCreateForm, CommentForm

from datetime import datetime
import re


def home(request):
    boards = Board.objects.order_by('-created_at')
    paginator = Paginator(boards, 3)
    page = request.GET.get('page', 1)
    try:
        boards = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        boards = paginator.page(1)

    return render(request, 'board/home.html',
                  {'boards': boards})


def detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    comments = board.comment.all()
    for comment in comments:
        print(comment.body)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = request.user.id
            comment.save()
            board.comment.add(comment)

            return HttpResponseRedirect(reverse('board:detail', args=(board_id,)))
    else:
        form = CommentForm()

    return render(request, 'board/detail.html',
                  {'board': board,
                   'comments': comments,
                   'form': form})


def create_board(request):
    if request.method == 'POST':
        form = BoardCreateForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.admin_user_id = request.user.id
            board.save()
            # title = form.cleaned_data.get('title')
            # body = form.cleaned_data.get('body')
            # tag_row = form.cleaned_data.get('tag')
            # tags = re.split('[,、\s]+', tag_row)
            # tag_set = []
            # for tag in tags:
            #     if not Tag.objects.filter(name=tag).exists():
            #         Tag.objects.create(name=tag)
            #     tag_set.append(Tag.objects.get(name=tag))
            #
            # Board.objects.create(title=title, body=body,  admin_user=request.user,
            #                      created_at=datetime.now(), updated_at=datetime.now())

            return redirect('board:home')
    else:
        form = BoardCreateForm()

        return render(request, 'board/create.html',
                      {'form': form})