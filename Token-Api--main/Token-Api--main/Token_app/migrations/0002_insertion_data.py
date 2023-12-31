# Generated by Django 4.2.6 on 2023-10-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Token_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insertion_data',
            fields=[
                ('id', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('tagline', models.CharField(blank=True, max_length=100, null=True)),
                ('first_brewed', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('image_url', models.CharField(blank=True, max_length=100, null=True)),
                ('abv', models.IntegerField(blank=True, null=True)),
                ('ibu', models.IntegerField(blank=True, null=True)),
                ('target_fg', models.IntegerField(blank=True, null=True)),
                ('target_og', models.CharField(blank=True, max_length=100, null=True)),
                ('ebc', models.IntegerField(blank=True, null=True)),
                ('srm', models.IntegerField(blank=True, null=True)),
                ('ph', models.CharField(blank=True, max_length=100, null=True)),
                ('attenuation_level', models.CharField(blank=True, max_length=100, null=True)),
                ('volume', models.CharField(blank=True, max_length=100, null=True)),
                ('boil_volume', models.CharField(blank=True, max_length=100, null=True)),
                ('method', models.CharField(blank=True, max_length=5000, null=True)),
                ('ingredients', models.CharField(blank=True, max_length=5000, null=True)),
                ('food_pairing', models.CharField(blank=True, max_length=1000, null=True)),
                ('brewers_tips', models.CharField(blank=True, max_length=555, null=True)),
                ('contributed_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
