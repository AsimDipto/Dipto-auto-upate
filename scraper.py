import requests

# আপনার দেওয়া বেস আইপি এবং পোর্ট
base_ip = "103.229.254."
port = "7001"
endpoint = "/play/a0c0/index.m3u8" # আপনার দেওয়া পাথ

found_channels = []

print(f"Scanning subnet {base_ip}0/24...")

# ১ থেকে ২৫৫ পর্যন্ত আইপি চেক করবে
for i in range(1, 256):
    target_ip = f"{base_ip}{i}"
    url = f"http://{target_ip}:{port}{endpoint}"
    
    try:
        # ৫ সেকেন্ড সময় দেব রেসপন্স পাওয়ার জন্য
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            print(f"[SUCCESS] Found active stream: {url}")
            found_channels.append(url)
        else:
            print(f"[INFO] Checked {target_ip} - Status: {response.status_code}")
            
    except requests.exceptions.RequestException:
        # কানেক্ট না হলে বা টাইমআউট হলে স্কিপ করবে
        pass

# রেজাল্ট একটি ফাইলে সেভ করা
with open("active_streams.m3u", "w") as f:
    f.write("#EXTM3U\n")
    for link in found_channels:
        f.write(f"#EXTINF:-1, IP TV Channel\n{link}\n")

print("\nScanning complete. Check 'active_streams.m3u' for results.")
