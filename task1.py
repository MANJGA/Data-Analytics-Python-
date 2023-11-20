import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

columns = ['UserID', 'Country', 'Programming_Lang', 'Years_of_Exp', 'Job_Satisfaction', 'Age', 'Salary', 'Work_Hours', 'Remote_Work', 'Education_Level']
np.random.seed(0)
data = {
    'UserID' np.arange(1, 101),
    'Country' np.random.choice(['USA', 'India', 'Germany', 'Canada', 'UK', 'France', 'Brazil', 'Japan'], 100),
    'Programming_Lang' np.random.choice(['Python', 'Java', 'C++', 'JavaScript', 'C#', 'PHP', 'Ruby'], 100),
    'Years_of_Exp' np.random.choice(['1', '1-2', '3-5', '6-10', '11-20', '20'], 100),
    'Job_Satisfaction' np.random.choice(['Very satisfied', 'Satisfied', 'Neutral', 'Dissatisfied', 'Very dissatisfied'], 100),
    'Age' np.random.randint(18, 60, 100),
    'Salary' np.random.uniform(30000, 150000, 100),
    'Work_Hours' np.random.randint(20, 60, 100),
    'Remote_Work' np.random.choice(['Yes', 'No'], 100),
    'Education_Level' np.random.choice(['High School', 'Bachelor', 'Master', 'PhD', 'None'], 100)
}
survey_df = pd.DataFrame(data, columns=columns)

# გამოიტანთ ცხრილის სასურველ სტრიქონებს და სვეტებს,
extracted_df = survey_df.loc[1020, ['Country', 'Programming_Lang', 'Salary']]

# დაუნიშნეთ ინდექსირება ცხრილის კონკრეტული სვეტის მიმართ;
indexed_df = survey_df.set_index('UserID')

# შექმნით 2 პარამეტრზე დამოკიდებულ ფილტრს.
filtered_df = survey_df[(survey_df['Country'].isin(['USA', 'Canada'])) & (survey_df['Years_of_Exp'] == '10')]

# დაასორტირეთ ცხრილი 2 პარამეტრის გამოყენებით
sorted_df = survey_df.sort_values(by=['Country', 'Salary'])

# გამოიყენეთ კონკრეტული სვეტის მნიშვნელობისთვის სტატისტიკური ფუნქციები
mean_salary = survey_df['Salary'].mean()
std_dev_salary = survey_df['Salary'].std()
median_salary = survey_df['Salary'].median()
min_salary = survey_df['Salary'].min()
max_salary = survey_df['Salary'].max()

# ------------------------
job_satisfaction_counts = survey_df['Job_Satisfaction'].value_counts()
plt.bar(job_satisfaction_counts.index, job_satisfaction_counts.values)
plt.xlabel('Job Satisfaction')
plt.ylabel('Count')
plt.title('Job Satisfaction Bar Chart')
plt.show()

# --------------------------------
plt.plot(survey_df['Age'], survey_df['Salary'], linestyle='-', marker='o')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs. Salary Line Chart')
plt.show()

print(Extracted Datan, extracted_df)
print(nIndexed Datan, indexed_df.head())
print(nFiltered Datan, filtered_df)
print(nSorted Datan, sorted_df.head())
print(nSalary Statistics Mean {.2f}, Std Dev {.2f}, Median {.2f}, Min {.2f}, Max {.2f}.format(mean_salary, std_dev_salary, median_salary, min_salary, max_salary))
