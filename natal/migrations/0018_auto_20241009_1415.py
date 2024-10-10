# Generated by Django 3.2.13 on 2024-10-09 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0017_auto_20241009_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='ativa',
            field=models.BooleanField(default=True, verbose_name='Ativa'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='descricao',
            field=models.CharField(max_length=10000, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='section_video',
            field=models.CharField(max_length=300, null=True, verbose_name='Iframe'),
        ),
        migrations.AlterField(
            model_name='sections',
            name='subtitulo',
            field=models.CharField(max_length=300, verbose_name='Subtítulo'),
        ),
    ]
