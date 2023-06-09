# Generated by Django 4.1.5 on 2023-02-13 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0018_remove_banker_banker_remove_business_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_type', models.CharField(max_length=100)),
                ('interest_rate', models.FloatField()),
                ('loan_amount', models.FloatField()),
                ('asset_type', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True, max_length=600, null=True)),
                ('banker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
            ],
        ),
    ]
