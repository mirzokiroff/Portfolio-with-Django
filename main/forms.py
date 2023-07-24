from django import forms

from .models import Skill, Services, PortfolioInfo, Blog, Priz, About_me, CustomerOpinion, BlogSingle, \
    PersonalInfo


class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = ['profile', 'tel_num', 'image']


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']


class About_meForm(forms.ModelForm):
    class Meta:
        model = About_me
        fields = ['about_me']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['name', 'description']


class PortfolioDetailsForm(forms.ModelForm):
    class Meta:
        model = PortfolioInfo
        fields = ['category', 'client', 'project_url', 'example_detail']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'category', 'description']


class PrizForm(forms.ModelForm):
    class Meta:
        model = Priz
        fields = ['title', 'amount']


class CustomerOpForm(forms.ModelForm):
    class Meta:
        model = CustomerOpinion
        fields = ['name', 'description']


# class MainPortfolioForm(forms.ModelForm):
#     class Meta:
#         model = MainPortfolio
#         fields = ['title', 'category']


class BlogDetailsForm(forms.ModelForm):
    class Meta:
        model = BlogSingle
        fields = ['title', 'name', 'job', 'comment', 'article', 'main_data']
