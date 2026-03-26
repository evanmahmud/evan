import codecs
import re

with codecs.open('portfolio/styles.css', 'r', 'utf-8') as f:
    css = f.read()

# Make Publication Link Teal/Green
css = re.sub(
    r'\.publication-link\s*\{\s*color:\s*#007BFF;(\s*.*?)\}',
    r'.publication-link {\n    color: #20c997;\1}', 
    css, flags=re.DOTALL
)

css = re.sub(
    r'\.publication-link:hover\s*\{\s*color:\s*#0056b3;(\s*.*?)\}',
    r'.publication-link:hover {\n    color: #138496;\1}',
    css, flags=re.DOTALL
)

# Add active/click state and dynamic text for About Section
click_css = """
.publication-link:active {
    color: #0f6674;
    transform: scale(0.95);
    display: inline-block;
}

/* Dynamic Text for About Section and Info Items (Education/Research) */
.about-text p, .info-item p {
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    padding: 5px;
    border-radius: 5px;
}

.about-text p:hover, .info-item p:hover {
    transform: translateX(10px) scale(1.02);
    color: #20c997; /* Change to teal on hover */
    background-color: rgba(32, 201, 151, 0.05); /* Slight dynamic background glow */
    text-shadow: 0 1px 2px rgba(0,0,0,0.1);
}
"""

if "rgba(32, 201, 151, 0.05);" not in css:
    css += click_css
    with codecs.open('portfolio/styles.css', 'w', 'utf-8') as f:
        f.write(css)
    print("Added dynamic text to about and teal click colors!")
else:
    print("Already added.")
