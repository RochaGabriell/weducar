# Generated by Django 5.1.2 on 2024-11-06 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_color_rename_housing_id_student_housing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='color',
            field=models.ForeignKey(db_column='id_cor', default=6, on_delete=django.db.models.deletion.DO_NOTHING, to='students.color', verbose_name='Cor'),
        ),
    ]
