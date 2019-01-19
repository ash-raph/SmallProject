# Generated by Django 2.1.5 on 2019-01-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20190119_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shops',
        ),
        migrations.AddField(
            model_name='user',
            name='disliked_shops',
            field=models.ManyToManyField(related_name='disliked_by', through='shops.ShopUser', to='shops.Shop'),
        ),
        migrations.AddField(
            model_name='user',
            name='liked_shops',
            field=models.ManyToManyField(related_name='liked_by', to='shops.Shop'),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='disliked_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]