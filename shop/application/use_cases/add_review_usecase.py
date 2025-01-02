class AddReviewUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user, product_id, review_data):
        product = self.repository.get_product_by_id(product_id)
        
        if not self.repository.has_user_purchased_product(user, product):
            raise PermissionError("You can't review this product because you haven't purchased it.")
        
        self.repository.add_review(user, product, review_data)