import json
import os

def run_simple_scraper():
    # আপনার দেওয়া স্টার জলসার লিঙ্কটিকে বেস হিসেবে রাখা হলো
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # আপাতত আমরা জানি a0c0 কাজ করে, তাই এটিকে লিস্টে রাখছি
    # যাতে ফাইলটি খালি না থাকে
    active_ids = ["a0c0", "a0c1", "a0c2"] 
    
    for cid in active_ids:
        channels.append({
            "name": f"Channel_{cid}",
            "link": f"{base_url}{cid}/index.m3u8"
        })

    # ফাইলটি তৈরি করা হচ্ছে
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    
    print("Success: all_channels.json created!")

if __name__ == "__main__":
    run_simple_scraper()
