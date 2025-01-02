class ToggleChat:
    def __init__(self, site_configuration_repository):
        self.site_configuration_repository = site_configuration_repository

    def execute(self):
        self.site_configuration_repository.toggle_show_chat()
