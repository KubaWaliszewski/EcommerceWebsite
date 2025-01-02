from shop.infrastructure.orm.models import Product
from shop.infrastructure.orm.mappers import ProductMapper


class ProductRepository:
    @staticmethod
    def get_filtered(query_params):
        from admin_panel.infrastructure.filters import ProductFilter
        
        products = Product.objects.all()
        applied_filter = ProductFilter(query_params, queryset=products)
        domain_products = [ProductMapper.to_domain(product) for product in applied_filter.qs]

        return domain_products, applied_filter, products
