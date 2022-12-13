def apply_likes_count(article):
    article.likes_count = article.articlelike_set.count()
    return article


def apply_dislikes_count(article):
    article.dislikes_count = article.articledislike_set.count()
    return article


def apply_likes_count_for_comment(comment):
    comment.likes_count = comment.commentlike_set.count()
    return comment


def apply_dislikes_count_for_comment(comment):
    comment.dislikes_count = comment.commentdislike_set.count()
    return comment
