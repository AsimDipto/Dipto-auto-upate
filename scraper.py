import requests
import re
import json

def fetch_ip_channels():
    # Targeted IP and pattern from your Star Jalsha link
    target_ip = "103.229.254.25:7001"
    search_query = f'"{target_ip}/play/"'
    github_api_url = f"https://api.github.com/search/code?q={search_query}"
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    channel_list = []
    unique_links = set()

    try:
        response = requests.get(github_api_url, headers=headers)
        if response.status_code == 200:
            items = response.json().get('items', [])
            for item in items:
                raw_url = item['html_url'].replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                file_data = requests.get(raw_url).text
                
                # Matches links like http://103.229.254.25:7001/play/a0c0/index.m3u8
                pattern = r'http://103\.229\.254\.25:7001/play/[\w/]+'
                found_links = re.findall(pattern, file_data)
                
                for link in found_links:
                    if link not in unique_links:
                        unique_links.add(link)
                        channel_list.append({
                            "name": f"Channel_{len(channel_list) + 1}",
                            "link": link
                        })
            
            with open('all_channels.json', 'w') as f:
                json.dump(channel_list, f, indent=2)
            print(f"Success: Found {len(channel_list)} channels.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    fetch_ip_channels()
