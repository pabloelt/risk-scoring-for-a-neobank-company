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

The client for this project is a large retailer based in the United States. The company has identified issues in its warehouse operations, leading to losses and stock-outs for several products. The objective is to implement a forecasting model using artificial intelligence algorithms to predict the appropriate stock levels for at least the next 8 days. This initiative aims to enhance operational efficiency and increase the company’s profitability.

 * [See a technical explanation of the project here](https://pabloelt.github.io/project/project7/)

## Objectives

The primary objective is to develop a forecasting model utilizing a set of machine learning algorithms to predict sales for the next 8 days at the store-product level. These algorithms are trained using the extensive three-year history available in the retail company’s SQL database, employing massive modeling techniques to ensure accuracy and reliability.

## Project results

### Recommended actions from EDA

Several insights have been uncovered through the exploratory data analysis. The main actionable initiatives are summarized below.

1. With the current information collected by the company, it is challenging to determine whether intermittent demand is due to stock-outs or simply zero demand for the product. Therefore, it is highly recommended to track warehouse data closely.

2. To optimize sales and reduce warehouse costs, implementing a forecasting model based on machine learning algorithms can be highly effective. A bottom-up approach, starting at the product level, is particularly recommended in this context.

3. Discounts have proven to be quite successful, especially for product 090, which is the top seller. It may be worthwhile to apply this strategy to other products and evaluate the overall impact.

4. Saturdays and Sundays show the highest sales volumes, presenting an opportunity to develop targeted strategies and campaigns.

5. Special days like Thanksgiving, Labor Day, and Easter generate significant sales. These occasions should be thoroughly analyzed, and marketing strategies should be developed to enhance the company’s profitability.


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
