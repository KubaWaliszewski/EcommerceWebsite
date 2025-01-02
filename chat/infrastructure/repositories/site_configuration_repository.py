class SiteConfigurationRepository:
    def get_config(self):
        from core.infrastructure.orm.models import SiteConfiguration
        return SiteConfiguration.objects.first()