# Cas d'étude complet - Analyse des données du Titanic
## Contexte
Dans ce cas d'étude, nous allons analyser le dataset du Titanic qui contient des informations sur les passagers du célèbre navire. Notre objectif est d'effectuer une analyse approfondie de ces données pour comprendre différents aspects liés aux passagers, tels que leur survie en fonction de divers facteurs, les caractéristiques démographiques, etc.
## Dataset
```python
  from seaborn import load_dataset

  # Charger le dataset "titanic" à partir de Seaborn
  titanic_dataset = load_dataset('titanic')
```
Le dataset "titanic.csv" contient les colonnes suivantes :

- `Survived` : Indique si le passager a survécu (1) ou non (0).
- `Pclass` : Classe du billet (1 = 1ère classe, 2 = 2ème classe, 3 = 3ème classe).
- `Name` : Nom du passager.
- `Sex` : Genre du passager (male ou female).
- `Age` : Âge du passager.
- `SibSp` : Nombre de frères/soeurs ou conjoints à bord.
- `Parch` : Nombre de parents/enfants à bord.
- `Ticket` : Numéro du billet.
- `Fare` : Prix du billet.
- `Cabin` : Numéro de cabine.
- `Embarked` : Port d'embarquement (C = Cherbourg, Q = Queenstown, S = Southampton).

## Travail pratique

Votre tâche consiste à réaliser une analyse approfondie des données du Titanic en implémentant les consignes ci-dessus en utilisant les connaissances acquises dans les modules précédents sur Pandas, NumPy, Matplotlib et Seaborn. Assurez-vous d'explorer en profondeur les différentes caractéristiques des passagers et de présenter les résultats avec des visualisations claires et informatives. Vous pouvez également ajouter des commentaires et des explications pour aider à interpréter les résultats obtenus.
À la fin du travail pratique, vous devriez être en mesure de fournir une analyse détaillée des données des passagers du Titanic, avec des visualisations informatives et des insights pertinents sur les facteurs influençant leur survie. Bonne exploration !

## Consignes
 
1. **Chargement des données :**
Charger le jeu de données `titanic.csv` en utilisant Pandas.
Afficher les premières lignes du jeu de données pour vérifier sa structure. Décrire les données brutes.

2. Nettoyage et préparation des données :
Vérifier s'il y a des valeurs manquantes dans le jeu de données et les traiter si nécessaire.
Explorer et traiter les valeurs aberrantes éventuelles dans les colonnes numériques.
Convertir les colonnes appropriées en format catégorique si nécessaire. 

3. Analyse exploratoire des données avec Pandas et NumPy :
  - Calculer le taux global de survie des passagers du Titanic.
  - Analyser la répartition des passagers par classe (Pclass) et par port d'embarquement (Embarked).
  - Calculer la proportion de passagers masculins et féminins.
  - Identifier la distribution d'âge des passagers et trouver les catégories d'âge les plus représentées. (look `pd.cut()` function with `bins`)

4. Analyse de la survie en fonction de différents facteurs :
  - Analyser la survie en fonction de la classe des billets (Pclass). 
  - Examiner la survie en fonction du genre (Sex) des passagers.
  - Étudier la survie en fonction de l'âge (Age) des passagers.
  - Analyser la survie en fonction du port d'embarquement (Embarked).
  
5. Présentation des résultats avec des visualisations :
  - Créer un diagramme à barres (plt.bar) pour visualiser le taux de survie global.
  - Générer un graphique en barres (plt.bar) pour montrer la répartition des passagers par classe (Pclass) et par port d'embarquement (Embarked). (laisser le pour la fin)
  - Créer un nuage de points (plt.scatter) pour représenter la relation entre l'âge (Age) et le prix du billet (Fare) en fonction de la survie.
  - Produire un diagramme circulaire (Pie chart) pour montrer la proportion de passagers masculins et féminins. [Exemple de diagramme circulaire](https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py)
  
6. Analyse complémentaire (facultative) :
  - Examiner la corrélation entre les différentes caractéristiques des passagers pour identifier les relations significatives.
  - Effectuer une analyse plus approfondie en créant des graphiques supplémentaires pour mettre en évidence des tendances ou des insights intéressants.
