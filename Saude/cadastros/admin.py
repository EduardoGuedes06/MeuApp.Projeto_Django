from django.conf import PASSWORD_RESET_TIMEOUT_DAYS_DEPRECATED_MSG
from django.contrib import admin

# importar as classes

from .models import Paciente, UnidadeSolicitante, UnidadeExecutante, Procedimento, VagaOfertada
admin.site.register(Paciente)
admin.site.register(UnidadeSolicitante)
admin.site.register(UnidadeExecutante)
admin.site.register(Procedimento)
admin.site.register(VagaOfertada)
