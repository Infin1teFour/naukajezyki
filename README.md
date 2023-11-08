# Nauka języka fińskiego
Program służy do pomocy w nauce języka fińskiego.
Zawarte są 4 poziomy trudności, każdy działający na innej podstawie.
Program używa integracji z bazą danych sql w której zawarte są wszystkie pytania i odpowiedzi.

# Wymagane Biblioteki
Aby używać tego programu wymagane są następujące biblioteki programu python:
- mysql.connector; aby łączyć z bazą danych,
- Pillow; aby wyświetlać obrazy w łatwym poziomem trudności.

# Poziom łatwy
W poziomie łatwym wyświetla się pewiem obraz, a gracz ma za zadanie wybrać słowo odpowiadające mu z 6 podanych opcji.
Jeśli zostanie wybrana niepoprawna odpowiedź, przycisk zablokuje się i gracz otrzyma drugą szansę na zgadnięcie odpowiedzi.
W tym poziomie użyta jest 1 tabela w bazie danych, o nazwie "poziom1".

# Poziom średni
W tym poziomie gracz podane ma słowo po polsku, i musi wybrać jego fiński odpowiednik.
Tak jak w łatwym poziomie, po wybraniu odpowiedzi niepoprawnej opcja ta się blokuje, i gracz wybiera ponownie.
Użyta jest 2 tabela bazy danych o nazwie "poziom2"

# Poziom średnio-trudny
Gracz ma za zadanie wypełnienie reszty słowa którego podane są jedynie samogłoski. 
W tym poziomie, gracz może popełnić jedynie 3 błędy, po czym pokazuje się komunikat że przegrał i nie może już grać.
Tabela 3 o nazwie "poziom3" jest użyta w tym poziomie.

# Poziom trudny
Poziom trudny polega poprostu na podaniu fińskiej translacji podanego słowa w polu tekstowym pod spodem.
Tak jak w poziomie średnio-trudnym, gracz ma zezwolone tylko 3 błędy, i użyta jest taka sama tabela jak poprzednio.

# Credits
Jan Jakowicki - Programista, menu głowne, poziomy łatwy i średni.
Bastian Wiciński - Programista, poziomy średnio-trudny oraz trudny.
Jakub Dratwa - Testowanie programu.
Gerard Gondek - baza danych oraz grafiki.
Anastasiia Bondarenko - baza danych oraz grafiki.