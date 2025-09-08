import requests
import pandas as pd

# Replace with your API endpoint
url = "https://api.example.com/data"

# Optional: headers or authentication
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer YOUR_API_TOKEN"  # remove if not needed
}

# Make GET request
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv("output.csv", index=False)
    print("Data saved to output.csv")
else:
    print(f"Failed to fetch data: {response.status_code}, {response.text}")

