import codecs
import re

with codecs.open('portfolio/styles.css', 'r', 'utf-8') as f:
    css = f.read()

# Replace old generic hover rule for border colors
css = re.sub(
    r'border-color:\s*#007BFF;',
    r'border-left-color: #20c997;',
    css
)

glowing_glow = """
/* Smart App Glows */
.publication-card:hover, .project-card:hover, .reviewer-card:hover, .timeline-content:hover {
    border-left-color: #20c997 !important;
    box-shadow: 0 15px 35px rgba(32, 201, 151, 0.25) !important; /* Teal glowing shadow */
}

/* Nav Link Hover Green/Teal */
.nav-link:hover::after {
    background-color: #20c997;
}
.nav-link:hover {
    color: #20c997;
}

/* Primary Button Smart Styling */
.btn-primary {
    background: linear-gradient(135deg, #007BFF, #20c997);
    border: none;
    box-shadow: 0 4px 15px rgba(32, 201, 151, 0.3);
}
.btn-primary:hover {
    background: linear-gradient(135deg, #20c997, #007BFF);
    box-shadow: 0 6px 20px rgba(32, 201, 151, 0.5) !important;
    color: white !important;
}

/* Section Title Underlines Teal */
.section-title::after {
    background-color: #20c997;
}
"""

if "Smart App Glows" not in css:
    css += glowing_glow

with codecs.open('portfolio/styles.css', 'w', 'utf-8') as f:
    f.write(css)

print("Smart styling and green left borders applied!")
