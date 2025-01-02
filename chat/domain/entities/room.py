class Room:
    WAITING = 'waiting'
    ACTIVE = 'active'
    CLOSED = 'closed'

    def __init__(self, uuid, client, status, url=None, created_at=None, agent=None, messages=None):
        self.uuid = uuid
        self.client = client
        self.status = status
        self.url = url
        self.created_at = created_at
        self.agent = agent
        self.messages = messages or []
