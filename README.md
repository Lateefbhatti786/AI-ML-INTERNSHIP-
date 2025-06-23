Titanic Dataset - Data Cleaning and Preprocessing/ ElevateLabs Internship Task 1
This project is a part of my AI & ML Internship at ElevateLabs. It involves cleaning and preprocessing the Titanic dataset to prepare it for machine learning applications. The workflow includes handling missing values, encoding categorical features, normalizing numerical columns, and visualizing data distributions and outliers using Python libraries such as Pandas, NumPy, Seaborn, and Scikit-learn.

📁 Dataset
Dataset used: Titanic Dataset from Kaggle

🛠️ Tools & Libraries Used
Python
Pandas
NumPy
Seaborn
Matplotlib
Scikit-learn (StandardScaler)

📌 Task Objectives
Explore and understand the raw dataset
Handle missing values
Convert categorical features into numerical form
Normalize/standardize the data
Visualize distributions and outliers

✅ Steps Performed
1. Data Loading
Loaded the dataset using Pandas.
Displayed the first few rows for overview.
2. Data Exploration
Checked dataset info and types using .info().
Visualized missing values using a heatmap.
3. Handling Missing Values
Filled missing values in:
Age using median
Embarked using mode
Dropped the Cabin column due to excessive nulls.
4. Encoding Categorical Variables
Converted Sex and Embarked into numerical form using one-hot encoding.
5. Feature Scaling
Scaled Age and Fare using StandardScaler from sklearn.
6. Data Visualization
Created a KDE-enhanced histogram of the Fare column.
Added a mean line and grid for better interpretation.
7. Data Export
Saved the final cleaned dataset as cleaned_titanic.csv.

📊 Visualizations Included
🔥 Heatmap of missing values
📈 Histogram with KDE and mean line for Fare

📂 Output Files
cleaned_titanic.csv – Cleaned and processed dataset ready for modeling.

📚 Learning Outcomes
Practical hands-on with data wrangling
Experience with encoding, scaling, and visualization
Improved understanding of how preprocessing impacts machine learning pipelines

🌐 Submission
This task was submitted as part of Task 1 – Data Cleaning & Preprocessing under the AI & ML Internship Program at ElevateLabs.

🤝 Connect
Feel free to connect with me on https://www.linkedin.com/in/abdul-lateef-ai/ or reach out if you have questions about this project.
