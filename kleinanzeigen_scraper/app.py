"""Streamlit front‑end for the Kleinanzeigen seller scraper.

This module defines the user interface and wiring to call the core
scraper functions. It should be executed by Streamlit, e.g.
`streamlit run app.py`.
"""

import streamlit as st

from .scraper import scrape_seller_listings, create_download_file



def main() -> None:
    st.set_page_config(page_title="Kleinanzeigen Seller Scraper", page_icon="🔗")
    st.title("Kleinanzeigen Seller Listing Extractor")
    st.write(
        "Diese Anwendung sammelt alle Inserat‑Links eines Händlers auf "
        "[Kleinanzeigen](https://www.kleinanzeigen.de). Geben Sie dazu den Link "
        "zur Händlerseite ein (z. B. `https://www.kleinanzeigen.de/pro/ff-wheels-by-felgenforum`)."
    )

    url = st.text_input(
        "Händler‑URL",
        placeholder="https://www.kleinanzeigen.de/pro/...",
        help="Die URL zur pro‑Seite des Händlers."
    )
    file_type = st.selectbox(
        "Dateiformat",
        ["txt", "csv", "xlsx", "docx"],
        index=0,
        help="Wählen Sie das Format für den Download."
    )
    if st.button("Links extrahieren"):
        if not url:
            st.error("Bitte geben Sie eine Händler‑URL ein.")
        else:
            with st.spinner("Verarbeitung läuft …"):
                try:
                    links = scrape_seller_listings(url)
                except Exception as e:
                    st.error(f"Fehler beim Abrufen der Daten: {e}")
                    return
            if not links:
                st.warning("Keine Inserate gefunden.")
            else:
                st.success(f"Es wurden {len(links)} Inserat‑Links gefunden.")
                mime_type, data = create_download_file(links, file_type)
                st.download_button(
                    label=f"{file_type.upper()} herunterladen",
                    data=data,
                    file_name=f"kleinanzeigen_links.{file_type}",
                    mime=mime_type,
                )


if __name__ == "__main__":
    main()
