# Generated by Django 4.1.4 on 2023-01-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=1)),
                ('instock', models.BooleanField(default=True)),
            ],
        ),
    ]
