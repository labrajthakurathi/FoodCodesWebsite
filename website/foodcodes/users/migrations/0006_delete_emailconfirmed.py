# Generated by Django 3.0.5 on 2020-05-03 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_emailconfirmed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmailConfirmed',
        ),
    ]
