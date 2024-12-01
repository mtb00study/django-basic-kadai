from django.contrib import admin
#from .models import Product
from .models import Product, Category
from django.utils.safestring import mark_safe

class ProductAdmin(admin.ModelAdmin):
  #list_display = ('id', 'name', 'price')
  #list_display = ('id', 'name', 'price', 'category')
  list_display = ('id', 'name', 'price', 'category', 'image')
  search_fields = ('name',)
  list_filter = ('category',)

  def image(self, obj):
    return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  search_fields = ('name',)

# Register your models here.
#admin.site.register(Product)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)