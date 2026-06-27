import streamlit as tf
import json
from data_loader import load_resume_dataset
from model import AssistantWorkflowModel

# App Configuration
tf.set_page_config(page_title="AI Job Application Workflow Assistant", layout="wide")
tf.title("💼 AI Job Application Workflow Assistant")
tf.caption("A structured, repeatable workflow assistant for job applications.")

# Step 1: Initialize Session State Data and Loader
if "dataset_msg" not in tf.session_state:
    with tf.spinner("Downloading baseline Kaggle resume dataset templates..."):
        df, msg = load_resume_dataset()
        tf.session_state.dataset_df = df
        tf.session_state.dataset_msg = msg

tf.sidebar.success(tf.session_state.dataset_msg)
model = AssistantWorkflowModel(dataset_df=tf.session_state.get("dataset_df"))

# Main Module Tabs Navigation
tab1, tab2, tab3, tab4 = tf.tabs([
    "📋 Module 1: Match Analysis", 
    "📝 Module 2: Tailored Materials", 
    "📊 Module 3: Tracking Data", 
    "🎯 Module 4: Interview Prep"
])

# ----------------------------------------------------
# MODULE 1: JOB ANALYSIS & MATCHING
# ----------------------------------------------------
with tab1:
    tf.header("Job Analysis & Matching")
    col1, col2 = tf.columns(2)
    
    with col1:
        job_input = tf.text_area(
            "Target Job Posting", 
            value="Spotify Senior Data Analyst role (requiring SQL, Python, and experience with A/B testing, Tableau)."
        )
        resume_input = tf.text_area(
            "Master Resume Content", 
            value="5 years of data experience, including a project where you analyzed user engagement using PowerBI."
        )
        sample_input = tf.text_area(
            "Writing Sample Tone Library", 
            value="Authentic, adaptive communication with clear and direct sentences."
        )
        analyze_btn = tf.button("Run Job Analysis Matching")
        
    with col2:
        tf.subheader("Model Output")
        if analyze_btn:
            res1 = model.module_1_job_analysis(job_input, resume_input, sample_input)
            tf.metric("Fit Assessment Score", res1["fit_score"])
            
            tf.write("**Key Keywords Identified:**")
            tf.write(", ".join(res1["keywords"]))
            
            tf.write("**Gaps Identified:**")
            for gap in res1["gaps"]:
                tf.warning(gap)

# ----------------------------------------------------
# MODULE 2: TAILORED MATERIAL GENERATION
# ----------------------------------------------------
with tab2:
    tf.header("Tailored Material Generation")
    col1, col2 = tf.columns(2)
    
    with col1:
        cmd_input2 = tf.text_input("Workflow Command", value="Generate a tailored resume and cover letter for this Spotify role using my master templates.")
        instr_input2 = tf.text_input("Special Tone/Context Instruction", value="Emphasize my user-engagement project to match their focus on user retention.")
        tailor_btn = tf.button("Generate Tailored Assets")
        
    with col2:
        tf.subheader("Model Output")
        if tailor_btn:
            res2 = model.module_2_tailor_materials(cmd_input2, instr_input2, resume_input, sample_input)
            tf.subheader("📄 Tailored Resume Preview")
            tf.code(res2["tailored_resume"], language="text")
            
            tf.subheader("✉️ Tailored Cover Letter Preview")
            tf.info(res2["tailored_cover_letter"])

# ----------------------------------------------------
# MODULE 3: APPLICATION TRACKING & DATA ORGANIZATION
# ----------------------------------------------------
with tab3:
    tf.header("Application Tracking & Data Organization")
    col1, col2 = tf.columns(2)
    
    with col1:
        cmd_input3 = tf.text_input("Tracking Command", value="Log this application.")
        status_input3 = tf.text_input("Status Update Text", value="Submitted application on June 27, 2026.")
        log_btn = tf.button("Process & Structure Entry")
        
    with col2:
        tf.subheader("Model Output")
        if log_btn:
            res3 = model.module_3_track_application(cmd_input3, status_input3)
            tf.write("**Structured Data Payload (JSON):**")
            tf.json(res3)
            
            tf.write("**Spreadsheet Table Preview:**")
            tf.dataframe([res3])

# ----------------------------------------------------
# MODULE 4: INTERVIEW PREPARATION
# ----------------------------------------------------
with tab4:
    tf.header("Interview Preparation Modules")
    col1, col2 = tf.columns(2)
    
    with col1:
        cmd_input4 = tf.text_input("Preparation Scope Command", value="I have a first-round interview with the hiring manager. Prepare me.")
        prep_btn = tf.button("Generate Strategy Prep")
        
    with col2:
        tf.subheader("Model Output")
        if prep_btn:
            res4 = model.module_4_interview_prep(cmd_input4)
            tf.write("**Predicted Interview Questions:**")
            for q in res4["predicted_questions"]:
                tf.write(q)
                
            tf.write("---")
            tf.write(res4["star_cheatsheet"])