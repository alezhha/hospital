# Generated by Django 2.2.12 on 2021-09-21 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('hospital', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Maindoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('pin', models.CharField(max_length=4, verbose_name='Пин')),
                ('birthdate', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=10, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name': 'Главрач',
                'verbose_name_plural': 'Главрачи',
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pin', models.CharField(max_length=14)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Медсестра',
                'verbose_name_plural': 'Медсестры',
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('phone', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=255)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Doctor')),
            ],
            options={
                'verbose_name': 'Пациент',
                'verbose_name_plural': 'Пациенты',
            },
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='doctors',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Maindoctors',
        ),
        migrations.AddField(
            model_name='patients',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Hospital'),
        ),
        migrations.AddField(
            model_name='patients',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Nurse'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='nurse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Nurse'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Больница', to='main.Hospital'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='doctor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Врач', to='main.Maindoctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='nurse',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.Nurse'),
            preserve_default=False,
        ),
    ]
