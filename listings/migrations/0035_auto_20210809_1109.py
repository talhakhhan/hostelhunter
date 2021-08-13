# Generated by Django 3.2.3 on 2021-08-09 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0034_auto_20210809_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='area',
            field=models.CharField(choices=[('Mall Road', 'Mall Road'), ('Ichra', 'Ichra'), ('DHA', 'DHA'), ('Township', 'Township'), ('Model Town', 'Model Town'), ('Askari', 'Askari'), ('Thokar', 'Thokar'), ('Lakshmi Chock', 'Lakshmi Chock'), ('Iqbal Town', 'Iqbal Town'), ('Sadar', 'Sadar'), ('Jalo', 'Jalo'), ('Valencia Town', 'Valencia Town'), ('Wapda Town', 'Wapda Town'), ('Central Park', 'Central Park'), ('Johar Town', 'Johar Town'), ('Ferozpur Road', 'Ferozpur Road'), ('Gulberg', 'Gulberg'), ('Behria Town', 'Behria Town'), ('Canal Road', 'Canal Road')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Girls', 'Girls'), ('Both', 'Both'), ('Boys', 'Boys')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='rent_agreement',
            field=models.FileField(blank=True, default='/Tenancy_Agreement.pdf', upload_to=''),
        ),
        migrations.AlterField(
            model_name='listing',
            name='standard',
            field=models.CharField(choices=[('Diamond', 'Diamond'), ('Gold', 'Gold'), ('Silver', 'Silver')], max_length=100),
        ),
    ]
