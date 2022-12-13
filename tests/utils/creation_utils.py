from datetime import date

from the_forum.articles.models import Article
from the_forum.common.models import ArticleLike, ArticleDislike, ArticleComment, ArticleBookmark


def create_articles_for_user(user, count):
    result = [Article(
        title=f'Article {i + 1}',
        content=f'This is my {i + 1} opinion.',
        user=user
    ) for i in range(count)]

    [a.save() for a in result]

    return result


def create_article_likes_for_user_and_articles(user, articles):
    current = 0
    total_likes_count = 0

    for article in articles:
        for i in range(current):
            ArticleLike(
                article=article,
                user=user
            ).save()

            total_likes_count += 1
        current += 1
    return total_likes_count
