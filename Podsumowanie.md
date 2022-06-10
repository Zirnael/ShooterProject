## Co było zrobione dobrze
* Wszystkie obiekty będące wyświetlana na ekranie dziedziczą po DisplayObject co ułatwia wyświetlanie
* Wszystkie budynki dziedziczą po klasie Building co pozwala traktować je jednakowo. Każdy budynek nadpisuje dwie metody.
  * Metoda update - jest wywoływana w każdej klatce.
  * Metoda interact - jest wywoływana po kolizji gracza z budynkiem

## Co można było zrobić lepiej
* Wszystkie stałe są przechowywane w jednym pliku jako zmienne globalne, przez co zaimportowanie go powoduje zaśmiecenie przestrzeni nazw.
  * Można przemyśleć przechowywanie zmiennych w osobnych plikach
  * Można grupować zmienne podobne - jak zostało to zrobione z kolorami, które są trzymane w klasie Colors.
* Klasa GameEngine została niepotrzebnie rozbudowana o bardzo dużo funkcjonalności
  * Można przenieść kontrolę sterowania do innej klasy
  * Można przenieść budowę budynków do innej klasy
* Zdaje się, że są błędy zaokrągleń przy zmianie liczby klatek, przez co przeciwnicy i gracz poruszają się z inną prędkością.
