import requests
import argparse
import os

# Defining the arguments for the script
parser = argparse.ArgumentParser(description="Upload SBOM or scan results to DefectDojo")
parser.add_argument('--api-url', required=True, help="DefectDojo API URL")
parser.add_argument('--api-key', required=True, help="DefectDojo API Key")
parser.add_argument('--product-id', required=True, help="DefectDojo Product ID")
parser.add_argument('--file-path', required=True, help="Path to the SBOM or scan result file")
parser.add_argument('--engagement-id', required=True, help="DefectDojo Engagement ID")
parser.add_argument('--scan-type', required=True, help="Type of scan, e.g., 'CycloneDX'")

args = parser.parse_args()

# API headers including authentication
headers = {
    'Authorization': f'Token {args.api_key}',
    'Accept': 'application/json'
}

# Defining the data payload
data = {
    'engagement': args.engagement_id,
    'scan_type': args.scan_type,
    'active': True,
    'verified': False
}

# Opening the SBOM or scan result file
with open(args.file_path, 'rb') as file:
    files = {'file': (os.path.basename(args.file_path), file)}

    # Making a POST request to DefectDojo API
    response = requests.post(
        f'{args.api_url}/api/v2/import-scan/',
        headers=headers,
        data=data,
        files=files
    )

    # Checking the response
    if response.status_code == 201:
        print(f"File uploaded successfully to DefectDojo. Response: {response.json()}")
    else:
        print(f"Failed to upload file. Status Code: {response.status_code}. Response: {response.json()}")

