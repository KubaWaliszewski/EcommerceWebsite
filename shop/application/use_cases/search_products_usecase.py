class SearchProductsUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, query: str):
        if not query:
            return []
        return self.repository.search_products(query)
