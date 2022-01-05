from django.contrib import admin
#from django.db import models
from .models import Post, Category, Profile
#from tinymce.widgets import TinyMCE

# Register your models here.


# class PostAdmin(admin.ModelAdmin):
# formfield_overrides = {
#    models.TextField: {'widget': TinyMCE}
# }


#admin.site.register(Post, PostAdmin)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
