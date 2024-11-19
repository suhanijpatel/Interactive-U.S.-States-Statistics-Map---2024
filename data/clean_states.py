import json

#function to extract state boundaries from TopoJSON file
def extract_state_boundaries(input_path, output_path):
    #loading TopoJSON data
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    #filtering to only keep objects named 'states' 
    if "states" in data["objects"]:
        data["objects"] = {"states": data["objects"]["states"]}
    else:
        print("No 'states' object found in the TopoJSON.")
        return

    #write to new file
    with open(output_path, 'w') as f:
        json.dump(data, f)

extract_state_boundaries('us-state-boundaries.json', 'cleaned-us-state-boundaries.json')