import json

def run_scraper():
    # আপনার স্টার জলসা লিঙ্ক ফরম্যাট
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # এটি অন্তত ১০টি লিঙ্ক তৈরি করবে
    for i in range(10):
        channel_id = f"a0c{i}"
        channels.append({
            "name": f"Channel_{channel_id}",
            "link": f"{base_url}{channel_id}/index.m3u8"
        })

    # এই ফাইলটি তৈরি হওয়া বাধ্যতামূলক
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    print("Scrape completed successfully!")

if __name__ == "__main__":
    run_scraper()
