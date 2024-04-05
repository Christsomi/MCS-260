import urllib.request

url = "https://docs.python.org/3/library/urllib.request.html#module-urllib.request"

try:

    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')
    
    with open("downloaded.html", "w", encoding='utf-8') as file:
        file.write(html_content)

    print("HTML page downloaded successfully.")

except Exception as e:
    print("An error occurred:", e)
