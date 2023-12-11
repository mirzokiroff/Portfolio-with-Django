from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Skill, Service, Blog, Portfolio, PartnerComment, Statistic


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'image', 'phone', 'email', 'job', 'password1', 'password2')


class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'image', 'phone', 'email', 'job', 'about_me', 'street', 'city', 'state',
            'telegram',
            'instagram', 'telegram_id')


class AddSkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('title', 'level')


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ('title', 'description')


class AddBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('user_id', 'image', 'title', 'description')


class AddPortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('image', 'title', 'category', 'description', 'company', 'project_url')


class UpdateBlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('image', 'title', 'description')


class StatisticForm(ModelForm):
    class Meta:
        model = Statistic
        fields = ('year', 'total_client', 'won')


class PartnerCommentForm(ModelForm):
    class Meta:
        model = PartnerComment
        fields = ('fullname', 'email', 'text')
