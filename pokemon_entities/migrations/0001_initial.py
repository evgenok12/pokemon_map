# Generated by Django 2.2.24 on 2023-04-13 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/pokemon')),
                ('title_ru', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200)),
                ('title_jp', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('appeared_at', models.DateTimeField()),
                ('disappeared_at', models.DateTimeField()),
                ('level', models.IntegerField()),
                ('health', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('defence', models.IntegerField()),
                ('stamina', models.IntegerField()),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokemon_entities', to='pokemon_entities.Pokemon')),
            ],
        ),
    ]
