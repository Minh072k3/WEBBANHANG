# Generated by Django 4.2.6 on 2023-11-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product', to='app.category'),
        ),
    ]
