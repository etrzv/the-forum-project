
# A dictionary containing all available HTTP headers. Available headers depend on the client and server
def get_article_url(request, article_id):
    return request.META['HTTP_REFERER'] + f'#article-{article_id}'
