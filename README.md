# TestowanieOprogramowania
Projekt zaliczeniowy na studiach podyplomowych na kierunku Testowanie Oprogramowania, WSB 2019
# Autor: Maciej Nikonowicz

1. W katalogu "Dokumenty" znajdują się wszystkie dokumenty opisujące przebieg testów - plan testów, raport finalny oraz specyfikacja do każdego etapu testów. Jest tam opisane środowisko testowe oraz wszelkie niezbędne elementy. Sugeruje się zapoznanie z dokumentacją przed uruchamianiem testów.

1. W celu uruchomienia testów API należy zainstalowac SoapUI w wersji 5.5.0 - testy znajdują się w katalogu "API_Test".
Należy zaimportować projekt do programu i uruchomić Test Cases

2. W celu uruchomienia testów automatycznych należy zainstalować Python w wersji 3.7 oraz Selenium 3.14 - testy znajdują się w katalogu "testy automatyczne". Testy najlepiej uruchamiać jeden po drugim, a następnie sprawdzić w konsoli wynik testu oraz w katalogu "screenshots", czy wygenerowały się zrzuty ekranu. 

3. W celu uruchomienia testów wydajnościowych należy posiadać zainstalowane JMeter w wersji 5.1.1 - testy znajdują się w katalogu "jmeter/capybara". Należy otworzyć za pomocą JMeter plik 'capybara.jmx". W katalogu "assertion_responses" znajdują się logi z testów. W katalogu "capybara" znajdują się też pliki .csv z danymi potrzebnymi do poszczególnych testów.

