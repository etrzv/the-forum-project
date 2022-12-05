def apply_likes_count(article):
    article.likes_count = article.articlelike_set.count()
    return article


def apply_dislikes_count(article):
    article.dislikes_count = article.articledislike_set.count()
    return article


def apply_user_liked_photo(article):
    # TODO: fix this for current user when authentication is available
    article.is_liked_by_user = article.likes_count > 0
    return article

