import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy import stats
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings('ignore')

# Page configuration with custom theme
st.set_page_config(
    page_title="🤖 AI & Students Learning Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful UI/UX
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main app styling */
    .main {
        font-family: 'Inter', sans-serif;
    }
    
    /* Custom header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
    }
    
    /* Metric cards styling */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    /* Upload section styling */
    .upload-section {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        border: 2px dashed rgba(255,255,255,0.3);
    }
    
    /* Chart container styling */
    .chart-container {
        background: rgba(255,255,255,0.9);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Success message */
    .success-message {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 1.1rem;
        font-weight: 500;
        box-shadow: 0 8px 25px rgba(79, 172, 254, 0.3);
        margin-top: 2rem;
    }
    
    /* Custom button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8, #6a4190);
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🤖 AI & Students Learning Analytics</h1>
    <p>Discover how artificial intelligence is transforming student     learning experiences</p>
<h4>By: Soveen Safen, Ramyar Mohammed, San Mohammed, Hardy Hakim</h4>
</div>
""", unsafe_allow_html=True)

# Sidebar for additional controls
with st.sidebar:
    st.markdown("### 🎛️ Dashboard Controls")
    
    # Theme selector
    chart_theme = st.selectbox(
        "🎨 Chart Theme",
        ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white"]
    )
    
    # Color palette selector
    color_palette = st.selectbox(
        "🌈 Color Palette",
        ["Viridis", "Plasma", "Inferno", "Magma", "Cividis", "Blues", "Reds", "Greens"]
    )
    
    # Chart size
    chart_height = st.slider("📏 Chart Height", 400, 800, 500)
    
    # Statistical analysis options
    st.markdown("### 🔬 Statistical Analysis")
    show_regression = st.checkbox("📈 Show Regression Analysis", True)
    show_central_tendency = st.checkbox("📊 Show Central Tendency", True)
    show_advanced_stats = st.checkbox("🧮 Show Advanced Statistics", True)
    
    st.markdown("---")
    st.markdown("### 📊 Quick Stats")

# Upload section with custom styling
st.markdown('<div class="upload-section">', unsafe_allow_html=True)
st.markdown("### 📁 Upload Your Data")
uploaded_file = st.file_uploader(
    "Choose a CSV file", 
    type="csv",
    help="Upload your survey data in CSV format"
)
st.markdown('</div>', unsafe_allow_html=True)

if uploaded_file:
    # Load and process data
    df = pd.read_csv(uploaded_file)
    df.columns = [col.strip() for col in df.columns]
    
    # Remove any rows that are clearly not data (e.g., all 'Yes' row)
    df = df[df['Name'].str.lower() != 'yes']
    
    # Helper functions for data conversion
    def convert_usage_to_numeric(usage_text):
        usage_mapping = {
            'Never': 0,
            'Rarely': 1,
            'Sometimes': 2,
            'A few times a week': 3,
            'Once a week': 2.5,
            'Daily': 4,
            'Always': 4,
            'Weekly': 3,
            'Monthly': 2,
            'Occasionally': 1,
            'Very often': 4,
            'Very rarely': 1
        }
        if pd.isna(usage_text):
            return np.nan
        for key, value in usage_mapping.items():
            if key.lower() in str(usage_text).lower():
                return value
        return np.nan
    
    def convert_university_level_to_numeric(level_text):
        level_mapping = {
            'UG1': 1, 'Undergraduate 1': 1, 'First year': 1, '1st year': 1,
            'UG2': 2, 'Undergraduate 2': 2, 'Second year': 2, '2nd year': 2,
            'UG3': 3, 'Undergraduate 3': 3, 'Third year': 3, '3rd year': 3,
            'UG4': 4, 'Undergraduate 4': 4, 'Fourth year': 4, '4th year': 4,
            'Masters': 5, 'Master': 5, 'MS': 5, 'MA': 5, 'Graduate': 5,
            'PhD': 6, 'Doctorate': 6, 'Doctoral': 6
        }
        if pd.isna(level_text):
            return np.nan
        for key, value in level_mapping.items():
            if key.lower() in str(level_text).lower():
                return value
        return np.nan
    
    # Create numeric columns for analysis
    if 'how often do you use AI?' in df.columns:
        df['AI_Usage_Numeric'] = df['how often do you use AI?'].apply(convert_usage_to_numeric)
    if 'What is your university level?' in df.columns:
        df['University_Level_Numeric'] = df['What is your university level?'].apply(convert_university_level_to_numeric)
    if 'Age' in df.columns:
        df['Age_Numeric'] = pd.to_numeric(df['Age'], errors='coerce')
    if 'Final Grade' in df.columns:
        df['Final_Grade_Numeric'] = pd.to_numeric(df['Final Grade'], errors='coerce')
    if 'AI Usage Hours Per Day' in df.columns:
        df['AI_Usage_Hours_Numeric'] = pd.to_numeric(df['AI Usage Hours Per Day'], errors='coerce')
    if 'Screen Time Per Day (hours)' in df.columns:
        df['Screen_Time_Hours_Numeric'] = pd.to_numeric(df['Screen Time Per Day (hours)'], errors='coerce')
    if 'Confidence in AI (1–5)' in df.columns:
        df['Confidence_AI_Numeric'] = pd.to_numeric(df['Confidence in AI (1–5)'], errors='coerce')
    
    trust_col = 'How much do you trust AI tools for your learning?'
    has_trust_data = trust_col in df.columns and not df[trust_col].isna().all()
    
    # Quick stats in sidebar
    with st.sidebar:
        st.metric("Total Responses", len(df))
        st.metric("Data Columns", len(df.columns))
        st.metric("Completion Rate", f"{(df.count().sum() / (len(df) * len(df.columns)) * 100):.1f}%")
        if 'Final_Grade_Numeric' in df.columns:
            st.metric("Avg Final Grade", f"{df['Final_Grade_Numeric'].mean():.1f}")
        if 'AI_Usage_Hours_Numeric' in df.columns:
            st.metric("Avg AI Usage Hours", f"{df['AI_Usage_Hours_Numeric'].mean():.2f}")
        if 'Confidence_AI_Numeric' in df.columns:
            st.metric("Avg Confidence in AI", f"{df['Confidence_AI_Numeric'].mean():.2f}")
    
    # Main dashboard metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_responses = len(df)
        st.markdown(f"""
        <div class="metric-card">
            <h2 style="color: #667eea; margin: 0;">👥 {total_responses}</h2>
            <p style="margin: 0; color: #666;">Total Responses</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if 'Gender' in df.columns:
            gender_diversity = len(df['Gender'].unique())
            st.markdown(f"""
            <div class="metric-card">
                <h2 style="color: #764ba2; margin: 0;">⚖️ {gender_diversity}</h2>
                <p style="margin: 0; color: #666;">Gender Categories</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        if 'how often do you use AI?' in df.columns:
            ai_users = len(df[df['how often do you use AI?'].notna()])
            st.markdown(f"""
            <div class="metric-card">
                <h2 style="color: #4facfe; margin: 0;">🤖 {ai_users}</h2>
                <p style="margin: 0; color: #666;">AI Users</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col4:
        if trust_col in df.columns:
            avg_trust = pd.to_numeric(df[trust_col], errors='coerce').mean()
            st.markdown(f"""
            <div class="metric-card">
                <h2 style="color: #00f2fe; margin: 0;">❤️ {avg_trust:.1f}</h2>
                <p style="margin: 0; color: #666;">Avg Trust Score</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Data preview with enhanced styling
    with st.expander("👁️ **Raw Data Preview**", expanded=False):
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.dataframe(
            df.head(10), 
            use_container_width=True,
            height=400
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced visualizations
    st.markdown('<h2 class="section-header">📊 Data Visualizations</h2>', unsafe_allow_html=True)
    
    # Row 1: Gender and University Level
    col1, col2 = st.columns(2)
    
    with col1:
        if 'Gender' in df.columns:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### 👥 Gender Distribution")
            
            gender_counts = df['Gender'].value_counts()
            fig_gender = px.pie(
                names=gender_counts.index, 
                values=gender_counts.values,
                title="Gender Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3,
                template=chart_theme,
                height=chart_height
            )
            fig_gender.update_traces(
                textposition='inside', 
                textinfo='percent+label',
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )
            fig_gender.update_layout(
                font=dict(size=14),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig_gender, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        if 'What is your university level?' in df.columns:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### 🎓 University Level Distribution")
            
            uni_counts = df['What is your university level?'].value_counts()
            fig_uni = px.bar(
                x=uni_counts.index, 
                y=uni_counts.values,
                labels={'x': 'University Level', 'y': 'Count'},
                title="University Level Distribution",
                template=chart_theme,
                color=uni_counts.values,
                color_continuous_scale=color_palette,
                height=chart_height
            )
            fig_uni.update_traces(
                hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>'
            )
            fig_uni.update_layout(
                font=dict(size=14),
                xaxis_tickangle=-45,
                showlegend=False
            )
            st.plotly_chart(fig_uni, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Row 2: AI Usage and Trust Level
    col1, col2 = st.columns(2)
    
    with col1:
        if 'how often do you use AI?' in df.columns:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### 🕐 AI Usage Frequency")
            
            usage_counts = df['how often do you use AI?'].value_counts()
            fig_usage = px.bar(
                x=usage_counts.index, 
                y=usage_counts.values,
                labels={'x': 'Usage Frequency', 'y': 'Count'},
                title="Frequency of AI Usage",
                template=chart_theme,
                color=usage_counts.values,
                color_continuous_scale=color_palette,
                height=chart_height
            )
            fig_usage.update_traces(
                hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>'
            )
            fig_usage.update_layout(
                font=dict(size=14),
                xaxis_tickangle=-45,
                showlegend=False
            )
            st.plotly_chart(fig_usage, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        if trust_col in df.columns:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### 🤝 Trust Level in AI (1–5)")
            
            fig_trust = px.histogram(
                df, 
                x=trust_col,
                nbins=5, 
                title="Trust Level Distribution",
                template=chart_theme,
                color_discrete_sequence=[px.colors.qualitative.Set2[0]],
                height=chart_height
            )
            fig_trust.update_traces(
                hovertemplate='Trust Level: %{x}<br>Count: %{y}<extra></extra>'
            )
            fig_trust.update_layout(
                font=dict(size=14),
                bargap=0.1,
                xaxis_title="Trust Level (1-5)",
                yaxis_title="Number of Responses"
            )
            st.plotly_chart(fig_trust, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Full width charts
    if 'Which AI tools do you use the most? (Select all that apply)' in df.columns:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("#### 🛠️ Most Used AI Tools")
        
        tools_series = df['Which AI tools do you use the most? (Select all that apply)'].dropna()
        tools_split = tools_series.str.split(',')
        all_tools = [tool.strip() for sublist in tools_split for tool in sublist if tool]
        tools_df = pd.Series(all_tools).value_counts()
        
        fig_tools = px.bar(
            x=tools_df.index, 
            y=tools_df.values,
            labels={'x': 'AI Tool', 'y': 'Number of Users'},
            title="Most Popular AI Tools Among Students",
            template=chart_theme,
            color=tools_df.values,
            color_continuous_scale=color_palette,
            height=chart_height
        )
        fig_tools.update_traces(
            hovertemplate='<b>%{x}</b><br>Users: %{y}<extra></extra>'
        )
        fig_tools.update_layout(
            font=dict(size=14),
            xaxis_tickangle=-45,
            showlegend=False
        )
        st.plotly_chart(fig_tools, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Final Grade Visualization
    if 'Final_Grade_Numeric' in df.columns:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("#### 🎓 Final Grade Distribution")
        fig_grade = px.histogram(
            df,
            x='Final_Grade_Numeric',
            nbins=20,
            title="Final Grade Distribution",
            template=chart_theme,
            color_discrete_sequence=[px.colors.qualitative.Set2[2]],
            height=chart_height
        )
        fig_grade.update_layout(xaxis_title="Final Grade", yaxis_title="Frequency", font=dict(size=12))
        st.plotly_chart(fig_grade, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # AI Usage Hours Visualization
    if 'AI_Usage_Hours_Numeric' in df.columns:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("#### ⏰ AI Usage Hours Per Day")
        fig_hours = px.histogram(
            df,
            x='AI_Usage_Hours_Numeric',
            nbins=10,
            title="AI Usage Hours Per Day",
            template=chart_theme,
            color_discrete_sequence=[px.colors.qualitative.Set2[3]],
            height=chart_height
        )
        fig_hours.update_layout(xaxis_title="AI Usage Hours Per Day", yaxis_title="Frequency", font=dict(size=12))
        st.plotly_chart(fig_hours, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Confidence in AI Visualization
    if 'Confidence_AI_Numeric' in df.columns:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.markdown("#### 💡 Confidence in AI (1–5)")
        fig_conf = px.histogram(
            df,
            x='Confidence_AI_Numeric',
            nbins=5,
            title="Confidence in AI (1–5)",
            template=chart_theme,
            color_discrete_sequence=[px.colors.qualitative.Set2[4]],
            height=chart_height
        )
        fig_conf.update_layout(xaxis_title="Confidence in AI (1–5)", yaxis_title="Frequency", font=dict(size=12))
        st.plotly_chart(fig_conf, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Performance improvement analysis
    if 'Do you think AI tools have improved your academic performance?' in df.columns:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### 📈 Academic Performance Improvement")
            
            perf_counts = df['Do you think AI tools have improved your academic performance?'].value_counts()
            
            # Create a donut chart
            fig_perf = go.Figure(data=[go.Pie(
                labels=perf_counts.index, 
                values=perf_counts.values,
                hole=.3,
                hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}<extra></extra>'
            )])
            
            fig_perf.update_traces(
                textposition='inside', 
                textinfo='percent+label',
                marker=dict(colors=px.colors.qualitative.Set3)
            )
            
            fig_perf.update_layout(
                title="Students' Opinion on AI Impact",
                font=dict(size=14),
                template=chart_theme,
                height=chart_height,
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            
            st.plotly_chart(fig_perf, use_container_width=True)
        
        with col2:
            # Performance insights
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### 📊 Key Insights")
            
            positive_responses = perf_counts.get('Yes', 0)
            total_responses = perf_counts.sum()
            positive_percentage = (positive_responses / total_responses * 100) if total_responses > 0 else 0
            
            st.metric(
                "Positive Impact", 
                f"{positive_percentage:.1f}%",
                f"{positive_responses} students"
            )
            
            if trust_col in df.columns:
                avg_trust = pd.to_numeric(df[trust_col], errors='coerce').mean()
                st.metric(
                    "Average Trust", 
                    f"{avg_trust:.1f}/5",
                    f"{'High' if avg_trust >= 4 else 'Medium' if avg_trust >= 3 else 'Low'} confidence"
                )
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # --- DEEP INSIGHTS SECTION ---
    st.markdown('<h2 class="section-header">🔎 Deep Insights</h2>', unsafe_allow_html=True)
    
    # 1. What university level uses AI the most?
    st.markdown('#### 1. What university level uses AI the most?')
    st.caption('Compares university level with AI usage frequency.')
    if 'What is your university level?' in df.columns and 'AI_Usage_Numeric' in df.columns:
        usage_by_level = df.groupby('What is your university level?')['AI_Usage_Numeric'].mean().sort_values()
        fig1 = px.bar(
            x=usage_by_level.index,
            y=usage_by_level.values,
            labels={'x': 'University Level', 'y': 'Avg AI Usage Frequency'},
            title='Average AI Usage Frequency by University Level',
            template=chart_theme,
            color=usage_by_level.values,
            color_continuous_scale=color_palette,
            height=400
        )
        st.plotly_chart(fig1, use_container_width=True)

    # 2. Does using AI daily lead to better final grades?
    st.markdown('#### 2. Does using AI daily lead to better final grades?')
    st.caption('Compares AI usage frequency with final grades.')
    if 'how often do you use AI?' in df.columns and 'Final_Grade_Numeric' in df.columns:
        grade_by_usage = df.groupby('how often do you use AI?')['Final_Grade_Numeric'].mean().sort_values()
        fig2 = px.bar(
            x=grade_by_usage.index,
            y=grade_by_usage.values,
            labels={'x': 'AI Usage Frequency', 'y': 'Avg Final Grade'},
            title='Average Final Grade by AI Usage Frequency',
            template=chart_theme,
            color=grade_by_usage.values,
            color_continuous_scale=color_palette,
            height=400
        )
        st.plotly_chart(fig2, use_container_width=True)

    # 3. What AI tools are most popular in each university level?
    st.markdown('#### 3. What AI tools are most popular in each university level?')
    st.caption('Shows tool popularity by university level.')
    if 'What is your university level?' in df.columns and 'Which AI tools do you use the most? (Select all that apply)' in df.columns:
        tool_level_df = df[['What is your university level?', 'Which AI tools do you use the most? (Select all that apply)']].dropna()
        exploded = tool_level_df.assign(Tool=tool_level_df['Which AI tools do you use the most? (Select all that apply)'].str.split(',')).explode('Tool')
        exploded['Tool'] = exploded['Tool'].str.strip()
        tool_counts = exploded.groupby(['What is your university level?', 'Tool']).size().reset_index(name='Count')
        fig3 = px.bar(
            tool_counts,
            x='What is your university level?',
            y='Count',
            color='Tool',
            barmode='stack',
            title='AI Tool Popularity by University Level',
            template=chart_theme,
            height=400
        )
        st.plotly_chart(fig3, use_container_width=True)

    # # 4. Do students with high trust in AI get better grades?
    # st.markdown('#### 4. Do students with high trust in AI get better grades?')
    # st.caption('Scatter plot of trust in AI vs final grade.')
    # if trust_col in df.columns and 'Final_Grade_Numeric' in df.columns:
    #     trust_numeric = pd.to_numeric(df[trust_col], errors='coerce')
    #     valid = df[trust_numeric.notna() & df['Final_Grade_Numeric'].notna()]
    #     fig4 = px.scatter(
    #         valid,
    #         x=trust_col,
    #         y='Final_Grade_Numeric',
    #         trendline='ols',
    #         title='Trust in AI vs Final Grade',
    #         template=chart_theme,
    #         color='Final_Grade_Numeric',
    #         color_continuous_scale=color_palette,
    #         height=400
    #     )
    #     st.plotly_chart(fig4, use_container_width=True)

    # 5. Is there a difference between male and female students in AI usage?
    st.markdown('#### 5. Is there a difference between male and female students in AI usage?')
    st.caption('Compares gender with AI usage frequency.')
    if 'Gender' in df.columns and 'AI_Usage_Numeric' in df.columns:
        usage_by_gender = df.groupby('Gender')['AI_Usage_Numeric'].mean().sort_values()
        fig5 = px.bar(
            x=usage_by_gender.index,
            y=usage_by_gender.values,
            labels={'x': 'Gender', 'y': 'Avg AI Usage Frequency'},
            title='Average AI Usage Frequency by Gender',
            template=chart_theme,
            color=usage_by_gender.values,
            color_continuous_scale=color_palette,
            height=400
        )
        st.plotly_chart(fig5, use_container_width=True)

    # 6. What's the average grade for each trust level?
    st.markdown("#### 6. What's the average grade for each trust level?")
    st.caption('Shows average final grade by trust in AI.')
    if trust_col in df.columns and 'Final_Grade_Numeric' in df.columns:
        trust_numeric = pd.to_numeric(df[trust_col], errors='coerce')
        df_trust_grade = df.copy()
        df_trust_grade['Trust_Numeric'] = trust_numeric
        grade_by_trust = df_trust_grade.groupby('Trust_Numeric')['Final_Grade_Numeric'].mean().dropna()
        fig6 = px.bar(
            x=grade_by_trust.index.astype(str),
            y=grade_by_trust.values,
            labels={'x': 'Trust in AI (1-5)', 'y': 'Avg Final Grade'},
            title='Average Final Grade by Trust in AI',
            template=chart_theme,
            color=grade_by_trust.values,
            color_continuous_scale=color_palette,
            height=400
        )
        st.plotly_chart(fig6, use_container_width=True)

    # 7. What AI tool is used most by top-performing students?
    st.markdown('#### 7. What AI tool is used most by top-performing students?')
    st.caption('Pie chart of AI tools among students with top 25% grades.')
    if 'Final_Grade_Numeric' in df.columns and 'Which AI tools do you use the most? (Select all that apply)' in df.columns:
        top_quartile = df['Final_Grade_Numeric'].quantile(0.75)
        top_students = df[df['Final_Grade_Numeric'] >= top_quartile]
        tools_series = top_students['Which AI tools do you use the most? (Select all that apply)'].dropna()
        tools_split = tools_series.str.split(',')
        all_tools = [tool.strip() for sublist in tools_split for tool in sublist if tool]
        tools_df = pd.Series(all_tools).value_counts()
        fig7 = px.pie(
            names=tools_df.index,
            values=tools_df.values,
            title='AI Tools Used by Top-Performing Students',
            color_discrete_sequence=px.colors.qualitative.Set3,
            template=chart_theme,
            height=400
        )
        st.plotly_chart(fig7, use_container_width=True)

    # 8. Which age group uses AI the most?
    st.markdown('#### 8. Which age group uses AI the most?')
    st.caption('Shows average AI usage by age.')
    if 'Age_Numeric' in df.columns and 'AI_Usage_Numeric' in df.columns:
        age_bins = pd.cut(df['Age_Numeric'], bins=[15,18,21,24,30,100], labels=['16-18','19-21','22-24','25-30','30+'])
        df_age_usage = df.copy()
        df_age_usage['AgeGroup'] = age_bins
        usage_by_age = df_age_usage.groupby('AgeGroup')['AI_Usage_Numeric'].mean().dropna()
        fig8 = px.bar(
            x=usage_by_age.index.astype(str),
            y=usage_by_age.values,
            labels={'x': 'Age Group', 'y': 'Avg AI Usage Frequency'},
            title='Average AI Usage Frequency by Age Group',
            template=chart_theme,
            color=usage_by_age.values,
            color_continuous_scale=color_palette,
            height=400
        )
        st.plotly_chart(fig8, use_container_width=True)

    # # 9. Do students who use more tools get better grades?
    # st.markdown('#### 9. Do students who use more tools get better grades?')
    # st.caption('Scatter plot: number of tools used vs final grade.')
    # if 'Which AI tools do you use the most? (Select all that apply)' in df.columns and 'Final_Grade_Numeric' in df.columns:
    #     df_tools_grade = df.copy()
    #     df_tools_grade['NumTools'] = df_tools_grade['Which AI tools do you use the most? (Select all that apply)'].fillna('').apply(lambda x: len([t for t in x.split(',') if t.strip()]))
    #     valid = df_tools_grade[df_tools_grade['Final_Grade_Numeric'].notna()]
    #     fig9 = px.scatter(
    #         valid,
    #         x='NumTools',
    #         y='Final_Grade_Numeric',
    #         trendline='ols',
    #         title='Number of AI Tools Used vs Final Grade',
    #         template=chart_theme,
    #         color='Final_Grade_Numeric',
    #         color_continuous_scale=color_palette,
    #         height=400
    #     )
    #     st.plotly_chart(fig9, use_container_width=True)

    # 10. Does using AI less = low trust?
    st.markdown('#### 10. Does using AI less = low trust?')
    st.caption('Shows average trust in AI by usage frequency.')
    if 'how often do you use AI?' in df.columns and trust_col in df.columns:
        trust_numeric = pd.to_numeric(df[trust_col], errors='coerce')
        df_trust_usage = df.copy()
        df_trust_usage['Trust_Numeric'] = trust_numeric
        trust_by_usage = df_trust_usage.groupby('how often do you use AI?')['Trust_Numeric'].mean().dropna()
        fig10 = px.bar(
            x=trust_by_usage.index,
            y=trust_by_usage.values,
            labels={'x': 'AI Usage Frequency', 'y': 'Avg Trust in AI'},
            title='Average Trust in AI by Usage Frequency',
            template=chart_theme,
            color=trust_by_usage.values,
            color_continuous_scale=color_palette,
            height=400
        )
        st.plotly_chart(fig10, use_container_width=True)
    
    # Advanced Analytics Section
    st.markdown('<h2 class="section-header">🔍 Advanced Statistical Analysis</h2>', unsafe_allow_html=True)
    
    # Statistical Analysis Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Correlation & Regression", "📊 Central Tendency", "🧮 Advanced Statistics", "📋 Frequency Tables"])
    
    with tab1:
        if show_regression and has_trust_data:
            st.markdown("### 📈 Correlation & Regression Analysis")
            
            # Trust vs AI Usage
            if 'AI_Usage_Numeric' in df.columns:
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("#### 🤖 Trust vs AI Usage Frequency")
                    
                    # Filter out NaN values
                    trust_usage_df = df[[trust_col, 'AI_Usage_Numeric', 'how often do you use AI?']].dropna()
                    
                    if len(trust_usage_df) > 1:
                        # Calculate correlation
                        correlation = trust_usage_df[trust_col].corr(trust_usage_df['AI_Usage_Numeric'])
                        
                        # Create scatter plot with regression line
                        fig_trust_usage = px.scatter(
                            trust_usage_df, 
                            x='AI_Usage_Numeric', 
                            y=trust_col,
                            hover_data=['how often do you use AI?'],
                            title=f"Trust vs AI Usage (r = {correlation:.3f})",
                            template=chart_theme,
                            color=trust_col,
                            color_continuous_scale=color_palette,
                            height=400
                        )
                        
                        # Add regression line
                        if len(trust_usage_df) > 2:
                            X = trust_usage_df['AI_Usage_Numeric'].values.reshape(-1, 1)
                            y = trust_usage_df[trust_col].values
                            reg_model = LinearRegression().fit(X, y)
                            
                            x_range = np.linspace(trust_usage_df['AI_Usage_Numeric'].min(), 
                                                trust_usage_df['AI_Usage_Numeric'].max(), 100)
                            y_pred = reg_model.predict(x_range.reshape(-1, 1))
                            
                            fig_trust_usage.add_traces(
                                go.Scatter(x=x_range, y=y_pred, mode='lines', 
                                         name=f'Regression Line (R² = {reg_model.score(X, y):.3f})',
                                         line=dict(color='red', width=2))
                            )
                        
                        fig_trust_usage.update_layout(
                            xaxis_title="AI Usage Frequency (0=Never, 4=Always)",
                            yaxis_title="Trust Level (1-5)",
                            font=dict(size=12)
                        )
                        st.plotly_chart(fig_trust_usage, use_container_width=True)
                        
                        # Correlation interpretation
                        if abs(correlation) > 0.7:
                            strength = "Strong"
                        elif abs(correlation) > 0.3:
                            strength = "Moderate"
                        else:
                            strength = "Weak"
                        
                        direction = "positive" if correlation > 0 else "negative"
                        st.info(f"📊 **Correlation Analysis**: {strength} {direction} correlation (r = {correlation:.3f})")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    # Trust vs University Level
                    if 'University_Level_Numeric' in df.columns:
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.markdown("#### 🎓 Trust vs University Level")
                        
                        trust_level_df = df[[trust_col, 'University_Level_Numeric', 'What is your university level?']].dropna()
                        
                        if len(trust_level_df) > 1:
                            correlation_level = trust_level_df[trust_col].corr(trust_level_df['University_Level_Numeric'])
                            
                            fig_trust_level = px.scatter(
                                trust_level_df,
                                x='University_Level_Numeric',
                                y=trust_col,
                                hover_data=['What is your university level?'],
                                title=f"Trust vs University Level (r = {correlation_level:.3f})",
                                template=chart_theme,
                                color=trust_col,
                                color_continuous_scale=color_palette,
                                height=400
                            )
                            
                            # Add regression line
                            if len(trust_level_df) > 2:
                                X = trust_level_df['University_Level_Numeric'].values.reshape(-1, 1)
                                y = trust_level_df[trust_col].values
                                reg_model = LinearRegression().fit(X, y)
                                
                                x_range = np.linspace(trust_level_df['University_Level_Numeric'].min(),
                                                    trust_level_df['University_Level_Numeric'].max(), 100)
                                y_pred = reg_model.predict(x_range.reshape(-1, 1))
                                
                                fig_trust_level.add_traces(
                                    go.Scatter(x=x_range, y=y_pred, mode='lines',
                                             name=f'Regression Line (R² = {reg_model.score(X, y):.3f})',
                                             line=dict(color='red', width=2))
                                )
                            
                            fig_trust_level.update_layout(
                                xaxis_title="University Level (1=UG1, 6=PhD)",
                                yaxis_title="Trust Level (1-5)",
                                font=dict(size=12)
                            )
                            st.plotly_chart(fig_trust_level, use_container_width=True)
                            
                            # Correlation interpretation
                            if abs(correlation_level) > 0.7:
                                strength = "Strong"
                            elif abs(correlation_level) > 0.3:
                                strength = "Moderate"
                            else:
                                strength = "Weak"
                            
                            direction = "positive" if correlation_level > 0 else "negative"
                            st.info(f"📊 **Correlation Analysis**: {strength} {direction} correlation (r = {correlation_level:.3f})")
                        
                        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        if show_central_tendency:
            st.markdown("### 📊 Central Tendency Analysis")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                st.markdown("#### 🤝 Trust in AI Statistics")
                
                if has_trust_data:
                    trust_data = pd.to_numeric(df[trust_col], errors='coerce').dropna()
                    if len(trust_data) > 0:
                        # Calculate central tendency measures
                        mean_trust = trust_data.mean()
                        median_trust = trust_data.median()
                        mode_trust = trust_data.mode().iloc[0] if not trust_data.mode().empty else "No mode"
                        std_trust = trust_data.std()
                        # Display metrics
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("📊 Mean", f"{mean_trust:.2f}")
                            st.metric("📈 Median", f"{median_trust:.2f}")
                        with col_b:
                            st.metric("🎯 Mode", f"{mode_trust}")
                            st.metric("📏 Std Dev", f"{std_trust:.2f}")
                        # Visualization
                        fig_trust_dist = go.Figure()
                        # Histogram
                        fig_trust_dist.add_trace(go.Histogram(
                            x=trust_data,
                            nbinsx=5,
                            opacity=0.7,
                            name="Distribution",
                            marker_color=px.colors.qualitative.Set2[0]
                        ))
                        # Add vertical lines for mean, median, mode
                        fig_trust_dist.add_vline(x=mean_trust, line_dash="dash", line_color="red", annotation_text=f"Mean: {mean_trust:.2f}")
                        fig_trust_dist.add_vline(x=median_trust, line_dash="dash", line_color="green", annotation_text=f"Median: {median_trust:.2f}")
                        if isinstance(mode_trust, (int, float)):
                            fig_trust_dist.add_vline(x=mode_trust, line_dash="dash", line_color="blue", annotation_text=f"Mode: {mode_trust}")
                        fig_trust_dist.update_layout(
                            title="Trust Level Distribution with Central Tendency",
                            xaxis_title="Trust Level (1-5)",
                            yaxis_title="Frequency",
                            template=chart_theme,
                            height=400,
                            font=dict(size=12)
                        )
                        st.plotly_chart(fig_trust_dist, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                # Age analysis if available
                age_columns = [col for col in df.columns if 'age' in col.lower()]
                if age_columns:
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("#### 👥 Age Statistics")
                    
                    age_col = age_columns[0]
                    age_data = pd.to_numeric(df[age_col], errors='coerce').dropna()
                    
                    if len(age_data) > 0:
                        mean_age = age_data.mean()
                        median_age = age_data.median()
                        mode_age = age_data.mode().iloc[0] if not age_data.mode().empty else "No mode"
                        std_age = age_data.std()
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("📊 Mean Age", f"{mean_age:.1f}")
                            st.metric("📈 Median Age", f"{median_age:.1f}")
                        with col_b:
                            st.metric("🎯 Mode Age", f"{mode_age}")
                            st.metric("📏 Std Dev", f"{std_age:.1f}")
                        
                        # Age distribution
                        fig_age_dist = px.histogram(
                            x=age_data,
                            nbins=20,
                            title="Age Distribution",
                            template=chart_theme,
                            color_discrete_sequence=[px.colors.qualitative.Set2[1]]
                        )
                        fig_age_dist.update_layout(
                            xaxis_title="Age",
                            yaxis_title="Frequency",
                            height=400,
                            font=dict(size=12)
                        )
                        st.plotly_chart(fig_age_dist, use_container_width=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                # AI Usage Frequency (if numeric)
                elif 'AI_Usage_Numeric' in df.columns:
                    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                    st.markdown("#### 🤖 AI Usage Frequency Statistics")
                    
                    usage_data = df['AI_Usage_Numeric'].dropna()
                    
                    if len(usage_data) > 0:
                        mean_usage = usage_data.mean()
                        median_usage = usage_data.median()
                        mode_usage = usage_data.mode().iloc[0] if not usage_data.mode().empty else "No mode"
                        std_usage = usage_data.std()
                        
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.metric("📊 Mean Usage", f"{mean_usage:.2f}")
                            st.metric("📈 Median Usage", f"{median_usage:.2f}")
                        with col_b:
                            st.metric("🎯 Mode Usage", f"{mode_usage}")
                            st.metric("📏 Std Dev", f"{std_usage:.2f}")
                        
                        # Usage labels
                        usage_labels = {0: "Never", 1: "Rarely", 2: "Sometimes", 3: "Often", 4: "Always"}
                        st.info(f"💡 **Interpretation**: {usage_labels.get(int(mean_usage), 'Mixed')} usage on average")
                    
                    st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        if show_advanced_stats:
            st.markdown("### 🧮 Advanced Statistical Measures")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                st.markdown("#### 📊 Descriptive Statistics")
                
                if has_trust_data:
                    trust_data = pd.to_numeric(df[trust_col], errors='coerce').dropna()
                    if len(trust_data) > 0:
                        # Advanced statistics
                        q1 = trust_data.quantile(0.25)
                        q3 = trust_data.quantile(0.75)
                        iqr = q3 - q1
                        skewness = stats.skew(trust_data)
                        kurtosis = stats.kurtosis(trust_data)
                        stats_df = pd.DataFrame({
                            'Statistic': ['Count', 'Mean', 'Std Dev', 'Min', 'Q1', 'Median', 'Q3', 'Max', 'IQR', 'Skewness', 'Kurtosis'],
                            'Value': [
                                len(trust_data),
                                f"{trust_data.mean():.3f}",
                                f"{trust_data.std():.3f}",
                                f"{trust_data.min():.3f}",
                                f"{q1:.3f}",
                                f"{trust_data.median():.3f}",
                                f"{q3:.3f}",
                                f"{trust_data.max():.3f}",
                                f"{iqr:.3f}",
                                f"{skewness:.3f}",
                                f"{kurtosis:.3f}"
                            ]
                        })
                        st.dataframe(stats_df, use_container_width=True, hide_index=True)
                        # Interpretation
                        if abs(skewness) < 0.5:
                            skew_interpretation = "approximately symmetric"
                        elif skewness > 0.5:
                            skew_interpretation = "positively skewed (right tail)"
                        else:
                            skew_interpretation = "negatively skewed (left tail)"
                        st.info(f"📈 **Distribution Shape**: The trust data is {skew_interpretation}")
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                st.markdown("#### 📦 Box Plot Analysis")
                
                if has_trust_data:
                    trust_data = pd.to_numeric(df[trust_col], errors='coerce').dropna()
                    if len(trust_data) > 0:
                        fig_box = go.Figure()
                        fig_box.add_trace(go.Box(
                            y=trust_data,
                            name="Trust Level",
                            boxpoints='outliers',
                            marker_color=px.colors.qualitative.Set2[0]
                        ))
                        fig_box.update_layout(
                            title="Trust Level Distribution (Box Plot)",
                            yaxis_title="Trust Level (1-5)",
                            template=chart_theme,
                            height=400,
                            font=dict(size=12)
                        )
                        st.plotly_chart(fig_box, use_container_width=True)
                        # Outlier detection
                        q1 = trust_data.quantile(0.25)
                        q3 = trust_data.quantile(0.75)
                        iqr = q3 - q1
                        lower_bound = q1 - 1.5 * iqr
                        upper_bound = q3 + 1.5 * iqr
                        outliers = trust_data[(trust_data < lower_bound) | (trust_data > upper_bound)]
                        if len(outliers) > 0:
                            st.warning(f"⚠️ **Outliers detected**: {len(outliers)} data points outside normal range")
                        else:
                            st.success("✅ **No outliers detected** in the trust data")
                st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 📋 Frequency Tables")
        
        # Create frequency tables for categorical variables
        categorical_columns = []
        for col in df.columns:
            if df[col].dtype == 'object' or df[col].nunique() < 10:
                categorical_columns.append(col)
        
        if categorical_columns:
            selected_columns = st.multiselect(
                "Select columns for frequency analysis:",
                categorical_columns,
                default=categorical_columns[:3] if len(categorical_columns) >= 3 else categorical_columns
            )
            
            if selected_columns:
                cols = st.columns(min(len(selected_columns), 3))
                
                for i, col in enumerate(selected_columns):
                    with cols[i % 3]:
                        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
                        st.markdown(f"#### {col}")
                        
                        freq_table = df[col].value_counts().reset_index()
                        freq_table.columns = ['Value', 'Frequency']
                        freq_table['Percentage'] = (freq_table['Frequency'] / freq_table['Frequency'].sum() * 100).round(2)
                        
                        st.dataframe(freq_table, use_container_width=True, hide_index=True)
                        st.markdown('</div>', unsafe_allow_html=True)
    
    # Correlation matrix (existing functionality)
    if st.checkbox("🔗 Show Full Correlation Matrix"):
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if len(numeric_cols) > 1:
            st.markdown('<div class="chart-container">', unsafe_allow_html=True)
            st.markdown("#### Correlation Matrix")
            
            corr_matrix = df[numeric_cols].corr()
            fig_corr = px.imshow(
                corr_matrix,
                text_auto=True,
                aspect="auto",
                color_continuous_scale=color_palette,
                template=chart_theme,
                height=500
            )
            fig_corr.update_layout(
                title="Correlation Between Numeric Variables",
                font=dict(size=12)
            )
            st.plotly_chart(fig_corr, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Export functionality
    st.markdown('<h2 class="section-header">💾 Export Options</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Download Summary Report"):
            summary_stats = df.describe()
            st.download_button(
                label="📄 Download CSV",
                data=summary_stats.to_csv(),
                file_name="ai_students_summary.csv",
                mime="text/csv"
            )
    
    with col2:
        if st.button("📈 Generate Insights"):
            st.balloons()
            st.success("🎉 Insights generated successfully!")
    
    with col3:
        if st.button("🔄 Refresh Analysis"):
            st.experimental_rerun()
    
    # Success message
    st.markdown("""
    <div class="success-message">
        ✅ <strong>Analysis Complete!</strong> Your interactive dashboard is ready for presentation and insights extraction.
    </div>
    """, unsafe_allow_html=True)
    
    # Footer with additional info
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9rem; margin-top: 2rem;">
        <p>🚀 Enhanced AI & Students Learning Analytics Dashboard</p>
        <p>Built with ❤️ using Streamlit and Plotly</p>
    </div>
    """, unsafe_allow_html=True)

else:
    # Welcome message when no file is uploaded
    st.markdown("""
    <div style="text-align: center; padding: 3rem; color: #666;">
        <h3>👋 Welcome to the AI & Students Analytics Dashboard</h3>
        <p style="font-size: 1.1rem; margin-bottom: 2rem;">
            Upload your CSV file to start exploring how AI is transforming student learning experiences.
        </p>
        <div style="background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); 
                    padding: 2rem; border-radius: 15px; margin: 2rem 0;">
            <h4>📋 Expected Data Format:</h4>
            <ul style="text-align: left; max-width: 600px; margin: 0 auto;">
                <li>Gender</li>
                <li>What is your university level?</li>
                <li>how often do you use AI?</li>
                <li>How much do you trust AI tools for your learning?</li>
                <li>Which AI tools do you use the most? (Select all that apply)</li>
                <li>Do you think AI tools have improved your academic performance?</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)