# Generated by Django 5.0.7 on 2024-07-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_onepiececard_yugiohcard_delete_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onepiececard',
            name='description',
        ),
        migrations.RemoveField(
            model_name='yugiohcard',
            name='description',
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='card_id',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='color',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='cost',
            field=models.IntegerField(default=-999),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='counter',
            field=models.IntegerField(default=-999),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='effect',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='one_piece_cards/'),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='power',
            field=models.IntegerField(default=-999),
        ),
        migrations.AddField(
            model_name='onepiececard',
            name='type',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='attribute',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='card_type',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='defense',
            field=models.IntegerField(default=-999),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='effect',
            field=models.TextField(default='N/A'),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='yugioh_cards/'),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='level',
            field=models.IntegerField(default=-999),
        ),
        migrations.AddField(
            model_name='yugiohcard',
            name='power',
            field=models.IntegerField(default=-999),
        ),
        migrations.AlterField(
            model_name='onepiececard',
            name='name',
            field=models.TextField(default='N/A'),
        ),
        migrations.AlterField(
            model_name='yugiohcard',
            name='name',
            field=models.TextField(default='N/A'),
        ),
    ]