# Generated by Django 4.2 on 2023-06-08 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Preguntas', '0003_alter_contestacion_id_opcion_alter_pregunta_modulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='modulo',
            field=models.IntegerField(choices=[(3, '3'), ('', '-------------'), (2, '2'), (5, '5'), (1, '1'), (4, '4')]),
        ),
    ]
