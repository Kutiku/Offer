from django.contrib import admin
from .models import Company, Department, Staff, Tax, Ability
# Register your models here.


class AbilAdmin(admin.TabularInline):
    model = Ability
    extra = 1
class StafAdmin(admin.ModelAdmin):
    inlines = [AbilAdmin]
    class Meta:
        model = Staff





admin.site.register(Company)
admin.site.register(Tax)
admin.site.register(Department)
admin.site.register(Staff, StafAdmin)

