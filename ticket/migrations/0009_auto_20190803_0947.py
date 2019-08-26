# Generated by Django 2.1.7 on 2019-08-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("ticket", "0008_ticket_pub_date")]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="text",
            field=models.TextField(verbose_name="Comment text"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="body",
            field=models.TextField(verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="ticket_type",
            field=models.CharField(
                choices=[("Bug", "Bug"), ("Feature", "Feature")],
                default="1",
                max_length=10,
                verbose_name="Ticket type",
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Title"),
        ),
    ]
