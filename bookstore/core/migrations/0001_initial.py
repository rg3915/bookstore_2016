# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-04 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='nome')),
                ('age', models.PositiveIntegerField(verbose_name='idade')),
            ],
            options={
                'verbose_name_plural': 'autores',
                'verbose_name': 'autor',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('isbn', models.IntegerField()),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('rating', models.FloatField(verbose_name='classificação')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='preço')),
                ('stock_min', models.PositiveIntegerField(default=0, verbose_name='Estoque mínimo')),
                ('stock', models.IntegerField(verbose_name='Estoque atual')),
                ('authors', models.ManyToManyField(to='core.Author', verbose_name='autores')),
            ],
            options={
                'verbose_name_plural': 'livros',
                'verbose_name': 'livro',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, verbose_name='gênero')),
                ('treatment', models.CharField(blank=True, choices=[('a', 'Arq.'), ('aa', 'Arqa.'), ('d', 'Dona'), ('dr', 'Dr.'), ('dra', 'Dra.'), ('e', 'Eng.'), ('ea', 'Engª.'), ('p', 'Prof.'), ('pa', 'Profa.'), ('sr', 'Sr.'), ('sra', 'Sra.'), ('srta', 'Srta.')], max_length=4, verbose_name='tratamento')),
                ('first_name', models.CharField(max_length=30, verbose_name='nome')),
                ('last_name', models.CharField(max_length=30, verbose_name='sobrenome')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='nascimento')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
            ],
            options={
                'verbose_name_plural': 'clientes',
                'verbose_name': 'cliente',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('status', models.CharField(choices=[('ca', 'cancelado'), ('pe', 'pendente'), ('co', 'confirmado')], default='pe', max_length=2, verbose_name='status')),
            ],
            options={
                'verbose_name_plural': 'pedidos',
                'verbose_name': 'pedido',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='nome')),
                ('num_awards', models.PositiveIntegerField(verbose_name='prêmios')),
            ],
            options={
                'verbose_name_plural': 'editoras',
                'verbose_name': 'editora',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False, verbose_name='pago')),
                ('date_paid', models.DateTimeField(blank=True, null=True, verbose_name='pago em')),
                ('method', models.CharField(blank=True, max_length=20, verbose_name='forma de pagto')),
                ('deadline', models.CharField(blank=True, max_length=50, verbose_name='prazo de entrega')),
                ('ordered', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Ordered', verbose_name='pedido')),
            ],
            options={
                'verbose_name_plural': 'vendas',
                'verbose_name': 'venda',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, verbose_name='gênero')),
                ('treatment', models.CharField(blank=True, choices=[('a', 'Arq.'), ('aa', 'Arqa.'), ('d', 'Dona'), ('dr', 'Dr.'), ('dra', 'Dra.'), ('e', 'Eng.'), ('ea', 'Engª.'), ('p', 'Prof.'), ('pa', 'Profa.'), ('sr', 'Sr.'), ('sra', 'Sra.'), ('srta', 'Srta.')], max_length=4, verbose_name='tratamento')),
                ('first_name', models.CharField(max_length=30, verbose_name='nome')),
                ('last_name', models.CharField(max_length=30, verbose_name='sobrenome')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='nascimento')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('active', models.BooleanField(default=True, verbose_name='ativo')),
                ('blocked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('internal', models.BooleanField(default=True, verbose_name='interno')),
                ('commissioned', models.BooleanField(default=True, verbose_name='comissionado')),
                ('commission', models.DecimalField(blank=True, decimal_places=2, default=0.01, max_digits=6, verbose_name='comissão')),
            ],
            options={
                'verbose_name_plural': 'vendedores',
                'verbose_name': 'vendedor',
                'ordering': ['first_name'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('books', models.ManyToManyField(to='core.Book', verbose_name='livros')),
            ],
            options={
                'verbose_name_plural': 'lojas',
                'verbose_name': 'loja',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PF',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Customer')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('rg', models.CharField(max_length=10, verbose_name='RG')),
            ],
            options={
                'verbose_name_plural': 'pessoas físicas',
                'verbose_name': 'pessoa física',
            },
            bases=('core.customer',),
        ),
        migrations.CreateModel(
            name='PJ',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Customer')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('ie', models.CharField(max_length=10, verbose_name='IE')),
            ],
            options={
                'verbose_name_plural': 'pessoas jurídicas',
                'verbose_name': 'pessoa jurídica',
            },
            bases=('core.customer',),
        ),
        migrations.AddField(
            model_name='ordered',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_pedido', to='core.Customer', verbose_name='cliente'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Publisher', verbose_name='editora'),
        ),
    ]
