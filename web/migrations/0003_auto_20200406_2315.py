# Generated by Django 3.0.4 on 2020-04-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_blog_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to=''),
        ),
    ]