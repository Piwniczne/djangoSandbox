# Generated by Django 3.0 on 2022-01-23 15:27

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('dataCreated', models.DateTimeField(blank=True, null=True)),
                ('lastUpdated', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_blog_thumbnail.jpg', force_format=None, keep_meta=True, quality=75, size=[200, 250], upload_to='blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
    ]
