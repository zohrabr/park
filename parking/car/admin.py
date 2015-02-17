from django.contrib import admin
from car.models import parking

# Register your models here.
class Park(admin.ModelAdmin):
	 list_display = ('namepark', 'nbrplace','proprietaire','accept','identifiant')

admin.site.register(parking,Park)
 
