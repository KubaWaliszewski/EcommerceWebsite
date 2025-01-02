from shop.infrastructure.orm.models import Category

class CategoryRepository:
    def get_category_by_slug(self, slug):
        return Category.objects.filter(slug=slug).first()
