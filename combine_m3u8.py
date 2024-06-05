import requests

# List of URLs for .m3u8 files
urls = [
    'https://satstorm.com/iptv2.m3u8',
    'https://i.mjh.nz/SamsungTVPlus/in.m3u8',
    'https://i.mjh.nz/SamsungTVPlus/us.m3u8',
    'https://i.mjh.nz/SamsungTVPlus/gb.m3u8',
    'https://i.mjh.nz/SamsungTVPlus/ca.m3u8',
    'https://i.mjh.nz/PlutoTV/us.m3u8',
    'https://i.mjh.nz/PlutoTV/gb.m3u8',
    'https://i.mjh.nz/PlutoTV/ca.m3u8',
    'https://raw.githubusercontent.com/byte-capsule/FanCode-Hls-Fetcher/main/Fancode_Live.m3u',
    'https://github.com/subirkumarpaul/Subir-Max/raw/master/Discover%20TV',
    'https://github.com/aniketda/iptv2050/raw/main/iptv',
    'https://github.com/Nuttypro69/YouTube_to_m3u/raw/main/youtube.m3u',
    'https://github.com/Maxmentor/JioCinema-M3U-Playlist/raw/main/Jiocinema.m3u',
    'https://tg-aadi.vercel.app/starshare.m3u',
    'https://raw.githubusercontent.com/jack78692/StreamsToM3U8/main/streams.m3u8',
    # Add more URLs here as needed
]

# Initialize combined contents variable
combined_contents = ''

# Loop through each URL
for url in urls:
    try:
        # Fetch the contents of the .m3u8 file
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request failed

        # Append contents to combined contents
        combined_contents += response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")

# Save the combined contents to a local file
combined_filename = 'combined_playlist.m3u8'
with open(combined_filename, 'w') as f:
    f.write(combined_contents)

# Output a message indicating the combined file has been saved
print(f"Combined file saved as: {combined_filename}")
