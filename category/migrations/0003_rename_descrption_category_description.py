# Generated by Django 4.2.5 on 2023-09-22 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descrption',
            new_name='description',
        ),
    ]
