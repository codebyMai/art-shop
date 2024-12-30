# Generated by Django 5.1.4 on 2024-12-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('image', models.ImageField(null=True, upload_to='static/images')),
                ('image_alt', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('subject', models.CharField(choices=[('La', 'Landscape'), ('Se', 'Seascape'), ('St', 'Still life'), ('Fl', 'Flowers')], max_length=100)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('is_miniature', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
