import django.contrib.auth.models
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


# ______________________________________________________________________________________________________________________
# ______________________________________________________________________________________________________________________
# Код итогового задания
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # cвязь «один к одному» с встроенной моделью пользователей User;
    rating = models.IntegerField(default=0)

    def update_rating(self, author_id):
        #     Метод update_rating() модели Author, который обновляет рейтинг пользователя, переданный в аргумент этого метода.
        # Он состоит из следующего:
        # суммарный рейтинг каждой статьи автора умножается на 3;
        # суммарный рейтинг всех комментариев автора;
        # суммарный рейтинг всех комментариев к статьям автора.
        pass



class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    # ?subscribe = models.ManyToManyField(User, through='Subscribers')


class Post(models.Model):
    news = 'NW'
    article = 'AT'

    TP = [
        (news, 'новости'),
        (article, 'статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    types_of_post = models.CharField(max_length=2, default=news, choices=TP)
    post_create_datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    post_title = models.CharField(max_length=255)
    post_text = models.TextField(default="Здесь должен быть текст вашей статьи или новости...")
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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
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



# from resourses import POSITIONS
#
#
# class Staff(models.Model):
#     director = 'DI'
#     admin = 'AD'
#     cook = 'CO'
#     cashier = 'CA'
#     cleaner = 'CL'
#
#     full_name = models.CharField(max_length=255)
#     position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
#     labor_contract = models.BigIntegerField(default=0)
#
#     def get_last_name(self):
#         return self.full_name.split()[0]
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.FloatField(default=0.0)
#     composition = models.TextField(default="Состав не указан")
#
#
# class Order(models.Model):  # наследуемся от класса Model
#     time_in = models.DateTimeField(auto_now_add=True)
#     time_out = models.DateTimeField(null=True)
#     cost = models.FloatField(default=0.0)
#     pickup = models.BooleanField(default=False)
#     complete = models.BooleanField(default=False)
#     staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='ProductOrder')
#
#     def finish_order(self):
#         self.time_out = datetime.now()
#         self.complete = True
#         self.save()
#
#     def get_duration(self):
#         if self.complete:
#             return (self.time_out - self.time_in).total_seconds() // 60
#         else:
#             return (datetime.now() - self.time_in).total_seconds() // 60
#
#
# class ProductOrder(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     _amount = models.IntegerField(default=1, db_column='amount')
#
#     @property
#     def amount(self):
#         return self._amount
#
#     @amount.setter
#     def amount(self, value):
#         self._amount = int(value) if value > 0 else 0
#         self.save()
#
#     def product_sum(self):
#         product_price = self.product.price
#         return product_price * self.amount
