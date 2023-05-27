from django.contrib import admin

from school. models import Product,Department,Course,Person

# Register your models here.
admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Person)