# Generated by Django 3.0.4 on 2020-04-06 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_blog_imgpic_90x90'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='imgpic_90x90',
            new_name='imgpic_640x427',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
    ]