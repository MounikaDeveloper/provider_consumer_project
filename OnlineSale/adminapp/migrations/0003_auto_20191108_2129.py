# Generated by Django 2.2.3 on 2019-11-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_merchant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchant',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
