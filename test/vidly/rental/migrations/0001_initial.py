# Generated by Django 3.0.4 on 2020-03-21 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('star', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('price', models.FloatField()),
                ('in_stock', models.IntegerField()),
                ('in_4k', models.BooleanField()),
                ('director', models.CharField(max_length=255)),
                ('image_url', models.TextField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Genre')),
            ],
        ),
    ]
