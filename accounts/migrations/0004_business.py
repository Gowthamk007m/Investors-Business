# Generated by Django 4.1.6 on 2023-02-03 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_userprofile_email_userprofile_name_userprofile_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Business_name', models.CharField(blank=True, max_length=255, null=True)),
                ('Category', models.CharField(blank=True, choices=[(' Sole Proprietorships', ' Sole Proprietorships'), ('Partnerships', 'Partnerships'), ('LLC', 'LLC'), ('Corporation', 'Corporation')], max_length=255, null=True)),
                ('registration_number', models.CharField(max_length=255)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('Experience', models.CharField(blank=True, max_length=255, null=True)),
                ('Skills', models.CharField(blank=True, max_length=255, null=True)),
                ('Active', models.BooleanField(default=False)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
