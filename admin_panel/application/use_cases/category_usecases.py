from admin_panel.infrastructure.repositories.category_repository import CategoryRepository


def add_category(data):
    return CategoryRepository.create(data)

def delete_category(category_id):
    return CategoryRepository.delete(category_id)