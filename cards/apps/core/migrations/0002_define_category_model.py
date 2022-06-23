# Generated by Django 4.0.5 on 2022-06-22 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_define_card_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('DIN', 'Dining'), ('ENT', 'Entertainment'), ('GAS', 'Gas'), ('GRO', 'Groceries'), ('ONL', 'Online'), ('STR', 'Streaming'), ('TRA', 'Travel'), ('TST', 'Transit')], max_length=3)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='core.card')),
            ],
        ),
    ]