from django.apps import AppConfig

# Define la configuración de la aplicación 'pagina'
class PaginaConfig(AppConfig):
    # Define el tipo de campo automático predeterminado para los modelos de esta aplicación
    default_auto_field = 'django.db.models.BigAutoField'
    # Define el nombre de la aplicación
    name = 'pagina'
