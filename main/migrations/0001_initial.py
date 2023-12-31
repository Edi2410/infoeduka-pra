# Generated by Django 4.2 on 2023-04-14 00:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kolegij',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('predavaci', models.ManyToManyField(limit_choices_to={'is_staff': False}, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Kolegiji',
            },
        ),
        migrations.CreateModel(
            name='Obavijest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naziv', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('datum_objave', models.DateTimeField(auto_now_add=True)),
                ('datum_isteka', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kolegij', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.kolegij')),
            ],
            options={
                'verbose_name_plural': 'Obavijesti',
            },
        ),
    ]
