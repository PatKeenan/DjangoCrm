# Generated by Django 3.1.5 on 2021-01-28 21:46

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
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(default='Other', max_length=50, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['relation'],
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_1', models.CharField(max_length=50, verbose_name='Street 1')),
                ('street_2', models.CharField(blank=True, max_length=50, verbose_name='Street 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('zip_code', models.CharField(max_length=50, verbose_name='Zip Code')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
                'ordering': ['street_1'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('level', models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], default='Bronze', max_length=50)),
                ('twitter_url', models.CharField(blank=True, max_length=200, verbose_name='Twitter Url')),
                ('facebook_url', models.CharField(blank=True, max_length=200, verbose_name='Facebook Url')),
                ('instagram_url', models.CharField(blank=True, max_length=200, verbose_name='Instagram Url')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('properties', models.ManyToManyField(blank=True, to='crm.Property')),
                ('relations', models.ManyToManyField(blank=True, to='crm.Relation')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Active',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Under Contract', 'Under Contract'), ('Dropped', 'Dropped'), ('Closed', 'Closed')], max_length=50)),
                ('Property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.property', verbose_name='Property')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('people', models.ManyToManyField(to='crm.Person', verbose_name='Clients')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
