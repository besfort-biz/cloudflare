import requests

# Replace 'YOUR_API_TOKEN' with your actual Cloudflare API token
api_token = 'xxxxxxxx'
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json',
}

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. List DNS Zones")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            zone_dict = fetch_zones()
            zone_id = input("Enter the ID of the zone to manage DNS records for: ")
            dns_menu(zone_dict, zone_id)
        elif choice == '2':
            print("Exiting...")
            break

def fetch_zones():
    print("Fetching zones...")
    url = "https://api.cloudflare.com/client/v4/zones"
    response = requests.get(url, headers=headers)
    zones = response.json().get('result', [])
    zone_dict = {str(index + 1): zone for index, zone in enumerate(zones)}
    for idx, zone in zone_dict.items():
        print(f"{idx}: {zone['name']}")
    return zone_dict

def dns_menu(zone_dict, zone_id):
    while True:
        print("\nDNS Management Menu:")
        print("1. List DNS Records")
        print("2. Add DNS Record")
        print("3. Back")
        choice = input("Choose an option: ")
        if choice == '1':
            manage_dns_records(zone_dict, zone_id)
        elif choice == '2':
            add_dns_record(zone_dict, zone_id)
        elif choice == '3':
            return

def manage_dns_records(zone_dict, zone_id):
    record_dict = list_dns_records(zone_dict, zone_id)
    while True:
        record_id = input("Enter the ID of the record to edit or delete, or type 'back' to return: ")
        if record_id.lower() == 'back':
            break
        action = input("Do you want to edit (e) or delete (d) this record? [e/d]: ")
        if action.lower() == 'e':
            new_content = input("Enter new content for the record: ")
            edit_dns_record(zone_dict, zone_id, record_dict, record_id, new_content)
        elif action.lower() == 'd':
            delete_dns_record(zone_dict, zone_id, record_dict, record_id)
        else:
            print("Invalid action selected.")
        record_dict = list_dns_records(zone_dict, zone_id)  # Refresh list after modifications

def list_dns_records(zone_dict, zone_id):
    print("\nFetching DNS records...")
    zone = zone_dict[zone_id]
    url = f"https://api.cloudflare.com/client/v4/zones/{zone['id']}/dns_records"
    response = requests.get(url, headers=headers)
    records = response.json().get('result', [])
    record_dict = {str(index + 1): record for index, record in enumerate(records)}
    for idx, record in record_dict.items():
        print(f"{idx}: Type: {record['type']}, Name: {record['name']}, Content: {record['content']}")
    return record_dict

def add_dns_record(zone_dict, zone_id):
    print("\nAdding new DNS Record...")
    zone = zone_dict[zone_id]
    record_type = input("Enter record type (e.g., A, CNAME): ")
    name = input("Enter record name: ")
    content = input("Enter record content: ")
    ttl = int(input("Enter TTL (Time To Live) in seconds (1 = automatic): "))
    proxied = input("Proxied? (true/false): ").lower() in ['true', '1', 'yes']
    
    data = {
        "type": record_type,
        "name": name,
        "content": content,
        "ttl": ttl,
        "proxied": proxied
    }
    
    url = f"https://api.cloudflare.com/client/v4/zones/{zone['id']}/dns_records"
    response = requests.post(url, headers=headers, json=data)
    print("DNS Record added successfully." if response.status_code == 200 else f"Failed to add DNS Record. Response: {response.text}")

def edit_dns_record(zone_dict, zone_id, record_dict, record_id, new_content):
    zone = zone_dict[zone_id]
    record = record_dict[record_id]
    url = f"https://api.cloudflare.com/client/v4/zones/{zone['id']}/dns_records/{record['id']}"
    data = {
        "type": record['type'],
        "name": record['name'],
        "content": new_content,
        "ttl": record.get('ttl', 1),
        "proxied": record.get('proxied', False)
    }
    response = requests.put(url, headers=headers, json=data)
    print("Record updated successfully." if response.status_code == 200 else "Failed to update record.")

def delete_dns_record(zone_dict, zone_id, record_dict, record_id):
    zone = zone_dict[zone_id]
    record = record_dict[record_id]
    url = f"https://api.cloudflare.com/client/v4/zones/{zone['id']}/dns_records/{record['id']}"
    response = requests.delete(url, headers=headers)
    print("Record deleted successfully." if response.status_code == 200 else "Failed to delete record.")

if __name__ == '__main__':
    main_menu()
