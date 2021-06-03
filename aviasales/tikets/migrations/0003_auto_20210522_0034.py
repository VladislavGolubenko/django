# Generated by Django 3.1.3 on 2021-05-21 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tikets', '0002_auto_20210507_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='baggage',
            field=models.BooleanField(blank=True, null=True, verbose_name='Наличие багажа'),
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата покупки'),
        ),
        migrations.AddField(
            model_name='order',
            name='place_class',
            field=models.CharField(max_length=25, null=True, verbose_name='Класс места'),
        ),
        migrations.AddField(
            model_name='order',
            name='window_place',
            field=models.BooleanField(blank=True, null=True, verbose_name='Место у окна'),
        ),
        migrations.AlterField(
            model_name='flights',
            name='plane_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='plane', to='tikets.plane', verbose_name='Самолёт'),
        ),
        migrations.AlterField(
            model_name='plane',
            name='carrier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='carrier', to='tikets.carrier', verbose_name='Перевозчик'),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='trunk',
            field=models.BooleanField(blank=True, null=True, verbose_name='Наличие багажа'),
        ),
    ]