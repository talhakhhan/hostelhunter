# Generated by Django 3.1.7 on 2021-05-18 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0002_auto_20210518_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='rooms',
            field=models.IntegerField(),
        ),
    ]
