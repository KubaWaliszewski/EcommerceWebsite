from shop.infrastructure.orm.models import Product as ProductORM, Category as CategoryORM, Review as ReviewORM
from shop.domain.entities import Product, Category, Review


class ProductMapper:
    @staticmethod
    def to_domain(product_orm: ProductORM) -> Product:
        reviews = [
            Review(
                id=review.id,
                user_id=review.user.id,
                rating=review.rating,
                comment=review.comment,
                created_at=review.created_at
            )
            for review in product_orm.reviews.all()
        ]
        return Product(
            id=product_orm.id,
            name=product_orm.name,
            slug=product_orm.slug,
            description=product_orm.description,
            price=product_orm.price,
            discount=product_orm.discount,
            stock=product_orm.stock,
            is_available=product_orm.is_available,
            category=CategoryMapper.to_domain(product_orm.category),
            created_at=product_orm.created_at,
            updated_at=product_orm.updated_at,
            image=product_orm.image,
            reviews=reviews,
        )


class CategoryMapper:
    @staticmethod
    def to_domain(category_orm: CategoryORM) -> Category:
        return Category(
            id=category_orm.id,
            name=category_orm.name,
            slug=category_orm.slug,
            created_at=category_orm.created_at,
        )
