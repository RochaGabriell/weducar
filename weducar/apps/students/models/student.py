from django.utils.crypto import get_random_string
from django.db import models

from ..models.student_classes import StudentClasses

GENDER_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
]


class Student(models.Model):
    registration = models.PositiveIntegerField(
        primary_key=True, blank=True, verbose_name='Matrícula', db_column='matricula',
    )
    student_status = models.ForeignKey(
        'students.StudentStatus', models.DO_NOTHING, verbose_name='Situacao Aluno', db_column='id_situacao_aluno',
    )
    city = models.ForeignKey(
        'locations.City', models.DO_NOTHING, verbose_name='Cidade',
        db_column='id_cidade',
    )
    instance = models.ForeignKey(
        'locations.Instance', models.DO_NOTHING, verbose_name='Instancia',
        db_column='id_instancia',
    )
    color = models.ForeignKey(
        'students.Color', models.DO_NOTHING, verbose_name='Cor',
        db_column='id_cor', default=6,
    )
    census_id = models.IntegerField(
        blank=True, null=True, verbose_name='ID do Censo', db_column='id_censo',
    )
    name = models.CharField(
        max_length=45, verbose_name='Nome', db_column='nome',
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, verbose_name='Sexo', db_column='sexo',
    )
    birth_date = models.DateField(
        verbose_name='Data de Nascimento', db_column='data_nascimento',
    )
    father_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Nome do Pai',
        db_column='pai_nome',
    )
    father_phone = models.CharField(
        max_length=11, blank=True, null=True,  verbose_name='Telefone do Pai', db_column='pai_telefone',
    )
    father_rg = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='RG do Pai',
        db_column='pai_rg',
    )
    father_cpf = models.CharField(
        max_length=11, blank=True, null=True, unique=True,
        verbose_name='CPF do Pai', db_column='pai_cpf',
    )
    mother_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Nome da Mãe',
        db_column='mae_nome',
    )
    mother_phone = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Telefone da Mãe', db_column='mae_telefone',
    )
    mother_rg = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='RG da Mãe',
        db_column='mae_rg',
    )
    mother_cpf = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='CPF da Mãe',
        db_column='mae_cpf',
    )
    housing = models.ForeignKey(
        'locations.Housing', models.DO_NOTHING, verbose_name='Moradia',
        db_column='id_moradia',
    )
    responsible_relationship = models.CharField(
        max_length=45, verbose_name='Parentesco do Responsável',
        db_column='parentesco_responsavel',
    )
    responsible_name = models.CharField(
        max_length=255, verbose_name='Nome do Responsável',
        db_column='responsavel_nome',
    )
    responsible_phone = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Telefone do Responsável', db_column='responsavel_telefone',
    )
    responsible_rg = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='RG do Responsável', db_column='responsavel_rg',
    )
    responsible_cpf = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='CPF do Responsável', db_column='responsavel_cpf',
    )
    address = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='Endereço',
        db_column='endereco',
    )
    neighborhood = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='Bairro',
        db_column='bairro',
    )
    allergy_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Alergia',
        db_column='check_alergia', default=0,
    )
    allergy_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações sobre Alergia', db_column='obs_alergia',
    )
    medical_monitoring_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Acompanhamento Médico', db_column='check_acompanhamento_medico', default=0,
    )
    medical_monitoring_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações sobre Acompanhamento Médico', db_column='obs_acompanhamento_medico',
    )
    physical_activity_restriction_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Restrição de Atividade Física', db_column='check_restricao_atv_fisica', default=0,
    )
    physical_activity_restriction_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações sobre Restrição de Atividade Física', db_column='obs_restricao_atv_fisica',
    )
    disorder_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Distúrbio',
        db_column='check_disturbio', default=0,
    )
    disorder_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações sobre Distúrbio', db_column='obs_disturbio',
    )
    disorder_instructions = models.TextField(
        blank=True, null=True, verbose_name='Instruções sobre Distúrbio', db_column='instrucoes_disturbio',
    )
    medication_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Medicação',
        db_column='check_medicacao', default=0,
    )
    medication_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações sobre Medicação', db_column='obs_medicacao',
    )
    food_restriction_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Restrição Alimentar',
        db_column='check_restricao_alimentar', default=0,
    )
    food_restriction_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações de Restrição Alimentar', db_column='obs_restricao_alimentar',
    )
    image_right_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Direito de Imagem', db_column='check_direito_imagem', default=0,
    )
    sus_number = models.CharField(
        max_length=15, blank=True, null=True, verbose_name='Número do SUS',
        db_column='num_sus',
    )
    nis_number = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='Número do NIS',
        db_column='num_nis',
    )
    old_birth_certificate_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Certidão Antiga',
        db_column='check_certidao_antiga', default=0,
    )
    birth_certificate = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Certidão de Nascimento',
        db_column='certidao_nascimento',
    )
    birth_certificate_issue_date = models.DateField(
        blank=True, null=True, verbose_name='Data de Expedição da Certidão',
        db_column='data_expedicao_certidao',
    )
    birth_certificate_registry = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Cartório da Certidão',
        db_column='certidao_cartorio',
    )
    birthplace = models.TextField(
        blank=True, null=True, verbose_name='Naturalidade', db_column='naturalidade',
    )
    rg = models.CharField(
        max_length=45, blank=True, null=True, verbose_name='RG', db_column='rg'
    )
    cpf = models.CharField(
        max_length=11, blank=True, null=True, verbose_name='CPF', db_column='cpf',
    )
    school_transport_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check Transporte Escolar', db_column='check_transporte_escolar', default=0,
    )
    disability_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check PCD',
        db_column='check_pcd', default=0,
    )
    disability_observations = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Observações de PCD', db_column='obs_pcd',
    )
    aee_check = models.IntegerField(
        blank=True, null=True, verbose_name='Check AEE',
        db_column='check_aee', default=0,
    )
    photo = models.TextField(
        blank=True, null=True, verbose_name='Foto', db_column='foto',
    )
    date_joined = models.DateTimeField(
        verbose_name='Data de Entrada', auto_now_add=True
    )
    date_changed = models.DateTimeField(
        verbose_name='Data de alteração', auto_now=True
    )

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.upper()
        if self.responsible_relationship:
            self.responsible_relationship = self.responsible_relationship.upper()
        if self.responsible_name:
            self.responsible_name = self.responsible_name.upper()
        if self.father_name:
            self.father_name = self.father_name.upper()
        if self.mother_name:
            self.mother_name = self.mother_name.upper()

        if not self.registration and self.instance_id:
            unique_suffix = get_random_string(
                length=5, allowed_chars='0123456789'
            )
            self.registration = int(f"{self.instance_id}{unique_suffix}")
        super().save(*args, **kwargs)

    def get_classe(self):
        student_registration = self.registration
        student_classe = StudentClasses.objects.filter(
            student_enrollment__registration=student_registration,
        ).select_related('classe__school_year').order_by('classe__school_year__academic_year')
        if student_classe.exists():
            latest_class = student_classe.first()
            return latest_class.to_dict()
        return None

    def __str__(self):
        return f'{self.registration} - {self.name} - {self.city.name}'

    class Meta:
        db_table = 'alunos'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
