# Generated by Django 3.0.4 on 2020-04-06 11:08

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, unique=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
            ],
            options={
                'verbose_name': '新闻',
                'verbose_name_plural': '新闻',
            },
        ),
    ]