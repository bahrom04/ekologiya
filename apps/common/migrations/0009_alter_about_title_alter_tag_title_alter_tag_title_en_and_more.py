# Generated by Django 5.0.3 on 2024-04-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0008_about_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="about",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="title_en",
            field=models.CharField(max_length=128, null=True, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="title_ru",
            field=models.CharField(max_length=128, null=True, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="tag",
            name="title_uz",
            field=models.CharField(max_length=128, null=True, verbose_name="Title"),
        ),
    ]
