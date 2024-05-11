from django.contrib import admin
from .models import CustomUserModel, Task, Tag
# Register your models here.

admin.site.register(CustomUserModel)
admin.site.register(Task)
admin.site.register(Tag)


