# Generated by Django 5.0.4 on 2024-07-17 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
