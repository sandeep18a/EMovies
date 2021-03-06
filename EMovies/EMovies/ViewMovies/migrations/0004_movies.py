# Generated by Django 4.0.3 on 2022-03-22 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ViewMovies', '0003_screens'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField(default='')),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ViewMovies.city')),
                ('screen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ViewMovies.screens')),
                ('theater_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ViewMovies.theater')),
            ],
        ),
    ]
