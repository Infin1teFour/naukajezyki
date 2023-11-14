# Nauka języka fińskiego
Program służy do pomocy w nauce języka fińskiego. <br>
Zawarte są 4 poziomy trudności, każdy działający na innej podstawie. <br>
Program używa integracji z bazą danych sql w której zawarte są wszystkie pytania i odpowiedzi. <br>

# Wymagane Biblioteki
Aby używać tego programu wymagane są następujące biblioteki programu python: <br>
- mysql.connector; aby łączyć z bazą danych, <br> 
- Pillow; aby wyświetlać obrazy w łatwym poziomem trudności. <br>

# Poziom łatwy
W poziomie łatwym wyświetla się pewiem obraz, a gracz ma za zadanie wybrać słowo odpowiadające mu z 6 podanych opcji. <br>
Jeśli zostanie wybrana niepoprawna odpowiedź, przycisk zablokuje się i gracz otrzyma drugą szansę na zgadnięcie odpowiedzi. <br>
W tym poziomie użyta jest 1 tabela w bazie danych, o nazwie "poziom1". <br>

# Poziom średni
W tym poziomie gracz podane ma słowo po polsku, i musi wybrać jego fiński odpowiednik. <br>
Tak jak w łatwym poziomie, po wybraniu odpowiedzi niepoprawnej opcja ta się blokuje, i gracz wybiera ponownie. <br>
Użyta jest 2 tabela bazy danych o nazwie "poziom2". <br>

# Poziom średnio-trudny
Gracz ma za zadanie wypełnienie reszty słowa którego podane są jedynie samogłoski. <br>
W tym poziomie, gracz może popełnić jedynie 3 błędy, po czym pokazuje się komunikat że przegrał i nie może już grać. <br>
Tabela 3 o nazwie "poziom3" jest użyta w tym poziomie. <br>

# Poziom trudny
Poziom trudny polega poprostu na podaniu fińskiej translacji podanego słowa w polu tekstowym pod spodem. <br>
Tak jak w poziomie średnio-trudnym, gracz ma zezwolone tylko 3 błędy, i użyta jest taka sama tabela jak poprzednio. <br>

# Credits
Jan Jakowicki - Programista, menu głowne, poziomy łatwy i średni. <br>
Bastian Wiciński - Programista, poziomy średnio-trudny oraz trudny. <br>
Jakub Dratwa - Testowanie programu. <br>
Gerard Gondek - grafiki. <br>
Anastasiia Bondarenko - baza danych. <br>






























