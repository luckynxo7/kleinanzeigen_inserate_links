# Kleinanzeigen Inserate Links Scraper

This project contains a Streamlit web application for extracting all listing URLs (Inserate) from a seller page on Kleinanzeigen (formerly eBay Kleinanzeigen). When you provide the URL of a seller's profile page (e.g. `https://www.kleinanzeigen.de/pro/ff-wheels-by-felgenforum`), the app automatically paginates through all of that seller’s adverts and collects the individual advert links. It then presents the list of URLs in the UI and allows you to download them as a file (text, CSV, Excel or Word).

## Features

- Input a seller page on Kleinanzeigen and scrape all advertisement URLs.
- Automatically navigates through pages using the `?seite` parameter (25 ads per page).
- Uses a polite `User-Agent` header to access the site.
- Presents the results in a table within the Streamlit UI.
- Download the list of URLs in different formats:
  - Plain text (`.txt`)
  - CSV (`.csv`)
  - Excel (`.xlsx`)
  - Word document (`.docx`)

## Requirements

The app depends on the following Python packages (see `requirements.txt` for exact versions):

- streamlit
- requests
- beautifulsoup4
- pandas
- openpyxl (for writing Excel files)
- python-docx (for Word output)

## Running locally

To run the application locally:

1. Clone this repository:
   ```bash
   git clone https://github.com/luckynxo7/kleinanzeigen_inserate_links.git
   cd kleinanzeigen_inserate_links
   ```
2. Install dependencies (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Streamlit app:
   ```bash
   streamlit run kleinanzeigen_scraper/app.py
   ```
4. Open the provided local URL in your browser.

## Usage

- Enter the URL of the seller page (beginning with `https://www.kleinanzeigen.de/pro/`).
- Click “Start Scraping”. The app will fetch each page, parse the advert links and count the total number of adverts.
- Once complete, the links are displayed in a table and can be downloaded.

## Notes

- The app uses simple HTTP requests with a custom `User-Agent`. It does not emulate JavaScript; it relies on the fact that the paginated HTML pages can be accessed with `?seite=1`, `?seite=2`, etc.
- Kleinanzeigen sometimes blocks heavy scraping. Use responsibly and avoid making too many repeated requests.
- If the seller has many adverts (e.g. thousands), scraping may take some time because each page contains 25 adverts.

## License

This project is licensed under the MIT License.
