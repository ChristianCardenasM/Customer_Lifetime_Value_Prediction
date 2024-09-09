# Customer Lifetime Value Prediction Project

In this repo, Customer Lifetime Value predicted using probabilistic model BG/NBD and Gamma-Gamma model.

<p style="margin-left: 20px;">Publicación del articulo en medium: 
<a href="https://medium.com/@ugursavci/customer-lifetime-value-prediction-in-python-89e4a50df12e"><i>link-medium</i></a></p>

<p style="margin-left: 20px;">Repositorio en GitHub:
<a ref="https://github.com/ugursavci/Customer_Lifetime_Value_Prediction"><i>link-github</i></a></p>


## Organización del Proyecto

------------

    ├── data
    │   ├── processed         <- Data de frecuancia recencia y value time.
    │   ├── raw               <- Data Original
    │   └── segments          <- Data con los segmentos obtenidos
    │
    ├── models                <- Modelos entrenados
    │
    ├── notebooks             <- Jupyter notebooks
    │
    ├── src                   <- Source code for use in this project.
    │   ├── __init__.py       <- Makes src a Python module
    │   │
    │   ├── mkdata_rfm.py     <- Script de preparación de data
    │   │
    │   ├── model_segment.py  <- Script de segmentación del modelo
    │
    ├── docker_file.md        <- Pasos para clonar y comprobar el proyecto.
    |
    ├── README.md             <- Organización del proyecto
    |
    └── requirements.txt      <- Módulos requeridos: lifetimes


--------