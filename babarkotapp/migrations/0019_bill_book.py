# Generated by Django 4.0.2 on 2022-03-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babarkotapp', '0018_cheque_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_no', models.IntegerField()),
                ('bill_from', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('bill_voucher', models.CharField(max_length=200)),
                ('bill_amount', models.CharField(max_length=255)),
                ('payable_amount', models.CharField(max_length=50)),
            ],
        ),
    ]
