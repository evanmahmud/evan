import codecs
import re

with codecs.open('portfolio/index.html', 'r', 'utf-8') as f:
    html = f.read()

# 1. REWRITE the Upcoming Projects Section to completely wipe out the massacre HTML
new_projects_section = """<!-- Upcoming Projects Section -->
    <section id="upcoming-projects" class="upcoming-projects">
        <div class="container">
            <h2 class="section-title">Upcoming Projects</h2>
            <div class="projects-grid">
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
            </div>
        </div>
    </section>"""

# Replace the mangled upcoming-projects section completely
html = re.sub(r'<!-- Upcoming Projects Section -->\s*<section id="upcoming-projects".*?</section>', new_projects_section, html, flags=re.DOTALL)

with codecs.open('portfolio/index.html', 'w', 'utf-8') as f:
    f.write(html)

with codecs.open('portfolio/styles.css', 'r', 'utf-8') as f:
    css = f.read()

# 2. Fix CSS fixed heights causing textual "massacre" (overflow out of the card boundaries)
css = re.sub(r'height:\s*260px;', 'min-height: 260px; height: auto;', css)
css = re.sub(r'height:\s*200px;', 'min-height: 200px; height: auto;', css)

# 3. Add projects-grid CSS
if '.projects-grid' not in css:
    css += """
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
    min-height: 300px;
}
"""

with codecs.open('portfolio/styles.css', 'w', 'utf-8') as f:
    f.write(css)

print("Layout massacre fixed!")
