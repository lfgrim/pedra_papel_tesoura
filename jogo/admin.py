from django.contrib import admin
from .models import Partida

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    list_display = (
        "jogador", "computador",
        "resultado", "criada_em"
    )
    list_filter = ("resultado","jogador","computador")
    search_fields = ("jogador","computador","resultado")