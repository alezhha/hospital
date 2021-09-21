# Generated by Django 2.2.12 on 2021-09-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210921_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='hospital',
            field=models.CharField(max_length=10, verbose_name='Больница'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Номер Телефона'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='pin',
            field=models.CharField(max_length=14, verbose_name='Пин'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Номер Телефона'),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='pin',
            field=models.CharField(max_length=14, verbose_name='Пин'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Номер Телефона'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pin',
            field=models.CharField(max_length=14, verbose_name='Пин'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='reason',
            field=models.CharField(max_length=255, verbose_name='Причина по которой в Больнице'),
        ),
    ]
