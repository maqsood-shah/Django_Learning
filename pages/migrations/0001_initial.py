# Generated by Django 2.2.5 on 2019-12-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=1000)),
                ('message', models.CharField(max_length=20000)),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
