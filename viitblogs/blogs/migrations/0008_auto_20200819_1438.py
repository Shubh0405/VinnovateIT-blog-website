# Generated by Django 3.1 on 2020-08-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='body',
            field=models.TextField(),
        ),
    ]
