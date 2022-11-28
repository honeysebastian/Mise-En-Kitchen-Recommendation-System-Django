# Generated by Django 4.0.4 on 2022-06-21 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Accepted', 'Accepted'), ('On the way', 'On the way'), ('Cancel', 'Cancel'), ('Packed', 'Packed')], default='Pending', max_length=50),
        ),
    ]
