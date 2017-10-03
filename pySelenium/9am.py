from py9anime import Client

client = Client()
print(client.get_schedule()) # Fetch the weekly schedule
print(client.search("naruto")) # Search for naruto