from django.contrib import admin
# from django.contrib.admin import ModelAdmin, TabularInline
# from django.utils.html import format_html
#
# from main.models import Product, Category, Rate, ProductImage
#
#
# class ProductImageInline(TabularInline):
#     model = ProductImage
#     fields = ('image',)
#     extra = 1
#
#
# @admin.register(Product)
# class ProductAdmin(ModelAdmin):
#     list_display = ('title', 'price', 'image', 'product_categories', 'is_active', 'button')
#     filter_horizontal = ['categories']
#     search_fields = ('title', 'price', 'categories__title')
#     sortable_by = ('title', 'price')
#     inlines = [ProductImageInline]
#     list_filter = ('created_at', 'is_active')
#     readonly_fields = ('is_active',)
#
#     def has_delete_permission(self, request, obj=None):
#         if request.user.is_superuser:
#             return super().has_change_permission(request, obj)
#         return False
#
#     def product_categories(self, obj):
#         return ', '.join(obj.categories.values_list('title', flat=True))
#
#     def image(self, obj):
#         try:
#             url = obj.productimage_set.first().image.url
#         except AttributeError:
#             url = ''
#         return format_html(f'<img style="border-radius: 5px;" width="100px" height="50px" src="{url}"/>')
#
#
#     def status(self, obj):
#         data = (
#             '''<script src="https://cdn.lordicon.com/fudrjiwc.js"></script><lord-icon src="https://cdn.lordicon.com/uutnmngi.json" trigger="hover" colors="primary:#4be1ec,secondary:#cb5eee" stroke="65" style="width:30px;height:30px"></lord-icon>''',
#             # 'pending': '<i class="fas fa-spinner fa-pulse" style="color: orange; font-size: 1.5em;"></i>',
#             '<i class="fa-solid fa-check" style="color: green; font-size: 1.5em;"></i>',
#             '<i class="fa-solid fa-circle-xmark"  style="color: red; font-size: 1.5em;"></i>'
#         )
#         return format_html(data[1] if obj.is_active else data[0])
#
#     def button(self, obj):
#         return format_html('''<a href="canceled/">
#                         <input type="button" style="background-color: #de8652;" value="Cancel">
#                     </a>''')
#
# # admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Rate)
# admin.site.register(ProductImage)

from .models import Skill, Services, PortfolioInfo, ProjectImages, Blog, About_me, Priz, CustomerOpinion, \
    PersonalInfo, BlogSingle, BlogImages
from .forms import SkillForm, ServiceForm, PortfolioDetailsForm, About_meForm, BlogForm, PrizForm, CustomerOpForm, \
    PersonalInfoForm, BlogDetailsForm


class PersonalAdmin(admin.ModelAdmin):
    form = PersonalInfoForm


class SkillAdmin(admin.ModelAdmin):
    form = SkillForm


class About_meAdmin(admin.ModelAdmin):
    form = About_meForm


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm


class ProfileImageAdmin(admin.TabularInline):
    model = ProjectImages
    fields = ['image']
    extra = 1


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [ProfileImageAdmin]


class PortfoliosAdmin(admin.ModelAdmin):
    form = PortfolioDetailsForm


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    # fields = ['name', 'category', 'description', 'banner']


class BlogImageAdmin(admin.TabularInline):
    model = BlogImages
    fields = ['image']
    extra = 1


class BlogsAdmin(admin.ModelAdmin):
    inlines = [BlogImageAdmin]


class PrizAdmin(admin.ModelAdmin):
    form = PrizForm


class CustomerOpAdmin(admin.ModelAdmin):
    form = CustomerOpForm


# class MainPortfolioAdmin(admin.ModelAdmin):
#     form = MainPortfolioForm


class BlogDetailsAdmin(admin.ModelAdmin):
    form = BlogDetailsForm


admin.site.register(PersonalInfo, PersonalAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(About_me, About_meAdmin)
admin.site.register(Services, ServiceAdmin)
admin.site.register(PortfolioInfo, PortfolioAdmin)
admin.site.register(Blog, BlogsAdmin)
admin.site.register(Priz, PrizAdmin)
admin.site.register(CustomerOpinion, CustomerOpAdmin)
# admin.site.register(MainPortfolio, MainPortfolioAdmin)
admin.site.register(BlogSingle, BlogDetailsAdmin)
