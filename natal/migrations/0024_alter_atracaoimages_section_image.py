# Generated by Django 3.2.13 on 2024-10-09 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0023_atracaoimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracaoimages',
            name='section_image',
            field=models.ImageField(upload_to='atracoes-images/'),
        ),
    ]
