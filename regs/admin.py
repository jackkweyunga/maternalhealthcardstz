from django.contrib import admin
from django.apps import apps
# Register your models here.

app_models = apps.get_models()

# Register all models in the regs app

for model in app_models:
    if model.__name__ not in ['Group']:
        admin.site.register(model)
