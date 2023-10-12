# Generated by Django 4.2.6 on 2023-10-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField()),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]
