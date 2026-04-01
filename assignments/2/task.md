Final project instruction

Deadline: 2 April 2025

Overview
In this project, you will apply the time series forecasting techniques covered in the course to a real-world dataset. You will perform exploratory data analysis, build and evaluate forecasting models, and communicate your findings through a blog post and a well-documented GitHub repository.

Dataset
Choose one of the datasets provided on the course page, or select your own from sources such as UCI Machine Learning Repository or Kaggle Datasets. If you choose your own dataset, make sure it is a time series dataset suitable for forecasting.

Tasks
Your project should include the following:
1.	Exploratory Data Analysis (EDA): Explore and visualize the dataset. Identify trends, patterns, missing values, and outliers.
2.	Time Series Analysis: Check for stationarity (e.g., ADF test) and perform seasonal decomposition to understand the underlying components of the data.
3.	Feature Engineering: If applicable, create relevant features such as lag variables, rolling statistics, or calendar-based features to improve model performance.
4.	Modeling: Choose one or more forecasting methodologies (e.g., ARIMA, Prophet, LSTM, XGBoost, etc.). You may also use AutoGluon if you want to evaluate multiple models in parallel.
5.	Model Evaluation: Select appropriate evaluation metrics (e.g., MAE, RMSE, MAPE) and assess your model’s performance. Compare models if you used more than one.
6.	Forecasting: Generate forecasts and visualize the results, including confidence intervals where applicable.
7.	Blog Post: Write a blog post on Medium where you explain the dataset, the methodology used, your results, and a section discussing the real-world use case or application of your forecast (see Blog Post section below for details).
 

Blog Post
Write a blog post on your personal Medium page. Publishing on your personal profile requires no editorial approval — you write it, hit publish, and it’s live. Your blog should be approximately 1,000–2,000 words and should be written for a general data science audience (not just your instructor).
Your blog post should include:
•	An introduction to the dataset and the problem you are addressing
•	A description of the methodology and models used
•	Key visualizations and results (include charts and plots, not just code)
•	A section on the real-world use case: why does this forecast matter and who could benefit from it?
•	Conclusions and any lessons learned
Tag your post with relevant topics (e.g., “Time Series”, “Data Science”, “Machine Learning”) to improve discoverability.
Here are some examples of good time series blog posts for reference (many more can be found online):
Example1
Example2

Optional: 
If you want to be ambitious, you can also submit your blog post to a publication like Towards Data Science or Analytics Vidhya for wider reach. Note that publications have an editorial review process and may accept, request revisions, or reject your submission, so this should not be your only submission.

Submission
Submit the following on Moodle by the deadline:

1. GitHub Repository Link
Upload your project to your GitHub account and submit the repository link on Moodle. Your repository should include:
•	Your code (Jupyter Notebook and/or Python scripts)
•	A README.md file describing the project, the dataset (with a link to the data source if the dataset is too large to upload), instructions on how to run the code, and any relevant notes
•	A requirements.txt file listing all Python packages and dependencies needed to run your code
Note: Since some datasets are quite large, you do not have to upload the dataset to GitHub. Instead, include a download link or instructions in the README file.

2. Medium Blog Post Link
Submit the link to your published Medium blog post on Moodle.

Grading Criteria
Your project will be evaluated based on the following:
•	Exploratory Data Analysis and Time Series Understanding (15%): Quality and depth of data exploration and visualization, correct application of stationarity tests and seasonal decomposition, and clear interpretation of the time series components.
•	Modeling and Forecasting (40%): Appropriate model selection, implementation, and forecast quality.
•	Model Evaluation (10%): Proper use of evaluation metrics and interpretation of results.
•	Blog Post (25%): Clarity of writing, quality of explanations and visualizations, and discussion of the real-world use case.
•	Code Quality and Repository (10%): Well-organized code, clear documentation, README, and requirements.txt.

Tips
•	Include visualizations in both your notebook and your blog post.
•	Write your blog for a general data science audience, not just your instructor.
•	If you use code or material from tutorials or other sources, do not forget to cite them
•	Have a clean code and well curated GitHub Repository