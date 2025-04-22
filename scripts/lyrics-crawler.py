import requests
from bs4 import BeautifulSoup
import time
import csv
import os

BASE_URL = "https://www.cmtv.com.ar"

def get_soup(url):
    response = requests.get(url)
    time.sleep(1)
    return BeautifulSoup(response.text, "html.parser")

def get_all_album_links(artist_url):
    soup = get_soup(artist_url)
    album_links = []
    for link in soup.select("a"):
        href = link.get("href", "")
        if "discos_letras/show.php?" in href and "disco=" in href:
            album_links.append(BASE_URL + href)
    return list(set(album_links))

def get_song_links_from_album(album_url):
    soup = get_soup(album_url)
    song_links = []
    for link in soup.select("a"):
        href = link.get("href", "")
        if "discos_letras/letra.php?" in href and "tema=" in href:
            song_links.append(BASE_URL + href)
    return song_links

def get_lyrics(song_url):
    soup = get_soup(song_url)
    
    # Obtener título de canción
    title_tag = soup.find("h4", class_="letra")
    title = title_tag.get_text(strip=True) if title_tag else "sin_titulo"
    title = title.split(maxsplit=1)[-1]  # Quita número de track si aparece (ej: "1 GOOD SHOW" → "GOOD SHOW")
    
    # Buscar letra
    candidates = soup.find_all("div", class_="col-sm-6 col-md-6")
    for div in candidates:
        if not div.find("figure"):
            p = div.find("p")
            if p:
                versos = [line.strip() for line in p.get_text(separator="\n").split("\n") if line.strip()]
                return title, versos

    return title, []

# Configurar archivo CSV
csv_filename = "letras_charly.csv"
with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["verso", "cancion"])

    # Empieza el crawling
    artist_url = "https://www.cmtv.com.ar/discos_letras/show.php?bnid=122&banda=Charly_Garcia&DS_DS=25127&disco=LA_LOGICA_DEL_ESCORPION"
    album_links = get_all_album_links(artist_url)
    print(f"Encontrados {len(album_links)} discos.")

    for album in album_links:
        print(f"\nEntrando al álbum: {album}")
        song_links = get_song_links_from_album(album)
        print(f"{len(song_links)} canciones encontradas.")

        for song in song_links:
            print(f"  Descargando letra: {song}")
            title, lyrics = get_lyrics(song)
            if lyrics:
                for line in lyrics:
                    writer.writerow([line, title])
                print(f"    ✓ Letra de '{title}' guardada con {len(lyrics)} versos.")
            else:
                print(f"    ✗ No se encontró letra para '{title}'.")

