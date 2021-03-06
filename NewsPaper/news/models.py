from django.contrib.auth.models import User
from django.db import models


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Код итогового задания
class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        # суммарный рейтинг каждой статьи автора умножается на 3;
        sum_post_rating = self.post_set.aggregate(allPostRating=models.Sum('post_rating'))
        postR = 0
        postR += sum_post_rating.get('allPostRating')

        # # суммарный рейтинг всех комментариев автора;
        sum_comment_rating = self.author_user.comment_set.aggregate(authorCommentRating=models.Sum('comment_rating'))
        commR = 0
        commR += sum_comment_rating.get('authorCommentRating')

        # # суммарный рейтинг всех комментариев к статьям автора.
        # sum_PostComment_rating = self.comment.postComment.all().aggregate(allCommentPostRating=models.Sum('comment_rating'))
        # s1 = self.author_user.post_set.comment_set.all().aggregate(allCommentRatingAuthorPost=models.Sum('comment_rating'))
        # pcommR = 0
        # pcommR += s1.get('allCommentRatingAuthorPost')

        self.author_rating = postR * 3 + commR #+ pcommR
        self.save()

    def test(self):
        allcom = Comment.objects.filter(user_id=self.author_user.id)
        return allcom.values('comment_text')



class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AT'

    CHOISE_NW_AT = [
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_of_post = models.CharField(max_length=2, default=NEWS, choices=CHOISE_NW_AT)
    post_create_datetime = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=128)
    post_text = models.TextField()
    post_rating = models.IntegerField(default=0)

    def like(self):
        self.post_rating += 1
        self.save()

    def dislike(self):
        self.post_rating -= 1
        self.save()

    def preview(self):
        return f'{self.post_text[:124]}...'


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    postComment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_datetime = models.DateTimeField(auto_now_add=True)
    comment_rating = models.IntegerField(default=0)

    def like(self):
        self.comment_rating += 1
        self.save()

    def dislike(self):
        self.comment_rating -= 1
        self.save()

