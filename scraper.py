import json

def create_list():
    # আপনার দেওয়া আইপি এবং লিঙ্ক প্যাটার্ন
    base_url = "http://103.229.254.25:7001/play/"
    channels = []
    
    # এটি অন্তত ৫টি লিঙ্ক তৈরি করবে যাতে ফাইলটি খালি না থাকে
    for i in range(5):
        cid = f"a0c{i}"
        channels.append({
            "name": f"Channel_{cid}",
            "link": f"{base_url}{cid}/index.m3u8"
        })

    # এই ফাইলটি তৈরি না হলে গিটহাব এরর দেয়
    with open('all_channels.json', 'w') as f:
        json.dump(channels, f, indent=2)
    print("Success: all_channels.json created!")

if __name__ == "__main__":
    create_list()
