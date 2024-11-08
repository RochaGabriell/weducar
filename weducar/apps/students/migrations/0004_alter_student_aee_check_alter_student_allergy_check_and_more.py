# Generated by Django 5.1.2 on 2024-11-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='aee_check',
            field=models.IntegerField(blank=True, db_column='check_aee', default=0, null=True, verbose_name='Check AEE'),
        ),
        migrations.AlterField(
            model_name='student',
            name='allergy_check',
            field=models.IntegerField(blank=True, db_column='check_alergia', default=0, null=True, verbose_name='Check Alergia'),
        ),
        migrations.AlterField(
            model_name='student',
            name='disability_check',
            field=models.IntegerField(blank=True, db_column='check_pcd', default=0, null=True, verbose_name='Check PCD'),
        ),
        migrations.AlterField(
            model_name='student',
            name='disorder_check',
            field=models.IntegerField(blank=True, db_column='check_disturbio', default=0, null=True, verbose_name='Check Distúrbio'),
        ),
        migrations.AlterField(
            model_name='student',
            name='food_restriction_check',
            field=models.FloatField(blank=True, db_column='check_restricao_alimentar', default=0, null=True, verbose_name='Check Restrição Alimentar'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], db_column='sexo', max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image_right_check',
            field=models.IntegerField(blank=True, db_column='check_direito_imagem', default=0, null=True, verbose_name='Check Direito de Imagem'),
        ),
        migrations.AlterField(
            model_name='student',
            name='medical_monitoring_check',
            field=models.IntegerField(blank=True, db_column='check_acompanhamento_medico', default=0, null=True, verbose_name='Check Acompanhamento Médico'),
        ),
        migrations.AlterField(
            model_name='student',
            name='medication_check',
            field=models.IntegerField(blank=True, db_column='check_medicacao', default=0, null=True, verbose_name='Check Medicação'),
        ),
        migrations.AlterField(
            model_name='student',
            name='old_birth_certificate_check',
            field=models.IntegerField(blank=True, db_column='check_certidao_antiga', default=0, null=True, verbose_name='Check Certidão Antiga'),
        ),
        migrations.AlterField(
            model_name='student',
            name='physical_activity_restriction_check',
            field=models.IntegerField(blank=True, db_column='check_restricao_atv_fisica', default=0, null=True, verbose_name='Check Restrição de Atividade Física'),
        ),
        migrations.AlterField(
            model_name='student',
            name='school_transport_check',
            field=models.IntegerField(blank=True, db_column='check_transporte_escolar', default=0, null=True, verbose_name='Check Transporte Escolar'),
        ),
    ]
