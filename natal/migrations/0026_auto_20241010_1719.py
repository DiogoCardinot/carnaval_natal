# Generated by Django 3.2.13 on 2024-10-10 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0025_auto_20241010_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atracao',
            old_name='section_image',
            new_name='atracao_image',
        ),
        migrations.RenameField(
            model_name='atracao',
            old_name='section_video',
            new_name='atracao_video',
        ),
        migrations.RenameField(
            model_name='atracaoimages',
            old_name='section_image',
            new_name='atracaoImage_image',
        ),
    ]