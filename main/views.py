from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from httpx import post

from .forms import SignUpForm, UpdateForm, AddSkillForm, ServiceForm, AddBlogForm, AddPortfolioForm, UpdateBlogForm, \
    PartnerCommentForm, StatisticForm
from .models import User, Skill, Service, Blog, Comment, Portfolio, PartnerComment, Statistic


# HomePage View


def homepagefunc(request):
    if request.GET:
        key = request.GET.get('q')
        user = User.objects.filter(
            Q(first_name__contains=key) |
            Q(last_name__contains=key) |
            Q(username__contains=key) |
            Q(job__contains=key))
        return render(request, 'main.html', {'users': user})
    else:
        return render(request, 'main.html')


# Account Views


def signupfunc(request):
    if request.method == 'POST':
        data = SignUpForm(request.POST, files=request.FILES)
        try:
            if data.is_valid():
                data.save()
                return redirect('login')
            else:
                return HttpResponse(f"Xatolik: {data.errors}")
        except Exception as e:
            return HttpResponse(f"Xatolik yuz berdi: {e}")
    return render(request, 'signup.html')


def loginfunc(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('my-profile')
    return render(request, 'login.html')


@login_required
def logoutfunc(request):
    data = User.objects.filter(id=request.user.id).first()
    if data:
        logout(request)
        return redirect('home')


# Profile Views


@login_required
def my_profile_func(request):
    statis = Statistic.objects.filter(user_id_id=request.user.id).first()
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        if name and email and text:
            message = f"👤 Name: {name}\n📥 Email: {email}\n💬 Text: {text}"
            send_message(request.user.telegram_id, message)
            return redirect('my-profile')
    partners = PartnerComment.objects.filter(user_id_id=request.user.id)
    users = User.objects.filter(id=request.user.id).first()
    skills = Skill.objects.filter(user_id_id=request.user.id)
    services = Service.objects.filter(user_id_id=request.user.id)
    blogs = Blog.objects.filter(user_id_id=request.user.id).order_by('-created_at')
    portfolio = Portfolio.objects.filter(user_id_id=request.user.id).order_by('-create_at')

    return render(request, 'index.html',
                  {'users': users, 'statis': statis, "skills": skills, 'services': services, 'blogs': blogs,
                   'portfolios': portfolio, 'partners': partners})


def userfunc(request, username):
    users = User.objects.filter(username=username).first()
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        if name and email and text:
            message = f"👤 Name: {name}\n📥 Email: {email}\n💬 Text: {text}"
            send_message(users.telegram_id, message)
            return redirect(reverse('user', args=(str(username),)))
    if users:
        statis = Statistic.objects.filter(user_id_id=users.id).first()
        partners = PartnerComment.objects.filter(user_id_id=users.id)
        skills = Skill.objects.filter(user_id_id=users.id)
        services = Service.objects.filter(user_id_id=users.id)
        blogs = Blog.objects.filter(user_id_id=users.id).order_by('-created_at')
        portfolio = Portfolio.objects.filter(user_id_id=users.id).order_by('-create_at')
        return render(request, 'index.html',
                      {'users': users, 'statis': statis, "skills": skills, 'services': services, 'blogs': blogs,
                       'portfolios': portfolio, 'username': username, 'partners': partners})
    else:
        return HttpResponse('<h1 style="text-align: center; margin-top: 200px;">404 - Page Not Found!</h1>')


@login_required
def updatefunc(request):
    if request.POST:
        data = UpdateForm(request.POST, files=request.FILES,
                          instance=request.user)
        if data.is_valid():
            data.save()
            return redirect('my-profile')
    return render(request, 'update.html')


# Skill Views

@login_required
def add_skillfunc(request):
    if request.POST:
        data = AddSkillForm(request.POST)
        if data.is_valid():
            data.instance.user_id = request.user
            data.save()
            return redirect('my-profile')
    return render(request, 'add_skill.html')


@login_required
def update_skillfunc(request, pk):
    post = Skill.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if request.POST:
        skill_name = request.POST.get('title')
        level = request.POST.get('level')
        if skill_name and level:
            Skill.objects.filter(id=pk).update(title=skill_name, level=level)
            return redirect('my-profile')
    return render(request, 'add_skill.html', {'info': post})


@login_required
def delete_skillfunc(request, pk):
    post = Skill.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if post:
        Skill.objects.filter(id=pk).delete()
        return redirect('my-profile')


# Blog Views

@login_required
def add_blogfunc(request):
    if request.POST:
        data = AddBlogForm(request.POST, files=request.FILES)
        if data.is_valid():
            data.save()
            return redirect('my-profile')
    return render(request, 'add_blog.html')


@login_required
def update_blogfunc(request, pk):
    post = Blog.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if request.POST:
        form = UpdateBlogForm(request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my-profile')
    return render(request, 'add_blog.html', {'info': post})


@login_required
def delete_blogfunc(request, pk):
    post = Blog.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if post:
        Blog.objects.filter(id=pk).delete()
        return redirect('my-profile')


# Service Views

@login_required
def add_servicefunc(request):
    if request.POST:
        data = ServiceForm(request.POST)
        if data.is_valid():
            data.instance.user_id = request.user
            data.save()
            return redirect('my-profile')
    return render(request, 'add_service.html')


@login_required
def update_servicefunc(request, pk):
    post = Service.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if request.POST:
        service = request.POST.get('title')
        desc = request.POST.get('description')
        if service and desc:
            Service.objects.filter(id=pk).update(
                title=service, description=desc)
            return redirect('my-profile')
    return render(request, 'add_service.html', {'info': post})


@login_required
def delete_servicefunc(request, pk):
    post = Service.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if post:
        Service.objects.filter(id=pk).delete()
        return redirect('my-profile')


# Add Statistic

@login_required
def add_statistic(request):
    post = Statistic.objects.filter(user_id_id=request.user.id).first()
    if request.POST:
        if post:
            form = StatisticForm(request.POST, instance=post)
            if form.is_valid():
                form.instance.user_id = request.user
                form.save()
                return redirect('my-profile')
        else:
            form = StatisticForm(request.POST)
            if form.is_valid():
                form.instance.user_id = request.user
                form.save()
                return redirect('my-profile')
    return render(request, 'statistic.html')


# Portfolio Views

@login_required
def add_portfoliofunc(request):
    if request.POST:
        data = AddPortfolioForm(request.POST, files=request.FILES)
        if data.is_valid():
            data.instance.user_id = request.user
            data.save()
            return redirect('my-profile')
    return render(request, 'add-portfolio.html')


@login_required
def update_portfoliofunc(request, pk):
    post = Portfolio.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if request.POST:
        form = AddPortfolioForm(
            request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('my-profile')
    return render(request, 'add-portfolio.html', {'info': post})


@login_required
def delete_portfoliofunc(request, pk):
    post = Portfolio.objects.filter(id=pk).first()
    if request.user.id != post.user_id_id:
        return redirect('my-profile')
    if post:
        Portfolio.objects.filter(id=pk).delete()
        return redirect('my-profile')


# Partner Comments Views

def partner_commentfunc(request, username):
    if request.user.username == username:
        return redirect('my-profile')
    user = User.objects.filter(username=username).first()
    if request.POST:
        form = PartnerCommentForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.user_id = user
            form.save()
            return redirect(reverse('user', args=(str(username),)))
    return render(request, 'partner_comment.html', {'username': username})


# Send Telegram Bot

def send_message(telegram_id, message):
    try:
        url = f'https://api.telegram.org/bot6108967749:AAH7aVD7nSyHk6FZjdOjLWdHbYiVFkS_6rU/sendmessage'
        params = {
            'chat_id': int(telegram_id),
            'text': message
        }
        post(url, params=params)
    except:
        pass


# Content Views

def blogfunc(request, pk):
    posts = Blog.objects.filter(pk=pk).first()
    usr = User.objects.filter(id=posts.user_id_id).first()
    all_posts = Blog.objects.filter(user_id_id=usr.id).order_by('-created_at')[:6]
    if request.POST:
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        post_id = pk
        text = request.POST.get('text')
        if fullname and post_id and text and email:
            Comment.objects.create(fullname=fullname, email=email, post_id_id=post_id, text=text)
            return redirect(reverse('post', args=(pk,)))
    searchs = ''
    if request.GET:
        key = request.GET.get('s')
        searchs = Blog.objects.filter(title__contains=key)
    comments = Comment.objects.filter(post_id=pk).order_by('-created_at')
    return render(request, 'blog-single.html',
                  {'post': posts, 'user': usr, 'comments': comments, 'posts': all_posts, 'searchs': searchs})


def portfoliofunc(request, pk):
    portfolio = Portfolio.objects.filter(pk=pk).first()
    users = User.objects.filter(id=portfolio.user_id_id).first()
    return render(request, 'portfolio-details.html', {'portfolio': portfolio, 'users': users})
