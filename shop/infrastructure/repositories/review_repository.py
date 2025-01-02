from shop.infrastructure.orm.models import Product, Review
from orders.infrastructure.orm.models import OrderItem
from django.shortcuts import get_object_or_404

class ReviewRepository:
    def get_product_by_id(self, product_id):
        return get_object_or_404(Product, id=product_id)

    def has_user_purchased_product(self, user, product):
        return OrderItem.objects.filter(order__user=user, product=product).exists()

    def add_review(self, user, product, review_data):
        review = Review(
            product=product,
            user=user,
            rating=review_data.get('rating'),
            comment=review_data.get('comment'),
        )
        review.save()
        return review