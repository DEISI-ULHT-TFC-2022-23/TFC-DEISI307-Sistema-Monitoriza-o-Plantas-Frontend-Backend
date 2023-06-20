# Generated by Django 4.1.2 on 2023-05-03 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tfc", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Monitorizacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instante", models.DateTimeField(auto_now=True)),
                ("luz", models.FloatField(default=0.0)),
                ("humidade", models.FloatField(default=0.0)),
                ("temperatura", models.FloatField(default=0.0)),
                ("condutividade", models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name="PlantaCuidada",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tratamento",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instante", models.DateTimeField(auto_now=True)),
                ("quantidade_agua", models.FloatField(default=0.0)),
                ("quantidade_fertilizante", models.FloatField(default=0.0)),
                (
                    "planta_cuidada",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tfc.plantacuidada",
                    ),
                ),
            ],
        ),
        migrations.RemoveField(model_name="planta", name="condicoes",),
        migrations.RemoveField(model_name="utilizador", name="plantas",),
        migrations.AddField(
            model_name="planta",
            name="dificuldade",
            field=models.CharField(default="", max_length=16),
        ),
        migrations.AddField(
            model_name="planta",
            name="expo_solar",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="planta",
            name="quantidade_agua",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="planta",
            name="quantidade_fertilizante",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="planta",
            name="tipo_fertilizante",
            field=models.CharField(default="", max_length=64),
        ),
        migrations.DeleteModel(name="Condicao",),
        migrations.AddField(
            model_name="plantacuidada",
            name="planta",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tfc.planta"
            ),
        ),
        migrations.AddField(
            model_name="plantacuidada",
            name="utilizador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tfc.utilizador"
            ),
        ),
        migrations.AddField(
            model_name="monitorizacao",
            name="planta_cuidada",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="tfc.plantacuidada"
            ),
        ),
    ]