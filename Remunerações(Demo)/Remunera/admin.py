from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import RemuneraServ, CobrancaServ

class CobrancaResource(resources.ModelResource):
    class Meta:
        model = CobrancaServ

class CobrancaAdmin(ImportExportModelAdmin):
    resource_classes = [CobrancaResource]
        
admin.site.register(RemuneraServ)
admin.site.register(CobrancaServ, CobrancaAdmin)



# Register your models here.
