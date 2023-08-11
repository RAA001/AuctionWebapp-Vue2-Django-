from django.contrib import admin

# Register your models here.
from .models import Category,Profile,Product,Bids,Questions,Answers

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Bids)
admin.site.register(Questions)
admin.site.register(Answers)


