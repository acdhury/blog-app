# Generated by Django 4.2.7 on 2024-01-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.TextField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
