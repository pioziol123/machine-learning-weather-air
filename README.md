# Implementacja modelu uczenia maszynowego który na podstawie historycznych zestawień warunków atmosferycznych z poziomem zanieczyszczenia powietrza oraz przewidywanych warunków atmosferycznych na najbliższe dni przewiduje możliwy poziom zanieczyszczenia powietrza.
Projekt zakłada powiązanie pomiędzy warunkami atmosferycznymi, a poziomem zanieczyszczenia powietrza dla miasta Poznań.
Źródłem danych dla modelu są strony: www.weather.com (dla danych pogodowych) oraz www.aqicn.org (dla danych o zanieczyszczeniu powietrza). Model przewiduje poziom jednego z czynników zanieczyszczenia powietrza - pyłów zawieszonych PM 2.5.
Wyniku analizy korelacji danych pogodowych i poziomu PM 2.5 stwierdziłem występowanie wysokiej korelacji ujemnej z poziomem wilgotności względnej powietrza (-0,69) oraz prędkością wiatru (-0,45).
Z powodu drastycznie małej ilości danych treningowych model cechuje się niską skutecznośćią przewidywania poziomu zanieczysczeń (Rmse powyżej 500). Dodatkowo na niską przewidywalność modelu wpływa brak ujęcia temperatury powietrza w danych treningowych. Brak temperatury spowodowany jest umieszczeniem danych na stronie pogodowej (pd.read_html nie jest w stanie jej pobrać). Rozwiązaniem jest użycie bilbioteki scrapy i przy jej pomocy ręczne parsowanie kodu html strony. Przewiduję, że wraz ze zwiększeniem się ilości danych model stanie się bardziej skuteczny.
