````markdown
### Retail Sales Forecasting with Prophet

### Project Title
Retail Sales Forecasting and Analysis

---

### Description
This project focuses on providing accurate sales forecasts for a retail business. By leveraging a historical sales dataset of **over 540,000 rows**, the solution performs a series of data cleaning and transformation steps to prepare the data for analysis. The core objective of the project is a time-series forecasting model built with **Facebook's Prophet library**, which predicts future sales to help with inventory management, staffing decisions, and financial planning.

The project demonstrates the ability to manage and process a large dataset for valuable business insights.

---

## Key Features
- **Data Engineering:** An automated ETL (Extract, Transform, Load) pipeline cleans and loads raw CSV data into a MySQL database for structured storage and querying.

- **Exploratory Data Analysis (EDA) & Time-Series Analysis:**The Jupyter Notebook explores key sales metrics, identifies trends, and performs a 7-day rolling average analysis to establish an initial daily prediction baseline before preparing the data for advanced modeling.

- **Time-Series Forecasting:** A Prophet model is built and trained to forecast future sales with high accuracy. The model accounts for seasonality and trend changes within the data.

- **Database Management:** SQL scripts are used to create the database schema and perform complex queries, ensuring data integrity and efficient retrieval.

---




## Technologies Used
- **Programming Language:** Python, SQL
- **Libraries:** Pandas, SQLAlchemy, pymysql, Prophet, Matplotlib
- **Environment:** Jupyter Notebook, PyCharm
- **Database:** MySQL
- **Version Control:** Git, GitHub

---

## Installation
To set up and run this project locally, follow these steps.

### Step 1: Database Setup
1. Navigate to the `SQL` folder.
2. Run the `sales_project.sql` script to create the database and tables.

### Step 2: Download the Dataset
The raw dataset is too large to be included in the repository. Please download it from the following link:

The dataset used for this project is the "E-Commerce Data" dataset, publicly available on Kaggle.

  * **Dataset Link:** [https://www.kaggle.com/datasets/carrie1/ecommerce-data](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

### Step 3: Python Environment
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ollamidee/Retail-Sales-Forecasting-with-Prophet.git](https://github.com/Ollamidee/Retail-Sales-Forecasting-with-Prophet.git)
````

2.  **Navigate to the project directory:**
    ```bash
    cd Retail-Sales-Forecasting-with-Prophet
    ```
3.  **Install the required libraries:**
    ```
    pip install -r requirements.txt
    ```

### Step 4: Database Credentials

For security, this project uses environment variables to store database credentials.

1.  Create a file named `.env` in the root of the project.
2.  Add your credentials in the following format:
    ```text
    MYSQL_USER=your_username
    MYSQL_PASSWORD=your_password
    MYSQL_HOST=localhost
    MYSQL_DB=sales_project
    ```

-----

## How to Use

1.  **Run the ETL Pipeline:**
      - Navigate to the project root directory.
      - Run the `ETL_pipeline.py` script from your terminal to clean and load the data into your MySQL database:
        ```bash
        python ETL_pipeline.py
        ```
2.  **Open the Jupyter Notebook:**
      - Launch Jupyter Notebook from your terminal:
        ```bash
        jupyter notebook
        ```
      - Open `sales_forecasting_analysis.ipynb`.
3.  **Run the Notebook:**
      - Follow the instructions within the notebook to see the data analysis, model training, and sales forecasting steps.

-----

## Project Structure

```text
Retail-Sales-Forecasting-with-Prophet/
├── ETL_pipeline.py
├── sales_forecasting_analysis.ipynb
├── SQL/
│   ├── daily_sales_summary.sql
│   └── sales_project.sql
├── data.csv/
│   ├── data.csv(Download Separately)
├── README.md
├── requirements.txt
└── .gitignore
```

-----

## Challenges & Learnings

This project presented several key challenges that honestly required a professional approach to overcome.

  - **Handling a Large Dataset:** The initial dataset contained over half a million rows, which posed challenges for memory management and processing time. The solution involved using an ETL pipeline to load and process the data incrementally into a database, which was a best practice for handling large-scale data.

  - **Data Inconsistencies:** The raw data contained negative quantities and other inconsistencies that would have skewed the analysis. This was resolved by implementing a robust data cleaning process within the ETL pipeline and using SQL queries to filter out invalid records before the analysis phase.

  -**Understanding Data Volatility:** The raw daily sales data was extremely volatile, with sharp spikes that obscured the underlying trend. To address this, a 7-day rolling average was applied to smooth the data, providing a clearer view of the sales trend and making it easier to identify seasonal patterns for the forecasting model.

  - **Time-Series Modeling:** Selecting an appropriate forecasting model was crucial. Prophet was chosen for its outstanding  ability to handle seasonality and holidays automatically, which is essential for retail data. The key learning was understanding the model's parameters and how to interpret its components to fine-tune the forecast.

  - **Data Security:** Initially, database credentials were hardcoded. A critical learning was to migrate these credentials to a `.env` file or create custom environment variables locally and add this file to `.gitignore`. This was a crucial step for preventing sensitive information from being exposed in a public repository and it was a core practice in learning to be a professional developer.

This project was honestly an incredible learning experience for me that reinforced the importance of a structured data science workflow, from initial data ingestion to final model deployment and documentation.

```
```