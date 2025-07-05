# instalacja środowiska
wchodzisz w **windows store** i pobierasz python
pobierasz **Visual studio code**
otwierasz folder strony w **Visual studio code**

# komendy wpisuje się w zakładce terminal na dole programu
jeśli na dole nie ma terminalu, znajduje się on również na górze programu
klikasz: Terminal/New Terminal

# komenda na pobranie Flask
    pip install Flask

# komenda na uruchomienie środowinka

    python -m venv venv

    . .venv\Scripts\Activate  
albo
    .venv\Scripts\Activate

jeśli po wpisaniu tej komendy wyświetli się błąd, zignoruj to i przejdź do następnej komendy

# komenda na uruchomenie servera:

    python -m flask --app run run --debug  

# aby wyświetlić stronę w przeglądarce wklej ten link

    http://127.0.0.1:5000 

możesz również wejść w link klikająć w niego ctrl + lewy przycisk myszy

# aby dodać nowe produkty lub je usunąć należy

otworzyć poniższy **plik**

    list_of_products.csv 

# przykłady jak należy dodać produkt

jeśli cena ma być wyświetlona w **PLN** w przeliczeniu z **EUR**

    7,nazwa,tytuł,opis produtku,100,,

jesli cena ma być wyświetlona w **PLN** bez przelicznika

    8,nazwa,tytuł,opisproduktu,,100
    
**ważne** co złego to nie ja :)

**ADDEV**
