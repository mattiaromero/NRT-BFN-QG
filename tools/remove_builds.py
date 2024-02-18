import ruamel.yaml as yaml
import sys

# Function to remove the section after the second equal sign
def remove_build(yaml_file):
    # Load YAML file
    with open(yaml_file, 'r') as file:
        yaml_content = file.read()
    # Split each line by "=" and keep only parts to the left of the second "="
    new_lines = [
        "=".join(line.split("=")[:2]) + "\n" if "=" in line else line + "\n" for line in yaml_content.split("\n")
    ]

    # Write updated YAML file and split into multiple lines
    with open(yaml_file, 'w') as file:
        file.write("".join(new_lines))
    return 

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_builds.py <yaml_file>")
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    remove_build(yaml_file)
    print("Builds section removed from", yaml_file)
