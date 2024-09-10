# Sales Forecasting for a Retail Company

![featured](https://github.com/pabloelt/risk-scoring-for-a-neobank-company//blob/main/00_Imagenes/featured.jpg?raw=true)

##### Table of Contents 
* [Introduction](#introduction)
* [Objectives](#objectives)
* [Project results](#project-results)
   * [Recommended actions from EDA](#recommended-actions-from-eda)
   * [Sales forecasting model](#sales-forecasting-model)
* [Project structure](#project-structure)
* [Instructions](#instructions)

<div align="justify">
 
## Introduction

The client for this project is a neobank specializing in offering competitively priced loans. However, the company is concerned about the quality of borrowers accessing their products. They require a robust system to assist in making informed loan approval decisions based on applicants’ profiles.

The goal is to implement a risk-scoring model using artificial intelligence algorithms to identify ‘risky’ applicants and estimate their associated expected losses. This information will be used to manage the bank’s economic capital, portfolio, and risk assessment effectively.

 * [See a technical explanation of the project here](https://pabloelt.github.io/project/project7/)

## Objectives

The main objective is to develop a risk-scoring model using machine learning algorithms to predict potentially risky borrowers. This model will estimate the expected financial loss for each new customer-loan pairing, based on the company’s historical data. By leveraging this advanced analytical tool, the company’s performance will be significantly enhanced.

## Project results

### Recommended actions from EDA

Several insights have been uncovered through the exploratory data analysis. The main actionable initiatives are summarized below.

1. Credit scores appear to be effective in identifying high-quality borrowers. These profiles should be targeted for promotion, and a broader range of products, such as investment opportunities, stocks, and index funds, could be offered to them.

2. The job title category needs improvement to provide more accurate information, which will be beneficial for the development of the machine learning algorithms.

3. Since three main borrower profiles have been identified based on credit card usage, targeted campaigns can be developed for each group. Customized products or loans tailored to their specific needs could be offered to them.

4. According to the company’s historical data, 30-month loans are performing better. These should be promoted, and additional products in this category could be considered.


### Sales forecasting model

In this project, we have developed a robust recursive forecasting model based on a set of machine learning algorithms for sales prediction. This model analyzes each product-store combination individually and tailors the algorithm to predict demand for the next 8 days. LightGBM, with standard hyperparameters, was identified as the best option for predictive performance. The model was tested with new data from December 2015, yielding satisfactory results, with a mean absolute error of approximately 4.73.

This forecasting model will help to reduce warehouse costs and stock-outs, significantly boosting the company's performance and profitability.


## Project structure

* 📁 00_Imagenes: Contains project images.
* 📁 01_Documentos: Contains basic project files:
  * <mark>retail.yml</mark>: Project environment file.
  * <mark>FaseDesarrollo_Transformaciones.xlsx</mark>: Support file for designing feature transformation processes.
  * <mark>FaseProduccion_Procesos.xlsx</mark>: Support file for designing final production script.
* 📁 02_Datos
  * 📁 01_Originales
    * <mark>hipermercado.db</mark>: Original SQL dataset.
  * 📁 02_Validacion
    * <mark>validacion.csv</mark>: Sample extracted from the original dataset at the beginning of the project, which is used to check the correct performance of the model once it is put into production.
    * <mark>DatosParaProduccion.csv</mark>: Support file for the execution of the recursive forecasting model. It also shows the required structure for the files that are passed to the forecasting model.
  * 📁 03_Trabajo
    * This folder contains the datasets resulting from each of the stages of the project (data quality, exploratory data analysis, variable transformation, ...).
* 📁 03_Notebooks
  * 📁 01_Funciones
      * <mark>FuncionesRetail.ipynb</mark>: Notebook containing all custom functions used in the training and production of the model.
    * 📁 02_Desarrollo
      * <mark>01_Set Up.ipynb</mark>: Notebook used for the initial set up of the project.
      * <mark>02_Calidad de Datos.ipynb</mark>: Notebook detailing and executing all data quality processes.
      * <mark>03_EDA.ipynb</mark>: Notebook used for the execution of the exploratory data analysis.
      * <mark>04_Transformacion de datos.ipynb</mark>: Notebook that details and executes the data transformation processes necessary to prepare the variables for the models.
      * <mark>05_Preseleccion de variables.ipynb</mark>: Notebook used for the variable selection process.
      * <mark>06_Modelizacion para Regresion.ipynb</mark>: Notebook for modeling the predictive forecasting model. It contains the model selection, the hyperparametrization, the selection of the optimal discrimination threshold, and the evaluation of results. Both individual and massive modeling are also developed in this notebook.
      * <mark>07_Preparacion del codigo de produccion.ipynb</mark>: Notebook used to compile all the quality, transformation, and variable selection processes, as well as the final model and execution and retraining processes. It is used to create the final retraining and execution pipes that condense all the aforementioned processes.
      * 📁 03_Sistema
      * This folder contains the files (app script, production script, models, functions ...) used in the model's deployment. 
* 📁 04_Modelos
  * <mark>lista_modelos_retail.pickle</mark>: File containing all of the developed models for each product-store combination.
  * <mark>ohe_retail.pickle</mark>: File containing the one hot encoding pipe.
  * <mark>te_retail.pickle</mark>: File containing the target encoding pipe.
* 📁 05_Resultados
  * <mark>FuncionesRetail.py</mark>: Python script that contains all custom functions needed when training or executing the model.
  * <mark>Codigo de ejecucion.py</mark>: Python script to execute the model and obtain the results.
  * <mark>Codigo de reentrenamiento.py</mark>: Python script to retrain the model with new data when necessary.
  * <mark>lista_modelos_retail.pickle</mark>: File containing all of the developed models for each product-store combination.
  * <mark>variables_finales.pickle</mark>: Names of the final selected variables after training.

## Instructions

The project should be run using the same environment in which it was created.

* Project environment can be replicated using the <mark>retail.yml</mark> file, which was created during the set up phase of the project. It can be found in the folder <mark>01_Documentos</mark>.
* To replicate the environment it is necessary to copy the <mark>retail.yml</mark> file to the directory and use the terminal or anaconda prompt executing:
  * conda env create --file leadscoring.yml --name project_name

On the other hand, remember to update the project_path variable of the notebooks to the path where you have replicated the project.
