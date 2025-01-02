from django.contrib import messages
from shop.infrastructure.orm.models import Product
from admin_panel.interface.controllers.forms import ProductCreationForm, EditProductForm


class AddProductUseCase:
    @staticmethod
    def execute(request):
        form = ProductCreationForm()
        if request.method == 'POST':
            form = ProductCreationForm(request.POST, request.FILES)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.user = request.user
                new_product.save()
                messages.success(request, 'The product was added successfully')
                return True, None 
        return False, form
    

class EditProductUseCase:
    @staticmethod
    def execute(request, pk):
        product = Product.objects.get(id=pk)
        form = EditProductForm(instance=product)

        if request.method == 'POST':
            form = EditProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
                messages.success(request, 'The product was edited!')
                return True, None  

        return False, (form, product)