user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

def update_preferences(user_pref):
    updated_pref = {}
    for key, value in user_pref.items():
        if value is not None:
            updated_pref[key] = value
    return updated_pref

print("Version 1:", update_preferences(user_preferences))

def update_preferences_2 (user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}

print("Version 2:", update_preferences_2(user_preferences))
