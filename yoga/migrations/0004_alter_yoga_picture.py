# Generated by Django 4.1.1 on 2022-11-19 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga', '0003_alter_yoga_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yoga',
            name='picture',
            field=models.ImageField(upload_to='static/image/'),
        ),
    ]