# Generated by Django 4.1.7 on 2023-05-16 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                ("sname", models.CharField(max_length=20)),
                ("sage", models.IntegerField(primary_key=True, serialize=False)),
                ("smobile", models.IntegerField()),
            ],
        ),
    ]
