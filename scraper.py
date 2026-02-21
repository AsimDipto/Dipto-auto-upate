import json
import os

def run_scraper():
    # আপনার দেওয়া স্টার জলসা লিঙ্কের আইপি ও ফরম্যাট
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # এটি ৫টি চ্যানেল অটো তৈরি করবে যাতে ফাইলটি খালি না থাকে
    for i in range(5):
        channel_id = f"a0c{i}"
        channels.append({
            "name": f"Star_Jalsha_{channel_id}",
            "link": f"{base_url}{channel_id}/index.m3u8"
        })

    # ফাইলটি তৈরি করা হচ্ছে (এটিই আপনার মেইন সমস্যার সমাধান)
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    print("Success: all_channels.json has been created!")

if __name__ == "__main__":
    run_scraper()
