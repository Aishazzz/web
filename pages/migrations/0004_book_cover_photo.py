# Generated by Django 5.0.4 on 2024-05-19 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
