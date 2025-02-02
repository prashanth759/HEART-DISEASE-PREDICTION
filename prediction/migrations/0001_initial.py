# Generated by Django 4.2.6 on 2023-10-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(0, 'Female'), (1, 'Male')])),
                ('cp', models.IntegerField(choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')])),
                ('trestbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('restecg', models.IntegerField(choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality'), (2, 'Left Ventricular Hypertrophy')])),
                ('thalach', models.IntegerField()),
                ('exang', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')])),
                ('oldpeak', models.FloatField()),
                ('slope', models.IntegerField(choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')])),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField(choices=[(0, 'Normal'), (1, 'Fixed Defect'), (2, 'Reversible Defect')])),
                ('result', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
