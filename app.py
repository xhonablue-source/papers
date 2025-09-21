import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

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
    background: #f8f9fa;
    font-family: 'Inter', sans-serif;
}

.paper-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 2rem;
    text-align: center;
}

.paper-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.paper-author {
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 0.3rem;
}

.paper-affiliation {
    font-size: 0.9rem;
    opacity: 0.9;
}

.section-header {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    border-left: 4px solid #667eea;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.abstract-box {
    background: #f0f4f8;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1.5rem;
    margin: 1rem 0;
}

.content-section {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.reference-item {
    background: #f7fafc;
    border-left: 3px solid #4299e1;
    padding: 0.8rem;
    margin: 0.5rem 0;
    border-radius: 0 4px 4px 0;
}

.discussion-box {
    background: #e6fffa;
    border: 1px solid #81e6d9;
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
}

.key-insight {
    background: linear-gradient(135deg, #ffd89b 0%, #19547b 100%);
    color: white;
    padding: 1rem;
    border-radius: 8px;
    margin: 1rem 0;
    text-align: center;
    font-weight: 600;
}

.visualization-container {
    background: white;
    padding: 1.5rem;
    border-radius: 8px;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.full-paper-text {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    margin: 1rem 0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    font-size: 0.95rem;
    line-height: 1.6;
}

.paper-section {
    margin-bottom: 2rem;
}

.keywords {
    font-style: italic;
    color: #666;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="paper-header">
    <h1 class="paper-title">Information Networks and Moral Responsibility</h1>
    <h2 class="paper-author">Xavier Honablue, M.Ed.</h2>
    <p class="paper-affiliation">University of Michigan Ann Arbor • MADS Scholar • September 2025</p>
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
        "References & Further Reading"
    ])
    
    st.markdown("---")
    st.subheader("Study Tools")
    if st.button("Download Paper", use_container_width=True):
        st.info("Paper download would be available in full implementation")
    
    if st.button("Citation Format", use_container_width=True):
        st.code("""
Honablue, X. (2025). Information Networks and Moral 
Responsibility: How Digital Connectivity Transforms 
Ethical Obligations. PHL201 Course Materials.
        """)

# Define content display function
def display_content():
    if section == "Paper Overview":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("📖 Paper Overview")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("**Research Question:** How does digital connectivity transform moral responsibility in contemporary society?")
        
        st.write("**Methodology:** Interdisciplinary analysis drawing on moral psychology, network theory, and media studies")
        
        st.write("**Key Contribution:** The Information-Mediated Responsibility (IMR) model - a framework for understanding ethical obligations in digital environments")
        
        st.subheader("🎯 Learning Objectives")
        st.write("After engaging with this paper, students will be able to:")
        st.write("• Analyze how digital information affects moral judgment and behavior")
        st.write("• Evaluate the strengths and limitations of traditional ethical frameworks in digital contexts") 
        st.write("• Apply the IMR model to contemporary moral challenges")
        st.write("• Critically assess the role of technology in shaping moral communities")
        
        # Visualization: Moral Information Flow
        st.markdown('<div class="visualization-container">', unsafe_allow_html=True)
        st.subheader("Moral Information Flow in Digital Networks")
        
        # Create network visualization
        fig = go.Figure()
        
        # Add nodes
        fig.add_trace(go.Scatter(
            x=[0, 1, 2, 1, 0.5, 1.5, 1],
            y=[1, 2, 1, 0, 0.5, 0.5, 1],
            mode='markers+text',
            text=['Individual', 'Media', 'Global Event', 'Community', 'Response 1', 'Response 2', 'Moral Agent'],
            textposition='middle center',
            marker=dict(size=[40, 60, 80, 50, 30, 30, 45], 
                       color=['lightblue', 'orange', 'red', 'green', 'yellow', 'yellow', 'purple']),
            showlegend=False
        ))
        
        # Add connections
        connections = [(0,1), (1,2), (1,3), (0,4), (0,5), (3,6), (1,6)]
        for start, end in connections:
            x_coords = [fig.data[0].x[start], fig.data[0].x[end]]
            y_coords = [fig.data[0].y[start], fig.data[0].y[end]]
            fig.add_trace(go.Scatter(
                x=x_coords, y=y_coords,
                mode='lines',
                line=dict(width=2, color='gray'),
                showlegend=False
            ))
        
        fig.update_layout(
            title="How Information Networks Shape Moral Response",
            xaxis=dict(showgrid=False, showticklabels=False),
            yaxis=dict(showgrid=False, showticklabels=False),
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Full Paper Text":
        st.markdown('<div class="full-paper-text">', unsafe_allow_html=True)
        
        st.write("""
        # Information Networks and Moral Responsibility: How Digital Connectivity Transforms Ethical Obligations

        **Xavier Honablue, M.Ed.**  
        University of Michigan Ann Arbor • MADS Scholar  
        September 2025

        ## Abstract

        This paper examines how information networks and digital connectivity affect moral responsibility in contemporary global society. Drawing on empirical research in moral psychology, network theory, and media studies, we analyze how awareness of distant suffering through digital media creates new forms of moral obligation that challenge traditional proximity-based ethical frameworks. We propose the Information-Mediated Responsibility (IMR) model, which accounts for how technological mediation affects moral salience, emotional engagement, and behavioral response. Key findings include: (1) digital information exposure creates measurable changes in moral judgment patterns, (2) network effects amplify individual moral responses through social reinforcement mechanisms, and (3) information overload can paradoxically reduce moral responsiveness through psychological defense mechanisms. We conclude with practical recommendations for ethical engagement in digital environments and educational approaches for developing critical moral literacy in an interconnected world.

        **Keywords:** moral responsibility, digital ethics, information networks, moral psychology, global ethics, media effects

        ## 1. Introduction

        The digital revolution has fundamentally altered the landscape of moral responsibility. Unlike previous generations, who remained largely unaware of distant suffering, contemporary individuals receive constant streams of information about global injustices, environmental crises, and human rights violations. This unprecedented access to information about suffering raises profound questions about the scope and nature of moral obligation.

        Traditional ethical frameworks developed under assumptions of limited information and local communities. Utilitarian calculations assumed practical constraints on knowledge and action. Virtue ethics focused on character development within particular communities. Deontological systems emphasized universal principles but were applied within contexts of limited awareness. None adequately address the moral implications of instantaneous global information access.

        This paper proposes the Information-Mediated Responsibility (IMR) model as a framework for understanding how digital connectivity transforms moral obligations. Unlike speculative theoretical approaches, IMR builds on established research in moral psychology, media effects, and network theory to generate empirically grounded insights about contemporary ethical challenges.

        ## 2. Theoretical Framework

        ### 2.1 Moral Salience and Information Exposure

        Research in moral psychology demonstrates that moral judgment depends heavily on salience - the degree to which moral considerations capture attention and emotional engagement (Greene, 2013; Haidt, 2012). Digital media fundamentally alters moral salience through several mechanisms:

        **Proximity Override**: Visual media can make distant suffering more psychologically proximate than local issues. Neuroimaging studies show that viewing images of distant suffering activates similar empathy networks as witnessing local distress (Decety & Jackson, 2004).

        **Narrative Framing**: Digital platforms use storytelling techniques that enhance emotional engagement with distant moral issues. Research indicates that narrative structure significantly influences moral judgment independent of factual content (Nussbaum, 2001).

        **Algorithmic Curation**: Social media algorithms selectively expose users to morally charged content based on engagement patterns, creating echo chambers that amplify certain moral concerns while obscuring others (Pariser, 2011).

        ### 2.2 Network Effects in Moral Responsibility

        Social network theory provides tools for understanding how individual moral responses aggregate into collective moral phenomena:

        **Moral Cascade Effects**: When individuals observe others responding to moral issues, they become more likely to respond themselves, creating cascading waves of moral engagement (Bicchieri, 2006).

        **Diffusion of Responsibility**: Paradoxically, awareness that many others are also aware of moral issues can reduce individual feelings of responsibility through diffusion effects documented in social psychology (Latané & Darley, 1970).

        **Network Polarization**: Digital networks can amplify moral polarization by sorting individuals into like-minded communities that reinforce existing moral commitments while demonizing alternative perspectives (Sunstein, 2017).

        ### 2.3 Information Overload and Moral Numbing

        Psychological research reveals systematic limitations in human capacity to process moral information:

        **Finite Pool of Worry**: Individuals have limited capacity for moral concern, leading to zero-sum competition between moral issues for attention and emotional engagement (Weber, 2006).

        **Compassion Fatigue**: Repeated exposure to suffering can reduce empathetic responding through psychological defense mechanisms (Figley, 2002).

        **Psychic Numbing**: Research demonstrates that moral responsiveness decreases as the number of victims increases, violating normative principles of proportional response (Slovic, 2007).

        ## 3. The Information-Mediated Responsibility Model

        ### 3.1 Core Principles

        The IMR model proposes that moral responsibility in digital environments operates according to the following principles:

        **Information Integration Principle**: Moral obligations arise through the integration of factual information, emotional engagement, and capacity for effective action. All three components are necessary for full moral responsibility.

        **Network Amplification Principle**: Individual moral responses are amplified or diminished through network effects that can either reinforce or undermine moral engagement.

        **Cognitive Load Principle**: Moral responsiveness is subject to cognitive limitations that create systematic biases in how individuals process moral information.

        **Mediation Transparency Principle**: The technological mediation of moral information affects moral judgment in ways that are often invisible to the moral agent, requiring critical literacy for appropriate moral response.

        ### 3.2 Empirical Predictions

        Unlike purely theoretical frameworks, IMR generates specific testable predictions:

        **Prediction 1**: Individuals exposed to narrative-rich presentations of distant suffering will show greater moral engagement than those receiving statistical information about larger-scale suffering.

        **Prediction 2**: Moral responsiveness will correlate with network position, with individuals at network centers showing both greater initial engagement and faster saturation effects.

        **Prediction 3**: Individuals will show measurable decreases in moral responsiveness when exposed to multiple simultaneous moral demands compared to sequential presentation.

        **Prediction 4**: Training in media literacy will improve calibration between moral response and objective moral significance of issues.

        ## 4. Case Studies

        ### 4.1 Social Media and Crisis Response

        The 2010 Haiti earthquake provides a paradigmatic case of information-mediated moral responsibility. Social media enabled unprecedented rapid response, with millions of individuals donating through text messaging within hours of the disaster. However, analysis reveals several concerning patterns:

        - **Attention Decay**: Initial massive engagement declined rapidly as media attention shifted, despite ongoing need
        - **Visible vs. Invisible Needs**: Highly visible rescue efforts received disproportionate support compared to less dramatic but equally important infrastructure needs
        - **Geographic Bias**: Haiti received more per-capita aid than simultaneous crises in less media-accessible regions

        ### 4.2 Climate Change and Temporal Responsibility

        Climate change presents unique challenges for information-mediated responsibility due to temporal distance and causal complexity:

        - **Present Bias**: Individuals show reduced moral engagement with future compared to present suffering, even when future suffering is more severe
        - **Causal Opacity**: Complex causal chains between individual action and climate outcomes reduce feelings of personal responsibility
        - **Statistical vs. Narrative**: Abstract statistics about future climate impacts generate less moral engagement than personal stories about present climate effects

        ### 4.3 Global Health Inequities

        The COVID-19 pandemic revealed both possibilities and limitations of global moral solidarity:

        - **Initial Universalism**: Early pandemic response showed unprecedented global cooperation based on shared vulnerability
        - **Rapid Localization**: As vaccines became available, moral concern quickly narrowed to national and local priorities
        - **Information Fatigue**: Sustained information exposure led to measurable decreases in moral engagement over time

        ## 5. Practical Applications

        ### 5.1 Ethical Design of Information Systems

        IMR analysis suggests several principles for ethical design of information systems:

        **Moral Calibration**: Systems should present moral information in ways that promote appropriate rather than maximal emotional engagement.

        **Attention Distribution**: Platforms should avoid algorithms that concentrate moral attention on highly engaging but potentially less significant issues.

        **Action Facilitation**: Moral information should be coupled with concrete, effective action opportunities to prevent learned helplessness.

        **Transparency Requirements**: Users should understand how algorithmic curation affects their moral information environment.

        ### 5.2 Educational Implications

        Digital moral literacy requires new educational approaches:

        **Media Effects Education**: Students need explicit instruction in how digital media affects moral judgment and behavior.

        **Network Awareness**: Understanding how social networks shape moral beliefs and responses.

        **Cognitive Bias Training**: Recognition of systematic limitations in moral information processing.

        **Practical Ethics**: Development of frameworks for navigating complex moral information environments.

        ### 5.3 Policy Recommendations

        Several policy interventions could improve moral information environments:

        **Platform Transparency**: Requirements for social media platforms to disclose algorithmic curation of moral content.

        **Information Diversity**: Policies promoting exposure to diverse moral perspectives and global moral concerns.

        **Attention Protection**: Recognition that human attention is a finite moral resource requiring protection from exploitation.

        **Global Information Justice**: Efforts to ensure equitable representation of global moral concerns in information systems.

        ## 6. Limitations and Future Research

        ### 6.1 Methodological Limitations

        Current research on information-mediated moral responsibility faces several limitations:

        - **Correlation vs. Causation**: Much evidence is correlational, making causal claims tentative
        - **Cultural Specificity**: Most studies focus on Western, educated populations
        - **Laboratory vs. Real-World**: Experimental studies may not generalize to complex real-world moral environments
        - **Temporal Constraints**: Long-term effects of digital moral engagement remain understudied

        ### 6.2 Future Research Directions

        Several research programs could advance understanding of information-mediated moral responsibility:

        **Longitudinal Studies**: Tracking how digital moral engagement evolves over time and life course.

        **Cross-Cultural Research**: Examining how cultural differences affect information-mediated moral responsibility.

        **Intervention Studies**: Testing specific approaches for improving moral calibration in digital environments.

        **Neuroscience Applications**: Using brain imaging to understand neural mechanisms of digitally mediated moral response.

        **Network Analysis**: Large-scale studies of how moral beliefs and behaviors spread through digital networks.

        ## 7. Conclusion

        The Information-Mediated Responsibility model provides a framework for understanding how digital connectivity transforms moral obligation. Unlike traditional ethical theories developed for limited-information environments, IMR acknowledges both the opportunities and limitations created by global information access.

        Key insights include recognition that:

        - Moral responsibility is not simply expanded by information access but qualitatively transformed
        - Network effects create collective moral phenomena that exceed individual moral capacities
        - Cognitive limitations require systematic approaches to moral information management
        - Technological mediation affects moral judgment in ways requiring critical literacy

        These insights have practical implications for educational curricula, platform design, and public policy. As digital connectivity continues to evolve, developing sophisticated frameworks for information-mediated moral responsibility becomes increasingly urgent.

        The goal is not to maximize moral engagement but to calibrate it appropriately - responding to genuine moral demands while avoiding the psychological defense mechanisms that lead to moral numbing and disengagement. This requires both individual moral literacy and collective efforts to create information environments that support rather than undermine moral agency.

        Future research should focus on empirical testing of IMR predictions and development of practical tools for navigating moral complexity in digital environments. The stakes are high: our capacity for appropriate moral response to global challenges may depend on our ability to understand and manage the transformation of moral responsibility in the digital age.

        ## References

        Bicchieri, C. (2006). *The grammar of society: The nature and dynamics of social norms*. Cambridge University Press.

        Decety, J., & Jackson, P. L. (2004). The functional architecture of human empathy. *Behavioral and Cognitive Neuroscience Reviews*, 3(2), 71-100.

        Figley, C. R. (2002). *Compassion fatigue: Psychotherapists' chronic lack of self care*. Journal of Clinical Psychology, 58(11), 1433-1441.

        Greene, J. D. (2013). *Moral tribes: Emotion, reason, and the gap between us and them*. Penguin Press.

        Haidt, J. (2012). *The righteous mind: Why good people are divided by politics and religion*. Vintage Books.

        Latané, B., & Darley, J. M. (1970). *The unresponsive bystander: Why doesn't he help?* Appleton-Century-Crofts.

        Nussbaum, M. C. (2001). *Upheavals of thought: The intelligence of emotions*. Cambridge University Press.

        Pariser, E. (2011). *The filter bubble: What the Internet is hiding from you*. Penguin Press.

        Slovic, P. (2007). "If I look at the mass I will never act": Psychic numbing and genocide. *Judgment and Decision Making*, 2(2), 79-95.

        Sunstein, C. R. (2017). *#Republic: Divided democracy in the age of social media*. Princeton University Press.

        Weber, E. U. (2006). Experience-based and description-based perceptions of long-term risk: Why global warming does not scare us (yet). *Climatic Change*, 77(1-2), 103-120.
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)
