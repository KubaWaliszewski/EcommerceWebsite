from shop.infrastructure.orm.models import Product

class ProductRepository:
    def get_newest_products(self, limit):
        return Product.objects.filter(is_available=True).order_by('-created_at')[:limit]

    def get_products_by_category(self, category, limit):
        if not category:
            return []
        return Product.objects.filter(category=category, is_available=True)[:limit]
