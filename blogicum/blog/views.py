from datetime import datetime

from django.shortcuts import render, get_object_or_404  # type: ignore

from blog.models import Post, Category


current_date = datetime.now()


def index(request):

    template = 'blog/index.html'

    post_list = Post.objects.select_related(
        'category', 'location').filter(
            is_published=True,
            category__is_published=True,
            pub_date__date__lte=current_date)[:5]

    context = {'post_list': post_list}

    return render(request, template, context)


def post_detail(request, pk):

    post = get_object_or_404(
        Post.objects.select_related(
            'category', 'location'
        ).filter(pub_date__date__lte=current_date,
                 is_published=True,
                 category__is_published=True), pk=pk)

    context = {'post': post}
    template = 'blog/detail.html'

    return render(request, template, context)


def category_posts(request, category_slug):

    template = 'blog/category.html'

    category = get_object_or_404(
        Category, slug=category_slug, is_published=True)

    post_detail = Post.objects.select_related(
        'category', 'location').filter(
            category__slug=category_slug,
            category__is_published=True,
            pub_date__date__lte=current_date,
            is_published=True)

    context = {'post_list': post_detail,
               'category': category}

    return render(request, template, context)
