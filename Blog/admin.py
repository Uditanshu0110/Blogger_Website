from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostLike)
admin.site.register(PostComment)
admin.site.register(UserDetail)
