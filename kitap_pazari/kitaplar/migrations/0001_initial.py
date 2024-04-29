# Generated by Django 5.0.4 on 2024-04-29 19:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=255)),
                ('yazar', models.CharField(max_length=255)),
                ('aciklama', models.TextField(blank=True, null=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
                ('yayin_tarihi', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yorum_sahibi', models.CharField(max_length=255)),
                ('yorum', models.TextField(blank=True, null=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
                ('degerlendirme', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('kitap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='kitaplar.kitap')),
            ],
        ),
    ]