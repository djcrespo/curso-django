# Generated by Django 3.2.6 on 2024-01-23 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='empresaRepresentante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresa', verbose_name='Empresa que representa la persona')),
                ('representante', models.ManyToManyField(to='empresas.representante')),
            ],
        ),
    ]