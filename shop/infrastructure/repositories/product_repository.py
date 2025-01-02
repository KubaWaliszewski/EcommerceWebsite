from django.db.models import Q
from shop.infrastructure.orm.models import Product as ProductORM, Category as CategoryORM
from shop.infrastructure.orm.mappers import ProductMapper, CategoryMapper
from shop.infrastructure.orm.models import Product, Category
from django.core.exceptions import ObjectDoesNotExist


class ProductRepository:
    def search_products(self, query: str) -> list[Product]:
        products = ProductORM.objects.filter(
            is_available=True
        ).filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return [ProductMapper.to_domain(product) for product in products]

    def list_all_products(self) -> list[Product]:
        products = ProductORM.objects.filter(is_available=True)
        return [ProductMapper.to_domain(product) for product in products]

    def list_products_by_category(self, category) -> list[Product]:
        products = ProductORM.objects.filter(category_id=category.id, is_available=True)
        return [ProductMapper.to_domain(product) for product in products]

    def get_product_by_slug(self, slug) -> Product:
        product = ProductORM.objects.get(slug=slug, is_available=True)
        return ProductMapper.to_domain(product)

    def get_by_id(self, product_id):
        return ProductORM.objects.get(id=product_id)

    def list_categories(self) -> list[Category]:
        categories = CategoryORM.objects.all()
        return [CategoryMapper.to_domain(category) for category in categories]

    def get_category_by_slug(self, slug) -> Category:
        try:
            category = CategoryORM.objects.get(slug=slug)
            return CategoryMapper.to_domain(category)
        except ObjectDoesNotExist:
            return None


