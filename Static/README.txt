# Biblioteka Książek

## Opis projektu
Aplikacja webowa pozwalająca na zarządzanie listą książek – dodawanie, edycję, usuwanie oraz sortowanie według autora lub oceny.

## Technologie
- Python (Flask)
- HTML, CSS
- JSON (przechowywanie danych)

## Instalacja
1. Pobierz projekt.
2. Zainstaluj wymagane biblioteki:
pip install -r requirements.txt 

3. Uruchom aplikację:
-python app.py 

## Funkcje
- Dodawanie nowych książek 
- Edycja istniejących wpisów
- Usuwanie kisążek 
- Sortowanie wg autora lub oceny 

##Struktura pliów 
biblioteka/ 
│── app.py # Główna aplikacja Flask 
│── models.py # Obsługa danych o książkach 
│── forms.py # Formularz dodawania książek 
│── static/ │ 
    ├── styles.css # Plik CSS 
│── templates/ │ 
    ├── index.html # Strona główna  
    ├── todos.html # Dodawanie i usuwanie książek  
    ├── todo.html # Edycja książek
│── todos.json # Plik z zapisanymi książkami 
│── requirements.txt # Bilioteki do zainstalowania aby program działał

│── README.txt # Dokumentacja projektu


##Autor 
Marek Swachta
