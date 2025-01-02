from shop.infrastructure.orm.models import Category
from shop.infrastructure.orm.mappers import CategoryMapper
from shop.domain.entities import Category as CategoryEntity

    
class CategoryRepository:
    @staticmethod
    def create(data: dict) -> CategoryEntity:
        category_orm = Category(**data)
        category_orm.save()
        return CategoryMapper.to_domain(category_orm)

    @staticmethod
    def delete(category_id: int) -> None:
        category = Category.objects.get(id=category_id)
        category.delete()

    @staticmethod
    def get_filtered(query_params: dict) -> tuple[list[CategoryEntity], object, list[CategoryEntity]]:
        from admin_panel.infrastructure.filters import CategoryFilter
        
        categories = Category.objects.all()
        applied_filter = CategoryFilter(query_params, queryset=categories)
        domain_categories = [CategoryMapper.to_domain(category) for category in applied_filter.qs]
        return domain_categories, applied_filter, categories