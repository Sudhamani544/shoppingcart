# Generated by Django 3.1.7 on 2021-05-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210501_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='name',
            field=models.CharField(default='chicken_pesto', max_length=100),
        ),
    ]
