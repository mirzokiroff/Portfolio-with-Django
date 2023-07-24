from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from httpx import post

from .models import Skill, Services, PortfolioInfo, Blog, About_me, Priz, CustomerOpinion, BlogSingle, \
    PersonalInfo, Comment


# Create your views here.
def home(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        Message = request.POST.get("text")
        if name and email and Message:
            message = f"Name: {name}, Email: {email}, Message: {Message}"
            send_message(message)
    skills = Skill.objects.all()
    services = Services.objects.all()
    blog = Blog.objects.all()
    about_me = About_me.objects.all()
    priz = Priz.objects.all()
    customer_opinion = CustomerOpinion.objects.all()
    main_portfolio = PortfolioInfo.objects.all()
    personal_info = PersonalInfo.objects.first()
    users = User.objects.filter(id=request.user.id).first()
    return render(request, 'index.html',
                  {'skills': skills, 'services': services, 'blog': blog, 'about_me': about_me, 'priz': priz,
                   'customer_opinion': customer_opinion, 'main_portfolios': main_portfolio, 'personal': personal_info,
                   'user': users})


def blog_single(request):
    blog = Blog.objects.all()
    blog_article = BlogSingle.objects.all()
    return render(request, 'blog_single.html', {'blog_articles': blog_article, 'blog': blog})


def portfolio_details(request, id):
    portfolio = PortfolioInfo.objects.filter(id=id).first()
    return render(request, 'portfolio_details.html', {'portfolio': portfolio})


def send_message(message):
    url = f'https://api.telegram.org/bot6108967749:AAH7aVD7nSyHk6FZjdOjLWdHbYiVFkS_6rU/sendmessage'
    params = {
        'chat_id': 5467465403,
        'text': message
    }
    post(url, params=params)


def commentfunc(request, pk):
    post = Blog.objects.filter(id=pk).first()
    if request.POST:
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        post_id = pk
        text = request.POST.get('text')
        if fullname and post_id and text and email:
            Comment.objects.create(
                fullname=fullname, email=email, post_id_id=post_id, text=text)
            return redirect(reverse('post', args=(pk, )))
    searchs = ''
    if request.GET:
        key = request.GET.get('s')
        searchs = BlogSingle.objects.filter(title__contains=key)
    comments = Comment.objects.filter(post_id=pk).order_by('created_at')
    return render(request, 'blog_single.html', {'comments': comments, 'searchs': searchs, 'post': post})
