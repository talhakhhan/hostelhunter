# Generated by Django 3.2.3 on 2021-05-31 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_user_favourites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rate_listing',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
