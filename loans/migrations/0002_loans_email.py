# Generated by Django 4.1.3 on 2023-06-16 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]