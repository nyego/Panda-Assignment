
# coding: utf-8

# # PyCity Schools Analysis
# 
# * As a whole, schools with higher budgets, did not yield better test results. By contrast, schools with higher spending per student actually (\$645-675) underperformed compared to schools with smaller budgets (<\$585 per student).
# 
# * As a whole, smaller and medium sized schools dramatically out-performed large sized schools on passing math performances (89-91% passing vs 67%).
# 
# * As a whole, charter schools out-performed the public district schools across all metrics. However, more analysis will be required to glean if the effect is due to school practices or the fact that charter schools tend to serve smaller student populations per school. 
# ---

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[4]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])


# ## District Summary
# 
# * Calculate the total number of schools
# 
# * Calculate the total number of students
# 
# * Calculate the total budget
# 
# * Calculate the average math score 
# 
# * Calculate the average reading score
# 
# * Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
# 
# * Calculate the percentage of students with a passing math score (70 or greater)
# 
# * Calculate the percentage of students with a passing reading score (70 or greater)
# 
# * Create a dataframe to hold the above results
# 
# * Optional: give the displayed data cleaner formatting

# In[5]:


#Calculate the Total no. of Schools
total_schools = school_data["School ID"].count()
total_schools


# In[6]:


#Calculate the Total no. of Students
total_students = student_data["Student ID"].count()
total_students


# In[7]:


# Calculate the Total Budget
total_budget = school_data["budget"].sum()
total_budget


# In[8]:


# Calculate the Average Math Score
district_avg_math_score = student_data["math_score"].mean()
district_avg_math_score                                           


# In[9]:


# Calculate the Average Reading Score
district_avg_reading_score = student_data["reading_score"].mean()
district_avg_reading_score


# In[10]:


# Calculate the % Passing Math
district_passing_math_count = (student_data.loc[student_data["math_score"]>70]).count()["student_name"]
district_passing_math_percentage = district_passing_math_count / total_students * 100 
district_passing_math_percentage


# In[11]:


# Calculate the % Passing Reading
district_passing_reading_count = (student_data.loc[student_data["reading_score"]>70]).count()["student_name"]
district_passing_reading_percentage = district_passing_reading_count / total_students * 100
district_passing_reading_percentage


# In[12]:


# Calculate the Overall Passing Rate
district_overall_passing_rate = (district_passing_math_percentage + district_passing_reading_percentage) / 2
district_overall_passing_rate


# In[13]:


# Calculate the Summary for the District
district_summary = pd.DataFrame({"Total Schools": [total_schools],
                                "Total Students": [total_students],
                                "Total Budgets": [total_budget],
                                "Average Math Score": [district_avg_math_score],
                                "Average Reading Score": [district_avg_reading_score],
                                "% Passing Math": [district_passing_math_percentage],
                                "% Passing Reading": [district_passing_reading_percentage],
                                "Overall Passing Rate": [district_overall_passing_rate]})
district_summary = district_summary[["Total Schools",
                                    "Total Students",
                                    "Total Budgets",
                                    "Average Math Score",
                                    "Average Reading Score",
                                    "% Passing Math",
                                    "% Passing Reading",
                                    "Overall Passing Rate"]]
district_summary



# ## School Summary

# * Create an overview table that summarizes key metrics about each school, including:
#   * School Name
#   * School Type
#   * Total Students
#   * Total School Budget
#   * Per Student Budget
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)
#   
# * Create a dataframe to hold the above results

# ## Top Performing Schools (By Passing Rate)

# * Sort and display the top five schools in overall passing rate

# In[14]:


# School Name
schoolsum_school_type = school_data.set_index(["school_name"])["type"]
schoolsum_school_type


# In[15]:


# Total Students per School
schoolsum_total_students = student_data["school_name"].value_counts()
schoolsum_total_students


# In[16]:


# Total School Budget
schoolsum_total_budget = school_data["budget"].sum()
schoolsum_total_budget


# In[34]:


# Per School Budget
ss_total_school_budget = school_data.groupby(["school_name"]).sum()["budget"]
ss_total_school_budget


# In[18]:


# Average Math Score per School
schoolsum_avg_math_score = student_data.groupby(["school_name"]).mean()["math_score"]
schoolsum_avg_math_score


# In[57]:


# Calculate the Average Reading Score per School
schoolsum_avg_reading_score = student_data.groupby(["school_name"]).mean()["reading_score"]
schoolsum_avg_reading_score


# In[58]:


# % Passing Math per School
schoolsum_passing_math = student_data[(student_data["math_score"] >70)]
schoolsum_passing_math_list = schoolsum_passing_math.groupby(["school_name"]).count()["student_name"] / 100
schoolsum_total_students * 100
schoolsum_passing_math_list


# In[64]:


# % Passing Reading per School
schoolsum_passing_reading = student_data[(student_data["reading_score"] >70)]
schoolsum_passing_reading_percentage = schoolsum_passing_reading.groupby(["school_name"]).count()["student_name"] / 100
schoolsum_total_students * 100
schoolsum_passing_reading_list


# In[65]:


# Overall Passing Rate per School
schoolsum_overall_passing_rate = (schoolsum_passing_math_list + schoolsum_passing_reading_list) 
schoolsum_overall_passing_rate


# In[67]:


# Calculate the School Summary
school_summary = pd.DataFrame({"School Type": [schoolsum_school_type],
                                "Total Students": [schoolsum_total_students],
                                "Total Budgets": [schoolsum_total_budget],
                                "Average Math Score": [schoolsum_avg_math_score],
                                "Average Reading Score": [schoolsum_avg_reading_score],
                                "% Passing Math": [schoolsum_passing_math_percentage],
                                "% Passing Reading": [schoolsum_passing_reading_percentage],
                                "Overall Passing Rate": [schoolsum_overall_passing_rate]})

school_summary = school_summary[["School Type",
                                    "Total Students",
                                    "Total Budgets",
                                    "Average Math Score",
                                    "Average Reading Score",
                                    "% Passing Math",
                                    "% Passing Reading",
                                    "Overall Passing Rate"]]
school_summary


# ## Bottom Performing Schools (By Passing Rate)

# * Sort and display the five worst-performing schools

# In[68]:


bottom_performing_schools = school_summary.sort_values(["Overall Passing Rate"],
ascending=True)
bottom_performing_schools.head()


# ## Math Scores by Grade

# * Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# 
#   * Create a pandas series for each grade. Hint: use a conditional statement.
#   
#   * Group each series by school
#   
#   * Combine the series into a dataframe
#   
#   * Optional: give the displayed data cleaner formatting

# In[74]:


# Calculate the Math Scores by Grade

nineth_grade = student_data[(student_data["grade"] == "9th")]
tenth_grade = student_data[(student_data["grade"] == "9th")]
eleventh_grade = student_data[(student_data["grade"] == "9th")]
twelfth_grade = student_data[(student_data["grade"] == "9th")]

nineth_math = nineth_grade.groupby(["school_name"]).mean()["math_score"]
tenth_math = tenth_grade.groupby(["school_name"]).mean()["math_score"]
eleventh_math = eleventh_grade.groupby(["school_name"]).mean()["math_score"]
twelfth_math = twelfth_grade.groupby(["school_name"]).mean()["math_score"]

math_scores_by_grade = pd.DataFrame({"9th Grade": nineth_math,
                                     "10th Grade": tenth_math,
                                     "11th Grade": eleventh_math,
                                     "12th Grade": twelfth_math})

math_scores_by_grade = math_scores_by_grade[["9th Grade", "10th Grade", "11th Grade", "12th Grade"]]

math_scores_by_grade


# ## Reading Score by Grade 

# * Perform the same operations as above for reading scores

# In[76]:


# Calculate the Reading Scores by Grade

nineth_grade = student_data[(student_data["grade"] == "9th")]
tenth_grade = student_data[(student_data["grade"] == "9th")]
eleventh_grade = student_data[(student_data["grade"] == "9th")]
twelfth_grade = student_data[(student_data["grade"] == "9th")]

nineth_reading = nineth_grade.groupby(["school_name"]).mean()["reading_score"]
tenth_reading = tenth_grade.groupby(["school_name"]).mean()["reading_score"]
eleventh_reading = eleventh_grade.groupby(["school_name"]).mean()["reading_score"]
twelfth_reading = twelfth_grade.groupby(["school_name"]).mean()["reading_score"]

reading_scores_by_grade = pd.DataFrame({"9th Grade": nineth_reading,
                                     "10th Grade": tenth_reading,
                                     "11th Grade": eleventh_reading,
                                     "12th Grade": twelfth_reading})

reading_scores_by_grade = reading_scores_by_grade[["9th Grade", "10th Grade", "11th Grade", "12th Grade"]]

reading_scores_by_grade


# ## Scores by School Spending

# * Create a table that breaks down school performances based on average Spending Ranges (Per Student). Use 4 reasonable bins to group school spending. Include in the table each of the following:
#   * Average Math Score
#   * Average Reading Score
#   * % Passing Math
#   * % Passing Reading
#   * Overall Passing Rate (Average of the above two)

# In[77]:


# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
group_names = ["<$585", "$585-615", "$615-645", "$645-675"]


# ## Scores by School Size

# * Perform the same operations as above, based on school size.

# In[69]:


# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]


# ## Scores by School Type

# * Perform the same operations as above, based on school type.
