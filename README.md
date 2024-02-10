
# Cloudflare DNS Management Tool

This Python script provides a simple command-line interface to manage DNS records for domains hosted on Cloudflare. It utilizes Cloudflare's API to allow users to list DNS zones, add, edit, or delete DNS records within those zones. This tool is designed to simplify the process of DNS management without the need to navigate through the Cloudflare dashboard.

## Features

- **List DNS Zones:** Display all DNS zones associated with your Cloudflare account.
- **List DNS Records:** For a selected zone, list all the DNS records.
- **Add DNS Record:** Add a new DNS record to a selected zone.
- **Edit DNS Record:** Edit an existing DNS record within a selected zone.
- **Delete DNS Record:** Remove an existing DNS record from a selected zone.

## Setup

Before you start, ensure you have Python installed on your system and the `requests` library available. If you do not have the `requests` library, you can install it using pip:

```bash
pip install requests
```

## Configuration

Replace `'YOUR_API_TOKEN'` in the script with your actual Cloudflare API token. Ensure your API token has the permissions required to manage DNS records.

## Usage

Run the script in your terminal or command prompt:

```bash
python cloudflare_dns_management.py
```

Follow the on-screen prompts to manage your DNS records.

## Security Note

This script requires your Cloudflare API token, which provides access to your Cloudflare account. Keep your API token secure and do not share it with others.

## Disclaimer

This tool is provided as-is, without warranty of any kind. Use it at your own risk.
