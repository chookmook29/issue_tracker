# Generated by Django 2.1.7 on 2019-08-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0007_auto_20190803_2254")]

    operations = [
        migrations.AlterField(
            model_name="blog", name="pub_date", field=models.DateTimeField(null=True)
        )
    ]
