# Generated by Django 4.1.5 on 2023-02-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_banker_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banker',
            name='Description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]