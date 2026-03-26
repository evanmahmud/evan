import codecs

with codecs.open('portfolio/styles.css', 'r', 'utf-8') as f:
    css = f.read()

jumping_css = """
/* Jumping Text Animation for Education & Research Interests */
@keyframes jump-text {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-8px); }
    60% { transform: translateY(-4px); }
}

.info-item h3 {
    animation: jump-text 2.5s infinite;
    display: inline-block;
    color: #007BFF;
}

.info-item p {
    transition: transform 0.3s ease;
}

.info-item:hover p {
    transform: translateX(5px);
}

.info-item {
    transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.4s ease;
}

.info-item:hover {
    transform: translateY(-12px);
    box-shadow: 0 10px 30px rgba(0, 123, 255, 0.15);
    border-left-color: #28a745;
}
"""

if "jump-text" not in css:
    css += jumping_css
    with codecs.open('portfolio/styles.css', 'w', 'utf-8') as f:
        f.write(css)
    print("Added jumping animation to Education and Research interests!")
else:
    print("Animation already exists.")
