import json

def run_scraper():
    # স্টার জলসা লিঙ্কের ফরম্যাট
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # এটি অন্তত ৫টি লিঙ্ক তৈরি করে ফাইলটি সেভ করবে
    for i in range(5):
        channel_id = f"a0c{i}"
        channels.append({
            "name": f"Channel_{channel_id}",
            "link": f"{base_url}{channel_id}/index.m3u8"
        })

    # এই অংশটিই আপনার এরর বন্ধ করবে
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    print("Scraping finished successfully!")

if __name__ == "__main__":
    run_scraper()
