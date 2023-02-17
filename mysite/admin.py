from django.contrib import admin
from .models import *

@admin.register(Comments)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','comment','image','published']
    list_filter = ['published']
    search_fields = ["id"]


@admin.register(MyResume)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['file']
    list_filter = ['file']
    search_fields = ["file"]


@admin.register(MyProjects)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['category','side','image','title','body','link','published']
    list_filter = ['category']
    search_fields = ["id"]


@admin.register(MySkills)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','image','published']
    list_filter = ['published']
    search_fields = ["id"]


@admin.register(MyWorkExprea)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','image','start_date','finish_date','published']
    list_filter = ['start_date','finish_date']
    search_fields = ["id"]


@admin.register(GetInTouch)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['fullname','email','body','published']
    list_filter = ['published']
    search_fields = ["id"]




