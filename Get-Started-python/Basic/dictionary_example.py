# Example of nested dictionary with safe access methods

# Create a nested dictionary
person = {
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "country": "USA",
        "details": {
            "street": "123 Main St",
            "zip": "10001"
        }
    }
}

# Method 1: Direct access (when you're sure keys exist)
print("\nMethod 1: Direct access")
try:
    print(f"Street: {person['address']['details']['sajid']}")
except KeyError as e:
    print(f"Key not found: {e}")

# Method 2: Using get() with default value
print("\nMethod 2: Using get() with default")
street = person.get("address", {}).get("details", {}).get("street", "Not found")
print(f"Street: {street}")

# Method 3: Safe nested access function
def safe_get(dictionary, *keys, default=None):
    """Safely get nested dictionary values"""
    result = dictionary
    for key in keys:
        try:
            result = result[key]
        except (KeyError, TypeError):
            return default
    return result

# Using the safe access function
print("\nMethod 3: Using safe access function")
street = safe_get(person, "address", "details", "street", default="Not found")
print(f"Street: {street}") 