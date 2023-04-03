# Generated by Django 4.1.5 on 2023-02-13 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0018_remove_banker_banker_remove_business_user_and_more'),
        ('business_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_type', models.CharField(max_length=250)),
                ('amount', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=100, null=True)),
                ('expected_revenue', models.PositiveIntegerField()),
                ('skill_set', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userprofile')),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business_app.business')),
            ],
        ),
    ]
