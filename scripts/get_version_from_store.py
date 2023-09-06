"""
This script retrieves the version of an application on the Google Play Store
using the specified application ID.
"""
import sys
from google_play_scraper import app

def get_app_version(application_id):
    """
    Retrieves the current version of the specified application from the Google Play Store.

    Args:
        application_id (str): The ID of the application to retrieve the version information for.

    Returns:
        str: The current version of the application.

    Example:
        >>> get_app_version('com.example.app')
        '1.0.0'
    """
    result = app(application_id, lang='ja', country='jp')
    return result['version']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_version_from_store.py <app_id>")
        sys.exit(1)

    version = get_app_version(sys.argv[1])
    print(version, end="")
