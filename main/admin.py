from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Skill, Service, Statistic, PartnerComment, Portfolio, Blog
from .forms import AddSkillForm, ServiceForm, AddPortfolioForm, AddBlogForm, StatisticForm, PartnerCommentForm


class SkillAdmin(ModelAdmin):
    form = AddSkillForm


class ServiceAdmin(ModelAdmin):
    form = ServiceForm


class PortfoliosAdmin(ModelAdmin):
    form = AddPortfolioForm


class BlogAdmin(ModelAdmin):
    form = AddBlogForm
    # fields = ['name', 'category', 'description', 'banner']


class StatisticAdmin(ModelAdmin):
    form = StatisticForm


class PartnerCommentAdmin(ModelAdmin):
    form = PartnerCommentForm


admin.site.register(Skill, SkillAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Portfolio, PortfoliosAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Statistic, StatisticAdmin)
admin.site.register(PartnerComment, PartnerCommentAdmin)
