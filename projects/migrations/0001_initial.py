# Generated by Django 2.1 on 2018-08-24 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('summary', models.TextField()),
            ],
        ),
    ]
