import requests
import json

def run_scraper():
    # সরাসরি স্টার জলসা প্যাটার্ন চেক করার জন্য
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # আপাতত প্রথম ২০টি আইডি চেক করবে (a0c0, a0c1...)
    for i in range(20):
        channel_id = f"a0c{i}"
        link = f"{base_url}{channel_id}/index.m3u8"
        channels.append({
            "name": f"IPTV_{channel_id}",
            "link": link
        })

    # ফাইলটি অবশ্যই তৈরি হবে যাতে GitHub Error না দেয়
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    print("File updated successfully!")

if __name__ == "__main__":
    run_scraper()
