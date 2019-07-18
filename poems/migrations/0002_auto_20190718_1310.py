# Generated by Django 2.2.3 on 2019-07-18 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poem',
            name='text',
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=16)),
                ('text', models.TextField()),
                ('poem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poems.Poem')),
            ],
        ),
    ]
