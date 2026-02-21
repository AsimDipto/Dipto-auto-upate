import requests
import json
import os

def run_scraper():
    # Target settings based on your Star Jalsha link
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # Scanning channel range (a0c0 to a0c50 as example)
    for i in range(50):
        channel_id = f"a0c{i}"
        stream_link = f"{base_url}{channel_id}/index.m3u8"
        
        try:
            # Checking if the link is active (timeout set for speed)
            response = requests.head(stream_link, timeout=2)
            if response.status_code == 200:
                channels.append({
                    "name": f"Channel_{channel_id}",
                    "link": stream_link
                })
        except:
            continue

    # Creating the file even if empty to prevent GitHub Action error
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    print(f"Scrape completed. Found {len(channels)} channels.")

if __name__ == "__main__":
    run_scraper()
