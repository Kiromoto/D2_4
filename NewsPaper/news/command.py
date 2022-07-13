from models import *
User.objects.create_user('UserFirst')
User.objects.create_user('UserSecond')
User.objects.create_user('UserThird')

User1 = Author.objects.create(user_id=1)
User2 = Author.objects.create(user_id=2)
User3 = Author.objects.create(user_id=3)

Category.objects.create(name='Экономика')
Category.objects.create(name='Наука')
Category.objects.create(name='Спорт')
Category.objects.create(name='Авто')
