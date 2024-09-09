# Ejecución de Tests Funcionales - Customer Lifetime Value Prediction

**Paso 0: Ingrese al Escritorio remoto**

**Paso 1: Fork del Repositorio Original**

En el navegador, inicie sesión en Github. Luego, vaya al enlace del proyecto original (https://github.com/ChristianCardenasM/Customer_Lifetime_Value_Prediction), 
hacer click en "Fork" para copiar el proyecto en su usuario de Github.

**Paso 2: Levantar el contenedor de Python**

docker run -it --rm -p 8888:8888 jupyter/scipy-notebook

**Paso 3: Configurar git**

Abra una Terminal en JupyterLab e ingrese los siguientes comandos

git config --global user.name "<USER>"
git config --global user.email <CORREO>

**Paso 4: Clonar el Proyecto desde su propio Github**

git clone https://github.com/<USER>/model-credit.git

**Paso 5: Instalar los pre-requisitos**

cd Customer_Lifetime_Value_Prediction/

pip install -r requirements.txt

**Paso 6: Ejecutar las pruebas en el entorno**

cd src

python mkdata_rfm.py

python model_segment.py

cd ..

**Paso 7: Guardar los cambios en el Repo**

git add .

git config --global user.name <Usuario_Github>

git config --global user.email <User email>

git commit -m "Revisión Finalizada"

git push

Ingrese su usuario y Personal Access Token de Github.

finalizar JupyterLab ("File" => "Shut Down").