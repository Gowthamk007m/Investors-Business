# Generated by Django 4.1.5 on 2023-02-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_dateofinvestor_investorsmodel_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='Category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
