import re

with open('portfolio/index.html', 'r') as f:
    html = f.read()

# 1. Replace Conference Papers
new_conference_html = """                <div class="publications-grid">
                    <div class="publication-card">
                        <h4>A Comparative and Hybrid Study of CNN and Transformer Models for Multi-Class Virus Classification in Transmission Electron Microscopy.</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Md. Mamunur Rahman Moon, Md. Hadi Al-amin, H.M. Asraf</p>
                        <p class="venue">1th International Conference on Information and Communication Technology for Intelligent Systems, APRIL 9 - 11, 2026 in Bangkok, Thailand.<br><span class="status" style="margin-top: 5px; display: inline-block;">Accepted (Springer)</span></p>
                    </div>
                    <div class="publication-card">
                        <h4>Computer Vision Hybrid Approach: CNN and Transformer Models for Accurate Alzheimer’s Detection from Brain MRI Scans.</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Shuvo Karmaker, Md. Hadi Al-amin, Md Modabberul Islam, Jisun Junayed, Farha Ulfat Mahi</p>
                        <p class="venue">7th Mediterranean Conference on Pattern Recognition &amp; Artificial Intelligence (MedPRAI), Jan 23–24, 2026, Istinye University, Istanbul, Turkey.<br><span class="status" style="margin-top: 5px; display: inline-block;">Accepted (Springer)</span> <a href="https://doi.org/10.48550/arXiv.2601.15202" target="_blank" class="publication-link">doi: arXiv.2601.15202</a></p>
                    </div>
                    <div class="publication-card">
                        <h4>Vision Models for Medical Imaging: A Hybrid Approach for PCOS Detection from Ultrasound Scans.</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Md Mehedi Hassain, Muntakimur Rahaman, Md Towhidul Islam, Shaista Rani, Md Sharif Mollah</p>
                        <p class="venue">International Conference on System Engineering,Technology, and Sustainable Solutions (ICSETS 2025), Nov 3-6, Muscat, Oman.<br><span class="status" style="margin-top: 5px; display: inline-block;">Accepted (IOP)</span> <a href="https://doi.org/10.48550/arXiv.2601.15119" target="_blank" class="publication-link">doi: arXiv.2601.15119</a></p>
                    </div>
                    <div class="publication-card">
                        <h4>Bengali Text Classification: An Evaluation of Large Language Model Approaches</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Md Mehedi Hassain, Md Hojaifa Tanvir, Rahul Nandi</p>
                        <p class="venue">International Conference on Intelligent Digital Systems and Sustainable Technology (ICIDST), June 24-25, Al Farahidi University, Baghdad, Iraq.<br><span class="status" style="margin-top: 5px; display: inline-block;">Accepted (Springer)</span> <a href="https://doi.org/10.48550/arXiv.2601.12132" target="_blank" class="publication-link">doi: arXiv.2601.12132</a></p>
                    </div>
                    <div class="publication-card">
                        <h4>Bangla Music Genre Classification Using Bidirectional LSTMS</h4>
                        <p class="authors">Muntakimur Rahaman, <strong>Md Mahmudul Hoque</strong>, Md Mehedi Hassain</p>
                        <p class="venue">International Conference on Intelligent Digital Systems and Sustainable Technology (ICIDST), June 24-25, Al Farahidi University, Baghdad, Iraq.<br><span class="status" style="margin-top: 5px; display: inline-block;">Accepted (Springer)</span> <a href="https://doi.org/10.48550/arXiv.2601.15083" target="_blank" class="publication-link">doi: arXiv.2601.15083</a></p>
                    </div>
                    <div class="publication-card">
                        <h4>Machine Learning Algorithms and Image Processing based Smart Parking System using IoT</h4>
                        <p class="authors">Md Mehedi Hassain, <strong>Md Mahmudul Hoque</strong>, Rahul Nondi, Md Hojaifa Tanvir, Saad Ahmed</p>
                        <p class="venue">In: Idrissi, N., et al. Artificial Intelligence and Green Computing. ICAIGC 2025. Lecture Notes in Networks and Systems, vol 1589. Springer, Cham.<br><a href="https://doi.org/10.1007/978-3-032-02312-4_2" target="_blank" class="publication-link">doi: 10.1007/978..._2</a></p>
                    </div>
                    <div class="publication-card">
                        <h4>LSB Image Steganography Detection Using CNN With L2 Regularization</h4>
                        <p class="authors">Afroza Islam, Ikbal Ahmed, Farhana Abedin, <strong>Md Mahmudul Hoque</strong>, Auntor Chandra Das</p>
                        <p class="venue">2nd International Conference on Intelligent Systems, Blockchain, and Communication Technologies, ElSewedy University of Technology, Egypt.<br><span class="status" style="margin-top: 5px; display: inline-block;">Accepted (Springer)</span></p>
                    </div>
                </div>"""

html = re.sub(r'<div class="publications-scroll-container">.*?</div>\s*</div>', new_conference_html + '\n            </div>', html, flags=re.DOTALL)

# 2. Add Reviewer
reviewer_card = """                <div class="reviewer-card">
                    <h4>IAES International Journal of Robotics and Automation (IJRA)</h4>
                    <p class="journal-type">International Journal</p>
                    <p class="conference-venue" style="font-size: 0.95em; color: #555;">Review manuscripts since May 2025 in the areas of Deep Learning, and IoT. Assessed technical rigor and provided recommendations for acceptance.</p>
                    <p class="reviewer-role">Peer Reviewer</p>
                </div>"""

html = re.sub(r'(<div class="reviewer-grid">)', r'\1\n' + reviewer_card, html)

# 3. Update Projects
new_projects_html = """                <div class="projects-scroll">
                    <div class="project-card">
                        <h4>Railway Automation System</h4>
                        <p class="project-description">Advanced system based on Sensors, Automatic Barrier System, and Traffic Management for railways.</p>
                        <div class="project-tags">
                            <span class="project-tag">IoT</span>
                            <span class="project-tag">Automation</span>
                            <span class="project-tag">Sensors</span>
                        </div>
                    </div>
                    
                    <div class="project-card">
                        <h4>Heart Signal Processing</h4>
                        <p class="project-description">Advanced processing and analytical modeling of heart signals for medical applications.</p>
                        <div class="project-tags">
                            <span class="project-tag">Medical AI</span>
                            <span class="project-tag">Signal Processing</span>
                            <span class="project-tag">Deep Learning</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <h4>Human Bone Fracture Measurement Device</h4>
                        <p class="project-description">Hardware and software device to accurately measure and analyze Human bone fracture.</p>
                        <div class="project-tags">
                            <span class="project-tag">Embedded Systems</span>
                            <span class="project-tag">Healthcare</span>
                            <span class="project-tag">Sensors</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <h4>TEM Virus Analysis</h4>
                        <p class="project-description">Classification and analysis of completely unlabelled viruses in Transmission Electron Microscopy.</p>
                        <div class="project-tags">
                            <span class="project-tag">Computer Vision</span>
                            <span class="project-tag">Microscopy</span>
                            <span class="project-tag">Deep Learning</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <h4>Body Vibration Analysis</h4>
                        <p class="project-description">Precise monitoring and quantitative assessment of human body vibrations for medical contexts.</p>
                        <div class="project-tags">
                            <span class="project-tag">Signal Processing</span>
                            <span class="project-tag">Data Integration</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <h4>Bangla Visual Question Answering LLM and VLLM</h4>
                        <p class="project-description">Creating a Visual Language Model (VLLM) specialized in answering questions about images in the Bengali language.</p>
                        <div class="project-tags">
                            <span class="project-tag">NLP</span>
                            <span class="project-tag">LLM / VLLM</span>
                            <span class="project-tag">Computer Vision</span>
                        </div>
                    </div>
                    
                    <!-- duplicates for infinite scrolling effect -->
                    <div class="project-card">
                        <h4>Railway Automation System</h4>
                        <p class="project-description">Advanced system based on Sensors, Automatic Barrier System, and Traffic Management for railways.</p>
                        <div class="project-tags">
                            <span class="project-tag">IoT</span>
                            <span class="project-tag">Automation</span>
                            <span class="project-tag">Sensors</span>
                        </div>
                    </div>
                    
                    <div class="project-card">
                        <h4>Heart Signal Processing</h4>
                        <p class="project-description">Advanced processing and analytical modeling of heart signals for medical applications.</p>
                        <div class="project-tags">
                            <span class="project-tag">Medical AI</span>
                            <span class="project-tag">Signal Processing</span>
                            <span class="project-tag">Deep Learning</span>
                        </div>
                    </div>

                    <div class="project-card">
                        <h4>Human Bone Fracture Measurement Device</h4>
                        <p class="project-description">Hardware and software device to accurately measure and analyze Human bone fracture.</p>
                        <div class="project-tags">
                            <span class="project-tag">Embedded Systems</span>
                            <span class="project-tag">Healthcare</span>
                            <span class="project-tag">Sensors</span>
                        </div>
                    </div>
                </div>"""

html = re.sub(r'<div class="projects-scroll">.*?</div>\s*</div>', new_projects_html + '\n            </div>', html, flags=re.DOTALL)

# 4. Integrate Video Background into Hero section
hero_replacement = """    <!-- Hero Section -->
    <section id="home" class="hero">
        <video autoplay muted loop playsinline class="hero-video-bg">
            <source src="background-video.mp4" type="video/mp4">
        </video>
        <div class="hero-overlay"></div>
        <div class="hero-container">"""

html = html.replace("""    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-container">""", hero_replacement)

with open('portfolio/index.html', 'w') as f:
    f.write(html)


# Update styles.css
with open('portfolio/styles.css', 'r') as f:
    css = f.read()

new_css = """
/* Update styles for video background */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding-top: 70px;
    position: relative;
    overflow: hidden;
    background: none;
}

.hero-video-bg {
    position: absolute;
    top: 50%;
    left: 50%;
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    transform: translateX(-50%) translateY(-50%);
    z-index: 1;
    object-fit: cover;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5); /* darkened overlay */
    z-index: 2;
}

.hero-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    position: relative;
    z-index: 3;
}

/* Update text colors in hero */
.hero-title, .hero-description {
    color: #ffffff;
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}

.hero-subtitle {
    color: #b3d7ff; /* Lighter vivid blue */
    text-shadow: 0 1px 3px rgba(0,0,0,0.5);
}

/* Dynamics */
.publication-card, .project-card, .reviewer-card, .timeline-content {
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.publication-card:hover, .project-card:hover, .reviewer-card:hover, .timeline-content{
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    border-color: #007BFF;
}
"""

css = css.replace("""/* Hero Section */
.hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
    padding-top: 70px;
}""", new_css)

with open('portfolio/styles.css', 'w') as f:
    f.write(css)
