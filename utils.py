# REPLACE THIS WITH YOUR CODE
import os
import yaml

def get_apikey():
    """
    Reads API key from a configuration file.

    This function opens a configuration file named "apikeys.yml", reads the 
    API key for OpenAI, and returns it.

    Returns:
        str: The OpenAI API key.
    """
    # Construct the full path to the configuration file
    script_dir = "./apiKeys.yml"
    file_path = script_dir

    # Load the YAML file
    with open(file_path, 'r') as yamlfile:
        loaded_yamlfile = yaml.safe_load(yamlfile)

    # Extract the OpenAI API key
    api_key = loaded_yamlfile.get('openai', {}).get('api_key')
    if not api_key:
        raise ValueError("API key not found in the configuration file.")    
    return api_key
