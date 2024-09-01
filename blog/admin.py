from django.contrib import admin
from blog.models import *

admin.site.register(User)
admin.site.register(BlogPost)
admin.site.register(Comment)
