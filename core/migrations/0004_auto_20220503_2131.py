# Generated by Django 3.2.13 on 2022-05-04 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_informacoesdositedecarnaval_primeiro_dia_de_carnaval'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegendasFotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legenda', models.CharField(max_length=40)),
                ('foto', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='agendacarnaval',
            name='local',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='agendacarnaval',
            name='titulo',
            field=models.CharField(max_length=50),
        ),
    ]
