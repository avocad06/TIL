# Generated by Django 3.2.13 on 2022-10-01 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.TimeField(blank=True, null=True),
        ),
    ]