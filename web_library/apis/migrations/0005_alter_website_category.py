# Generated by Django 4.2.2 on 2023-07-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_website_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='category',
            field=models.ManyToManyField(blank=True, to='apis.category'),
        ),
    ]