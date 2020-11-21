# Generated by Django 3.1.3 on 2020-11-21 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.PositiveIntegerField(default=1, unique=True)),
                ('seat_type', models.CharField(choices=[('aisle', 'Aisle'), ('front_row', 'Front Row'), ('balcony', 'Balcony')], max_length=20)),
                ('is_blocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('rank', models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three')], max_length=10)),
                ('seat_preference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.seat')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(choices=[('main_hall', 'Main Hall'), ('first_balcony', 'First Balcony'), ('second_balcony', 'Second Balcony')], default='first_balcony', max_length=25)),
                ('rows', models.ManyToManyField(related_name='section_row', to='app.Row')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='allocated_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='row',
            name='seats',
            field=models.ManyToManyField(blank=True, related_name='row_seat', to='app.Seat'),
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Zaal 1', max_length=25)),
                ('sections', models.ManyToManyField(related_name='hall_section', to='app.Section')),
            ],
        ),
    ]
