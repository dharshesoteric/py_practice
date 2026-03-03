test_settings = {
    'theme' : 'dark',
    'notifications' : 'muted',
    'volume' : 'medium'
}

def add_setting(settings_dict, kvpair):
    
    #Lowercase conversion
    lc_key = kvpair[0].lower()
    lc_val = kvpair[1].lower()

    #check if the key already exists in the dict
    if lc_key in settings_dict:
            return f"Setting '{lc_key}' already exists! Cannot add a new setting with this name."
    
    #add if the provided settings are new
    settings_dict[lc_key] = lc_val
    return f"Setting '{lc_key}' added with value '{lc_val}' successfully!"   

def update_setting(settings_dict, kvpair):

    #Lowercase conversion
    lc_key = kvpair[0].lower()
    lc_val = kvpair[1].lower()

    #Check if key is present
    if lc_key in settings_dict:
        settings_dict[lc_key] = lc_val
        return f"Setting '{lc_key}' updated to '{lc_val}' successfully!"
    else:
        return f"Setting '{lc_key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, key):
    
    #Lower case conversion
    lc_key = key.lower()
    
    #Check if key is present and delete the specified key
    if lc_key in settings_dict:
        del settings_dict[lc_key]
        return f"Setting '{lc_key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings_dict):
    
    #Check if the dict is empty
    if not settings_dict:
        return "No settings available."
    
    #Create a list to contain all the kv pairs from the dict in str
    settings = [""] * len(settings_dict)

    #Store the modified tuple elements as strs in the settings list
    for index, kv in enumerate(settings_dict.items()):
        settings[index] = kv[0].capitalize() + ": " + kv[1]

    #Join the settings list using newline for formatting
    settings = "\n".join(settings)
    return f"Current User Settings:\n{settings}\n"