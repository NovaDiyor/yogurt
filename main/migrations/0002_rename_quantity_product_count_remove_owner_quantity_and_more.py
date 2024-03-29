# Generated by Django 4.1.7 on 2023-03-27 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quantity',
            new_name='count',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='owner',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
