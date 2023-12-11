from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import IntegerChoices, CASCADE

from root import settings


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    job = models.CharField(max_length=128, blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    telegram = models.URLField(max_length=128, null=True, blank=True)
    instagram = models.URLField(max_length=128, null=True, blank=True)
    telegram_id = models.CharField(max_length=25, null=True, blank=True)


class Skill(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='skill_user')
    title = models.CharField(max_length=128)
    level = models.IntegerField(default=0)


class Service(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='service_user')
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=400)


class Portfolio(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='portfolio_user')
    image = models.ImageField(upload_to='portfolio')
    title = models.CharField(max_length=128)

    class RateChoice(IntegerChoices):
        SOFT = 1, 'Software Development'
        CYBER = 2, 'Cybersecurity'
        CLOUD = 3, 'Cloud Computing'
        AI = 4, 'Artificial Intelligence and Machine Learning'
        ECOM = 5, 'E-commerce and Online Retail'
        GRAPH = 6, 'Graphic Design'

    category = models.PositiveIntegerField(choices=RateChoice.choices, default=RateChoice.SOFT)
    description = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    company = models.CharField(max_length=128)
    project_url = models.URLField(max_length=128)


class Blog(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='blog_user')
    image = models.ImageField(upload_to='blog_pics')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='comment_user')
    fullname = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    post_id = models.ForeignKey('main.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Statistic(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='statistic_user')
    year = models.PositiveIntegerField(default=0)
    total_client = models.PositiveIntegerField(default=0)
    won = models.PositiveIntegerField(default=0)


class PartnerComment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, CASCADE, related_name='partner_comment_user')
    fullname = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
