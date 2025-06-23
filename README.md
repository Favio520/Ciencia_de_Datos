Ejecucion del proyecto:

Para la ejecucion del proyecto tenemos dos alternativas ejecutar cada notebook por separado o ejecutar todo en conjunto a continuacion se explicara cada una de estas:

Ejecucion por SeleccionModelos.py

Abrimos mediante algun IDE o editor de codigo con soporte de codigo python
Le instalamos las siguientes librerias en caso de no contar con las mismas:

!pip install pandas numpy matplotlib seaborn statsmodels scikit-learn prophet tensorflow keras-tuner

![image](https://github.com/user-attachments/assets/37402a8d-199d-4a22-8876-82c593fab49c)

una vez en el menu podemos elegir cualquier modelo o todos de los cuales nos entregara el mejor resultado de dicho modelo 

Ejecucion mediante Notebooks .ipynb

Para el notebook de los modelos tipo ARIMA:
!pip install pandas numpy matplotlib seaborn statsmodels scikit-learn
Para el notebook de los modelos tipo LSTM:
!pip install pandas numpy matplotlib seaborn statsmodels scikit-learn tensorflow keras-tuner
Para el notebook de los modelos tipo PROPHET:
!pip install pandas numpy prophet scikit-learn matplotlib seaborn statsmodels
En el caso de no usar anaconda instalar (install -c conda-forge prophet)

Todos los modelos se encuentran desarrollados en notebooks y para ejecutarlos podemos hacer uso de alguna herramienta como jupyter notebook o google colab 
Estos modelos se encuentran divididos por la metodologia CRISP-DM por lo que se encuentran separados por diferentes partes.

![image](https://github.com/user-attachments/assets/829d0286-2099-48b6-8801-ee72566bd9e9)

