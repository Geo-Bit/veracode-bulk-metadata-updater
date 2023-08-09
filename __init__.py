import requests, sys, csv
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC


# Generate report of all apps and metadata
def generate_metadata_report():
    #get current metadata for all apps in Veracode
    try:
        response = requests.get("https://api.veracode.com/appsec/v1/applications/?page=0&size=50", auth=RequestsAuthPluginVeracodeHMAC())
    except requests.RequestException as e:
        print("Pulling all application info in Veracode request failed. Exception code: " + e)
        sys.exit(1)
    if response.ok:
        app_data = response.json()
        print(app_data)
    

# Ingest report of all apps and metadata
    # For each application
    # Update metadata for that field
    # Verify differences
    # Prompt confirmation

def main():
    generate_metadata_report()

if __name__ == "__main__":
    main()