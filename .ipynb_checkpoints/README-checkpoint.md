# Customer Lifetime Value Prediction Project

In this repo, Customer Lifetime Value predicted using probabilistic model BG/NBD and Gamma-Gamma model.

Publicación del articulo en medium: 
<a href="https://medium.com/@ugursavci/customer-lifetime-value-prediction-in-python-89e4a50df12e">link</a>

Repositorio en GitHub:
<a ref="https://github.com/ugursavci/Customer_Lifetime_Value_Prediction">link en github</a>

├── data

|   ├── processed

|   ├── raw

|   ├── segments

|

├── models

├── notebooks

|   

├── src

├── LICENSE

├── README.md          <- The top-level README for developers using this project.

├── data

│   ├── scores         <- Results from scoring model.

│   ├── processed      <- The final, canonical data sets for modeling.

│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── make_dataset.py<- Script to prepare data
│   │
│   ├── train.py       <- Script to train models
│   │                    
│   ├── evaluate.py    <- Script to evaluate models using kpi's
│   │
│   └── predict.py     <- Script to use trained models to make predictions
│
└── LICENSE            <- License