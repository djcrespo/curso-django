# Generated by Django 3.2.6 on 2024-01-23 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_empresarepresentante'),
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='computadoraEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computadora', models.ManyToManyField(to='inventario.computadora')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresarepresentante')),
            ],
        ),
    ]
