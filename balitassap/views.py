
from django.shortcuts import render, redirect
from telethon.tl.types import PhotoSize

from .pagenation import Pagination
from .models import Post, Contact, Comment, Tags, Category


def home(request):
    sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]
    more = Post.objects.all().order_by('created_at')[:3]
    posts = Post.objects.all().order_by('-created_at')
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    uchtalik = Post.objects.all().order_by('created_at')[2:5]
    carousel = Post.objects.filter(is_published=True).order_by('created_at')
    pagenator = Pagination(posts , 2)
    data = request.GET
    page = int(data.get('page' , 1 ))


    a = {
        # 'posts': posts,
        'carousel':carousel,
        'sidebar':sidebar,
        'more':more,
        'uchtalik':uchtalik,
        'latest':latest,
        'posts': pagenator.get_page(page),
        'page_count': range(1, pagenator.page_count + 1),
        'current_page': page,
        'next_page': page + 1,
        'prev_page': page - 1,
        'is_last': pagenator.is_last(page),
        'is_first': pagenator.is_first(page),
    }
    return render(request, 'index.html', context=a)


def about(request):
    sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]
    posts = Post.objects.all()
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    comment_count = Comment.objects.filter(name=id).count()

    a = {
        'posts': posts,
        'sidebar':sidebar,
        'latest':latest,
        'comment_count': comment_count,

    }
    return render(request, 'about.html' , context=a)


def blog(request ,pk):
    post = Post.objects.all()
    a = {
        'post':post
    }
    return render(request, 'blog.html' , a)


def blog_single(request, pk):
    print('*' * 50)
    print(request.method)
    print('*' * 50)

    post = Post.objects.get(id=pk)
    post.views_count += 1
    post.save()
    comment = Comment.objects.filter(post=post).order_by('-created_at')
    comment_count = Comment.objects.filter(post=post).count()
    sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]
    tags = Tags.objects.filter(post=post)
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]


    a = {
        'post':post,
        'comments':comment,
        'comment_count': comment_count,
        'sidebar': sidebar,
        'tags': tags,
        'latest':latest
    }



    return render(request, 'blog-single.html', context=a)


def category(request , name):
    posts = Post.objects.filter(category__name=name)
    pagenator = Pagination(posts , 2)
    data = request.GET
    page = int(data.get('page' , 1 ))
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]

    a = {
        'posts': pagenator.get_page(page),
        'page_count': range(1, pagenator.page_count + 1),
        'current_page': page,
        'next_page': page + 1,
        'prev_page': page - 1,
        'sidebar':sidebar,
        'is_last': pagenator.is_last(page),
        'is_first': pagenator.is_first(page),
        'latest':latest,

    }
    return render(request, 'category.html' , context=a)


def contact(request):
    posts = Post.objects.all()
    sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    comment_count = Comment.objects.filter(name=id).count()


    a = {
        'posts' : posts ,
        'sidebar':sidebar,
        'latest':latest,
        'comment_count': comment_count + 1,

    }
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        message = data.get('message')

        obj = Contact.objects.create( name = name, email = email, phone = phone , message = message)
        obj.save()
        return redirect('/contact/')

    return render(request, 'contact.html' , context=a)


def uchtalik(request):
    posts = Post.objects.all()[:3]
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    comment_count = Comment.objects.filter(name=id).count()

    a ={
        'posts':posts,
        'latest':latest,
        'comment_count': comment_count + 1,

    }
    return render(request , 'uchtalik.html' , context=a)


def tags(request , tags):
    posts = Post.objects.filter(tag__name = tags).order_by('-views_count')
    sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]
    latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
    pagenator = Pagination(posts , 2)
    data = request.GET
    page = int(data.get('page' , 1 ))
    comment_count = Comment.objects.filter(name=id).count()

    a = {
        'latest':latest,
        'sidebar':sidebar,
        'posts': pagenator.get_page(page),
        'page_count': range(1, pagenator.page_count + 1),
        'current_page': page,
        'next_page': page + 1,
        'prev_page': page - 1,
        'is_last': pagenator.is_last(page),
        'is_first': pagenator.is_first(page),
        'comment_count': comment_count + 1,

    }

    return render(request, 'tags.html' , context=a)


def comment_create(request , pk):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        website = data.get('website')
        message = data.get('message')
        obj = Comment.objects.create( name = name, email = email, website = website , message = message, post_id=pk)
        obj.save()
        return redirect(f'/blog-single/{ pk }/')


def search(request ):
    if request.method == 'POST':
        search_query = request.POST.get('query')
        posts = Post.objects.filter(title__icontains=search_query)
        latest = Post.objects.filter(is_published=True).order_by('-created_at')[:3]
        sidebar = Post.objects.filter(is_published=True).order_by("-views_count")[:3]

        # pagenator = Pagination(posts , 2)
        # data = request.GET
        # page = int(data.get('page' , 1 ))

        a = {
            'posts': posts,
            'sidebar':sidebar,
            'latest':latest,

            # 'page_count': range(1, pagenator.page_count + 1),
            # 'current_page': page,
            # 'next_page': page + 1,
            # 'prev_page': page - 1,
            # 'is_last': pagenator.is_last(page),
            # 'is_first': pagenator.is_first(page),

        }
        return render(request, 'search.html' , context=a)





