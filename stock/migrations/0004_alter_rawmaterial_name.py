# Generated by Django 5.1.3 on 2024-11-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_alter_rawmaterial_humidity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawmaterial',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
