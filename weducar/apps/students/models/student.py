from django.db import models


class Student(models.Model):
    registration = models.PositiveIntegerField(
        primary_key=True, db_column='matricula',
    )
    student_status_id = models.ForeignKey(
        'students.StudentStatus', models.DO_NOTHING, db_column='id_situacao_aluno',
    )
    city_id = models.ForeignKey(
        'locations.City', models.DO_NOTHING, db_column='id_cidade',
    )
    instance_id = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, db_column='id_instancia',
    )
    census_id = models.IntegerField(
        blank=True, null=True, db_column='id_censo',
    )
    name = models.CharField(max_length=45, db_column='nome')
    gender = models.CharField(max_length=1, db_column='sexo')
    birth_date = models.DateField(db_column='data_nascimento')
    father_name = models.CharField(
        max_length=255, blank=True, null=True, db_column='pai_nome',
    )
    father_phone = models.CharField(
        max_length=11, blank=True, null=True, db_column='pai_telefone',
    )
    father_rg = models.CharField(
        max_length=45, blank=True, null=True, db_column='pai_rg',
    )
    father_cpf = models.CharField(
        max_length=11, blank=True, null=True, db_column='pai_cpf',
    )
    mother_name = models.CharField(
        max_length=255, blank=True, null=True, db_column='mae_nome',
    )
    mother_phone = models.CharField(
        max_length=11, blank=True, null=True, db_column='mae_telefone',
    )
    mother_rg = models.CharField(
        max_length=45, blank=True, null=True, db_column='mae_rg',
    )
    mother_cpf = models.CharField(
        max_length=11, blank=True, null=True, db_column='mae_cpf',
    )
    housing_id = models.ForeignKey(
        'locations.Housing', models.DO_NOTHING, db_column='id_moradia',
    )
    responsible_relationship = models.CharField(
        max_length=45, db_column='parentesco_responsavel',
    )
    responsible_name = models.CharField(
        max_length=255, db_column='responsavel_nome',
    )
    responsible_phone = models.CharField(
        max_length=11, blank=True, null=True, db_column='responsavel_telefone',
    )
    responsible_rg = models.CharField(
        max_length=45, blank=True, null=True, db_column='responsavel_rg',
    )
    responsible_cpf = models.CharField(
        max_length=11, blank=True, null=True, db_column='responsavel_cpf',
    )
    address = models.CharField(
        max_length=45, blank=True, null=True, db_column='endereco',
    )
    neighborhood = models.CharField(
        max_length=45, blank=True, null=True, db_column='bairro',
    )
    allergy_check = models.IntegerField(
        blank=True, null=True, db_column='check_alergia',
    )
    allergy_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_alergia',
    )
    medical_monitoring_check = models.IntegerField(
        blank=True, null=True, db_column='check_acompanhamento_medico',
    )
    medical_monitoring_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_acompanhamento_medico',
    )
    physical_activity_restriction_check = models.IntegerField(
        blank=True, null=True, db_column='check_restricao_atv_fisica',
    )
    physical_activity_restriction_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_restricao_atv_fisica',
    )
    disorder_check = models.IntegerField(
        blank=True, null=True, db_column='check_disturbio',
    )
    disorder_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_disturbio',
    )
    disorder_instructions = models.TextField(
        blank=True, null=True, db_column='instrucoes_disturbio',
    )
    medication_check = models.IntegerField(
        blank=True, null=True, db_column='check_medicacao',
    )
    medication_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_medicacao',
    )
    food_restriction_check = models.FloatField(
        blank=True, null=True, db_column='check_restricao_alimentar',
    )
    food_restriction_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_restricao_alimentar',
    )
    image_right_check = models.IntegerField(
        blank=True, null=True, db_column='check_direito_imagem',
    )
    sus_number = models.CharField(
        max_length=15, blank=True, null=True, db_column='num_sus',
    )
    nis_number = models.CharField(
        max_length=11, blank=True, null=True, db_column='num_nis',
    )
    old_birth_certificate_check = models.IntegerField(
        blank=True, null=True, db_column='check_certidao_antiga',
    )
    birth_certificate = models.CharField(
        max_length=255, blank=True, null=True, db_column='certidao_nascimento',
    )
    birth_certificate_issue_date = models.DateField(
        blank=True, null=True, db_column='data_expedicao_certidao',
    )
    birth_certificate_registry = models.CharField(
        max_length=255, blank=True, null=True, db_column='certidao_cartorio',
    )
    birthplace = models.TextField(
        blank=True, null=True, db_column='naturalidade',
    )
    rg = models.CharField(max_length=45, blank=True, null=True, db_column='rg')
    cpf = models.CharField(
        max_length=11, blank=True, null=True, db_column='cpf',
    )
    school_transport_check = models.IntegerField(
        blank=True, null=True, db_column='check_trasnporte_escolar',
    )
    disability_check = models.IntegerField(
        blank=True, null=True, db_column='check_pcd',
    )
    disability_observations = models.CharField(
        max_length=255, blank=True, null=True, db_column='obs_pcd',
    )
    aee_check = models.IntegerField(
        blank=True, null=True, db_column='check_aee',
    )
    photo = models.TextField(blank=True, null=True, db_column='foto')

    class Meta:
        db_table = 'alunos'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
