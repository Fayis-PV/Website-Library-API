# Generated by Django 4.2.2 on 2023-07-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_alter_website_category_alter_website_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
