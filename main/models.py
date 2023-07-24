from django.db import models


class PersonalInfo(models.Model):
    image = models.ImageField(upload_to='personal_pics/')
    profile = models.CharField(max_length=222)
    tel_num = models.CharField(max_length=77)

    def __str__(self):
        return self.profile


class PortfolioInfo(models.Model):
    name = models.CharField(max_length=111)
    category = models.CharField(max_length=222)
    client = models.CharField(max_length=222)
    project_date = models.DateTimeField(auto_now_add=True)
    project_url = models.URLField(max_length=222)
    example_detail = models.TextField()

    def __str__(self):
        return self.category


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class About_me(models.Model):
    about_me = models.TextField()

    def __str__(self):
        return self.about_me


class Services(models.Model):
    name = models.CharField(max_length=111)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectImages(models.Model):
    image = models.ImageField(upload_to='profile_pics/')
    project = models.ForeignKey('main.PortfolioInfo', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.project.name


class Blog(models.Model):
    name = models.CharField(max_length=222)
    category = models.CharField(max_length=222)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogImages(models.Model):
    image = models.ImageField(upload_to='blog_pics/')
    blog = models.ForeignKey('main.Blog', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.blog.name


class Priz(models.Model):
    title = models.CharField(max_length=222)
    amount = models.PositiveIntegerField()
    upload_to = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CustomerOpinion(models.Model):
    name = models.CharField(max_length=111)
    description = models.TextField()
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# class MainPortfolio(models.Model):
#     title = models.CharField(max_length=222)
#     category = models.CharField(max_length=222)
#     upload_date = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title


class BlogSingle(models.Model):
    title = models.CharField(max_length=222)
    name = models.CharField(max_length=222)
    job = models.CharField(max_length=111)
    comment = models.PositiveIntegerField()
    article = models.TextField()
    main_data = models.CharField(max_length=9999)

    def __str__(self):
        return self.name


# class GetInTouch(models.Model):
#     name = models.CharField(222)
#     instagram = models.CharField(max_length=111)
#     facebook = models.CharField(max_length=111)
#     linkedin = models.CharField(max_length=111)
#     twitter = models.CharField(max_length=111)
#     about_it = models.CharField(max_length=111)
#     location = models.CharField(max_length=111)
#     phone = models.CharField(max_length=111)
#     email = models.CharField(max_length=111)
#
#     def __str__(self):
#         return self.name


class Comment(models.Model):
    fullname = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(max_length=128, blank=True, null=True)
    post_id = models.ForeignKey('main.Blog', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
