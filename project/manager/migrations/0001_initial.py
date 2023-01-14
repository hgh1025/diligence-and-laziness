# Generated by Django 4.1.3 on 2023-01-14 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Commute",
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
                ("current_time", models.DateTimeField(auto_now_add=True)),
                ("go_time", models.DateTimeField(auto_now_add=True)),
                ("leave_time", models.DateTimeField(auto_now_add=True)),
                ("total_time", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Pay",
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
                ("overtime", models.IntegerField(null=True)),
                ("night", models.IntegerField(null=True)),
                ("weekend", models.IntegerField(null=True)),
                ("travel", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_email", models.EmailField(max_length=20, unique=True)),
                (
                    "user_name",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("user_date", models.DateTimeField(auto_now_add=True)),
                ("user_password", models.CharField(max_length=100)),
                (
                    "gender",
                    models.CharField(
                        choices=[("남자", "남자"), ("여자", "여자")], max_length=5, null=True
                    ),
                ),
                ("age", models.IntegerField(null=True)),
                ("year", models.IntegerField(null=True)),
                ("month", models.IntegerField(null=True)),
                ("day", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Working_condition",
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
                ("go", models.CharField(max_length=20)),
                ("leave", models.CharField(max_length=20)),
                ("vacation", models.CharField(max_length=20)),
                ("sick", models.CharField(max_length=20)),
                ("holiday", models.CharField(max_length=20)),
                ("absence", models.CharField(max_length=20)),
                ("half_vacation", models.CharField(max_length=20)),
                ("travel", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Vacation",
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
                ("total_vacation", models.IntegerField(null=True)),
                ("rest_vacation", models.IntegerField(null=True)),
                ("use_vacation", models.IntegerField(null=True)),
                (
                    "user_name",
                    models.ForeignKey(
                        db_column="user_name",
                        max_length=20,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vacation",
                        to="manager.user",
                    ),
                ),
            ],
        ),
    ]
