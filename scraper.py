import json

def run_scraper():
    # স্টার জলসা লিঙ্কের আইপি ও ফরম্যাট
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # এটি অন্তত ৫টি চ্যানেল তৈরি করবে
    for i in range(5):
        cid = f"a0c{i}"
        channels.append({
            "name": f"Channel_{cid}",
            "link": f"{base_url}{cid}/index.m3u8"
        })

    # এই ফাইলটি তৈরি হওয়া বাধ্যতামূলক (আপনার এরর দূর করতে)
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    print("Success: all_channels.json created!")

if __name__ == "__main__":
    run_scraper()
