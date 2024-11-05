import json

def clean_us_state_boundaries(file_path, output_path):
    # Load the data
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    cleaned_data = []
    
    # Iterate over each feature (state)
    for feature in data:
        # Prepare the cleaned structure
        cleaned_feature = {
            "type": "Feature",
            "properties": {
                "name": feature["name"],
                "state_code": feature["stusab"]
            },
            "geometry": feature["st_asgeojson"]["geometry"]
        }
        
        # Remove any invalid coordinates if necessary
        if cleaned_feature["geometry"]["type"] == "Polygon":
            cleaned_feature["geometry"]["coordinates"] = [
                [coord for coord in ring if coord]
                for ring in cleaned_feature["geometry"]["coordinates"]
            ]
        elif cleaned_feature["geometry"]["type"] == "MultiPolygon":
            cleaned_feature["geometry"]["coordinates"] = [
                [[coord for coord in ring if coord] for ring in polygon]
                for polygon in cleaned_feature["geometry"]["coordinates"]
            ]
        
        cleaned_data.append(cleaned_feature)
    
    # Save the cleaned data
    with open(output_path, 'w') as f:
        json.dump({
            "type": "FeatureCollection",
            "features": cleaned_data
        }, f, indent=2)

# Usage example
clean_us_state_boundaries('us-state-boundaries.json', 'cleaned_us_state_boundaries.json')
