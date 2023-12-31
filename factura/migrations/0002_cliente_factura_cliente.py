# Generated by Django 4.2.2 on 2023-06-20 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.IntegerField(null=True)),
                ('nombre', models.CharField(max_length=20, null=True)),
                ('apellido', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('telefono', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='factura.cliente'),
        ),
    ]
