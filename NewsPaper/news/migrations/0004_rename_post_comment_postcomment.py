# Generated by Django 4.0.6 on 2022-07-14 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_rating_author_author_rating_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='postComment',
        ),
    ]