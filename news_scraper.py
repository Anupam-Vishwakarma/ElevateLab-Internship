import requests
from bs4 import BeautifulSoup

def fetch_headlines(url, output_file="headlines.txt"):
    try:
        # Step 1: Send GET request with User-Agent
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # Step 2: Check status code
        if response.status_code != 200:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
            return

        # Step 3: Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 4: Find all <h2> or title tags
        headlines = soup.find_all("h2")  # change tag if needed

        # Step 5: Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            for idx, headline in enumerate(headlines, 1):
                text = headline.get_text(strip=True)
                if text:  # avoid empty headlines
                    f.write(f"{idx}. {text}\n")

        print(f"Headlines saved to {output_file}")

    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    url = "https://www.bbc.com/news"  # Example site
    fetch_headlines(url)
