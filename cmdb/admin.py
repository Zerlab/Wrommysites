from django.contrib import admin

# Register your models here.
from cmdb.models import bookInfo


class hbookInfo(admin.ModelAdmin):
    list_display = ('ranking','bookname','infos', 'appraise', 'peoplenum', 'content')

admin.site.register(bookInfo, hbookInfo)