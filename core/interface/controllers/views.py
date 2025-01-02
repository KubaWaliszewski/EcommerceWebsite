from django.shortcuts import render, redirect

from core.interface.decorators import check_group

from core.infrastructure.repositories.product_repository import ProductRepository
from core.infrastructure.repositories.category_repository import CategoryRepository
from core.infrastructure.repositories.site_configuration_repository import SiteConfigurationRepository
from core.application.use_cases.get_home_page_data import GetHomePageData
from core.application.use_cases.get_contact_page_data import GetContactPageData
from core.application.use_cases.toggle_chat import ToggleChat


def home(request):
    product_repository = ProductRepository()
    category_repository = CategoryRepository()
    use_case = GetHomePageData(product_repository, category_repository)

    data = use_case.execute(limit=8)
    return render(request, 'core/home.html', data)


def contact(request):
    site_configuration_repository = SiteConfigurationRepository()
    use_case = GetContactPageData(site_configuration_repository)

    data = use_case.execute()
    return render(request, 'core/contact.html', data)


@check_group(allowed_groups=['Agent'], redirect_url='chat:admin')
def toggle_chat(request):
    site_configuration_repository = SiteConfigurationRepository()
    use_case = ToggleChat(site_configuration_repository)

    use_case.execute()
    return redirect('chat:admin')