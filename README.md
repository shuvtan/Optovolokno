# Анализ рефлектограмм протяженных оптоволоконных сетей

*Ключевые слова: рефлектометрия, одномодовое оптическое волокно, потери в изогнутом волокне, оптические линии, цифровая обработка сигнала*

**Аннотация:**

В настоящее время основная доля магистральных сетей передачи данных построена по
технологии волоконно-оптических линий связи(ВОЛС). С развитием портативной мобильной телефонии и технологий высокоскоростного доступа в Интернет, большая пропускная
способность оптических волокон необходима в 21 веке, в связи с чем значительное внимание уделяется вопросам измерения качества систем передачи и способам их улучшения.

Собраны данные для различных конфигураций оптических линий с помощью рефлектометра Anritsu MT9085A-063-010-037-ES210. Сняты рефлектограммы на длинах волн
1310 и 1550 нм. Проведены измерения потерь в одномодовых оптоволокнах типов SMF
и PCSF. Оценены численно: динамический диапазон рефлектометра, потери мощности на
коннекторах и погонное затухание, потери мощности на изгибах оптоволокна в зависимости от радиуса и угла, мертвые зоны и их зависимость от ширины подаваемого импульса.

На основе экспериментальных данных создан анализатор рефлектограмм, способный
определять следующие параметры: конец линии волокна, количество и координаты соединения катушек, погонные потери волокна. Программа находит предположительные места
соединенния коннектеров и оценивает в них дополнительные потери.

Исследование выполнено при поддержке Кафедры общей физики МФТИ. Авторы благодарят А.Ю. Игуменова за организацию проведения измерений.

**Авторы:** Вазюля Василиса, Сметанина Елена, Шувайникова Татьяна

*МФТИ, Факультет аэрокосмических технологий, май 2023*

# Структура github

Данные измерений рефлектометра: [data-files](https://github.com/shuvtan/Optovolokno/tree/master/data-files)

Код для решения обратной задачи в формате .py: [cod-py](https://github.com/shuvtan/Optovolokno/tree/master/cod-py)

Пример выполнения решения обратной задачи на файле [1310-SMF-SMF-GNUL4-N6.txt](https://github.com/shuvtan/Optovolokno/blob/master/data-files/1310-SMF-SMF-GNUL4-N6.txt) :

[result-gnul-1310-d10-n4.ipynb](https://github.com/shuvtan/Optovolokno/blob/master/result-gnul-1310-d10-n4.ipynb) 

Пример выполнения решения обратной задачи на файле [1550SMF-PSCF.txt](https://github.com/shuvtan/Optovolokno/blob/master/data-files/1550SMF-PSCF.txt) :

[result-1550-SMF-PSCF.ipynb](https://github.com/shuvtan/Optovolokno/blob/master/result-1550-SMF-PSCF.ipynb)


**[Полный текст статьи](https://github.com/shuvtan/Optovolokno/blob/master/analizator-reflectogram.pdf)**

**[Страница на MURZILKA2023](https://easychair.org/conferences/submission?a=30846458;submission=6509756)**
