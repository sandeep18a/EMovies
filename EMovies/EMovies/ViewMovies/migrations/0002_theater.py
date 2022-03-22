# Generated by Django 4.0.3 on 2022-03-22 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ViewMovies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theater_name', models.CharField(default='', max_length=70)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ViewMovies.city')),
            ],
        ),
    ]
