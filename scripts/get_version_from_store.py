import sys
from google_play_scraper import app

def get_app_version(app_id):
    result = app(app_id, lang='ja', country='jp')
    return result['version']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <app_id>")
        sys.exit(1)

    app_id = sys.argv[1]
    version = get_app_version(app_id)
    print(version, end="")


