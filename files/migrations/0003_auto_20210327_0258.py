# Generated by Django 3.1.7 on 2021-03-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20210327_0243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sn0', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='about',
        ),
    ]