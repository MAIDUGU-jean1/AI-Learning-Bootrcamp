profile = {
    "name": "Perrin",
    "age": 29,
    "country": "Cameroon",
    "favourite_subject": "Computer Science",
    "goal": "Become a software engineer"
}

# Print the profile information neatly
print("User Profile:")
for key, value in profile.items():
    # Capitalize the key for nicer output
    pretty_key = key.replace("_", " ").title()
    print(f"{pretty_key}: {value}")