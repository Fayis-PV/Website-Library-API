# Generated by Django 4.2.2 on 2023-07-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='imgs/web_imgs/')),
                ('brand', models.ImageField(blank=True, null=True, upload_to='imgs/brand_imgs/')),
                ('added_on', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='apis.category')),
            ],
        ),
    ]
