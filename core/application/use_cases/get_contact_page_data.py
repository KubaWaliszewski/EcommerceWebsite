class GetContactPageData:
    def __init__(self, site_configuration_repository):
        self.site_configuration_repository = site_configuration_repository

    def execute(self):
        config = self.site_configuration_repository.get_or_create()
        return {'show_chat': config.show_chat}
