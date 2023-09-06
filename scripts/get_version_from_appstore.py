"""
fetch the current version of an app from the App Store using its bundle ID. 
"""

import sys
import requests

def get_app_version(bundle_id, country=None):
    """
    This function retrieves the version of an app from the App Store using its bundle ID.

    Parameters:
    bundle_id (str): The bundle ID of the app.
    country (str, optional): The country code to specify the country's App Store to search in.
    """

    base_url = "https://itunes.apple.com/lookup"
    params = {
        "bundleId": bundle_id,
        "country": country
    }

    response = requests.get(base_url, params=params, timeout=(10.0, 10.0))
    data = response.json()

    if data["resultCount"] == 0:
        print("not found")
        return None

    app_info = data["results"][0]
    return app_info["version"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_version_from_appstore.py.py <app_id>")
        sys.exit(1)

    APP_ID = sys.argv[1]
    COUNTRY_CODE = None
    if len(sys.argv) > 2 and sys.argv[2] is not None:
        ctr = sys.argv[2]

    version = get_app_version(APP_ID, COUNTRY_CODE)
    print(version, end="")
