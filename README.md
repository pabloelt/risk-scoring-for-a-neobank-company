# Risk Scoring for a Neobank Company

![featured](https://github.com/pabloelt/risk-scoring-for-a-neobank-company//blob/main/00_Imagenes/featured.jpg?raw=true)

##### Table of Contents 
* [Introduction](#introduction)
* [Objectives](#objectives)
* [Project results](#project-results)
   * [Recommended actions from EDA](#recommended-actions-from-eda)
   * [Risk scoring model](#risk-scoring-model)
   * [Risk scoring analyzer web app](#risk-scoring-analyzer-web-app)
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


### Risk scoring model

In this project, we have developed a risk-scoring model to predict the Expected Loss (EL) associated with a new loan application. To achieve that, three key risk parameters are considered:

* **Probability of Default (PD):** This measures the likelihood that a borrower will default, based on an internally assigned credit rating.
* **Exposure at Default (EAD):** This indicates the amount of outstanding debt at the time of default.
* **Loss Given Default (LGD):** This metric represents the percentage of the loan exposure that is not expected to be recovered if a default occurs.

To estimate these risk parameters, three predictive machine learning models are developed. For the PD model, a logistic regression algorithm is used since high interpretability and auditability are required at this stage in the financial sector. On the other hand, for estimating the EAD and LGD models LightGBM algorithms are finally selected due to their superior performance. The predictions from these models are then combined to calculate the EL for each loan transaction. To calculate this value, the following formula is applied:

$$
EL[\textdollar] = PD \cdot P[\textdollar] \cdot EAD \cdot LDG,
$$

where P is the loan principal, i.e., the amount of money the borrower whises to apply for.

### Risk scoring analyzer web app

To maximize the value of the developed machine learning models, it is essential to seamlessly deploy them into production so that employees can start utilizing them to make informed, practical decisions.

To achieve this, a prototype web application has been designed. This web app gathers internal data from the company for each client, as well as information provided by the borrower through their loan application.

[Launch Risk Scoring Analyzer Web App!](https://risk-scoring-analyzer-web-app.streamlit.app/)

![featured](https://github.com/pabloelt/risk-scoring-for-a-neobank-company//blob/main/00_Imagenes/web_app_1.png?raw=true)

## Project structure

* 📁 00_Imagenes: Contains project images.
* 📁 01_Documentos: Contains basic project files:
  * <mark>Diccionario.xlsx</mark>: Feature-level metadata.
  * <mark>riesgos.yml</mark>: Project environment file.
  * <mark>FaseDesarrollo_Transformaciones.xlsx</mark>: Support file for designing feature transformation processes.
  * <mark>FaseProduccion_Procesos.xlsx</mark>: Support file for designing final production script.
  * <mark>stop_words_english.txt</mark>: Dictionary for the non-relevant words used in the text data analysis (TF-IDF analysis).
* 📁 02_Datos
  * 📁 01_Originales
    * <mark>prestamos.csv</mark>: Original dataset.
  * 📁 02_Validacion
    * <mark>validacion.csv</mark>: Sample extracted from the original dataset at the beginning of the project, which is used to check the correct performance of the model once it is put into production.
  * 📁 03_Trabajo
    * This folder contains the datasets resulting from each of the stages of the project (data quality, exploratory data analysis, variable transformation, ...).
* 📁 03_Notebooks
    * 📁 02_Desarrollo
      * <mark>01_Set Up.ipynb</mark>: Notebook used for the initial set up of the project.
      * <mark>02_Calidad de Datos.ipynb</mark>: Notebook detailing and executing all data quality processes.
      * <mark>03_EDA.ipynb</mark>: Notebook used for the execution of the exploratory data analysis.
      * <mark>04_Transformacion de datos.ipynb</mark>: Notebook that details and executes the data transformation processes necessary to prepare the variables for the models.
      * <mark>05_Modelizacion Clasificacion PD.ipynb</mark>: Notebook used for modeling the predictive Probability of Default model. It contains the model selection, the hyperparametrization, and the evaluation of results.
      * <mark>06_Modelizacion para Regresion EAD.ipynb</mark>: Notebook for modeling the predictive Exposure at Default model. It contains the model selection, the hyperparametrization, and the evaluation of results.
      * <mark>07_Modelizacion para Regresion LGD.ipynb</mark>: Notebook for modeling the predictive Loss Given default model. It contains the model selection, the hyperparametrization, and the evaluation of results.
      * <mark>08_Preparacion del codigo de produccion.ipynb</mark>: Notebook used to compile all the quality, transformation, and variable selection processes, as well as the final model and execution and retraining processes. It is used to create the final retraining and execution pipes that condense all the aforementioned processes.
    * 📁 03_Sistema
      * This folder contains the files (production script, models, functions ...) used in the model's deployment.
      * 📁 app_riesgos
        * This folder contains the app files necessary for the deployment of the web application [Risk Scoring Analyzer](https://risk-scoring-analyzer-web-app.streamlit.app/).    
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

* Project environment can be replicated using the <mark>riesgos.yml</mark> file, which was created during the set up phase of the project. It can be found in the folder <mark>01_Documentos</mark>.
* To replicate the environment it is necessary to copy the <mark>riesgos.yml</mark> file to the directory and use the terminal or anaconda prompt executing:
  * conda env create --file riesgos.yml --name project_name

On the other hand, remember to update the project_path variable of the notebooks to the path where you have replicated the project.
