# Generated by Django 3.1.7 on 2021-03-31 06:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstName', models.TextField(help_text='First name')),
                ('lastName', models.TextField(help_text='Last name')),
                ('birthday', models.DateTimeField(help_text='Birthday')),
                ('user', models.ForeignKey(help_text='User this Profile belongs to.', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]