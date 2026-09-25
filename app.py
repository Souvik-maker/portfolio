import io
import streamlit as st
import plotly.express as px
import pandas as pd
from sqlalchemy import text

# PDF Generation imports from ReportLab
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


# Page Configuration
st.set_page_config(
    page_title="Souvik Ghosh | Backend & GenAI Engineer",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------------
# HELPER FUNCTION: Generate PDF Resume in Memory
# ---------------------------------------------------------
def generate_resume_pdf():
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    styles = getSampleStyleSheet()
    story = []

    # Custom Styles
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, leading=22, textColor=colors.HexColor('#1E3A8A'))
    subtitle_style = ParagraphStyle('SubTitleStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor('#4B5563'))
    heading_style = ParagraphStyle('HeadingStyle', parent=styles['Heading2'], fontSize=12, leading=16, textColor=colors.HexColor('#1E3A8A'), spaceBefore=8, spaceAfter=4)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=9, leading=13)
    bullet_style = ParagraphStyle('BulletStyle', parent=styles['Normal'], fontSize=9, leading=13, leftIndent=12)

    # Header
    story.append(Paragraph("<b>SOUVIK GHOSH</b>", title_style))
    story.append(Paragraph("souvikghosh.sovi@gmail.com | +91 9674847794 | Kolkata, India", subtitle_style))
    story.append(Spacer(1, 10))

    # Education
    story.append(Paragraph("<b>EDUCATION</b>", heading_style))
    story.append(Paragraph("<b>B.Tech in Computer Science and Engineering</b> - St. Thomas' College of Engineering and Technology (2020-2024)", body_style))
    story.append(Paragraph("Average CGPA: 9.0", bullet_style))
    story.append(Spacer(1, 8))

    # Experience
    story.append(Paragraph("<b>WORK EXPERIENCE</b>", heading_style))
    story.append(Paragraph("<b>Backend Engineer | Tata Consultancy Services (TCS)</b> (May 2025 - Present)", body_style))
    story.append(Paragraph("• Architected and migrated legacy procedural COBOL payment rails into modular, cloud-ready Spring Boot microservices.", bullet_style))
    story.append(Paragraph("• Utilized Spring Data JPA to remap mainframe flat files into relational schemas and containerized services using Docker.", bullet_style))
    
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Intern & Backend Engineer | Zediant Technologies</b> (Feb 2024 - May 2025)", body_style))
    story.append(Paragraph("• Developed microservices, designed RESTful APIs using Spring Boot, and optimized complex SQL queries.", bullet_style))
    story.append(Spacer(1, 8))

    # Skills
    story.append(Paragraph("<b>TECHNICAL SKILLS</b>", heading_style))
    story.append(Paragraph("<b>Languages & GenAI:</b> Java, Python, SQL, LangChain, LangGraph, OpenAI API, RAG, Vector DBs (Chroma, PGVector)", body_style))
    story.append(Paragraph("<b>Frameworks & Tools:</b> Spring Boot, Spring Security, Hibernate, FastAPI, Apache Kafka, Docker, AWS, Postman, Git", body_style))
    story.append(Spacer(1, 8))

    # Projects
    story.append(Paragraph("<b>FEATURED PROJECTS</b>", heading_style))
    story.append(Paragraph("<b>Autonomous AI Agent Network (LangGraph):</b> Built stateful multi-agent pipelines with human-in-the-loop validation.", body_style))
    story.append(Paragraph("<b>ShopEase E-Commerce Platform:</b> Spring Boot & Angular platform integrated with OpenAI API and Apache Kafka.", body_style))

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:
    st.title("Souvik Ghosh")
    st.write("🚀 **Backend & Generative AI Engineer**")
    st.write("📍 Kolkata, India")
    st.write("📧 souvik.ghosh12@tcs.com")
    st.write("📞 +91 9674847794")
    
    st.markdown("---")
    st.subheader("Links & Profiles")
    st.markdown("[GitHub](https://github.com)")
    st.markdown("[LeetCode](https://leetcode.com)")
    st.markdown("[GeeksforGeeks](https://geeksforgeeks.org)")
    st.markdown("[HackerRank](https://hackerrank.com)")
    
    st.markdown("---")
    
    # PDF RESUME DOWNLOAD BUTTON
    pdf_bytes = generate_resume_pdf()
    st.download_button(
        label="📄 Download Resume (PDF)",
        data=pdf_bytes,
        file_name="Souvik_Ghosh_Resume.pdf",
        mime="application/pdf"
    )

# ---------------------------------------------------------
# MAIN CONTENT
# ---------------------------------------------------------
st.title("Souvik Ghosh")
st.subheader("Backend Engineer & Generative AI Developer")
st.write("""
Backend Engineer combining microservices development (**Spring Boot, Java, Python, FastAPI,AWS**) with modern **Generative AI systems**. 
Specialized in building complex autonomous multi-agent workflows using **LangGraph**, retrieval-augmented systems (**LangChain, RAG**), 
and enterprise vector database integrations alongside cloud-native systems.
""")

st.markdown("---")

# Navigation Tabs
tab_ai, tab_proj, tab_exp, tab_skills, tab_edu = st.tabs([
    "🤖 GenAI Capabilities", 
    "🚀 Featured Projects", 
    "💼 Experience", 
    "🛠️ Technical Skills", 
    "🎓 Education & Achievements"
])

# Tab 1: GenAI Capabilities & Interactive Demo
with tab_ai:
    st.header("Generative AI & Agentic Architecture")
    st.write("""
    I architect production-grade LLM applications, ranging from enterprise-grade RAG and agentic workflows 
    to stateful multi-agent systems with active human-in-the-loop controls.
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🕸️ LangGraph & Multi-Agents")
        st.write("""
        - Stateful, cyclic workflows using StateGraph structures.
        - Hierarchical supervisor & worker multi-agent topologies.
        - Persistence layers with checkpointers for resilient conversations.
        - Native Human-In-The-Loop (HITL) interrupt and state editing.
        """)
        
    with col2:
        st.subheader("🔗 Advanced RAG & Vector Systems")
        st.write("""
        - **Hybrid Search**: Dense embeddings + Sparse BM25 keyword matching.
        - **Retrieval Optimization**: Contextual compression, Cohere re-ranking, & Parent Document Retriever.
        - **Vector Databases**: Pinecone, ChromaDB, PGVector, and Qdrant.
        """)

    with col3:
        st.subheader("🛡️ Enterprise Guardrails & Security")
        st.write("""
        - Prompt injection defense & PII redaction layers.
        - Deterministic schema enforcement using Pydantic / Structured Outputs.
        - Fallback routing and token bucket rate-limiting strategies.
        """)

    st.markdown("---")

    # Interactive Sandbox
    st.subheader("🕹️ Interactive Architecture Visualizer: LangGraph Execution Simulation")
    st.caption("Select an industry use case to visualize its underlying multi-agent execution pipeline.")
    
    workflow_type = st.selectbox(
        "Select Industry Workflow:",
        [
            "1. Financial Fraud & Suspicious Activity Agent (HITL)",
            "2. Enterprise Knowledge Base (Advanced RAG with Re-ranking)",
            "3. Multi-Agent Code Review & Security Scanner",
            "4. E-Commerce Real-Time Event Recommendations (Kafka + Agent)"
        ]
    )
    
    if workflow_type == "1. Financial Fraud & Suspicious Activity Agent (HITL)":
        st.info("💡 **Use Case:** Analyzes high-risk banking transactions, flags anomalies, and pauses execution for human compliance approval before taking action.")
        st.graphviz_chart('''
            digraph {
                rankdir=LR;
                node [shape=box, style="filled,rounded", fillcolor="#E3F2FD", fontname="sans-serif"];
                Transaction_Event -> Fraud_Classifier_Node;
                Fraud_Classifier_Node -> Risk_Scorer;
                Risk_Scorer -> Tool_Freeze_Account [label="Low Risk"];
                Risk_Scorer -> HITL_Human_Interrupt [label="High Risk"];
                HITL_Human_Interrupt -> Analyst_Approval;
                Analyst_Approval -> Action_Execution_Node;
            }
        ''')

    elif workflow_type == "2. Enterprise Knowledge Base (Advanced RAG with Re-ranking)":
        st.info("💡 **Use Case:** High-accuracy document search over complex PDFs using hybrid search and contextual re-ranking.")
        st.graphviz_chart('''
            digraph {
                rankdir=LR;
                node [shape=box, style="filled,rounded", fillcolor="#E8F5E9", fontname="sans-serif"];
                User_Query -> Query_Decomposition;
                Query_Decomposition -> Hybrid_Search_Pinecone;
                Query_Decomposition -> Sparse_BM25_Search;
                Hybrid_Search_Pinecone -> Cohere_Reranker;
                Sparse_BM25_Search -> Cohere_Reranker;
                Cohere_Reranker -> LLM_Synthesis;
                LLM_Synthesis -> Final_Response;
            }
        ''')

    elif workflow_type == "3. Multi-Agent Code Review & Security Scanner":
        st.info("💡 **Use Case:** A supervisor agent delegates code analysis to specialized security, performance, and unit-test agents.")
        st.graphviz_chart('''
            digraph {
                rankdir=TB;
                node [shape=box, style="filled,rounded", fillcolor="#FFF3E0", fontname="sans-serif"];
                PR_Trigger -> Supervisor_Agent;
                Supervisor_Agent -> Security_Agent;
                Supervisor_Agent -> Performance_Agent;
                Supervisor_Agent -> Unit_Test_Agent;
                Security_Agent -> Aggregator_Node;
                Performance_Agent -> Aggregator_Node;
                Unit_Test_Agent -> Aggregator_Node;
                Aggregator_Node -> GitHub_PR_Comment;
            }
        ''')

    else:
        st.info("💡 **Use Case:** Real-time stream processing of user interactions via Kafka to generate immediate contextual recommendations.")
        st.graphviz_chart('''
            digraph {
                rankdir=LR;
                node [shape=box, style="filled,rounded", fillcolor="#F3E5F5", fontname="sans-serif"];
                Kafka_Cart_Stream -> Event_Consumer_Service;
                Event_Consumer_Service -> User_Embedding_Node;
                User_Embedding_Node -> Vector_Similarity_Search;
                Vector_Similarity_Search -> Recommender_Agent;
                Recommender_Agent -> FastAPI_Push_Notification;
            }
        ''')

# Tab 2: Projects
with tab_proj:
    st.header("Featured Projects")
    
    st.header("🚀 Featured Projects")
    
    # ---------------------------------------------------------
    # PROJECT 1: AI RESUME TAILORING & JOB MATCH ENGINE
    # ---------------------------------------------------------
    with st.expander("🎯 AI-Powered Semantic Resume Tailoring & Job Match Engine"):
        st.caption("Automated End-to-End Career Copilot | Vector Embeddings • LangChain • ATS Engine")
        
        # Action Links & Metrics
        col_m1, col_m2, col_m3, col_m4 = st.columns(4)
        col_m1.metric(label="Workflow Reduction", value="1-Click", delta="From 6 Steps")
        col_m2.metric(label="Time Saved / App", value="~2 Hours", delta="Instant PDF")
        col_m3.metric(label="Matching Method", value="Vector Cosine", delta="Semantic Similarity")
        col_m4.metric(label="ATS Optimization", value="Automated", delta="Keyword Alignment")
        
        st.markdown("[🔗 View Live Demo](https://lnkd.in/gbWujVCs) | [💻 GitHub Repository](https://lnkd.in/g5uhjbcm)")
        
        st.markdown("---")
        
        # Problem vs Solution Side-by-Side Comparison
        st.markdown("### ⚡ The Problem vs. The Solution")
        col_problem, col_solution = st.columns(2)
        
        with col_problem:
            st.error("#### ❌ The Old Manual Way (6-Step Loop)")
            st.markdown("""
            1. **Search & Filter:** Filter listings manually on multiple job portals.
            2. **Sift Listings:** Review 100+ job descriptions individually.
            3. **Manual Audit:** Cross-examine required skills against personal background.
            4. **Guess Alignment:** Manually judge match potential without metrics.
            5. **Custom Resume Engineering:** Spend 1–2 hours tweaking keywords for ATS.
            6. **Burnout Cycle:** Repeat 20–30 times per week with high fatigue.
            """)
            
        with col_solution:
            st.success("#### ⚡ The 1-Click Automated AI Solution")
            st.markdown("""
            1. **Upload Once:** Upload a single master `.pdf` or `.docx` resume.
            2. **Live Retrieval:** System fetches and parses job posts via live APIs.
            3. **Vector Semantic Search:** Embeddings evaluate context (e.g., *Spring Boot* ➔ *Spring MVC*).
            4. **Top 5 Ranking:** Pinpoints high-yield positions with maximum callback potential.
            5. **Skill-Gap Roadmap:** Identifies missing skills and builds an execution plan.
            6. **Instant ATS Resumes:** Auto-generates tailored resumes with live editing & PDF download.
            """)

        st.markdown("---")
        
        # Architectural Workflow Visualization
        st.markdown("### 🏗️ Pipeline Architecture")
        st.graphviz_chart('''
            digraph {
                rankdir=LR;
                node [shape=box, style="filled,rounded", fillcolor="#E3F2FD", fontname="sans-serif", fontsize=10];
                
                Resume [label="📄 Master Resume\n(PDF / DOCX)", fillcolor="#FFF3E0"];
                APIs [label="🌐 Live Job Portals\n(API Ingestion)", fillcolor="#E8F5E9"];
                Vector [label="🧠 Vector Embeddings\n(sentence-transformers)", fillcolor="#E1BEE7"];
                Match [label="📊 Cosine Match\n(Top 5 Selection)", fillcolor="#BBDEFB"];
                Gap [label="🗺️ Skill-Gap Analysis\n& Roadmap", fillcolor="#C8E6C9"];
                ATS [label="⚡ ATS Resume Generator\n(xhtml2pdf / python-docx)", fillcolor="#FFCDD2"];
                
                Resume -> Vector;
                APIs -> Vector;
                Vector -> Match;
                Match -> Gap;
                Match -> ATS;
            }
        ''')
        
        st.markdown("**Tech Stack:** `Python` `Streamlit` `LangChain` `Groq` `Sentence-Transformers` `Supabase` `xhtml2pdf` `python-docx`")

    st.markdown("---")
        
    with st.expander("🛒 ShopEase E-Commerce Platform with RAG & OpenAI"):
        st.write("""
        Developed an e-commerce backend platform featuring AI-driven search and recommendation capabilities.
        - Built RESTful APIs in **Spring Boot** managing inventory, cart, and orders integrated with **Angular**.
        - Integrated **OpenAI API**, **Apache Tika**, and **Apache Kafka** for automated product document processing and smart search.
        - Utilized **Spring Data JPA** with **MySQL** for relational persistence and **AWS S3** for media assets.
        """)
        st.markdown("**Tech Stack:** `Spring Boot` `MySQL` `OpenAI API` `Apache Kafka` `AWS S3` `Apache Tika` `JWT` `ELK Stack`")
        st.markdown("[GitHub Repository](#)")

# Tab 3: Experience
with tab_exp:
    st.header("Work Experience")
    
    st.subheader("Backend Engineer | Tata Consultancy Services (TCS)")
    st.caption("May 2025 – Present | Hybrid")
    st.write("""
    - **Core Impact:** Architected and migrated legacy procedural COBOL payment rails into modular, cloud-ready **Spring Boot microservices**, exposing secure RESTful APIs for the Gateway Payments ecosystem.
    - Utilized **Spring Data JPA** to remap mainframe flat files into relational schemas.
    - Containerized services using **Docker** for production deployments.
    """)
    
    st.markdown("---")
    
    st.subheader("Intern and Backend Engineer | Zediant Technologies")
    st.caption("Feb 2024 – May 2025 | Hybrid")
    st.write("""
    - Focused on backend development, API design, microservices architecture, and software lifecycle management.
    - Designed and implemented RESTful APIs using **Spring Boot** and optimized complex SQL queries for performance.
    """)

# Tab 4: Technical Skills
with tab_skills:
    st.header("Technical Skills & Proficiency")
    
    skills_data = {
        "Skill": ["Spring Boot / Java", "LangChain / LangGraph", "Python / GenAI", "SQL / Vector DBs", "Docker / AWS", "System Design"],
        "Proficiency Level (%)": [95, 90, 88, 85, 80, 85]
    }
    df_skills = pd.DataFrame(skills_data)
    fig = px.bar(df_skills, x="Proficiency Level (%)", y="Skill", orientation='h', color="Proficiency Level (%)", color_continuous_scale="Viridis")
    fig.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**AI & Data Tools:** LangChain, LangGraph, OpenAI API, LlamaIndex, ChromaDB, PGVector, Hugging Face")
        st.markdown("**Backend Frameworks:** Spring Boot, Spring Data JPA, Spring Security, Hibernate, Spring Batch, FastAPI")
    with col2:
        st.markdown("**Languages & Databases:** Java, Python, SQL, MySQL, PostgreSQL, MongoDB, Redis")
        st.markdown("**DevOps & Infrastructure:** AWS, GCP, Docker, CI/CD (GitHub Actions), Apache Kafka, Git")

# Tab 5: Education
with tab_edu:
    col_a, col_b = st.columns(2)
    with col_a:
        st.header("Education")
        st.subheader("B.Tech in Computer Science and Engineering")
        st.write("**St. Thomas' College of Engineering and Technology** (2020 – 2024)")
        st.write("📊 **Avg CGPA:** 9.0 / 10")
        
    with col_b:
        st.header("Key Achievements")
        st.write("- 🏆 **AIR-248** in All INDIA Contest")
        st.write("- 🥇 Recognition on **GeeksforGeeks** and multiple badges on **LeetCode**")
        st.write("- 📜 **Letter of Recommendation** for performance in Everest Team")

# ---------------------------------------------------------
# GET IN TOUCH SECTION (DIRECT POSTGRESQL INTEGRATION)
# ---------------------------------------------------------
st.markdown("---")
st.header("📬 Get In Touch")

# Initialize PostgreSQL Connection
conn = None
try:
    conn = st.connection("postgresql", type="sql",connect_args={"prepare_threshold": None})
except Exception as e:
    st.error(f"⚠️ Secrets Error: {e}")

with st.form("contact_form", clear_on_submit=True):
    c1, c2 = st.columns(2)
    with c1:
        user_name = st.text_input("Name")
    with c2:
        user_email = st.text_input("Email")
    user_msg = st.text_area("Message")
    
    submitted = st.form_submit_button("Send Message")
    
    if submitted:
        if not user_name or not user_email or not user_msg:
            st.warning("Please fill out all fields before submitting.")
        else:
            if conn:
                try:
                    with conn.session as session:
                        # Use sqlalchemy's text() instead of st.text()
                        query = text("INSERT INTO messages (name, email, message) VALUES (:name, :email, :message)")
                        session.execute(query, {"name": user_name, "email": user_email, "message": user_msg})
                        session.commit()
                    st.success("Thank you! Your message has been sent successfully.")
                except Exception as ex:
                    st.error(f"SQL Execution Error: {ex}")
            else:
                st.error("Database connection not configured. Check your .streamlit/secrets.toml file.")