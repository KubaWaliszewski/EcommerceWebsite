class Message:
    def __init__(self, body, sent_by, created_at, created_by=None):
        self.body = body
        self.sent_by = sent_by
        self.created_at = created_at
        self.created_by = created_by
