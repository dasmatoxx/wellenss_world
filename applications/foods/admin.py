from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Food, FoodImage


class InlineFoodImage(admin.TabularInline):
    model = FoodImage
    extra = 1
    fields = ['image', ]


class FoodAdminDisplay(admin.ModelAdmin):
    inlines = [InlineFoodImage, ]

    def image(self, obj):
        img = obj.image.first()
        if img:
            return mark_safe(f'<img src="{img.image.url}" width="80" height="80" style="object-fit: contain" />')
        else:
            return ""


admin.site.register(Food, FoodAdminDisplay)
