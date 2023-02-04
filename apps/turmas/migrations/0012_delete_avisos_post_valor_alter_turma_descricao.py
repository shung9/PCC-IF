# Generated by Django 4.0.3 on 2023-02-04 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0011_remove_turma_criacao_post_criacao'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Avisos',
        ),
        migrations.AddField(
            model_name='post',
            name='valor',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
