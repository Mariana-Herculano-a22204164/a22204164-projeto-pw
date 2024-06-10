import json
from django.db import transaction
from curso.models import Curso, AreaCientifica, Disciplina, LinguagemProgramacao, Projeto, Docente

def importarcurso(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    with transaction.atomic():
        course_details = data['courseDetail']
        curso, _ = Curso.objects.update_or_create(
            nome=course_details['courseName'],
            defaults={
                'apresentacao': course_details['presentation'],
                'objetivos': course_details['objectives'],
                'competencias': course_details['competences']
            }
        )

        for item in data['courseFlatPlan']:
            if 'codigo_curso' not in curso.__dict__ or not curso.codigo_curso:
                curso.codigo_curso = item['curricularIUnitReadableCode'].split('-')[0]
                curso.save()

            area_cientifica, _ = AreaCientifica.objects.update_or_create(
                nome=item["curricularBranchName"],
                defaults={
                    'codigo': item["curricularUnitGroupCode"],
                    'codigo_cnaef': str(item["curricularBranchCode"])
                }
            )

            disciplina, _ = Disciplina.objects.update_or_create(
                curricular_unit_readable_code=item['curricularIUnitReadableCode'],
                defaults={
                    'nome': item['curricularUnitName'],
                    'ano': item['curricularYear'],
                    'semestre': item['semester'],
                    'ects': item['ects'],
                    'area_cientifica': area_cientifica
                }
            )

        print("Course and associated disciplines updated!")