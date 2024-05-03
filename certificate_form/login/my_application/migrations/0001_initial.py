# Generated by Django 4.2.10 on 2024-03-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='certificate_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(default='', max_length=10)),
                ('name', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=20)),
                ('course', models.CharField(default='', max_length=20)),
                ('trainer', models.CharField(default='', max_length=15)),
                ('phone', models.CharField(default='', max_length=10)),
            ],
        ),
    ]