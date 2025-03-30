def generate_layout(input_data):
    area_sqft = input_data['land_cents'] * 435.6
    builtup_area = area_sqft * 0.7
    return {
        'ground': {'type': 'open_workshop', 'area': builtup_area * 0.55},
        'first': {'type': 'workspace', 'area': builtup_area * 0.45},
        'solar_roof': input_data['solar_required']
    }
