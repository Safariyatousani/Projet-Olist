# Analyse E-Commerce Olist - Python | SQL | Power BI

## Contexte
Olist est une plateforme e-commerce brésilienne.
Ce projet analyse 96 478 commandes livrées entre 2016 et 2018
afin d'extraire des insights business actionnables.

## Objectifs
- Analyser l'évolution du chiffre d'affaires
- Identifier les catégories et régions les plus performantes
- Comprendre le comportement des délais de livraison
- Segmenter les clients via une analyse RFM

## Stack technique
- **Python** : Pandas, Matplotlib, Seaborn
- **SQL** : SQLite3 (analyses en mémoire)
- **Power BI** : Dashboard interactif 3 pages

## Analyses réalisées
- Exploration des données (EDA) sur 5 tables
- Nettoyage et conversion des types
- Analyse SQL : CA par mois, délais, paiements, catégories
- Segmentation RFM : 5 segments clients identifiés
- Dashboard Power BI : KPIs, géographie, clients

## Résultats clés
| Indicateur | Valeur |
|---|---|
| CA total | 15,42M R$ |
| Panier moyen | 190 R$ |
| Taux de livraison | 97% |
| Champions RFM | 24 022 clients |
| Délai min (SP) | 9 jours |
| Délai max (RR) | 29 jours |

## Structure du projet
```
projet-olist/
├── notebooks/
│   └── analyse_olist.ipynb
├── data/
│   └── exports/
├── visuals/
│   ├── ca_par_mois.png
│   ├── delais_livraison.png
│   ├── modes_paiement.png
│   ├── rfm_segmentation.png
│   └── top_categories.png
└── dashboard_olist.pbix
```

## Liens
- [LinkedIn](www.linkedin.com/in/safariyatouss)
- [GitHub](https://github.com/Safariyatousani)
