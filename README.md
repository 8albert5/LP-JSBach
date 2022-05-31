# El Llenguatge de Programació JSBach

> Pràctica de Llenguatges de Programació curs 2021-2022 Q2

Aquesta pàgina descriu la implementació d'un (doble) intèrpret del llenguatge de programació [JSBach](https://github.com/jordi-petit/lp-jsbach-2022).

Per tal de realitzar aquest projecte s'ha utilitzat [ANTLR4](https://www.antlr.org/) per la gramàtica del llenguatge i [Python](https://www.python.org/) per l'intèrpret. El programa [LilyPond](https://lilypond.org/) s'utilitza per crear les partitures en format `pdf` i fitxers `.midi` i els programes [TiMidity++](https://en.wikipedia.org/wiki/TiMidity%2B%2B) i [FFmpeg](https://www.ffmpeg.org/) per generar els fitxers `.wav` i `.mp3`.


## Continguts del directori

Aquest directori conté els seguents fitxers:
- `jsbach.g4` amb la gramàtica del llenguatge.
- `jsbach.py` amb el programa de l'intèrpret.
- `jsbachTreeVisitor.py` amb el visitador/avaluador per recoórrer els ASTs.
- `jsbachScript.py` amb el qual es generaran els fitxers necessaris per obtenir el `.mp3` final.
- `requirements.txt` amb les llibreries utilitzades.
- `template.lily` amb el que es generen els arxius `.lily` de cada programa.
- Aquest `README.md`.
- Fitxers test amb l'extensió `*.jsb`
    - [test-euclides.jsb](test-euclides.jsb) &rarr; Programa que troba el MCD de dos nombres (no genera partitura).
    - [test-fibonacci.jsb](test-fibonacci.jsb) &rarr; Programa que genera la sequència de Fibonacci de n elements (no genera partitura).
    - [test-hanoi.jsb](test-hanoi.jsb) &rarr; Programa que implementa una solució al problema de les Torres de Hanoi (no genera partitura).
    - [test-hanoi-musica.jsb](test-hanoi-musica.jsb) &rarr; Programa que implementa una solució al problema de les Torres de Hanoi i genera una partitura en el procés. Executar amb el procediment `Hanoi`.
    - [test-musica.llull](test-musica.jsb) &rarr; Programa que genera totes les tecles blanques del piano de més greu a més aguda. Executar amb el procediment `Alle_Schlüssel`.


## Requeriments

Aquest programa utilitza l'instal·lador de paquets [pip](https://pip.pypa.io/en/stable/) per instal·lar les llibreries que utilitza el projecte.

```bash
pip install -r requirements.txt
```

## Utilització

Cal executar la següent comanda per generar els lexers, parsers i visitors de la gramàtica.

```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4
```
### Avaluar un programa

Amb el fitxer `jsbach.py` executem un script que avaluarà el codi font del programa que li passem com a paràmetre, amb l'extensió `.jsb`. Per exemple:

```bash
py jsbach.py [nom_fitxer].jsb
```

Si es vol començar des d'un procediment diferent del Main, es pot donar el seu nom com a paràmetre. Per exemple:

```bash
py jsbach.py [nom_fitxer].jsb [nom_procediment]
```
### Generació de fitxers

Amb l'execució del script `jsbach.py` es genera automàticament el fitxer `.lily`, la partitura en `.pdf` i el fitxer `.midi`. Després es generen els fitxers `.wav` i `.mp3`. Finalment amb el programa `ffplay` es reprodueix de manera automàtica l'arxiu `.mp3` resultant.

El script `jsbach.py` està fet de tal manera que si el programa de prova no genera una partitura, és a dir, no utilitza instruccions de reproducció, no es genera cap fitxer `.lily` i per tant, la resta tampoc.

## Aclariments sobre la realització d'aquesta pràctica

