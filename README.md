# College Admissions Analysis

- __This project template demonstrates__: linear regression analysis, chi-squared testing, t-test, ROC curve and AUC (Area Under the Curve) to visualize and test my model.

This project examines the most influencial factors when selecting students for admission. This project explores the question: When using ChatGPT for college admissions assistance, does it exhibit demographic biases that illegitimately favor certain groups over others?
The Null Hypotheis: Male Anglo names with a high GPA and high income have a highest chance of admission. 

## Running the project

The process is outlined in with Step 1: Prompt Generator, Step 2: Data Collection, and lastly Step 3: Analysis. 

In Step 1, 33,600 inputs are created to put into OpenAI's model `gpt-4o-mini-2024-07-18`. Here, the different iterations of name, gender, income, and gpa and put together to create several prompts asking ChatGPT if each individual is either accepted, waitlisted, or declined.

Before Step 2, I processed the output of Step 1 into ChatGPT using batchwizard. 

The data cleaning process began in Step 2 by importing collecting the results from ChatGPT into the dataset. 

Step 3 contains the more data clean up, analysis, and the final results.
