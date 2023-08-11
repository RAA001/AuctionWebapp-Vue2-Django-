from django.apps import AppConfig

"""This class is a productconfig which allows the app to run"""
class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'
