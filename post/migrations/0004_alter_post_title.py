# Generated by Django 4.1.7 on 2023-03-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0003_alter_comment_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100, null=True, verbose_name="Заголовок"),
        ),
    ]