# Generated by Django 3.0.7 on 2020-06-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilegeek', '0002_auto_20200621_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
    ]
