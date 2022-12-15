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


def create_article_dislikes_for_user_and_articles(user, articles):
    current = 0
    total_likes_count = 0

    for article in articles:
        for i in range(current):
            ArticleDislike(
                article=article,
                user=user
            ).save()

            total_likes_count += 1
        current += 1
    return total_likes_count


'''
def test_user_details__when_pets_and_1_photo__expect_pets_1_photo(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        pets = create_pets_for_user(user, count=5)
        photos = create_photo_for_user_and_pets(user, pets=pets[:2], count=1)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, len(response.context['pets']))
        self.assertEqual(1, len(response.context['photos']))
        self.assertListEqual(list(photos), list(response.context['photos']))
        self.assertEqual(1, response.context['photos_count'])

    def test_user_details__when_pets_and_2_photos__expect_pets_2_photos(self):
        pass

    def test_user_details__when_pets_and_7_photos_no_page__expect_pets_7_photos(self):
        pass

    def test_user_details__when_pets_and_7_photos_page_1__expect_pets_7_photos(self):
        pass

    def test_user_details__when_pets_and_7_photos_page_2__expect_pets_7_photos(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        pets = create_pets_for_user(user, count=5)
        photos = create_photo_for_user_and_pets(user, pets=pets[:2], count=7)

        response = self.client.get(
            reverse_lazy('details user', kwargs={'pk': user.pk}),
            data={
                'page': 2,
            })

        self.assertListEqual(pets, list(response.context['pets']))
        self.assertListEqual(photos[2:4], list(response.context['photos']))
        self.assertEqual(7, response.context['photos_count'])

    def test_user_details__when_no_likes__expect_0_likes_count(self):
        pass

    def test_user_details__when_likes_for_single_pet__expect_correct_likes_count(self):
        pass

    def test_user_details__when_likes_for_multiple_pets__expect_combined_likes_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        pets = create_pets_for_user(user, count=5)
        photos = create_photo_for_user_and_pets(user, pets=pets[:2], count=7)
        total_likes_count = create_photo_likes_for_user_and_photos(user, photos)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(total_likes_count + 1, response.context['likes_count'])

'''