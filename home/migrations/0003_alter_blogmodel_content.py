# Generated by Django 3.2.13 on 2022-12-10 14:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
