# Generated manually to add water_source and irrigation_type fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krushi_app', '0004_add_farm_id_owner_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerdata',
            name='water_source',
            field=models.CharField(choices=[('Canal', 'Canal'), ('Borewell', 'Borewell'), ('Rain-fed', 'Rain-fed')], default='Rain-fed', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='farmerdata',
            name='irrigation_type',
            field=models.CharField(default='Traditional', max_length=50),
            preserve_default=False,
        ),
    ]