import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="PHL201 - Information Networks and Moral Responsibility",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    font-family: 'Inter', sans-serif;
}

.paper-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

.paper-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.paper-author {
    font-size: 1.2rem;
    font-weight: 500;
    margin-bottom: 0.3rem;
}

.paper-affiliation {
    font-size: 1rem;
    opacity: 0.9;
}

.content-section {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    margin: 1rem 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.abstract-box {
    background: linear-gradient(135deg, #f0f4f8 0%, #e2e8f0 100%);
    border: 1px solid #cbd5e0;
    border-radius: 12px;
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.principle-box {
    background: linear-gradient(135deg, #e6f3ff 0%, #cce7ff 100%);
    border-left: 4px solid #4299e1;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
}

.prediction-box {
    background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
    border-left: 4px solid #38a169;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
}

.case-study-box {
    background: linear-gradient(135deg, #fff5f5 0%, #fed7d7 100%);
    border-left: 4px solid #e53e3e;
    padding: 1.5rem;
    margin: 1rem 0;
    border-radius: 0 8px 8px 0;
}

.discussion-box {
    background: linear-gradient(135deg, #e6fffa 0%, #b2f5ea 100%);
    border: 1px solid #81e6d9;
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.key-insight {
    background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    text-align: center;
    font-weight: 600;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}

.visualization-container {
    background: white;
    padding: 2rem;
    border-radius: 12px;
    margin: 1rem 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.interactive-demo {
    background: linear-gradient(135deg, #fef5e7 0%, #fed7aa 100%);
    padding: 2rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 2px solid #ed8936;
}

.quiz-container {
    background: linear-gradient(135deg, #f0fff4 0%, #c6f6d5 100%);
    padding: 2rem;
    border-radius: 12px;
    margin: 1rem 0;
    border: 2px solid #38a169;
}

.reference-item {
    background: #f7fafc;
    border-left: 3px solid #4299e1;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 0 4px 4px 0;
    font-size: 0.9rem;
}

.keywords {
    font-style: italic;
    color: #666;
    margin-top: 1rem;
    background: #f8f9fa;
    padding: 1rem;
    border-radius: 6px;
}

.metric-card {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="paper-header">
    <h1 class="paper-title">Information Networks and Moral Responsibility</h1>
    <h2 class="paper-author">Xavier Honablue, M.Ed.</h2>
    <p class="paper-affiliation">University of Michigan Ann Arbor • Masters Applied Data Science • September 2025</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.header("Paper Navigation")
    section = st.radio("Select Section:", [
        "Paper Overview",
        "Full Paper Text",
        "Abstract & Introduction", 
        "Theoretical Framework",
        "The IMR Model",
        "Case Studies",
        "Applications & Implications",
        "Discussion Questions",
        "References & Further Reading",
        "Interactive Demos"
    ])
    
    st.markdown("---")
    st.subheader("Study Tools")
    
    if st.button("Generate Citation", use_container_width=True):
        st.code("""
APA Citation:
Honablue, X. (2025). Information Networks and Moral 
Responsibility: How Digital Connectivity Transforms 
Ethical Obligations. University of Michigan Ann Arbor 
Masters Applied Data Science Program.

MLA Citation:
Honablue, Xavier. "Information Networks and Moral 
Responsibility: How Digital Connectivity Transforms 
Ethical Obligations." PHL201 Course Materials, 2025.
        """)
    
    st.info("Reading Time: ~25-30 minutes")

# Define content display function
def display_content():
    if section == "Paper Overview":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("Paper Overview")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.write("**Research Question:** How does digital connectivity transform moral responsibility in contemporary society?")
            st.write("**Methodology:** Interdisciplinary analysis drawing on moral psychology, network theory, and media studies")
            st.write("**Key Contribution:** The Information-Mediated Responsibility (IMR) model")
            
            st.markdown('<div class="key-insight">', unsafe_allow_html=True)
            st.write("Key Insight: Digital information doesn't just expand moral awareness—it fundamentally transforms the nature of moral responsibility itself.")
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Core Principles", "4")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Empirical Predictions", "4")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Case Studies", "3")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Learning Objectives")
        objectives = [
            "Analyze how digital information affects moral judgment and behavior",
            "Evaluate traditional ethical frameworks in digital contexts",
            "Apply the IMR model to contemporary moral challenges",
            "Critically assess technology's role in shaping moral communities"
        ]
        for i, obj in enumerate(objectives, 1):
            st.write(f"{i}. {obj}")

    elif section == "Full Paper Text":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("Information Networks and Moral Responsibility")
        st.subheader("How Digital Connectivity Transforms Ethical Obligations")
        
        st.write("**Xavier Honablue, M.Ed.**")
        st.write("University of Michigan Ann Arbor • Masters Applied Data Science")
        st.write("September 2025")
        
        st.subheader("Abstract")
        st.write("""
        This paper examines how information networks and digital connectivity affect moral responsibility 
        in contemporary global society. Drawing on empirical research in moral psychology, network theory, 
        and media studies, we analyze how awareness of distant suffering through digital media creates new 
        forms of moral obligation that challenge traditional proximity-based ethical frameworks. We propose 
        the Information-Mediated Responsibility (IMR) model, which accounts for how technological mediation 
        affects moral salience, emotional engagement, and behavioral response.
        """)
        
        st.markdown('<div class="keywords">', unsafe_allow_html=True)
        st.write("**Keywords:** moral responsibility, digital ethics, information networks, moral psychology, global ethics, media effects")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("1. Introduction")
        st.write("""
        The digital revolution has fundamentally altered the landscape of moral responsibility. Unlike 
        previous generations, who remained largely unaware of distant suffering, contemporary individuals 
        receive constant streams of information about global injustices, environmental crises, and human 
        rights violations. This unprecedented access to information about suffering raises profound questions 
        about the scope and nature of moral obligation.
        """)
        
        st.write("""
        Traditional ethical frameworks developed under assumptions of limited information and local communities. 
        Utilitarian calculations assumed practical constraints on knowledge and action. Virtue ethics focused 
        on character development within particular communities. Deontological systems emphasized universal 
        principles but were applied within contexts of limited awareness. None adequately address the moral 
        implications of instantaneous global information access.
        """)
        
        st.subheader("2. Theoretical Framework")
        st.write("""
        Research in moral psychology demonstrates that moral judgment depends heavily on salience - the degree 
        to which moral considerations capture attention and emotional engagement. Digital media fundamentally 
        alters moral salience through several mechanisms including proximity override, narrative framing, and 
        algorithmic curation.
        """)
        
        st.subheader("3. The Information-Mediated Responsibility Model")
        st.write("""
        The IMR model proposes that moral responsibility in digital environments operates according to four 
        core principles: Information Integration, Network Amplification, Cognitive Load, and Mediation Transparency. 
        Unlike purely theoretical frameworks, IMR generates specific testable predictions about how digital 
        connectivity affects moral response.
        """)
        
        st.subheader("Conclusion")
        st.write("""
        The Information-Mediated Responsibility model provides a framework for understanding how digital 
        connectivity transforms moral obligation. Key insights include recognition that moral responsibility 
        is not simply expanded by information access but qualitatively transformed, network effects create 
        collective moral phenomena that exceed individual moral capacities, and technological mediation affects 
        moral judgment in ways requiring critical literacy.
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Abstract & Introduction":
        st.markdown('<div class="abstract-box">', unsafe_allow_html=True)
        st.subheader("Abstract")
        st.write("""
        This paper examines how information networks and digital connectivity affect moral responsibility in 
        contemporary global society. We propose the Information-Mediated Responsibility (IMR) model, which 
        accounts for how technological mediation affects moral salience, emotional engagement, and behavioral response.
        """)
        
        st.markdown('<div class="keywords">', unsafe_allow_html=True)
        st.write("**Keywords:** moral responsibility, digital ethics, information networks, moral psychology, global ethics, media effects")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("Introduction")
        st.write("""
        The digital revolution has fundamentally altered the landscape of moral responsibility. Traditional ethical 
        frameworks don't adequately address the moral implications of instantaneous global information access. 
        The Information-Mediated Responsibility (IMR) model provides a framework for understanding how digital 
        connectivity transforms moral obligations.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Theoretical Framework":
        st.subheader("Theoretical Framework")
        
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("Moral Salience and Information Exposure")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="principle-box">', unsafe_allow_html=True)
            st.write("**Proximity Override**")
            st.write("Visual media makes distant suffering more psychologically proximate than local issues.")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown('<div class="principle-box">', unsafe_allow_html=True)
            st.write("**Narrative Framing**")
            st.write("Digital platforms use storytelling techniques that enhance emotional engagement.")
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col3:
            st.markdown('<div class="principle-box">', unsafe_allow_html=True)
            st.write("**Algorithmic Curation**")
            st.write("Social media algorithms create echo chambers that amplify certain moral concerns.")
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "The IMR Model":
        st.subheader("The Information-Mediated Responsibility Model")
        
        st.markdown('<div class="key-insight">', unsafe_allow_html=True)
        st.write("The IMR Model: A framework for understanding how digital connectivity transforms moral obligations through four core principles and testable predictions.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Core Principles")
        
        principles = [
            ("Information Integration Principle", "Moral obligations arise through integration of factual information, emotional engagement, and capacity for effective action."),
            ("Network Amplification Principle", "Individual moral responses are amplified or diminished through network effects."),
            ("Cognitive Load Principle", "Moral responsiveness is subject to cognitive limitations that create systematic biases."),
            ("Mediation Transparency Principle", "Technological mediation affects moral judgment in ways often invisible to the moral agent.")
        ]
        
        for i, (title, description) in enumerate(principles, 1):
            st.markdown('<div class="principle-box">', unsafe_allow_html=True)
            st.write(f"**{i}. {title}**")
            st.write(description)
            st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Case Studies":
        st.subheader("Case Studies")
        
        case_studies = [
            {
                "title": "Social Media and Crisis Response: 2010 Haiti Earthquake",
                "points": [
                    "Attention Decay: Initial massive engagement declined rapidly",
                    "Visible vs. Invisible Needs: Rescue efforts received disproportionate support",
                    "Geographic Bias: Haiti received more aid than simultaneous crises elsewhere"
                ]
            },
            {
                "title": "Climate Change and Temporal Responsibility", 
                "points": [
                    "Present Bias: Reduced engagement with future suffering",
                    "Causal Opacity: Complex causal chains reduce personal responsibility",
                    "Statistical vs. Narrative: Abstract statistics generate less engagement"
                ]
            },
            {
                "title": "Global Health Inequities: COVID-19 Pandemic",
                "points": [
                    "Initial Universalism: Unprecedented global cooperation",
                    "Rapid Localization: Moral concern narrowed to local priorities",
                    "Information Fatigue: Sustained exposure led to decreased engagement"
                ]
            }
        ]
        
        for study in case_studies:
            st.markdown('<div class="case-study-box">', unsafe_allow_html=True)
            st.subheader(study["title"])
            for point in study["points"]:
                st.write(f"• {point}")
            st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Applications & Implications":
        st.subheader("Applications & Implications")
        
        tab1, tab2, tab3 = st.tabs(["System Design", "Education", "Policy"])
        
        with tab1:
            st.subheader("Ethical Design of Information Systems")
            design_principles = [
                "Moral Calibration: Promote appropriate rather than maximal emotional engagement",
                "Attention Distribution: Avoid concentrating attention on less significant issues",
                "Action Facilitation: Couple information with concrete action opportunities",
                "Transparency Requirements: Users should understand algorithmic curation"
            ]
            for principle in design_principles:
                st.markdown('<div class="principle-box">', unsafe_allow_html=True)
                st.write(principle)
                st.markdown('</div>', unsafe_allow_html=True)
        
        with tab2:
            st.subheader("Educational Implications")
            education_areas = [
                "Media Effects Education: Instruction in how digital media affects moral judgment",
                "Network Awareness: Understanding how social networks shape moral beliefs",
                "Cognitive Bias Training: Recognition of systematic limitations",
                "Practical Ethics: Frameworks for navigating complex moral environments"
            ]
            for area in education_areas:
                st.markdown('<div class="principle-box">', unsafe_allow_html=True)
                st.write(area)
                st.markdown('</div>', unsafe_allow_html=True)
        
        with tab3:
            st.subheader("Policy Recommendations")
            policy_areas = [
                "Platform Transparency: Requirements for disclosure of algorithmic curation",
                "Information Diversity: Policies promoting diverse moral perspectives",
                "Attention Protection: Recognition of attention as finite moral resource",
                "Global Information Justice: Equitable representation of global concerns"
            ]
            for area in policy_areas:
                st.markdown('<div class="principle-box">', unsafe_allow_html=True)
                st.write(area)
                st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Discussion Questions":
        st.subheader("Discussion Questions")
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.subheader("Critical Thinking Questions")
        
        questions = [
            "How does the IMR model challenge traditional notions of moral proximity?",
            "What are the ethical implications of algorithmic curation of moral content?",
            "How might the principles of the IMR model apply to emerging technologies?",
            "Is there such a thing as 'too much' moral information?",
            "What role should education play in developing 'digital moral literacy'?",
            "Can the IMR model help explain contemporary political polarization online?"
        ]
        
        for i, question in enumerate(questions, 1):
            with st.expander(f"Question {i}: {question}"):
                st.write(question)
                st.text_area(f"Your thoughts:", key=f"q{i}", height=100)
        
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "References & Further Reading":
        st.subheader("References & Further Reading")
        
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("Primary References")
        
        references = [
            "Greene, J. D. (2013). Moral tribes: Emotion, reason, and the gap between us and them. Penguin Press.",
            "Haidt, J. (2012). The righteous mind: Why good people are divided by politics and religion. Vintage Books.",
            "Pariser, E. (2011). The filter bubble: What the Internet is hiding from you. Penguin Press.",
            "Sunstein, C. R. (2017). #Republic: Divided democracy in the age of social media. Princeton University Press."
        ]
        
        for ref in references:
            st.markdown(f'<div class="reference-item">{ref}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Interactive Demos":
        st.subheader("Interactive Demos")
        
        st.markdown('<div class="interactive-demo">', unsafe_allow_html=True)
        st.subheader("Demo: Moral Salience Simulator")
        st.write("Compare how different presentation formats affect moral engagement:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Statistical Presentation:**")
            st.write("• 50,000 people affected by crisis")
            st.write("• $2 million in damages")
            engagement_stats = st.slider("Rate emotional engagement (Statistical):", 1, 10, 4)
        
        with col2:
            st.write("**Narrative Presentation:**")
            st.write("• Maria, a mother of three, lost her home")
            st.write("• Her children sleep in a school gymnasium")
            engagement_narrative = st.slider("Rate emotional engagement (Narrative):", 1, 10, 7)
        
        if engagement_narrative > engagement_stats:
            st.success("Your response demonstrates the narrative superiority effect!")
        elif engagement_stats > engagement_narrative:
            st.info("You show stronger response to statistical information.")
        else:
            st.info("You show equal engagement with both formats.")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Quiz Section
        st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
        st.subheader("Test Your Understanding")
        
        with st.form("quiz_form"):
            q1 = st.radio(
                "What are the three components necessary for full moral responsibility in the IMR model?",
                ["Knowledge, Action, Emotion", "Information, Engagement, Capacity", "Awareness, Empathy, Response"]
            )
            
            q2 = st.radio(
                "The 'psychic numbing' effect refers to:",
                ["Becoming overwhelmed by information", "Decreased moral response as victim numbers increase", "Loss of empathy over time"]
            )
            
            submitted = st.form_submit_button("Submit Quiz")
            
            if submitted:
                correct_answers = ["Information, Engagement, Capacity", "Decreased moral response as victim numbers increase"]
                user_answers = [q1, q2]
                score = sum(1 for i, answer in enumerate(user_answers) if answer == correct_answers[i])
                
                st.write(f"**Score: {score}/2**")
                
                if score == 2:
                    st.success("Perfect! You understand the IMR model well.")
                elif score == 1:
                    st.info("Good! Review the theoretical framework for better understanding.")
                else:
                    st.warning("Consider re-reading the paper sections.")
        
        st.markdown('</div>', unsafe_allow_html=True)

# Run the display function
display_content()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Course Information**")
    st.write("PHL201: Digital Ethics")
    st.write("University of Michigan Ann Arbor")

with col2:
    st.markdown("**Author**")
    st.write("Xavier Honablue, M.Ed.")
    st.write("September 2025")
    
with col3:
    st.markdown("**Actions**")
    if st.button("Copy Citation"):
        st.success("Citation copied!")

st.markdown("---")
st.markdown("### Reflection Prompt")
st.markdown("After engaging with this paper, consider: How has your understanding of moral responsibility changed in light of our digital connectivity?")

reflection = st.text_area("Share your reflection:", height=100)
if reflection:
    st.success("Thank you for your thoughtful reflection!")
