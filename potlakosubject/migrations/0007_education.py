# Generated by Django 3.1.4 on 2021-01-25 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potlakosubject', '0006_auto_20210125_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no')], max_length=5, null=True, verbose_name='Are you currently working?')),
                ('type_of_work', models.CharField(blank=True, choices=[('occasion', 'occasional or Casual employment (piece job)'), ('seasonal_employment', 'seasonal employment'), ('full_time', 'Formal wage employment(full time)'), ('part_time', 'Formal wage employment (part-time)'), ('self_employed_agriculture', 'Self-employed in agriculture'), ('self_employed making money_full time', 'Self-employed making money, full time')], max_length=50, null=True, verbose_name='In your main job what type of work do you do?')),
            ],
        ),
    ]