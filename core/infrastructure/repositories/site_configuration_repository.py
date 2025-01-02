from core.infrastructure.orm.models import SiteConfiguration

class SiteConfigurationRepository:
    def get_or_create(self):
        config, _ = SiteConfiguration.objects.get_or_create(pk=1)
        return config

    def toggle_show_chat(self):
        config, _ = SiteConfiguration.objects.get_or_create(pk=1)
        config.show_chat = not config.show_chat
        config.save()
