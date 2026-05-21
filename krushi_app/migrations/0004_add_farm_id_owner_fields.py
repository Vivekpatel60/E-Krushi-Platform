# Generated manually to add farm_id and owner fields

from django.db import migrations, models


def populate_farm_ids(apps, schema_editor):
    FarmerData = apps.get_model('krushi_app', 'FarmerData')
    for i, farmer_data in enumerate(FarmerData.objects.all(), 1):
        farmer_data.farm_id = f'FARM{i:03d}'
        farmer_data.owner = 'Unknown'
        farmer_data.save()


class Migration(migrations.Migration):

    dependencies = [
        ('krushi_app', '0003_remove_farmerdata_fertilizer_used_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmerdata',
            name='farm_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='farmerdata',
            name='owner',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.RunPython(populate_farm_ids),
        migrations.AlterField(
            model_name='farmerdata',
            name='farm_id',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='farmerdata',
            name='owner',
            field=models.CharField(max_length=100),
        ),
    ]