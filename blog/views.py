from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Tag


def article_list(request):
    articles = Article.objects.filter(is_published=True).prefetch_related('tags')

    tag_slug = request.GET.get('tag')
    selected_tag = None

    if tag_slug:
        selected_tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags=selected_tag)

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    all_tags = Tag.objects.all()

    context = {
        'page_obj': page_obj,
        'all_tags': all_tags,
        'selected_tag': selected_tag,
    }

    return render(request, 'blog/article_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)

    context = {
        'article': article,
    }

    return render(request, 'blog/article_detail.html', context)
