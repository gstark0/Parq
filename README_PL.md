# PARQ
#### Sztuczna Inteligencja klasyfikująca miejsca parkingowe na podstawie obrazu z monitoringu.

<img src="https://raw.githubusercontent.com/gstark0/Parq/master/images/logo.png" width="500">

🇺🇸 <a href="https://github.com/gstark0/Parq/blob/master/README_PL.md">Click here to see English readme</a> | 🇵🇱 Polish
### O Projekcie
Główną ideą stojąca za projektem było rozwiązane jednego z najważniejszych problemów, występującego w większości nowoczesnych miast na świecie - problemu związanego z miejscami parkingowymi. Można pomyśleć, że czujniki wykrywające wolne/zajęte miejsca załatwiają sprawę, ale są one często drogie i nieopłacalne. Tymczasem ponad tymi parkingami wiszą kamery z których bardzo często transmitowany jest żywo obraz. To rozwiązane wykorzystuje właśnie te kamery - te, które są otwarte i dostępne do podglądu dla wszystkich.

![](https://raw.githubusercontent.com/gstark0/Parq/master/images/2.png)

### Technologia
W celu rozwiązania tego problemu, PARQ wykorzystuje algorytmy głębokiego uczenia maszynowego - Aplikuje konwolucyjne sieci neuronowe dla każdego miejsca parkingowego dostępnego na obrazie z kamery, dzięki temu jest w stanie przewidzieć z dokładnością 95% (w zależności od kątu kamery), które miejsca są zajęte, a które wolne. Model sieci neuronowej został zaprojektowany dzięki bibliotece Keras (na backendzie TensorFlow) i wytrenowany na danych zdobytych przez pewien okres czasu z dostępnego publcznie monitoringu nad parkingiem centrum handlowego w Inowrocławiu. Serwer działa na bazie Python Flask.

<img src="https://raw.githubusercontent.com/gstark0/Parq/master/images/mobile.png" width="300">

### Aktualny stan prac
Dane o wszystkich miejscach parkingowych są zapisywane w lokalnej bazie danych (aktualizowane są ręcznie, poprzez podstronę /update) i ładowane bezpośrednio z plikami HTML lub są pobierane przez skrypty JS. PARQ może wyświetlać informacje o dokładnym położeniu wolnych miejsc parkingowych w tabelce, tak aby użytkownik był w stanie zobaczyć gdzie dokładnie się znajdują. Wcześniejsza lokalizacja wszystkich miejsc musi najpierw zostać dodadana korzystając ze skryptu `add_spot.py`.

<img alt="Real parking image" src="https://raw.githubusercontent.com/gstark0/Parq/master/images/single_column_real.png" width="300"><img alt="PARQ representation" src="https://raw.githubusercontent.com/gstark0/Parq/master/images/single_column.png" width="300">

### Future
Aktualnie PARQ działa jedynie jako aplikacja internetowa, natomiast w przyszłości zostanie rozbudowana o aplikacje iOS/Android. Oprócz tego, PARQ będzie w stanie automatycznie wykrywać pozycje wszystkich miejsc parkingowych na parkingu (co aktualnie trzeba zrobić ręcznie za pomocą skryptu `add_spot.py`).
