import argparse
import urllib.request
import re
import csv
import datetime

def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        url_data = response.read().decode('utf-8')

    return url_data
"""

"""

def processData(url_data):
    data = url_data.split("\r\n")
    img_hits = total_hits = internet_explorer = mozilla_firefox = google_chrome = apple_safari = 0
    browser_count = {"MSIE": internet_explorer, "Firefox": mozilla_firefox, "Chrome": google_chrome, "Safari": apple_safari}
    hits = {}

    for line in data:
        url_lines = line.split(",")
        if len(url_lines) <5:
            continue
        path = url_lines[0]
        datetime_accessed = url_lines[1]
        browser = url_lines[2]

        total_hits += 1
        if re.search(r"\.(jpg|jpeg|gif|png)$", path, re.I):
            img_hits += 1
        if re.search(r"msie", browser, re.I):
           browser_count["MSIE"] += 1
        elif re.search(r"firefox", browser, re.I):
           browser_count["Firefox"] += 1
        elif re.search(r"chrome", browser, re.I):
           browser_count["Chrome"] += 1
        elif re.search(r"safari", browser, re.I) and not re.search(r"chrome", browser, re.I):
           browser_count["Safari"] += 1

        hour = datetime.datetime.strptime(datetime_accessed, "%Y-%m-%d %H:%M:%S").hour
        if hour in hits:
            hits[hour] += 1
        else:
            hits[hour] = 1

    imagePercent = img_hits / total_hits * 100
    print("Image requests account for {0:0.1f}% of all requests".format(imagePercent))
    popular = max(browser_count, key=browser_count.get)
    print("{} is the most popular browser".format(popular))
    for hour in hits:
        print("Hour {} has {} hits".format(hour, (hits[hour])))

def main(url):
    print(f"Running main with URL = {url}...")
    try:
        weblog = downloadData(url)
        processData(weblog)
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)