class GetAdminDashboardDataUseCase:
    def __init__(self, room_repository, site_config_repository):
        self.room_repository = room_repository
        self.site_config_repository = site_config_repository

    def execute(self):

        rooms = self.room_repository.get_all()
        config = self.site_config_repository.get_config()

        return {
            'rooms': rooms,
            'show_chat': config.show_chat if config else False,
        }
