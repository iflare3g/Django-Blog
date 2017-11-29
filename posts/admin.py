from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['__str__','date']
    list_filter = ['date']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    
class Meta:
    model = Post
    
admin.site.register(Post,PostAdmin)
