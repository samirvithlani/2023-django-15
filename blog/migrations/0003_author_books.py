# Generated by Django 4.2.3 on 2023-08-03 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_product_saleunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=200)),
                ('bprice', models.FloatField()),
                ('book_genere', models.CharField(choices=[('Science', 'Science'), ('Fiction', 'Fiction'), ('Drama', 'Drama'), ('Action', 'Action')], max_length=20)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
