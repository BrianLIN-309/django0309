# Generated by Django 3.1.7 on 2021-03-09 02:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bigint_f', models.BigIntegerField()),
                ('bool_f', models.BooleanField()),
                ('date_f', models.DateField(auto_now=True)),
                ('char_f', models.CharField(max_length=20, unique=True)),
                ('datetime_f', models.DateTimeField(auto_now_add=True)),
                ('decimal_f', models.DecimalField(decimal_places=2, max_digits=10)),
                ('float_f', models.FloatField(null=True)),
                ('int_f', models.IntegerField(default=2010)),
                ('text_f', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('qty', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
