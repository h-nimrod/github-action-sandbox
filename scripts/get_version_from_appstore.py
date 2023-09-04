import sys
import requests

def get_app_version(bundle_id, country=None):
    base_url = "https://itunes.apple.com/lookup"
    params = {
        "bundleId": bundle_id,
        "country": country
    }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["resultCount"] == 0:
        print("not found")
        return None
    
    app_info = data["results"][0]
    version = app_info["version"]
    return version


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_version_from_appstore.py.py <app_id>")
        sys.exit(1)

    app_id = sys.argv[1]
    ctr = None
    if len(sys.argv) > 2 and sys.argv[2] != None:
        ctr = sys.argv[2]

    version = get_app_version(app_id, ctr)
    print(version, end="")


