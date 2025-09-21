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
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="paper-header">
    <h1 class="paper-title">Information Networks and Moral Responsibility</h1>
    <h2 class="paper-author">Xavier Honablue, M.Ed.</h2>
    <p class="paper-affiliation">Wayne County Community College District • September 2025</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.header("Paper Navigation")
    section = st.radio("Select Section:", [
        "Paper Overview",
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

    elif section == "Abstract & Introduction":
        st.markdown('<div class="abstract-box">', unsafe_allow_html=True)
        st.subheader("📋 Abstract")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.write("""
        This paper examines how information networks and digital connectivity affect moral responsibility in contemporary global society. Drawing on empirical research in moral psychology, network theory, and media studies, we analyze how awareness of distant suffering through digital media creates new forms of moral obligation that challenge traditional proximity-based ethical frameworks.

        We propose the Information-Mediated Responsibility (IMR) model, which accounts for how technological mediation affects moral salience, emotional engagement, and behavioral response. Key findings include: (1) digital information exposure creates measurable changes in moral judgment patterns, (2) network effects amplify individual moral responses through social reinforcement mechanisms, and (3) information overload can paradoxically reduce moral responsiveness through psychological defense mechanisms.
        """)
        
        st.write("**Keywords:** moral responsibility, digital ethics, information networks, moral psychology, global ethics, media effects")
        
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("🌍 Introduction: The Digital Transformation of Moral Responsibility")
        
        st.write("""
        The digital revolution has fundamentally altered the landscape of moral responsibility. Unlike previous generations, who remained largely unaware of distant suffering, contemporary individuals receive constant streams of information about global injustices, environmental crises, and human rights violations.
        """)
        
        st.subheader("The Challenge to Traditional Ethics")
        st.write("Traditional ethical frameworks developed under assumptions of limited information and local communities:")
        st.write("• **Utilitarian calculations** assumed practical constraints on knowledge and action")
        st.write("• **Virtue ethics** focused on character development within particular communities")
        st.write("• **Deontological systems** emphasized universal principles but were applied within contexts of limited awareness")
        
        st.write("None adequately address the moral implications of instantaneous global information access.")
        
        st.subheader("Research Approach")
        st.write("""
        This paper proposes the Information-Mediated Responsibility (IMR) model as a framework for understanding how digital connectivity transforms moral obligations. Unlike speculative theoretical approaches, IMR builds on established research in moral psychology, media effects, and network theory to generate empirically grounded insights about contemporary ethical challenges.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Theoretical Framework":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("🧠 Theoretical Framework")
        
        st.subheader("Moral Salience and Information Exposure")
        st.write("""
        Research in moral psychology demonstrates that moral judgment depends heavily on **salience** - the degree to which moral considerations capture attention and emotional engagement. Digital media fundamentally alters moral salience through several mechanisms:
        """)
        
        st.markdown("""
        <div class="key-insight">
            <strong>Proximity Override:</strong> Visual media can make distant suffering more psychologically proximate than local issues
        </div>
        """, unsafe_allow_html=True)
        
        st.write("**Narrative Framing:** Digital platforms use storytelling techniques that enhance emotional engagement with distant moral issues. Research indicates that narrative structure significantly influences moral judgment independent of factual content.")
        
        st.write("**Algorithmic Curation:** Social media algorithms selectively expose users to morally charged content based on engagement patterns, creating echo chambers that amplify certain moral concerns while obscuring others.")
        
        st.subheader("Network Effects in Moral Responsibility")
        st.write("Social network theory provides tools for understanding how individual moral responses aggregate into collective moral phenomena:")
        
        st.write("• **Moral Cascade Effects:** When individuals observe others responding to moral issues, they become more likely to respond themselves")
        st.write("• **Diffusion of Responsibility:** Awareness that many others are also aware of moral issues can reduce individual feelings of responsibility")
        st.write("• **Network Polarization:** Digital networks can amplify moral polarization by sorting individuals into like-minded communities")
        
        st.subheader("Information Overload and Moral Numbing")
        st.write("Psychological research reveals systematic limitations in human capacity to process moral information:")
        
        st.write("• **Finite Pool of Worry:** Individuals have limited capacity for moral concern")
        st.write("• **Compassion Fatigue:** Repeated exposure to suffering can reduce empathetic responding")
        st.write("• **Psychic Numbing:** Moral responsiveness decreases as the number of victims increases")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualization: Moral Response vs. Information Load
        st.markdown('<div class="visualization-container">', unsafe_allow_html=True)
        st.subheader("Moral Response Patterns")
        
        # Create data for moral response curve
        x = np.linspace(0, 10, 100)
        y = 10 * np.exp(-x/3) * (1 + 0.1 * np.sin(5*x))  # Exponential decay with noise
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=x, y=y,
            mode='lines',
            name='Moral Responsiveness',
            line=dict(color='red', width=3)
        ))
        
        fig.update_layout(
            title="Moral Responsiveness vs. Information Exposure",
            xaxis_title="Information Load (arbitrary units)",
            yaxis_title="Moral Response Intensity",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "The IMR Model":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("🔬 The Information-Mediated Responsibility Model")
        
        st.subheader("Core Principles")
        st.write("The IMR model proposes that moral responsibility in digital environments operates according to four key principles:")
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**1. Information Integration Principle**")
        st.write("Moral obligations arise through the integration of factual information, emotional engagement, and capacity for effective action. All three components are necessary for full moral responsibility.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**2. Network Amplification Principle**")
        st.write("Individual moral responses are amplified or diminished through network effects that can either reinforce or undermine moral engagement.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**3. Cognitive Load Principle**")
        st.write("Moral responsiveness is subject to cognitive limitations that create systematic biases in how individuals process moral information.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**4. Mediation Transparency Principle**")
        st.write("The technological mediation of moral information affects moral judgment in ways that are often invisible to the moral agent, requiring critical literacy for appropriate moral response.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Empirical Predictions")
        st.write("Unlike purely theoretical frameworks, IMR generates specific testable predictions:")
        
        st.write("• **Prediction 1:** Individuals exposed to narrative-rich presentations of distant suffering will show greater moral engagement than those receiving statistical information")
        st.write("• **Prediction 2:** Moral responsiveness will correlate with network position, with central individuals showing both greater initial engagement and faster saturation effects")
        st.write("• **Prediction 3:** Individuals will show measurable decreases in moral responsiveness when exposed to multiple simultaneous moral demands")
        st.write("• **Prediction 4:** Training in media literacy will improve calibration between moral response and objective moral significance")
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Case Studies":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("📚 Case Studies in Information-Mediated Moral Responsibility")
        
        st.subheader("Case Study 1: Social Media and Crisis Response")
        st.write("**Example:** 2010 Haiti Earthquake")
        
        st.write("Social media enabled unprecedented rapid response, with millions donating through text messaging within hours. However, analysis reveals concerning patterns:")
        
        st.write("• **Attention Decay:** Initial massive engagement declined rapidly as media attention shifted")
        st.write("• **Visible vs. Invisible Needs:** Highly visible rescue efforts received disproportionate support")
        st.write("• **Geographic Bias:** Haiti received more per-capita aid than simultaneous crises in less accessible regions")
        
        st.subheader("Case Study 2: Climate Change and Temporal Responsibility")
        st.write("Climate change presents unique challenges due to temporal distance and causal complexity:")
        
        st.write("• **Present Bias:** Reduced moral engagement with future compared to present suffering")
        st.write("• **Causal Opacity:** Complex causal chains reduce feelings of personal responsibility")
        st.write("• **Statistical vs. Narrative:** Abstract statistics generate less engagement than personal stories")
        
        st.subheader("Case Study 3: Global Health Inequities")
        st.write("**Example:** COVID-19 Pandemic Response")
        
        st.write("The pandemic revealed both possibilities and limitations of global moral solidarity:")
        
        st.write("• **Initial Universalism:** Early unprecedented global cooperation based on shared vulnerability")
        st.write("• **Rapid Localization:** As vaccines became available, moral concern quickly narrowed to national priorities")
        st.write("• **Information Fatigue:** Sustained exposure led to measurable decreases in moral engagement over time")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Visualization: Attention Decay
        st.markdown('<div class="visualization-container">', unsafe_allow_html=True)
        st.subheader("Crisis Attention Patterns")
        
        # Create data for attention decay
        days = list(range(1, 101))
        haiti_attention = [100 * np.exp(-day/20) + 5 for day in days]
        baseline_attention = [20 + 5 * np.sin(day/10) for day in days]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=days, y=haiti_attention,
            mode='lines',
            name='Crisis Attention',
            line=dict(color='red', width=3)
        ))
        fig.add_trace(go.Scatter(
            x=days, y=baseline_attention,
            mode='lines',
            name='Baseline Issues',
            line=dict(color='blue', width=2)
        ))
        
        fig.update_layout(
            title="Media Attention Over Time: Crisis vs. Ongoing Issues",
            xaxis_title="Days After Event",
            yaxis_title="Relative Attention Level",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Applications & Implications":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("🔧 Practical Applications")
        
        st.subheader("Ethical Design of Information Systems")
        st.write("IMR analysis suggests several principles for ethical design:")
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**Moral Calibration**")
        st.write("Systems should present moral information in ways that promote appropriate rather than maximal emotional engagement.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**Attention Distribution**")
        st.write("Platforms should avoid algorithms that concentrate moral attention on highly engaging but potentially less significant issues.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="section-header">', unsafe_allow_html=True)
        st.write("**Action Facilitation**")
        st.write("Moral information should be coupled with concrete, effective action opportunities to prevent learned helplessness.")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Educational Implications")
        st.write("Digital moral literacy requires new educational approaches:")
        
        st.write("• **Media Effects Education:** Explicit instruction in how digital media affects moral judgment")
        st.write("• **Network Awareness:** Understanding how social networks shape moral beliefs and responses")
        st.write("• **Cognitive Bias Training:** Recognition of systematic limitations in moral information processing")
        st.write("• **Practical Ethics:** Frameworks for navigating complex moral information environments")
        
        st.subheader("Policy Recommendations")
        st.write("Several policy interventions could improve moral information environments:")
        
        st.write("• **Platform Transparency:** Requirements for social media platforms to disclose algorithmic curation")
        st.write("• **Information Diversity:** Policies promoting exposure to diverse moral perspectives")
        st.write("• **Attention Protection:** Recognition that human attention is a finite moral resource")
        st.write("• **Global Information Justice:** Efforts to ensure equitable representation of global moral concerns")
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "Discussion Questions":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("💭 Discussion Questions for Critical Analysis")
        
        st.subheader("Conceptual Questions")
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**1. Moral Distance:** Does physical or temporal distance affect moral obligation? Why or why not? How does digital connectivity change this?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**2. Information vs. Action:** When does awareness of suffering create moral obligation? Is there a difference between knowing about suffering and being responsible for addressing it?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**3. Cognitive Limitations:** How should we account for human psychological limitations in moral theory? Should ethical frameworks be based on ideal or realistic expectations?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Applied Ethics Questions")
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**4. Social Media Ethics:** Do platforms have obligations to promote moral engagement? How should they balance engagement with moral calibration?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**5. Global Justice:** In an interconnected world, how do we determine which global issues deserve our moral attention? Should proximity still matter?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**6. Future Generations:** How should awareness of future suffering (like climate change) affect present moral obligations?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Critical Evaluation Questions")
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**7. Theory Assessment:** What are the strengths and weaknesses of the IMR model? What aspects need further development or empirical testing?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**8. Alternative Approaches:** How might other ethical frameworks (virtue ethics, care ethics, etc.) address the challenges posed by digital connectivity?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="discussion-box">', unsafe_allow_html=True)
        st.write("**9. Practical Implementation:** How could the insights from this paper be applied in education, policy, or technology design?")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    elif section == "References & Further Reading":
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("📚 References & Further Reading")
        
        st.subheader("Primary References")
        st.markdown('</div>', unsafe_allow_html=True)
        
        references = [
            "Bicchieri, C. (2006). The grammar of society: The nature and dynamics of social norms. Cambridge University Press.",
            "Greene, J. D. (2013). Moral tribes: Emotion, reason, and the gap between us and them. Penguin Press.",
            "Haidt, J. (2012). The righteous mind: Why good people are divided by politics and religion. Vintage Books.",
            "Latané, B., & Darley, J. M. (1970). The unresponsive bystander: Why doesn't he help? Appleton-Century-Crofts.",
            "Nussbaum, M. C. (2001). Upheavals of thought: The intelligence of emotions. Cambridge University Press.",
            "Pariser, E. (2011). The filter bubble: What the Internet is hiding from you. Penguin Press.",
            "Slovic, P. (2007). 'If I look at the mass I will never act': Psychic numbing and genocide. Judgment and Decision Making, 2(2), 79-95.",
            "Sunstein, C. R. (2017). #Republic: Divided democracy in the age of social media. Princeton University Press."
        ]
        
        for ref in references:
            st.markdown(f'<div class="reference-item">{ref}</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="content-section">', unsafe_allow_html=True)
        st.subheader("🔗 Further Reading")
        
        st.write("**Digital Ethics:**")
        st.write("• Floridi, L. (2019). Translating Digital Ethics. Philosophy & Technology, 32(4), 735-754.")
        st.write("• Winner, L. (1980). Do artifacts have politics? Daedalus, 109(1), 121-136.")
        
        st.write("**Moral Psychology:**")
        st.write("• Cushman, F. (2013). Action, outcome, and value: A dual-system framework for morality. Personality and Social Psychology Review, 17(3), 273-292.")
        st.write("• Klayman, J., & Ha, Y. W. (1987). Confirmation, disconfirmation, and information in hypothesis testing. Psychological Review, 94(2), 211-228.")
        
        st.write("**Network Theory:**")
        st.write("• Barabási, A. L. (2016). Network science. Cambridge University Press.")
        st.write("• Centola, D. (2018). How behavior spreads: The science of complex contagions. Princeton University Press.")
        
        st.write("**Global Ethics:**")
        st.write("• Singer, P. (2011). The expanding circle: Ethics, evolution, and moral progress. Princeton University Press.")
        st.write("• Pogge, T. (2008). World poverty and human rights. Polity Press.")
        st.markdown('</div>', unsafe_allow_html=True)

# Call the display function
display_content()

# Footer
st.markdown("---")
st.markdown("**PHL201: Information Networks and Moral Responsibility | Xavier Honablue M.Ed | Wayne County Community College District**")
st.caption("Academic Paper Platform - For Educational Use")
