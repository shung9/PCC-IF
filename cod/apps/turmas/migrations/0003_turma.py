# Generated by Django 4.0.3 on 2023-01-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0002_avisos_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(blank=True, max_length=150, null=True)),
                ('cor', models.CharField(blank=True, max_length=7, null=True)),
                ('codigo', models.CharField(max_length=5)),
            ],
        ),
    ]
