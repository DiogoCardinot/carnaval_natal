# Generated by Django 3.2.13 on 2022-09-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título do evento')),
                ('banner', models.ImageField(upload_to='eventos_banners', verbose_name='Banner para divulgação do evento')),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='logo',
            field=models.ImageField(upload_to='parceiros_logos', verbose_name='Imagem para logo do parceiro'),
        ),
    ]
