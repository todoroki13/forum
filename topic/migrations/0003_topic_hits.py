# Generated by Django 3.2.7 on 2021-12-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='hits',
            field=models.IntegerField(default=0, verbose_name='瀏覽次數'),
        ),
    ]
