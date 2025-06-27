# AI & Students Learning Analytics Dashboard

## Overview

This project is an interactive analytics dashboard built with Streamlit and Plotly, designed to help educators and researchers analyze how students use AI tools in their learning process. The dashboard visualizes survey data, provides deep insights, and answers key analytical questions about AI usage, trust, academic performance, and more.

## What Does It Do?

- **Loads survey data** from a CSV file (e.g., `response.csv`) containing student responses about AI usage, trust, grades, and demographics.
- **Visualizes key metrics** such as gender distribution, university level, AI usage frequency, trust in AI, and more.
- **Provides advanced analytics** including correlation, regression, central tendency, and outlier detection.
- **Answers deep analytical questions** with clear charts and summaries, helping teachers understand patterns and relationships in the data.

## Main Analytical Questions Answered

The dashboard includes a "Deep Insights" section that answers:

1. **What university level uses AI the most?**
2. **Does using AI daily lead to better final grades?**
3. **What AI tools are most popular in each university level?**
4. **Do students with high trust in AI get better grades?**
5. **Is there a difference between male and female students in AI usage?**
6. **What's the average grade for each trust level?**
7. **What AI tool is used most by top-performing students?**
8. **Which age group uses AI the most?**
9. **Do students who use more tools get better grades?**
10. **Does using AI less = low trust?**

Each question is visualized with the most appropriate chart (bar, scatter, pie, etc.) and includes a short explanation for easy interpretation.

## How to Use

1. **Install requirements:**
   - Python 3.8+
   - Install dependencies:
     ```bash
     pip install streamlit pandas plotly numpy scipy scikit-learn statsmodels
     ```
2. **Prepare your data:**
   - Use a CSV file with columns like: `Name`, `Age`, `Gender`, `What is your university level?`, `how often do you use AI?`, `Which AI tools do you use the most? (Select all that apply)`, `Final Grade`, `How much do you trust AI tools for your learning?`, etc.
   - Example: see `response.csv` in this repo.
3. **Run the dashboard:**
   ```bash
   streamlit run gg.py
   ```
4. **Upload your CSV file** in the web interface and explore the analytics and insights.

## Features

- **Beautiful, modern UI** with custom themes and color palettes.
- **Sidebar controls** for customizing chart appearance and analysis options.
- **Raw data preview** and quick stats.
- **Interactive charts** for all major survey questions.
- **Advanced statistics**: correlation, regression, central tendency, outlier detection, and more.
- **Export options** for summary reports.

## For Teachers & Academics

This dashboard is designed to:

- Help you understand how students use AI tools in their studies.
- Reveal patterns between AI usage, trust, and academic performance.
- Identify which groups (by age, gender, university level) are most engaged with AI.
- Support data-driven decisions for curriculum design or further research.

## Authors

- Soveen Safen
- Ramyar Mohammed
- San Mohammed
- Hardy Hakim

## License

This project is for educational and academic use.
