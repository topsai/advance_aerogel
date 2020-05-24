from django.contrib import admin

# Register your models here.
from .models import Blog


# 注册该模型
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['title', 'add_date', 'mod_date']
