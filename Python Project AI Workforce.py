#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


#Checking Folder
os.getcwd()


# In[5]:


#For Checking Excel Files
files = os.listdir()
files


# In[10]:


#Reading Excel File
abilities = pd.read_excel("Abilities.xlsx")
abilities.head()


# In[12]:


#Checking Size
abilities.shape


# In[ ]:


#Uploading File
abilities = pd.read_excel("Abilities.xlsx")

education = pd.read_excel("Education.xlsx")

essential_skills = pd.read_excel("Essential Skills.xlsx")

job_zones = pd.read_excel("Job Zones.xlsx")

knowledge = pd.read_excel("Knowledge.xlsx")

occupation_data = pd.read_excel("Occupation Data.xlsx")

software_skills = pd.read_excel("Software Skills.xlsx")

task_statements = pd.read_excel("Task Statements.xlsx")

work_activities = pd.read_excel("Work Activities.xlsx")

national_data = pd.read_excel("national_M2025_dl.xlsx")


# In[ ]:


#Checking 12 sheets
employment_projection.keys()


# In[20]:


occupation_data.shape


# In[22]:


#Checking top 5
software_skills.head()


# In[28]:


#Checking exact file names
import os

os.listdir()


# In[30]:


#This is using exact names
employment_projection = pd.read_excel(
    "Employment Projection Occupation Data 1.xlsx",
    sheet_name=None
)


# In[32]:


#Checking Sheet Names
employment_projection.keys()


# In[36]:


#Checking Sheet Size
for sheet_name, df in employment_projection.items():
    print(sheet_name, df.shape)


# In[39]:


#Checking 11 sheet size names
files = [
    "Abilities.xlsx",
    "Education.xlsx",
    "Essential Skills.xlsx",
    "Job Zones.xlsx",
    "Knowledge.xlsx",
    "national_M2025_dl.xlsx",
    "Occupation Data.xlsx",
    "Software Skills.xlsx",
    "Task Statements.xlsx",
    "Work Activities.xlsx"
]

for file in files:
    df = pd.read_excel(file)
    print(file, df.shape)


# In[48]:


#Checking Coloumns
occupation_data.columns


# In[50]:


knowledge.columns


# In[52]:


abilities.columns


# In[54]:


#Check all remaining files together
for df_name, df in {
    "Occupation": occupation_data,
    "Abilities": abilities,
    "Knowledge": knowledge,
    "Education": education,
    "Essential Skills": essential_skills,
    "Job Zones": job_zones,
    "Software Skills": software_skills,
    "Task Statements": task_statements,
    "Work Activities": work_activities
}.items():

    print(df_name)
    print(df['O*NET-SOC Code'].nunique())
    print("----------------")


# In[62]:


#Checking Duplicate exist or not
occupation_data['O*NET-SOC Code'].duplicated().sum()


# In[64]:


#Checking Shapes of all
occupation_data.shape


# In[66]:


abilities.shape


# In[68]:


knowledge.shape


# In[70]:


education.shape


# In[72]:


essential_skills.shape


# In[74]:


#Checking Uniquue values
occupation_data['O*NET-SOC Code'].nunique()


# In[76]:


abilities['O*NET-SOC Code'].nunique()


# In[78]:


knowledge['O*NET-SOC Code'].nunique()


# In[84]:


education['O*NET-SOC Code'].nunique()


# In[86]:


essential_skills['O*NET-SOC Code'].nunique()


# In[88]:


job_zones['O*NET-SOC Code'].nunique()


# In[90]:


work_activities['O*NET-SOC Code'].nunique()


# In[92]:


software_skills['O*NET-SOC Code'].nunique()


# In[94]:


task_statements['O*NET-SOC Code'].nunique()


# In[96]:


#Checking Common Keys
for df_name, df in {
    "Education": education,
    "Essential Skills": essential_skills,
    "Job Zones": job_zones,
    "Software Skills": software_skills,
    "Task Statements": task_statements,
    "Work Activities": work_activities
}.items():

    print(df_name, df['O*NET-SOC Code'].nunique())


# In[98]:


#Creating Data Dictionary before Merging
for df_name, df in {
    "Abilities": abilities,
    "Knowledge": knowledge,
    "Essential Skills": essential_skills,
    "Education": education,
    "Job Zones": job_zones,
    "Software Skills": software_skills,
    "Task Statements": task_statements,
    "Work Activities": work_activities
}.items():

    print("\n", df_name)
    print(df['Element Name'].nunique() if 'Element Name' in df.columns else "No Element Name")


# In[100]:


#Checking same occupation is present or not
occ_master = set(occupation_data['O*NET-SOC Code'])

occ_abilities = set(abilities['O*NET-SOC Code'])

print("Missing from abilities:")
print(len(occ_master - occ_abilities))


# In[102]:


#Creating Master Occupation Table
master = occupation_data.copy()


# In[106]:


#Which data is presnet in table checking
for sheet_name, df in employment_projection.items():
    print("\n")
    print(sheet_name)
    print(df.columns.tolist())


# In[108]:


for sheet_name, df in employment_projection.items():
    print("\n")
    print(sheet_name)
    print(df.shape)
    print(df.columns.tolist())


# In[110]:


employment_projection['Table 1.2'].head(10)


# In[112]:


employment_projection['Table 1.2'].iloc[:10]


# In[114]:


employment_projection['Table 1.2'].columns


# In[116]:


employment_projection['Table 1.2'].head(15)


# In[118]:


#Table Cleaning
table12 = employment_projection['Table 1.2']

table12.columns = table12.iloc[0]

table12 = table12[1:]

table12.head()


# In[120]:


table12.columns


# In[122]:


#Removing summary rows and keeping only main occupations
table12 = table12[
    table12['Occupation type'] == 'Line item'
]


# In[125]:


table12.shape


# In[127]:


table12[['2024 National Employment Matrix code']].head()


# In[129]:


occupation_data[['O*NET-SOC Code']].head()


# In[133]:


master = occupation_data


# In[135]:


future_jobs = table12


# In[137]:


essential_skills


# In[139]:


knowledge


# In[141]:


abilities


# In[145]:


table12.shape


# In[147]:


#Keeping only important coloumns
future_jobs = table12[[
    '2024 National Employment Matrix code',
    '2024 National Employment Matrix title',
    'Employment, 2024',
    'Employment, 2034',
    'Employment change, numeric, 2024–34',
    'Employment change, percent, 2024–34',
    'Occupational openings, 2024–34 annual average',
    'Median annual wage, dollars, 2024[1]',
    'Typical education needed for entry'
]]


# In[ ]:





# In[150]:


future_jobs.head()


# In[152]:


#Rename Columns
future_jobs = future_jobs.rename(columns={
    '2024 National Employment Matrix code':'Occupation_Code',
    '2024 National Employment Matrix title':'Occupation_Title',
    'Employment, 2024':'Employment_2024',
    'Employment, 2034':'Employment_2034',
    'Employment change, numeric, 2024–34':'Job_Change',
    'Employment change, percent, 2024–34':'Growth_Percent',
    'Occupational openings, 2024–34 annual average':'Annual_Openings',
    'Median annual wage, dollars, 2024[1]':'Median_Wage',
    'Typical education needed for entry':'Education'
})


# In[154]:


future_jobs.info()


# In[156]:


future_jobs.isnull().sum()


# In[158]:


future_jobs.dtypes


# In[160]:


future_jobs.head()


# In[164]:


#Changing data types
numeric_cols = [
    'Employment_2024',
    'Employment_2034',
    'Job_Change',
    'Growth_Percent',
    'Annual_Openings',
    'Median_Wage'
]

for col in numeric_cols:
    future_jobs[col] = pd.to_numeric(
        future_jobs[col],
        errors='coerce'
    )


# In[166]:


future_jobs.dtypes


# In[168]:


future_jobs[numeric_cols].isnull().sum()


# In[170]:


future_jobs.shape


# In[172]:


future_jobs.dtypes


# In[174]:


occupation_data.head()


# In[176]:


occupation_data['O*NET-SOC Code'].head(10)


# In[178]:


occupation_data['Occupation_Code'] = (
    occupation_data['O*NET-SOC Code']
    .astype(str)
    .str.replace('.00', '', regex=False)
)


# In[180]:


occupation_data[['O*NET-SOC Code','Occupation_Code']].head()


# In[182]:


master_jobs = future_jobs.merge(
    occupation_data,
    on='Occupation_Code',
    how='left'
)


# In[184]:


master_jobs.shape


# In[186]:


master_jobs.head()


# In[188]:


master_jobs['Description'].isnull().sum()


# In[190]:


master_jobs.shape
master_jobs.head()
master_jobs['Description'].isnull().sum()


# In[192]:


master_jobs.shape


# In[194]:


master_jobs.head()


# In[196]:


master_jobs['Description'].isnull().sum()


# In[198]:


#Save
master_jobs.to_csv(
    "master_jobs.csv",
    index=False
)


# In[200]:


essential_skills.head()


# In[202]:


essential_skills.columns


# In[204]:


essential_skills.shape


# In[208]:


essential_skills.head()


# In[210]:


#Create Occupation Code in Skills
essential_skills['Occupation_Code'] = (
    essential_skills['O*NET-SOC Code']
    .astype(str)
    .str.replace('.00', '', regex=False)
)


# In[212]:


#Finding Top Skills for each occupation
top_skills = essential_skills.sort_values(
    'Data Value',
    ascending=False
).drop_duplicates('Occupation_Code')

top_skills.head()


# In[214]:


#KMerging skills with Master Jobs
master_jobs_skills = master_jobs.merge(
    top_skills[['Occupation_Code','Element Name','Data Value']],
    on='Occupation_Code',
    how='left'
)


# In[216]:


#Rename Coloumns
master_jobs_skills.rename(columns={
    'Element Name':'Top_Skill',
    'Data Value':'Skill_Score'
}, inplace=True)


# In[219]:


#Save
master_jobs_skills.to_csv(
    "master_jobs_skills.csv",
    index=False
)


# In[221]:


#Creating Risk Score from Growth %
master_jobs['Automation_Risk_Score'] = (
    master_jobs['Growth_Percent'].max()
    - master_jobs['Growth_Percent']
)


# In[223]:


#Normalizing
master_jobs['Automation_Risk_Score'] = (
    (master_jobs['Automation_Risk_Score']
     - master_jobs['Automation_Risk_Score'].min())
    /
    (master_jobs['Automation_Risk_Score'].max()
     - master_jobs['Automation_Risk_Score'].min())
) * 100


# In[225]:


master_jobs[['Occupation_Title',
             'Growth_Percent',
             'Automation_Risk_Score']].head()


# In[227]:


#Which occupations face the highest automation risk?
q1 = master_jobs.sort_values(
    'Automation_Risk_Score',
    ascending=False
)[[
    'Occupation_Title',
    'Growth_Percent',
    'Automation_Risk_Score',
    'Education'
]]

q1.head(20)


# In[229]:


#Q2 - Future Career Resilience Score
#Creating Score
master_jobs['Career_Resilience_Score'] = (
      master_jobs['Growth_Percent'].rank(pct=True)*0.4
    + master_jobs['Median_Wage'].rank(pct=True)*0.3
    + master_jobs['Annual_Openings'].rank(pct=True)*0.3
) * 100


# In[231]:


#Top Careers
q3 = master_jobs.sort_values(
    'Career_Resilience_Score',
    ascending=False
)

q3[['Occupation_Title',
    'Career_Resilience_Score',
    'Median_Wage',
    'Growth_Percent']].head(20)


# In[233]:


q3.to_csv("Q3_Career_Resilience.csv", index=False)


# In[235]:


#Workforce Polarization
#Create skill groups
def skill_level(x):

    if x in [
        "No formal educational credential",
        "High school diploma or equivalent"
    ]:
        return "Low Skill"

    elif x in [
        "Associate's degree",
        "Some college, no degree"
    ]:
        return "Middle Skill"

    else:
        return "High Skill"


# In[237]:


master_jobs['Skill_Level'] = (
    master_jobs['Education']
    .apply(skill_level)
)


# In[239]:


#Growth by group:
q5 = master_jobs.groupby(
    'Skill_Level'
)['Growth_Percent'].mean()

print(q5)


# In[242]:


#Growing despite AI Exposure
q6 = master_jobs[
    (master_jobs['Growth_Percent'] > 5)
    &
    (master_jobs['Automation_Risk_Score'] > 50)
]

q6[['Occupation_Title',
    'Growth_Percent',
    'Automation_Risk_Score']]


# In[244]:


#High Value + High Risk
#Create Economic Value Score:
master_jobs['Economic_Value'] = (
      master_jobs['Median_Wage'].rank(pct=True)*0.5
    + master_jobs['Employment_2024'].rank(pct=True)*0.5
) * 100


# In[250]:


print(q9.shape)


# In[252]:


#Filtering:
q9 = master_jobs[
    (master_jobs['Economic_Value'] > 60)
    &
    (master_jobs['Automation_Risk_Score'] > 60)
]

q9[['Occupation_Title',
    'Economic_Value',
    'Automation_Risk_Score']]


# In[254]:


#Reskilling Emergency Index
#Estimate workers needing reskilling:
master_jobs['Reskilling_Emergency_Index'] = (
    master_jobs['Employment_2024']
    *
    (master_jobs['Automation_Risk_Score']/100)
)


# In[256]:


q4 = master_jobs.sort_values(
    'Reskilling_Emergency_Index',
    ascending=False
)

q4[['Occupation_Title',
    'Reskilling_Emergency_Index']]


# In[260]:


import pandas as pd
import matplotlib.pyplot as plt


# In[262]:


#Q1. Automation Risk by Occupation
top10_risk = q1.head(10)

plt.figure(figsize=(10,6))
plt.barh(
    top10_risk['Occupation_Title'],
    top10_risk['Automation_Risk_Score']
)
plt.title("Top 10 Occupations with Highest Automation Risk")
plt.xlabel("Automation Risk Score")
plt.ylabel("Occupation")
plt.tight_layout()
plt.show()


# In[264]:


#Q2. Future-Proof Careers
top10_resilient = q3.head(10)

plt.figure(figsize=(10,6))
plt.barh(
    top10_resilient['Occupation_Title'],
    top10_resilient['Career_Resilience_Score']
)
plt.title("Top 10 Future-Proof Careers")
plt.xlabel("Career Resilience Score")
plt.ylabel("Occupation")
plt.tight_layout()
plt.show()


# In[266]:


#Q4. Reskilling Emergency Index
top10_reskill = q4.head(10)

plt.figure(figsize=(10,6))
plt.barh(
    top10_reskill['Occupation_Title'],
    top10_reskill['Reskilling_Emergency_Index']
)
plt.title("Occupations Requiring Immediate Reskilling")
plt.xlabel("Reskilling Emergency Index")
plt.ylabel("Occupation")
plt.tight_layout()
plt.show()


# In[268]:


#Q5. Workforce Polarization
q5.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Average Growth by Skill Level")
plt.ylabel("Average Growth %")
plt.tight_layout()
plt.show()


# In[270]:


#Q6. Growing Despite AI Exposure
top10_q6 = q6.head(10)

plt.figure(figsize=(10,6))
plt.barh(
    top10_q6['Occupation_Title'],
    top10_q6['Growth_Percent']
)
plt.title("Growing Occupations Despite AI Exposure")
plt.xlabel("Growth Percent")
plt.tight_layout()
plt.show()


# In[272]:


#Q9. Economic Value vs Automation Risk
plt.figure(figsize=(10,6))

plt.scatter(
    master_jobs['Economic_Value'],
    master_jobs['Automation_Risk_Score']
)

plt.xlabel("Economic Value")
plt.ylabel("Automation Risk Score")
plt.title("Economic Value vs Automation Risk")

plt.show()


# In[274]:


#Q10. 2035 Workforce Simulation
master_jobs['Projected_2035_Workforce'] = (
    master_jobs['Employment_2034']
    *
    (1 - master_jobs['Automation_Risk_Score']/100)
)


# In[276]:


simulation = master_jobs[[
    'Employment_2024',
    'Employment_2034',
    'Projected_2035_Workforce'
]].sum()

simulation.plot(
    kind='line',
    marker='o',
    figsize=(8,5)
)

plt.title("Workforce Simulation")
plt.ylabel("Employment")
plt.show()


# In[278]:


pip install streamlit plotly


# In[282]:


#Dashboard for Simple
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(18, 12))

# Chart 1 - Top Growing Occupations
top_growth = master_jobs.sort_values(
    'Growth_Percent',
    ascending=False
).head(10)

axes[0,0].barh(
    top_growth['Occupation_Title'],
    top_growth['Growth_Percent']
)
axes[0,0].set_title('Top 10 Growing Occupations')

# Chart 2 - Highest Paying Occupations
top_salary = master_jobs.sort_values(
    'Median_Wage',
    ascending=False
).head(10)

axes[0,1].barh(
    top_salary['Occupation_Title'],
    top_salary['Median_Wage']
)
axes[0,1].set_title('Top 10 Highest Paying Occupations')

# Chart 3 - Education Distribution
edu = master_jobs['Education'].value_counts()

axes[1,0].pie(
    edu.values,
    labels=edu.index,
    autopct='%1.1f%%'
)
axes[1,0].set_title('Education Distribution')

# Chart 4 - Salary vs Growth
axes[1,1].scatter(
    master_jobs['Median_Wage'],
    master_jobs['Growth_Percent']
)
axes[1,1].set_title('Salary vs Growth')
axes[1,1].set_xlabel('Median Wage')
axes[1,1].set_ylabel('Growth Percent')

plt.tight_layout()
plt.show()


# In[284]:


#Save Final Dataset
master_jobs.to_csv(
    "AI_Workforce_Final_Dataset.csv",
    index=False
)


# In[286]:


#Save Dashboard Image
plt.savefig(
    "AI_Workforce_Dashboard.png",
    bbox_inches='tight'
)


# In[288]:


#Export Question Outputs
q1.to_csv("Q1_Automation_Risk.csv", index=False)
q3.to_csv("Q3_Career_Resilience.csv", index=False)
q4.to_csv("Q4_Reskilling_Index.csv", index=False)
q5.to_csv("Q5_Polarization.csv")
q6.to_csv("Q6_Growth_vs_AI.csv", index=False)
q9.to_csv("Q9_Economic_Value_Risk.csv", index=False)


# In[ ]:




