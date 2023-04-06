# LAIMAT-API

## Introduction

Une API construite sur la méthode du [TDD](https://fr.wikipedia.org/wiki/Test_driven_development), réalisée avec le microframework [Flask](https://flask.palletsprojects.com/en/2.2.x/).

## Installation

Installez les packages nécessaires avec la commande suivante :
```bash
pip install -r requirements.txt
```

## Endpoints

La gravité est définie par défaut à 9.81 m/s² sauf si vous la surchargez.

```
/hypotenuse
/hypotenuse?a=3&b=4
/speed
/speed?gravity=9.81&height=100
/speed?height=100
```

## Formules
Calcul d'une hypothénuse avec 2 longueurs
```
AB² + BC² = AC²
```

Calcul d'une vitesse d'après une hauteur
```
V = sqrt(2 gh)
```