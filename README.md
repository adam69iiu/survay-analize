

# AI & Students Learning Analytics Dashboard

## Project Team
- **Soveen Safen**
- **Ramyar Mohammed**
- **San Mohammed**
- **Hardy Hakim**

---

## 1. Introduction

This project presents an interactive analytics dashboard designed to help educators and researchers understand how students use AI tools in their learning process. By visualizing survey data, the dashboard provides deep insights into patterns of AI usage, trust, academic performance, and more.

---

## 2. Objectives

- To analyze the relationship between AI usage and academic performance among students.
- To identify which groups (by age, gender, university level) are most engaged with AI.
- To explore students’ trust in AI and its impact on their grades.
- To provide actionable insights for teachers and curriculum designers.

---

## 3. Data Description

The dashboard uses survey data collected from students, with each row representing a student’s response. The main columns include:

- **Name**
- **Age**
- **Gender**
- **What is your university level?**
- **How often do you use AI?**
- **Which AI tools do you use the most? (Select all that apply)**
- **Do you think AI tools have improved your academic performance?**
- **How much do you trust AI tools for your learning?**
- **Final Grade**
- **AI Usage Hours Per Day**
- **Main Purpose of AI Usage**
- **Do you double-check AI answers?**
- **Screen Time Per Day (hours)**
- **Confidence in AI (1–5)**
- **Do you feel AI use is ethical?**
- **Do you use AI during exams or quizzes?**
- **Preferred AI Tool**
- **Do you talk to AI like it’s a person?**

---

## 4. Features & Analytical Questions

The dashboard answers the following key questions, each with interactive charts and summaries:

1. **What university level uses AI the most?**
2. **Does using AI daily lead to better final grades?**
3. **What AI tools are most popular in each university level?**
4. **Do students with high trust in AI get better grades?**
5. **Is there a difference between male and female students in AI usage?**
6. **What’s the average grade for each trust level?**
7. **What AI tool is used most by top-performing students?**
8. **Which age group uses AI the most?**
9. **Do students who use more tools get better grades?**
10. **Does using AI less = low trust?**

Each question is visualized with the most appropriate chart (bar, scatter, pie, etc.) and includes a short explanation for easy interpretation.

---

## 5. How to Use the Dashboard

1. **Install requirements:**
   - Python 3.8+
   - Install dependencies:
     ```bash
     pip install streamlit pandas plotly numpy scipy scikit-learn statsmodels
     ```
2. **Prepare your data:**
   - Use a CSV file with the columns listed above (see `response.csv` for an example).
3. **Run the dashboard:**
   ```bash
   streamlit run gg.py
   ```
4. **Upload your CSV file** in the web interface and explore the analytics and insights.

---

## 6. Example Insights

- **UG2 students use AI more frequently than UG4 students.**
- **Daily AI users tend to have higher average grades.**
- **ChatGPT is the most popular tool among all university levels, but Grammarly is more common in UG1.**
- **Students with higher trust in AI generally achieve better grades.**
- **There is a moderate difference in AI usage frequency between male and female students.**
- **Top-performing students often use multiple AI tools.**

---

## 7. Technologies Used

- **Python**
- **Streamlit** (for the interactive dashboard)
- **Plotly** (for data visualization)
- **Pandas, NumPy, SciPy, scikit-learn, statsmodels** (for data analysis)

---

## 8. Authors

- Soveen Safen
- Ramyar Mohammed
- San Mohammed
- Hardy Hakim

---

## 9. License

This project is for educational and academic use.
