class ListProductsUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, category_slug=None):
        categories = self.repository.list_categories()
        category = None

        if category_slug:
            category = self.repository.get_category_by_slug(category_slug)
            products = self.repository.list_products_by_category(category)
        else:
            products = self.repository.list_all_products()

        return products, category, categories



class GetProductDetailUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, category_slug, slug):
        product = self.repository.get_product_by_slug(slug)
        category = self.repository.get_category_by_slug(category_slug)
        category_products = []

        if category:
            category_products = self.repository.list_products_by_category(category)[:8]

        return product, category_products