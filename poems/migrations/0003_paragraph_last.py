# Generated by Django 2.2.3 on 2019-07-19 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0002_auto_20190718_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='paragraph',
            name='last',
            field=models.BooleanField(default=False),
        ),
    ]
