class GetHomePageData:
    def __init__(self, product_repository, category_repository):
        self.product_repository = product_repository
        self.category_repository = category_repository

    def execute(self, limit=8):
        newest_products = self.product_repository.get_newest_products(limit)
        electronics_category = self.category_repository.get_category_by_slug('electronics')
        tools_category = self.category_repository.get_category_by_slug('tools')

        electronics_products = (
            self.product_repository.get_products_by_category(electronics_category, limit)
            if electronics_category else []
        )
        tools_products = (
            self.product_repository.get_products_by_category(tools_category, limit)
            if tools_category else []
        )

        return {
            'products': newest_products,
            'electronics_products': electronics_products,
            'tools_products': tools_products,
        }
