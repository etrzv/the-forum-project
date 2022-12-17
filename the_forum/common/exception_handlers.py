from django.shortcuts import render
from the_forum.common.forms import SearchArticleForm


def bad_request_custom_exception(request, exception):
    search_form = SearchArticleForm
    context = {
        'search_form': search_form,
    }

    return render(request, 'error_templates/400.html', context, status=400)


def forbidden_custom_exception(request, exception):
    search_form = SearchArticleForm
    context = {
        'search_form': search_form,
    }

    return render(request, 'error_templates/403.html', context, status=403)


def page_not_found_custom_exception(request, exception):
    search_form = SearchArticleForm
    context = {
        'search_form': search_form,
    }

    return render(request, 'error_templates/404.html', context, status=404)


def server_error_custom_exception(request):
    search_form = SearchArticleForm
    context = {
        'search_form': search_form,
    }

    return render(request, 'error_templates/500.html', context, status=500)
