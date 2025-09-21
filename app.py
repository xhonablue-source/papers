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
        st.markdown("""
        <div style="background: white; padding: 3rem; border-radius: 12px; margin: 1rem 0; box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-size: 1rem; line-height: 1.8; text-align: justify;">
        
        <div style="text-align: center; margin-bottom: 3rem; padding-bottom: 2rem; border-bottom: 2px solid #e2e8f0;">
            <h1 style="color: #2d3748; font-size: 2.2rem; margin-bottom: 1rem;">Information Networks and Moral Responsibility</h1>
            <h2 style="color: #4a5568; font-size: 1.4rem; margin-bottom: 1rem;">How Digital Connectivity Transforms Ethical Obligations</h2>
            <p style="font-size: 1.1rem; color: #2d3748; margin-bottom: 0.5rem;"><strong>Xavier Honablue, M.Ed.</strong></p>
            <p style="color: #666;">University of Michigan Ann Arbor • Masters Applied Data Science<br>September 2025</p>
        </div>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">Abstract</h2>
        
        <div style="background: #f0f4f8; padding: 2rem; border-radius: 8px; margin: 1rem 0; border-left: 4px solid #667eea;">
            <p>This paper examines how information networks and digital connectivity affect moral responsibility in contemporary global society. Drawing on empirical research in moral psychology, network theory, and media studies, we analyze how awareness of distant suffering through digital media creates new forms of moral obligation that challenge traditional proximity-based ethical frameworks. We propose the <strong>Information-Mediated Responsibility (IMR) model</strong>, which accounts for how technological mediation affects moral salience, emotional engagement, and behavioral response.</p>
            
            <p>Key findings include: (1) digital information exposure creates measurable changes in moral judgment patterns, (2) network effects amplify individual moral responses through social reinforcement mechanisms, and (3) information overload can paradoxically reduce moral responsiveness through psychological defense mechanisms. We conclude with practical recommendations for ethical engagement in digital environments and educational approaches for developing critical moral literacy in an interconnected world.</p>
            
            <p style="font-style: italic; margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e2e8f0;"><strong>Keywords:</strong> moral responsibility, digital ethics, information networks, moral psychology, global ethics, media effects</p>
        </div>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">1. Introduction</h2>
        
        <p>The digital revolution has fundamentally altered the landscape of moral responsibility. Unlike previous generations, who remained largely unaware of distant suffering, contemporary individuals receive constant streams of information about global injustices, environmental crises, and human rights violations. This unprecedented access to information about suffering raises profound questions about the scope and nature of moral obligation.</p>

        <p>Traditional ethical frameworks developed under assumptions of limited information and local communities. Utilitarian calculations assumed practical constraints on knowledge and action. Virtue ethics focused on character development within particular communities. Deontological systems emphasized universal principles but were applied within contexts of limited awareness. None adequately address the moral implications of instantaneous global information access.</p>

        <p>This paper proposes the Information-Mediated Responsibility (IMR) model as a framework for understanding how digital connectivity transforms moral obligations. Unlike speculative theoretical approaches, IMR builds on established research in moral psychology, media effects, and network theory to generate empirically grounded insights about contemporary ethical challenges.</p>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">2. Theoretical Framework</h2>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">2.1 Moral Salience and Information Exposure</h3>
        
        <p>Research in moral psychology demonstrates that moral judgment depends heavily on salience - the degree to which moral considerations capture attention and emotional engagement (Greene, 2013; Haidt, 2012). Digital media fundamentally alters moral salience through several mechanisms:</p>

        <div style="background: #e6f3ff; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #4299e1;">
            <p><strong>Proximity Override:</strong> Visual media can make distant suffering more psychologically proximate than local issues. Neuroimaging studies show that viewing images of distant suffering activates similar empathy networks as witnessing local distress (Decety & Jackson, 2004).</p>

            <p><strong>Narrative Framing:</strong> Digital platforms use storytelling techniques that enhance emotional engagement with distant moral issues. Research indicates that narrative structure significantly influences moral judgment independent of factual content (Nussbaum, 2001).</p>

            <p><strong>Algorithmic Curation:</strong> Social media algorithms selectively expose users to morally charged content based on engagement patterns, creating echo chambers that amplify certain moral concerns while obscuring others (Pariser, 2011).</p>
        </div>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">2.2 Network Effects in Moral Responsibility</h3>
        
        <p>Social network theory provides tools for understanding how individual moral responses aggregate into collective moral phenomena:</p>

        <p><strong>Moral Cascade Effects:</strong> When individuals observe others responding to moral issues, they become more likely to respond themselves, creating cascading waves of moral engagement (Bicchieri, 2006).</p>

        <p><strong>Diffusion of Responsibility:</strong> Paradoxically, awareness that many others are also aware of moral issues can reduce individual feelings of responsibility through diffusion effects documented in social psychology (Latané & Darley, 1970).</p>

        <p><strong>Network Polarization:</strong> Digital networks can amplify moral polarization by sorting individuals into like-minded communities that reinforce existing moral commitments while demonizing alternative perspectives (Sunstein, 2017).</p>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">2.3 Information Overload and Moral Numbing</h3>
        
        <p>Psychological research reveals systematic limitations in human capacity to process moral information:</p>

        <p><strong>Finite Pool of Worry:</strong> Individuals have limited capacity for moral concern, leading to zero-sum competition between moral issues for attention and emotional engagement (Weber, 2006).</p>

        <p><strong>Compassion Fatigue:</strong> Repeated exposure to suffering can reduce empathetic responding through psychological defense mechanisms (Figley, 2002).</p>

        <p><strong>Psychic Numbing:</strong> Research demonstrates that moral responsiveness decreases as the number of victims increases, violating normative principles of proportional response (Slovic, 2007).</p>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">3. The Information-Mediated Responsibility Model</h2>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">3.1 Core Principles</h3>
        
        <p>The IMR model proposes that moral responsibility in digital environments operates according to the following principles:</p>

        <div style="background: #e6f3ff; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #4299e1;">
            <p><strong>Information Integration Principle:</strong> Moral obligations arise through the integration of factual information, emotional engagement, and capacity for effective action. All three components are necessary for full moral responsibility.</p>
        </div>

        <div style="background: #e6f3ff; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #4299e1;">
            <p><strong>Network Amplification Principle:</strong> Individual moral responses are amplified or diminished through network effects that can either reinforce or undermine moral engagement.</p>
        </div>

        <div style="background: #e6f3ff; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #4299e1;">
            <p><strong>Cognitive Load Principle:</strong> Moral responsiveness is subject to cognitive limitations that create systematic biases in how individuals process moral information.</p>
        </div>

        <div style="background: #e6f3ff; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #4299e1;">
            <p><strong>Mediation Transparency Principle:</strong> The technological mediation of moral information affects moral judgment in ways that are often invisible to the moral agent, requiring critical literacy for appropriate moral response.</p>
        </div>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">3.2 Empirical Predictions</h3>
        
        <p>Unlike purely theoretical frameworks, IMR generates specific testable predictions:</p>

        <div style="background: #f0fff4; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #38a169;">
            <p><strong>Prediction 1:</strong> Individuals exposed to narrative-rich presentations of distant suffering will show greater moral engagement than those receiving statistical information about larger-scale suffering.</p>
        </div>

        <div style="background: #f0fff4; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #38a169;">
            <p><strong>Prediction 2:</strong> Moral responsiveness will correlate with network position, with individuals at network centers showing both greater initial engagement and faster saturation effects.</p>
        </div>

        <div style="background: #f0fff4; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #38a169;">
            <p><strong>Prediction 3:</strong> Individuals will show measurable decreases in moral responsiveness when exposed to multiple simultaneous moral demands compared to sequential presentation.</p>
        </div>

        <div style="background: #f0fff4; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #38a169;">
            <p><strong>Prediction 4:</strong> Training in media literacy will improve calibration between moral response and objective moral significance of issues.</p>
        </div>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">4. Case Studies</h2>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">4.1 Social Media and Crisis Response</h3>
        
        <div style="background: #fff5f5; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #e53e3e;">
            <p>The 2010 Haiti earthquake provides a paradigmatic case of information-mediated moral responsibility. Social media enabled unprecedented rapid response, with millions of individuals donating through text messaging within hours of the disaster. However, analysis reveals several concerning patterns:</p>
            
            <ul style="margin: 1rem 0;">
                <li><strong>Attention Decay:</strong> Initial massive engagement declined rapidly as media attention shifted, despite ongoing need</li>
                <li><strong>Visible vs. Invisible Needs:</strong> Highly visible rescue efforts received disproportionate support compared to less dramatic but equally important infrastructure needs</li>
                <li><strong>Geographic Bias:</strong> Haiti received more per-capita aid than simultaneous crises in less media-accessible regions</li>
            </ul>
        </div>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">4.2 Climate Change and Temporal Responsibility</h3>
        
        <div style="background: #fff5f5; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #e53e3e;">
            <p>Climate change presents unique challenges for information-mediated responsibility due to temporal distance and causal complexity:</p>
            
            <ul style="margin: 1rem 0;">
                <li><strong>Present Bias:</strong> Individuals show reduced moral engagement with future compared to present suffering, even when future suffering is more severe</li>
                <li><strong>Causal Opacity:</strong> Complex causal chains between individual action and climate outcomes reduce feelings of personal responsibility</li>
                <li><strong>Statistical vs. Narrative:</strong> Abstract statistics about future climate impacts generate less moral engagement than personal stories about present climate effects</li>
            </ul>
        </div>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">4.3 Global Health Inequities</h3>
        
        <div style="background: #fff5f5; padding: 1.5rem; margin: 1rem 0; border-radius: 8px; border-left: 4px solid #e53e3e;">
            <p>The COVID-19 pandemic revealed both possibilities and limitations of global moral solidarity:</p>
            
            <ul style="margin: 1rem 0;">
                <li><strong>Initial Universalism:</strong> Early pandemic response showed unprecedented global cooperation based on shared vulnerability</li>
                <li><strong>Rapid Localization:</strong> As vaccines became available, moral concern quickly narrowed to national and local priorities</li>
                <li><strong>Information Fatigue:</strong> Sustained information exposure led to measurable decreases in moral engagement over time</li>
            </ul>
        </div>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">5. Practical Applications</h2>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">5.1 Ethical Design of Information Systems</h3>
        
        <p>IMR analysis suggests several principles for ethical design of information systems:</p>
        
        <p><strong>Moral Calibration:</strong> Systems should present moral information in ways that promote appropriate rather than maximal emotional engagement.</p>
        
        <p><strong>Attention Distribution:</strong> Platforms should avoid algorithms that concentrate moral attention on highly engaging but potentially less significant issues.</p>
        
        <p><strong>Action Facilitation:</strong> Moral information should be coupled with concrete, effective action opportunities to prevent learned helplessness.</p>
        
        <p><strong>Transparency Requirements:</strong> Users should understand how algorithmic curation affects their moral information environment.</p>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">5.2 Educational Implications</h3>
        
        <p>Digital moral literacy requires new educational approaches:</p>
        
        <p><strong>Media Effects Education:</strong> Students need explicit instruction in how digital media affects moral judgment and behavior.</p>
        
        <p><strong>Network Awareness:</strong> Understanding how social networks shape moral beliefs and responses.</p>
        
        <p><strong>Cognitive Bias Training:</strong> Recognition of systematic limitations in moral information processing.</p>
        
        <p><strong>Practical Ethics:</strong> Development of frameworks for navigating complex moral information environments.</p>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">5.3 Policy Recommendations</h3>
        
        <p>Several policy interventions could improve moral information environments:</p>
        
        <p><strong>Platform Transparency:</strong> Requirements for social media platforms to disclose algorithmic curation of moral content.</p>
        
        <p><strong>Information Diversity:</strong> Policies promoting exposure to diverse moral perspectives and global moral concerns.</p>
        
        <p><strong>Attention Protection:</strong> Recognition that human attention is a finite moral resource requiring protection from exploitation.</p>
        
        <p><strong>Global Information Justice:</strong> Efforts to ensure equitable representation of global moral concerns in information systems.</p>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">6. Limitations and Future Research</h2>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">6.1 Methodological Limitations</h3>
        
        <p>Current research on information-mediated moral responsibility faces several limitations:</p>
        
        <ul style="margin: 1rem 0;">
            <li><strong>Correlation vs. Causation:</strong> Much evidence is correlational, making causal claims tentative</li>
            <li><strong>Cultural Specificity:</strong> Most studies focus on Western, educated populations</li>
            <li><strong>Laboratory vs. Real-World:</strong> Experimental studies may not generalize to complex real-world moral environments</li>
            <li><strong>Temporal Constraints:</strong> Long-term effects of digital moral engagement remain understudied</li>
        </ul>

        <h3 style="color: #4a5568; margin: 1.5rem 0 1rem;">6.2 Future Research Directions</h3>
        
        <p>Several research programs could advance understanding of information-mediated moral responsibility:</p>
        
        <p><strong>Longitudinal Studies:</strong> Tracking how digital moral engagement evolves over time and life course.</p>
        
        <p><strong>Cross-Cultural Research:</strong> Examining how cultural differences affect information-mediated moral responsibility.</p>
        
        <p><strong>Intervention Studies:</strong> Testing specific approaches for improving moral calibration in digital environments.</p>
        
        <p><strong>Neuroscience Applications:</strong> Using brain imaging to understand neural mechanisms of digitally mediated moral response.</p>
        
        <p><strong>Network Analysis:</strong> Large-scale studies of how moral beliefs and behaviors spread through digital networks.</p>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">7. Conclusion</h2>
        
        <p>The Information-Mediated Responsibility model provides a framework for understanding how digital connectivity transforms moral obligation. Unlike traditional ethical theories developed for limited-information environments, IMR acknowledges both the opportunities and limitations created by global information access.</p>

        <p>Key insights include recognition that:</p>
        
        <ul style="margin: 1rem 0;">
            <li>Moral responsibility is not simply expanded by information access but qualitatively transformed</li>
            <li>Network effects create collective moral phenomena that exceed individual moral capacities</li>
            <li>Cognitive limitations require systematic approaches to moral information management</li>
            <li>Technological mediation affects moral judgment in ways requiring critical literacy</li>
        </ul>

        <p>These insights have practical implications for educational curricula, platform design, and public policy. As digital connectivity continues to evolve, developing sophisticated frameworks for information-mediated moral responsibility becomes increasingly urgent.</p>

        <p>The goal is not to maximize moral engagement but to calibrate it appropriately - responding to genuine moral demands while avoiding the psychological defense mechanisms that lead to moral numbing and disengagement. This requires both individual moral literacy and collective efforts to create information environments that support rather than undermine moral agency.</p>

        <p>Future research should focus on empirical testing of IMR predictions and development of practical tools for navigating moral complexity in digital environments. The stakes are high: our capacity for appropriate moral response to global challenges may depend on our ability to understand and manage the transformation of moral responsibility in the digital age.</p>

        <h2 style="color: #2d3748; margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid #667eea;">References</h2>
        
        <div style="background: #f7fafc; padding: 2rem; border-radius: 8px; margin: 1rem 0;">
            <p>Bicchieri, C. (2006). <em>The grammar of society: The nature and dynamics of social norms</em>. Cambridge University Press.</p>

            <p>Decety, J., & Jackson, P. L. (2004). The functional architecture of human empathy. <em>Behavioral and Cognitive Neuroscience Reviews</em>, 3(2), 71-100.</p>

            <p>Figley, C. R. (2002). Compassion fatigue: Psychotherapists' chronic lack of self care. <em>Journal of Clinical Psychology</em>, 58(11), 1433-1441.</p>

            <p>Greene, J. D. (2013). <em>Moral tribes: Emotion, reason, and the gap between us and them</em>. Penguin Press.</p>

            <p>Haidt, J. (2012). <em>The righteous mind: Why good people are divided by politics and religion</em>. Vintage Books.</p>

            <p>Latané, B., & Darley, J. M. (1970). <em>The unresponsive bystander: Why doesn't he help?</em> Appleton-Century-Crofts.</p>

            <p>Nussbaum, M. C. (2001). <em>Upheavals of thought: The intelligence of emotions</em>. Cambridge University Press.</p>

            <p>Pariser, E. (2011). <em>The filter bubble: What the Internet is hiding from you</em>. Penguin Press.</p>

            <p>Slovic, P. (2007). "If I look at the mass I will never act": Psychic numbing and genocide. <em>Judgment and Decision Making</em>, 2(2), 79-95.</p>

            <p>Sunstein, C. R. (2017). <em>#Republic: Divided democracy in the age of social media</em>. Princeton University Press.</p>

            <p>Weber, E. U. (2006). Experience-based and description-based perceptions of long-term risk: Why global warming does not scare us (yet). <em>Climatic Change</em>, 77(1-2), 103-120.</p>
        </div>
        
        </div>
        """, unsafe_allow_html=True)

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
