import json

def extract_state_boundaries(input_path, output_path):
    # Load the TopoJSON data
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    # Check if there's an object named 'states' and keep only that
    if "states" in data["objects"]:
        data["objects"] = {"states": data["objects"]["states"]}
    else:
        print("No 'states' object found in the TopoJSON.")
        return

    # Save the modified TopoJSON
    with open(output_path, 'w') as f:
        json.dump(data, f)

# Usage
extract_state_boundaries('us-state-boundaries.json', 'cleaned-us-state-boundaries.json')
