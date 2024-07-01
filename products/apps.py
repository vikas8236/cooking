from django.apps import AppConfig
class productsConfig(AppConfig):
   
    name = 'products'
    def ready(self):
        import products.signals 
