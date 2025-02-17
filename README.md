### Igor Studziński


# Gra Sudoku

Pythonowa implementacja klasycznej gry Sudoku z graficznym interfejsem użytkownika opartym na Pygame.

## Funkcje

- Interaktywna plansza Sudoku z możliwością klikania na pola
- System wprowadzania liczb za pomocą przycisków
- Różne poziomy trudności
- System żyć
- Zarządzanie stanem gry (ekran startowy, rozgrywka, ekran końcowy)
- Funkcje resetowania i wychodzenia z gry
- Wizualna informacja zwrotna dla zdarzeń w grze

## Wymagania

```
pygame>=2.5.0
```

## Struktura projektu

Gra składa się z kilku modułów Pythona:

- `main.py` – Główny plik gry, pętla gry i inicjalizacja
- `grid.py` – Implementacja planszy Sudoku oraz ekranu końcowego
- `algoritm.py` – Generowanie i rozwiązywanie Sudoku
- `button.py` – Implementacja przycisków UI
- `hearts.py` – System żyć
- `startscreen.py` – Ekran startowy
- `messagedisplay.py` – System wyświetlania wiadomości w grze

## Wymagane zasoby

Gra wymaga następujących folderów z zasobami:

- `Numbers/` – Zawiera obrazy liczb (`1.png` do `9.png`)
- `Buttons/` – Zawiera obrazy przycisków (`start.png`, `exit.png`)

## Jak uruchomić

### Instalacja wymaganych bibiotek:

```bash
pip install -r requirements.txt
```


### Uruchomienie gry:

```bash
python main.py
```

## Sterowanie

- **Lewy przycisk myszy**:
  - Wybieranie pól na planszy
  - Wybieranie liczb z panelu numerycznego
  - Interakcja z przyciskami UI

- **Przycisk "Start"** – Resetuje bieżącą grę
- **Przycisk "Exit"** – Powrót do ekranu startowego

