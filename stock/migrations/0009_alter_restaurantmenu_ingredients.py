# Generated by Django 5.1.3 on 2024-12-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0008_alter_donation_id_alter_packagedfood_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmenu',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='menus', to='stock.rawmaterial'),
        ),
    ]
