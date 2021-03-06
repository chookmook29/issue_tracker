# Generated by Django 2.1.7 on 2019-05-20 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ticket", "0004_auto_20190429_1653")]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="progress",
            field=models.CharField(
                choices=[("To do", "To do"),
                         ("Doing", "Doing"), ("Done", "Done")],
                default="To do",
                max_length=10,
            ),
        )
    ]
