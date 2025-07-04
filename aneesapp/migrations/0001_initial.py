# Generated by Django 4.2.21 on 2025-06-25 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=100)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('venue', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('status', models.CharField(choices=[('a', 'Booked'), ('b', 'Cancelled'), ('c', 'Checked-in')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attendee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aneesapp.attendee')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aneesapp.event')),
            ],
        ),
    ]
