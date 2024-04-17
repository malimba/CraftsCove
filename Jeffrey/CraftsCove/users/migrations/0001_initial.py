# Generated by Django 4.2.1 on 2024-04-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=30)),
                ('emailAddr', models.EmailField(max_length=255, unique=True)),
                ('gender', models.CharField(max_length=6)),
                ('password', models.CharField(max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
