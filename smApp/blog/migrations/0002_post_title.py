# Generated by Django 3.0.8 on 2020-07-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
