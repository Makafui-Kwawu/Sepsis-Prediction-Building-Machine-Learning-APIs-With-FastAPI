<a name="readme-top"></a>

<div align="center">
  <h1><b># Sepsis-Prediction-Building-Machine-Learning-APIs-With-FastAPI</b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📗 Table of Contents](#-table-of-contents)
- [Project Description ](#Sepsi-Insights)
  - [🛠 Built with ](#-built-with-)
    - [Tech Stack ](#tech-stack-)
  - [💻 Getting Started ](#-getting-started-)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [👥 Authors ](#-authors-)
  - [🤝 Contributing ](#-contributing-)
  - [⭐️ Show your support ](#️-show-your-support-)
  - [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

# Sepsis Prediction <a name="about-project"></a>

**Sepsis-Prediction: Buiding classification model to predict Sepsis** Sepsis, a life-threatening condition, arises from the body’s exaggerated response to infection. Swift intervention is essential to prevent tissue damage, organ failure, and mortality because septic shock can cause death in as little as 12 hours. Therefore, Prompt diagnosis and treatment significantly enhance survival rates for individuals with mild sepsis. Conversely, without timely intervention, advanced stages of sepsis often prove fatal. Even with optimal care, septic shock—the most critical phase of sepsis—has a mortality rate of 30% to 40%..



1. **ID**: Unique Identifier of patient
2. **PRG(Plasma Glucose)**: Measurement of plasma glucose levels. 
3. **PL(Blood Work Result 1)**: Blood work result in mu U/ml. 
4. **PR(Blood Pressure)**: Measurement of blood pressure in mm Hg.
5. **SK(Blood Work Result 2)**: Blood work result in mm. 
6. **TS(Blood Work Result 3)**: Blood work result in mu U/ml.
7. **M11(Body Mass Index)**: BMI calculated as weight in kg/(height in m)^2
8. **BD2(Blood Work Result 4)**: Blood work result in mu U/ml
9. **Age**: Age of the patient in years. 
10. **Insurance**: Indicates whether the patient holds a valid insurance card.
11. **Sepsis**: Target variable indicating whether the patient will develop sepsis (Positive) or (Negative)


## 🛠 Built With <a name="Technologies Used"></a>
The P5-Sepsis-Prediction Project was done following the CRISP-DM process. It also involved a variety of technologies, programming languages, and libraries to process, analyze, and visualize the data. The following tools were utilized:
1. _Python_: Python programming language was the backbone of the project, used for data processing, analysis, and visualization tasks.

2. _Pandas_ and NumPy: Pandas and NumPy libraries were essential for data manipulation and numerical computations.

3. _Matplotlib and Seaborn_: Matplotlib and Seaborn were employed for data visualization, creating insightful charts and graphs to represent the findings.

4. _Visual Studio Code and Jupyter Notebooks_: Jupyter Notebooks within the Visual Studio IDE provided an interactive environment for running code, visualizing data, and documenting the analysis process.

5. _Scikit-learn_: Scikit-learn's library SimpleImputer was utilized for imputing null values in the amount column.

6. _Streamlit_: Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver interactive data apps – in only a few lines of code.

7. _FastAPI_: is a web framework first released in 2018 for building HTTP-based service APIs in Python. It is used for building APIs with Python 3.8+ based on standard Python-type hints. FastAPI is based on Pydantic and uses type hints to validate, serialize and deserialize data.

8. _Docker_: Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.


9. _GitHub_: GitHub served as the version control system for the project, enabling collaboration and tracking changes in the codebase.
    These technologies played a crucial role in the successful implementation of the project, providing the necessary tools to analyze and derive insights from the Indian Startup Ecosystem funding datasets.

<details>
  <summary>Data Sources</summary>
  <p>The dataset provided for this project is a modified version of a publicly available data source from Johns Hopkins University from Kaggle. It includes various patient attributes and their corresponding sepsis status. The dataset is subject to strict usage restrictions and can only be used for the purpose of this assignment. The data directory consists of both the training and testing data.</p>
</details>


<details>
<summary>Language</summary>
  <ul>
    <li><a href="">Python</a></li>
  </ul>
</details>


<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Success Criteria <a name="key-features"></a>
- Accuracy: The model's should obtain an accuracy of 75% or higher.
- Precision and Recall:The final model should maintain both Precision and Recall scores of 0.75 or above.
- F1 Score: The final model should attain an F1 score of 0.75 to 0.85 or higher according to state-of-the-art SOTA models
Area Under the Receiver Operating Characteristic Curve (AUC-ROC): According to the state-of-the-art SOTA models for sepsis prediction should achieve AUC-ROC scores in the range of 0.80 to 0.90 or higher.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/Makafui-Kwawu/Sepsis-Prediction-Building-Machine-Learning-APIs-With-FastAPI.git
```

Change into the cloned repository

```sh
  cd Sepsis-Prediction-Building-Machine-Learning-APIs-With-FastAPI
  
```

Create a virtual environment

```sh

python -m venv venv

```

Activate the virtual environment

```sh
    env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```

## Running The Docker Images from Dockerhub

To run the Docker images on your local machine, follow these steps.

### Prerequisites

In order to run this project, you need:

- Python installed on your machine

### Steps

1. **Install Docker**

   If you haven't already installed Docker, you can download and install it from the [official Docker website](https://www.docker.com/get-started). Follow the installation instructions specific to your operating system.

2. **Pull the Docker Images**

   Open your terminal or command prompt and pull the required Docker images from Dockerhub using the following commands:

   ``` sh
   docker pull makafuidev/sepsis_fastapi:v1.0
   docker pull makafuidev/sepsis_streamlit:v1

   ```

  ``` sh
   docker run -d --name mycontainer -p 8000:8000 pull makafuidev/sepsis_fastapi:v1.0
   docker run -d --name mycontainer -p 8501:8501 makafuidev/sepsis_streamlit:v1
   ```

### FastAPI backend

[API]()

[FastAPI Image](https://hub.docker.com/r/makafuidev/sepsis_fastapi)

### Streamlit frontend application

[client]()

[Streamlit Image](https://hub.docker.com/r/makafuidev/sepsis_streamlit)   


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

🕵🏽‍♀️ **Success Makafui Kwawu**

- GitHub: [GitHub Profile](https://github.com/Makafui-Kwawu)
- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/smkwawu)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


  
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p style="text-align: right;">
    <a href="https://medium.com/@sm.kwawu/building-machine-learning-apis-with-fastapi-integrating-machine-learning-models-for-sepsis-4b33fe550868">Link to Article</a>
</p>



