import os
import django
import json

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()
from api.models import FusionWorldCard
def upload_one_piece_cards():
    json_file = 'data.json'  # Replace with your JSON file path

    with open(json_file, 'r') as file:
        data = json.load(file)

        for card_data in data:
            card_id = '-'.join(card_data.get('CARD ID', []))
            color = ', '.join(card_data.get('Color', []))
            card_type = ', '.join(card_data.get('Type', []))
            
            image_path = os.path.join(
                'fusion_world_cards/',
                f"{card_data['Key']}.jpg"
            )

            card = FusionWorldCard(
                key=card_data['Key'],
                card_id=card_id,
                rarity=card_data['Rarity'],
                category=card_data['Category'],
                card_name=card_data['Card Name'],
                cost=card_data['Cost']['Generic'],
                power=card_data['Power'],
                counter=card_data['Counter'],
                color=color,
                type=card_type,
                effect=card_data['Effect'],
                art=card_data['Art'],
                card_set=card_data['Set'],
                image=image_path
            )
            card.save()

if __name__ == '__main__':
    upload_one_piece_cards()
