# Generated by Django 4.1.7 on 2023-03-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_user_birthday"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(null=True, verbose_name="Дата рождения"),
        ),
    ]
