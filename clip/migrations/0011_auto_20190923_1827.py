# Generated by Django 2.2.3 on 2019-09-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clip', '0010_auto_20190904_0735'),
    ]

    operations = [
        migrations.AddField(
            model_name='clip',
            name='embed_url',
            field=models.CharField(default='no embed', max_length=1000),
        ),
        migrations.AddField(
            model_name='clip',
            name='url',
            field=models.CharField(default='no url', max_length=500),
        ),
    ]