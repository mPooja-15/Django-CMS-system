# Generated by Django 3.0.1 on 2020-02-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tap_admin', '0016_auto_20200219_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_disciption',
            field=models.TextField(null=True),
        ),
    ]