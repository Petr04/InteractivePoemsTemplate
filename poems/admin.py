from django.contrib import admin

# Register your models here.

from .models import Poem, Paragraph

admin.site.register(Poem)
admin.site.register(Paragraph)
