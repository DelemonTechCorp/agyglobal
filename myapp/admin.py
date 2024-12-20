from django.contrib import admin

from .models import Contact,Service,BlogPost

@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'phone', 'subject', 'submitted_at')
   search_fields = ('name', 'email', 'subject')
   list_filter = ('submitted_at',)
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
   list_display = ('title','description','image')
   search_fields =  ('title','description')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
   list_display = ('title','content','image','created_at')
   search_fields= ('title','content',)