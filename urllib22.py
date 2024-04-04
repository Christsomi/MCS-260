import urllib.request

def download_html(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            return html_content.decode('utf-8')  
    except Exception as e:
        print("Error occurred while downloading:", e)
        return None

def main():
    url = "https://example.com"

    html_content = download_html(url)
    
    if html_content:
        print(html_content)

if __name__ == "__main__":
    main()
