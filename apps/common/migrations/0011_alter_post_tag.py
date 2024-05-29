# Generated by Django 5.0.3 on 2024-05-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0010_about_title_en_about_title_ru_about_title_uz"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(
                blank=True, related_name="tag", to="common.tag"
            ),
        ),
    ]
