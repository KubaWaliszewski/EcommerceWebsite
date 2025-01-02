from django.core.paginator import Paginator


def get_filtered_and_paginated_queryset(query_params, repository_method, page_number, per_page):

    queryset, applied_filter, original_queryset  = repository_method(query_params)
    paginator = Paginator(queryset, per_page)
    paginated_queryset = paginator.get_page(page_number)

    return paginated_queryset, paginator, applied_filter, original_queryset 


def extract_filters_from_query_params(query_params):
    params = query_params.copy()
    if 'page' in params:
        params.pop('page')
    return params.urlencode()



def paginate_queryset(queryset, page_number, per_page=4):
    paginator = Paginator(queryset, per_page)
    page = paginator.get_page(page_number)
    return page, paginator