from django.contrib import admin
from .models import Post_notice, Post_Question, Post_Answer

# Register your models here.
admin.site.register(Post_notice)
admin.site.register(Post_Question)
admin.site.register(Post_Answer)