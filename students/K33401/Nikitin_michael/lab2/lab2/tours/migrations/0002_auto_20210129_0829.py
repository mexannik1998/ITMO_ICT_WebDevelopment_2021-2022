# Generated by Django 3.1.5 on 2021-01-29 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='PlaceForTour',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='commentator',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='country',
            new_name='tour_agency',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='places_booked',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='places_total',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='price',
        ),
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nationality',
        ),
        migrations.RemoveField(
            model_name='user',
            name='surname',
        ),
        migrations.AddField(
            model_name='comments',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='count_of_booked',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tour',
            name='count_of_place',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='tour',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='name',
            field=models.CharField(default='tour_name', max_length=30),
        ),
        migrations.AddField(
            model_name='tour',
            name='payment',
            field=models.IntegerField(default=10000),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_duration',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='date_of_tour',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='passport',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='booked',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tour'),
        ),
        migrations.AddField(
            model_name='booked',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
