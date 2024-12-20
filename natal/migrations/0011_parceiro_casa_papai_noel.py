# Generated by Django 3.2.16 on 2022-12-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('natal', '0010_merge_0009_auto_20221122_1445_0009_auto_20221124_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parceiro_Casa_Papai_Noel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome do parceiro')),
                ('logo', models.ImageField(upload_to='parceiros_logos', verbose_name='Imagem para logo do parceiro')),
                ('site', models.CharField(max_length=50, null=True, verbose_name='URL do site do parceiro')),
            ],
        ),
    ]
