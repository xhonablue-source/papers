import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

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

# Header
st.markdown("""
<div class="paper-header">
    <h1 class="paper-title">Information Networks and Moral Responsibility</h1>
    <h2 class="paper-author">Xavier Honablue, M.Ed.</h2>
    <p class="paper-affiliation">Wayne County Community College District • September 2025</p>
</div>
""", unsafe_allow_html=True)

if section == "Paper Overview":
    st.markdown("""
    <div class="content-section">
        <h2>📖 Paper Overview</h2>
        
        <p><strong>Research Question:</strong> How does digital connectivity transform moral responsibility in contemporary society?</p>
        
        <p><strong>Methodology:</strong> Interdisciplinary analysis drawing on moral psychology, network theory, and media studies</p>
        
        <p><strong>Key Contribution:</strong> The Information-Mediated Responsibility (IMR) model - a framework for understanding ethical obligations in digital environments</p>
        
        <h3>🎯 Learning Objectives</h3>
        <p>After engaging with this paper, students will be able to:</p>
        <ul>
            <li>Analyze how digital information affects moral judgment and behavior</li>
            <li>Evaluate the strengths and limitations of traditional ethical frameworks in digital contexts</li>
            <li>Apply the IMR model to contemporary moral challenges</li>
            <li>Critically assess the role of technology in shaping moral communities</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
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
    st.markdown("""
    <div class="abstract-box">
        <h3>📋 Abstract</h3>
        <p>This paper examines how information networks and digital connectivity affect moral responsibility in contemporary global society. Drawing on empirical research in moral psychology, network theory, and media studies, we analyze how awareness of distant suffering through digital media creates new forms of moral obligation that challenge traditional proximity-based ethical frameworks.</p>
        
        <p>We propose the Information-Mediated Responsibility (IMR) model, which accounts for how technological mediation affects moral salience, emotional engagement, and behavioral response. Key findings include: (1) digital information exposure creates measurable changes in moral judgment patterns, (2) network effects amplify individual moral responses through social reinforcement mechanisms, and (3) information overload can paradoxically reduce moral responsiveness through psychological defense mechanisms.</p>
        
        <p><strong>Keywords:</strong> moral responsibility, digital ethics, information networks, moral psychology, global ethics, media effects</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-section">
        <h2>🌍 Introduction: The Digital Transformation of Moral Responsibility</h2>
        
        <p>The digital revolution has fundamentally altered the landscape of moral responsibility. Unlike previous generations, who remained largely unaware of distant suffering, contemporary individuals receive constant streams of information about global injustices, environmental crises, and human rights violations.</p>
        
        <h3>The Challenge to Traditional Ethics</h3>
        <p>Traditional ethical frameworks developed under assumptions of limited information and local communities:</p>
        <ul>
            <li><strong>Utilitarian calculations</strong> assumed practical constraints on knowledge and action</li>
            <li><strong>Virtue ethics</strong> focused on character development within particular communities</li>
            <li><strong>Deontological systems</strong> emphasized universal principles but were applied within contexts of limited awareness</li>
        </ul>
        
        <p>None adequately address the moral implications of instantaneous global information access.</p>
        
        <h3>Research Approach</h3>
        <p>This paper proposes the Information-Mediated Responsibility (IMR) model as a framework for understanding how digital connectivity transforms moral obligations. Unlike speculative theoretical approaches, IMR builds on established research in moral psychology, media effects, and network theory to generate empirically grounded insights about contemporary ethical challenges.</p>
    </div>
    """, unsafe_allow_html=True)

elif section == "Theoretical Framework":
    st.markdown("""
    <div class="content-section">
        <h2>🧠 Theoretical Framework</h2>
        
        <h3>Moral Salience and Information Exposure</h3>
        <p>Research in moral psychology demonstrates that moral judgment depends heavily on <strong>salience</strong> - the degree to which moral considerations capture attention and emotional engagement. Digital media fundamentally alters moral salience through several mechanisms:</p>
        
        <div class="key-insight">
            <strong>Proximity Override:</strong> Visual media can make distant suffering more psychologically proximate than local issues
        </div>
        
        <p><strong>Narrative Framing:</strong> Digital platforms use storytelling techniques that enhance emotional engagement with distant moral issues. Research indicates that narrative structure significantly influences moral judgment independent of factual content.</p>
        
        <p><strong>Algorithmic Curation:</strong> Social media algorithms selectively expose users to morally charged content based on engagement patterns, creating echo chambers that amplify certain moral concerns while obscuring others.</p>
        
        <h3>Network Effects in Moral Responsibility</h3>
        <p>Social network theory provides tools for understanding how individual moral responses aggregate into collective moral phenomena:</p>
        
        <ul>
            <li><strong>Moral Cascade Effects:</strong> When individuals observe others responding to moral issues, they become more likely to respond themselves</li>
            <li><strong>Diffusion of Responsibility:</strong> Awareness that many others are also aware of moral issues can reduce individual feelings of responsibility</li>
            <li><strong>Network Polarization:</strong> Digital networks can amplify moral polarization by sorting individuals into like-minded communities</li>
        </ul>
        
        <h3>Information Overload and Moral Numbing</h3>
        <p>Psychological research reveals systematic limitations in human capacity to process moral information:</p>
        
        <ul>
            <li><strong>Finite Pool of Worry:</strong> Individuals have limited capacity for moral concern</li>
            <li><strong>Compassion Fatigue:</strong> Repeated exposure to suffering can reduce empathetic responding</li>
            <li><strong>Psychic Numbing:</strong> Moral responsiveness decreases as the number of victims increases</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Visualization: Moral Response vs. Information Load
    st.markdown('<div class="visualization-container">', unsafe_allow_html=True)
    st.subheader("Moral Response Patterns")
    
    # Create data for moral response curve
    import numpy as np
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
    st.markdown("""
    <div class="content-section">
        <h2>🔬 The Information-Mediated Responsibility Model</h2>
        
        <h3>Core Principles</h3>
        <p>The IMR model proposes that moral responsibility in digital environments operates according to four key principles:</p>
        
        <div class="section-header">
            <h4>1. Information Integration Principle</h4>
            <p>Moral obligations arise through the integration of factual information, emotional engagement, and capacity for effective action. All three components are necessary for full moral responsibility.</p>
        </div>
        
        <div class="section-header">
            <h4>2. Network Amplification Principle</h4>
            <p>Individual moral responses are amplified or diminished through network effects that can either reinforce or undermine moral engagement.</p>
        </div>
        
        <div class="section-header">
            <h4>3. Cognitive Load Principle</h4>
            <p>Moral responsiveness is subject to cognitive limitations that create systematic biases in how individuals process moral information.</p>
        </div>
        
        <div class="section-header">
            <h4>4. Mediation Transparency Principle</h4>
            <p>The technological mediation of moral information affects moral judgment in ways that are often invisible to the moral agent, requiring critical literacy for appropriate moral response.</p>
        </div>
        
        <h3>Empirical Predictions</h3>
        <p>Unlike purely theoretical frameworks, IMR generates specific testable predictions:</p>
        
        <ul>
            <li><strong>Prediction 1:</strong> Individuals exposed to narrative-rich presentations of distant suffering will show greater moral engagement than those receiving statistical information</li>
            <li><strong>Prediction 2:</strong> Moral responsiveness will correlate with network position, with central individuals showing both greater initial engagement and faster saturation effects</li>
            <li><strong>Prediction 3:</strong> Individuals will show measurable decreases in moral responsiveness when exposed to multiple simultaneous moral demands</li>
            <li><strong>Prediction 4:</strong> Training in media literacy will improve calibration between moral response and objective moral significance</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif section == "Case Studies":
    st.markdown("""
    <div class="content-section">
        <h2>📚 Case Studies in Information-Mediated Moral Responsibility</h2>
        
        <h3>Case Study 1: Social Media and Crisis Response</h3>
        <p><strong>Example:</strong> 2010 Haiti Earthquake</p>
        
        <p>Social media enabled unprecedented rapid response, with millions donating through text messaging within hours. However, analysis reveals concerning patterns:</p>
        
        <ul>
            <li><strong>Attention Decay:</strong> Initial massive engagement declined rapidly as media attention shifted</li>
            <li><strong>Visible vs. Invisible Needs:</strong> Highly visible rescue efforts received disproportionate support</li>
            <li><strong>Geographic Bias:</strong> Haiti received more per-capita aid than simultaneous crises in less accessible regions</li>
        </ul>
        
        <h3>Case Study 2: Climate Change and Temporal Responsibility</h3>
        <p>Climate change presents unique challenges due to temporal distance and causal complexity:</p>
        
        <ul>
            <li><strong>Present Bias:</strong> Reduced moral engagement with future compared to present suffering</li>
            <li><strong>Causal Opacity:</strong> Complex causal chains reduce feelings of personal responsibility</li>
            <li><strong>Statistical vs. Narrative:</strong> Abstract statistics generate less engagement than personal stories</li>
        </ul>
        
        <h3>Case Study 3: Global Health Inequities</h3>
        <p><strong>Example:</strong> COVID-19 Pandemic Response</p>
        
        <p>The pandemic revealed both possibilities and limitations of global moral solidarity:</p>
        
        <ul>
            <li><strong>Initial Universalism:</strong> Early unprecedented global cooperation based on shared vulnerability</li>
            <li><strong>Rapid Localization:</strong> As vaccines became available, moral concern quickly narrowed to national priorities</li>
            <li><strong>Information Fatigue:</strong> Sustained exposure led to measurable decreases in moral engagement over time</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
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
    st.markdown("""
    <div class="content-section">
        <h2>🔧 Practical Applications</h2>
        
        <h3>Ethical Design of Information Systems</h3>
        <p>IMR analysis suggests several principles for ethical design:</p>
        
        <div class="section-header">
            <h4>Moral Calibration</h4>
            <p>Systems should present moral information in ways that promote appropriate rather than maximal emotional engagement.</p>
        </div>
        
        <div class="section-header">
            <h4>Attention Distribution</h4>
            <p>Platforms should avoid algorithms that concentrate moral attention on highly engaging but potentially less significant issues.</p>
        </div>
        
        <div class="section-header">
            <h4>Action Facilitation</h4>
            <p>Moral information should be coupled with concrete, effective action opportunities to prevent learned helplessness.</p>
        </div>
        
        <h3>Educational Implications</h3>
        <p>Digital moral literacy requires new educational approaches:</p>
        
        <ul>
            <li><strong>Media Effects Education:</strong> Explicit instruction in how digital media affects moral judgment</li>
            <li><strong>Network Awareness:</strong> Understanding how social networks shape moral beliefs and responses</li>
            <li><strong>Cognitive Bias Training:</strong> Recognition of systematic limitations in moral information processing</li>
            <li><strong>Practical Ethics:</strong> Frameworks for navigating complex moral information environments</li>
        </ul>
        
        <h3>Policy Recommendations</h3>
        <p>Several policy interventions could improve moral information environments:</p>
        
        <ul>
            <li><strong>Platform Transparency:</strong> Requirements for social media platforms to disclose algorithmic curation</li>
            <li><strong>Information Diversity:</strong> Policies promoting exposure to diverse moral perspectives</li>
            <li><strong>Attention Protection:</strong> Recognition that human attention is a finite moral resource</li>
            <li><strong>Global Information Justice:</strong> Efforts to ensure equitable representation of global moral concerns</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif section == "Discussion Questions":
    st.markdown("""
    <div class="content-section">
        <h2>💭 Discussion Questions for Critical Analysis</h2>
        
        <h3>Conceptual Questions</h3>
        <div class="discussion-box">
            <p><strong>1. Moral Distance:</strong> Does physical or temporal distance affect moral obligation? Why or why not? How does digital connectivity change this?</p>
        </div>
        
        <div class="discussion-box">
            <p><strong>2. Information vs. Action:</strong> When does awareness of suffering create moral obligation? Is there a difference between knowing about suffering and being responsible for addressing it?</p>
        </div>
        
        <div class="discussion-box">
            <p><strong>3. Cognitive Limitations:</strong> How should we account for human psychological limitations in moral theory? Should ethical frameworks be based on ideal or realistic expectations?</p>
        </div>
        
        <h3>Applied Ethics Questions</h3>
        <div class="discussion-box">
            <p><strong>4. Social Media Ethics:</strong> Do platforms have obligations to promote moral engagement? How should they balance engagement with moral calibration?</p>
        </div>
        
        <div class="discussion-box">
            <p><strong>5. Global Justice:</strong> In an interconnected world, how do we determine which global issues deserve our moral attention? Should proximity still matter?</p>
        </div>
        
        <div class="discussion-box">
            <p><strong>6. Future Generations:</strong> How should awareness of future suffering (like climate change) affect present moral obligations?</p>
        </div>
        
        <h3>Critical Evaluation Questions</h3>
        <div class="discussion-box">
            <p><strong>7. Theory Assessment:</strong> What are the strengths and weaknesses of the IMR model? What aspects need further development or empirical testing?</p>
        </div>
        
        <div class="discussion-box">
            <p><strong>8. Alternative Approaches:</strong> How might other ethical frameworks (virtue ethics, care ethics, etc.) address the challenges posed by digital connectivity?</p>
        </div>
        
        <div class="discussion-box">
            <p><strong>9. Practical Implementation:</strong> How could the insights from this paper be applied in education, policy, or technology design?</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif section == "References & Further Reading":
    st.markdown("""
    <div class="content-section">
        <h2>📚 References & Further Reading</h2>
        
        <h3>Primary References</h3>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    st.markdown("""
    <div class="content-section">
        <h3>🔗 Further Reading</h3>
        
        <p><strong>Digital Ethics:</strong></p>
        <ul>
            <li>Floridi, L. (2019). Translating Digital Ethics. Philosophy & Technology, 32(4), 735-754.</li>
            <li>Winner, L. (1980). Do artifacts have politics? Daedalus, 109(1), 121-136.</li>
        </ul>
        
        <p><strong>Moral Psychology:</strong></p>
        <ul>
            <li>Cushman, F. (2013). Action, outcome, and value: A dual-system framework for morality. Personality and Social Psychology Review, 17(3), 273-292.</li>
            <li>Klayman, J., & Ha, Y. W. (1987). Confirmation, disconfirmation, and information in hypothesis testing. Psychological Review, 94(2), 211-228.</li>
        </ul>
        
        <p><strong>Network Theory:</strong></p>
        <ul>
            <li>Barabási, A. L. (2016). Network science. Cambridge University Press.</li>
            <li>Centola, D. (2018). How behavior spreads: The science of complex contagions. Princeton University Press.</li>
        </ul>
        
        <p><strong>Global Ethics:</strong></p>
        <ul>
            <li>Singer, P. (2011). The expanding circle: Ethics, evolution, and moral progress. Princeton University Press.</li>
            <li>Pogge, T. (2008). World poverty and human rights. Polity Press.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("**PHL201: Information Networks and Moral Responsibility | Xavier Honablue M.Ed | Wayne County Community College District**")
st.caption("Academic Paper Platform - For Educational Use")
