from rest_framework.exceptions import ValidationError
from rest_framework import viewsets, permissions
from django.db.models import Q

from ..serializers.student_serializer import StudentSerializer, StudentDetailSerializer
from ..models import Student


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        instance_id = self.request.query_params.get('id_instancia')
        if not instance_id:
            raise ValidationError(
                {"error": "A Instância deve ser informada para este usuário."}
            )

        if instance_id:
            queryset = queryset.filter(instance_id=instance_id)

        academic_year_id = self.request.query_params.get('id_ano_letivo')
        situation = self.request.query_params.get('situacao')
        name = self.request.query_params.get('name')
        registration = self.request.query_params.get('matricula')
        order = self.request.query_params.get('order')
        initial_row = self.request.query_params.get('initial_row')
        final_row = self.request.query_params.get('final_row')
        responsible_name = self.request.query_params.get('responsavel_nome')
        color = self.request.query_params.get('cor')
        gender = self.request.query_params.get('sexo')
        school_transport = self.request.query_params.get('transporte_escolar')
        pcd = self.request.query_params.get('pcd')
        disorder = self.request.query_params.get('disturbio')
        food_restriction = self.request.query_params.get('restricao_alimentar')
        school_id = self.request.query_params.get('id_escola')

        if academic_year_id:
            queryset = queryset.filter(
                studentclasses__classe__school_year__academic_year_id=academic_year_id)
        if situation:
            queryset = queryset.filter(student_status__id=situation)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if registration:
            queryset = queryset.filter(registration=registration)
        if responsible_name:
            queryset = queryset.filter(
                responsible_name__icontains=responsible_name
            )
        if color:
            queryset = queryset.filter(color__id=color)
        if school_id:
            queryset = queryset.filter(
                studentclasses__classe__school_year__school_id=school_id
            )
        if gender:
            queryset = queryset.filter(gender=gender)
        if school_transport is not None:
            if school_transport == '1':
                queryset = queryset.filter(school_transport_check=1)
            elif school_transport == '0':
                queryset = queryset.filter(
                    Q(school_transport_check=0) | Q(
                        school_transport_check__isnull=True
                    )
                )
        if pcd is not None:
            if pcd == '1':
                queryset = queryset.filter(disability_check=1)
            elif pcd == '0':
                queryset = queryset.filter(
                    Q(disability_check=0) | Q(disability_check__isnull=True))
        if disorder is not None:
            if disorder == '1':
                queryset = queryset.filter(disorder_check=1)
            elif disorder == '0':
                queryset = queryset.filter(
                    Q(disorder_check=0) | Q(disorder_check__isnull=True))
        if food_restriction is not None:
            if food_restriction == '1':
                queryset = queryset.filter(food_restriction_check=1)
            elif food_restriction == '0':
                queryset = queryset.filter(
                    Q(food_restriction_check=0) | Q(
                        food_restriction_check__isnull=True
                    )
                )

        if order == 'A-Z':
            queryset = queryset.order_by('name')
        elif order == 'Z-A':
            queryset = queryset.order_by('-name')

        if initial_row is not None and final_row is not None:
            try:
                initial_row = int(initial_row)
                final_row = int(final_row)
                if initial_row < 0 or final_row < 0:
                    raise ValidationError(
                        {"error": "initial_row e final_row devem ser valores positivos."})
                queryset = queryset[initial_row:final_row]
            except ValueError:
                raise ValidationError(
                    {"error": "initial_row e final_row devem ser números inteiros."})

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        serializer = self.get_serializer(page, many=True)
        paginated_response = self.get_paginated_response(serializer.data)

        applied_filters = {
            "id_instancia": request.query_params.get('id_instancia'),
            "id_ano_letivo": request.query_params.get('id_ano_letivo'),
            "situacao": request.query_params.get('situacao'),
            "name": request.query_params.get('name'),
            "matricula": request.query_params.get('matricula'),
            "order": request.query_params.get('order'),
            "initial_row": request.query_params.get('initial_row'),
            "final_row": request.query_params.get('final_row'),
            "responsavel_nome": request.query_params.get('responsavel_nome'),
            "cor": request.query_params.get('cor'),
            "sexo": request.query_params.get('sexo'),
            "transporte_escolar": request.query_params.get('transporte_escolar'),
            "pcd": request.query_params.get('pcd'),
            "disturbio": request.query_params.get('disturbio'),
            "restricao_alimentar": request.query_params.get('restricao_alimentar'),
            "id_escola": request.query_params.get('id_escola'),
        }

        paginated_response.data['applied_filters'] = applied_filters

        return paginated_response
