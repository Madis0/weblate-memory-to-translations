import os
import json

def update_localization(translation_memory_file, localization_file, output_file):
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the file paths
    translation_memory_path = os.path.join(current_dir, translation_memory_file)
    localization_path = os.path.join(current_dir, localization_file)
    output_path = os.path.join(current_dir, output_file)

    # Load the translation memory file
    with open(translation_memory_path, 'r') as f:
        translation_memory = json.load(f)

    # Load the original localization file
    with open(localization_path, 'r') as f:
        localization = json.load(f)

    # Update the localization with the translations from the translation memory
    updated_localization = {}
    for key, value in localization.items():
        updated_value = None
        for translation in translation_memory:
            if translation['source'] == value:
                updated_value = translation['target']
                break
        if updated_value is not None:
            updated_localization[key] = updated_value

    # Write the updated localization file
    with open(output_path, 'w') as f:
        json.dump(updated_localization, f, indent=4)

# Example usage:
translation_memory_file = 'weblate-memory.json'
localization_file = 'file-name-en.json'
output_file = 'file-name-xx.json'

update_localization(translation_memory_file, localization_file, output_file)
