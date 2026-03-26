import codecs
import re

with codecs.open('portfolio/index.html', 'r', 'utf-8') as f:
    html = f.read()

replacement = """<div class="publications-grid">
                    <!-- Previous Conference Papers -->
                    <div class="publication-card">
                        <h4>Electric Vehicle Charging System Using RFID and IoT for Enhanced User Experience</h4>
                        <p class="authors">Md Mehedi Hassain, Injamul Haque Jamil,<strong>Md Mahmudul Hoque</strong>, Md. Jahid Hasan </p>
                        <p class="venue">2025 5th IEEE Middle East and North Africa Communications Conference (MENACOMM)</p>
                        <a href="https://ieeexplore.ieee.org/document/10939669" class="publication-link" target="_blank">View Paper</a>
                    </div>
                    <div class="publication-card">
                        <h4>A comparison of Bangladeshi daily news portals' various clustering techniques for online revenue generation</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Ikbal Ahmed and Injamul Haque Jamil</p>
                        <p class="venue">2024 International Conference on Innovations in Science, Engineering and Technology (ICISET)</p>
                        <a href="https://ieeexplore.ieee.org/document/10939669" class="publication-link" target="_blank">View Paper</a>
                    </div>
                    <div class="publication-card">
                        <h4>Sentiment Polarity Analysis of Bangla Food Reviews Using Machine and Deep Learning Algorithms</h4>
                        <p class="authors">Al Amin, Anik Sarkar, Md Mahamodul Islam, Asif Ahammad Miazee, Md Robiul Islam, and <strong>Md Mahmudul Hoque</strong></p>
                        <p class="venue">2024 3rd International Conference on Advancement in Electrical and Electronic Engineering (ICAEEE)</p>
                        <a href="https://ieeexplore.ieee.org/document/10561876" class="publication-link" target="_blank">View Paper</a>
                    </div>
                    <div class="publication-card">
                        <h4>Analyzing Price Forecasting of Grocery Products in Bangladesh: A Comparison of Time Series Modeling Approaches</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Ikbal Ahmed, Nayan Banik, and Mohammed Moshiul Hoque</p>
                        <p class="venue">International Conference on Intelligent Computing & Optimization, 2023</p>
                        <a href="https://link.springer.com/chapter/10.1007/978-3-031-50158-6_33" class="publication-link" target="_blank">View Paper</a>
                    </div>

                    <!-- New Conference Papers -->
                    <div class="publication-card">
                        <h4>Computer Vision Hybrid Approach: CNN and Transformer Models for Accurate Alzheimer’s Detection from Brain MRI Scans.</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Shuvo Karmaker, Md. Hadi Al-amin, Md Modabberul Islam, Jisun Junayed, Farha Ulfat Mahi</p>
                        <p class="venue">7th Mediterranean Conference on Pattern Recognition & Artificial Intelligence (MedPRAI), Jan 23–24, 2026, Istinye University, Istanbul, Turkey.</p>
                        <span class="status" style="margin-right:15px; display:inline-block; padding: 2px 8px; font-size: 0.8rem;">Accepted (Springer)</span>
                        <a href="https://doi.org/10.48550/arXiv.2601.15202" class="publication-link" target="_blank">View Paper/DOI</a>
                    </div>

                    <div class="publication-card">
                        <h4>Vision Models for Medical Imaging: A Hybrid Approach for PCOS Detection from Ultrasound Scans.</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Md Mehedi Hassain, Muntakimur Rahaman, Md Towhidul Islam, Shaista Rani, Md Sharif Mollah</p>
                        <p class="venue">International Conference on System Engineering,Technology, and Sustainable Solutions (ICSETS 2025), Nov 3-6, Muscat, Oman.</p>
                        <span class="status" style="margin-right:15px; display:inline-block; padding: 2px 8px; font-size: 0.8rem;">Accepted (IOP)</span>
                        <a href="https://doi.org/10.48550/arXiv.2601.15119" class="publication-link" target="_blank">View Paper/DOI</a>
                    </div>

                    <div class="publication-card">
                        <h4>Bengali Text Classification: An Evaluation of Large Language Model Approaches</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Md Mehedi Hassain, Md Hojaifa Tanvir, Rahul Nandi</p>
                        <p class="venue">International Conference on Intelligent Digital Systems and Sustainable Technology (ICIDST), June 24-25, Al Farahidi University, Baghdad, Iraq.</p>
                        <span class="status" style="margin-right:15px; display:inline-block; padding: 2px 8px; font-size: 0.8rem;">Accepted (Springer)</span>
                        <a href="https://doi.org/10.48550/arXiv.2601.12132" class="publication-link" target="_blank">View Paper/DOI</a>
                    </div>

                    <div class="publication-card">
                        <h4>Bangla Music Genre Classification Using Bidirectional LSTMS</h4>
                        <p class="authors">Muntakimur Rahaman, <strong>Md Mahmudul Hoque</strong>, Md Mehedi Hassain</p>
                        <p class="venue">International Conference on Intelligent Digital Systems and Sustainable Technology (ICIDST), June 24-25, Al Farahidi University, Baghdad, Iraq.</p>
                        <span class="status" style="margin-right:15px; display:inline-block; padding: 2px 8px; font-size: 0.8rem;">Accepted (Springer)</span>
                        <a href="https://doi.org/10.48550/arXiv.2601.15083" class="publication-link" target="_blank">View Paper/DOI</a>
                    </div>

                    <div class="publication-card">
                        <h4>Machine Learning Algorithms and Image Processing based Smart Parking System using IoT</h4>
                        <p class="authors">Md Mehedi Hassain, <strong>Md Mahmudul Hoque</strong>, Rahul Nondi, Md Hojaifa Tanvir, Saad Ahmed</p>
                        <p class="venue">In: Idrissi, N., et al. Artificial Intelligence and Green Computing. ICAIGC 2025. Lecture Notes in Networks and Systems, vol 1589. Springer, Cham.</p>
                        <a href="https://doi.org/10.1007/978-3-032-02312-4_2" class="publication-link" target="_blank">View Paper/DOI</a>
                    </div>

                    <div class="publication-card">
                        <h4>A Comparative and Hybrid Study of CNN and Transformer Models for Multi-Class Virus Classification in Transmission Electron Microscopy.</h4>
                        <p class="authors"><strong>Md Mahmudul Hoque</strong>, Md. Mamunur Rahman Moon, Md. Hadi Al-amin, H.M. Asraf</p>
                        <p class="venue">1th International Conference on Information and Communication Technology for Intelligent Systems, APRIL 9 - 11, 2026 in Bangkok, Thailand.</p>
                        <span class="status" style="display:inline-block; padding: 2px 8px; font-size: 0.8rem;">Accepted (Springer)</span>
                    </div>

                    <div class="publication-card">
                        <h4>LSB Image Steganography Detection Using CNN With L2 Regularization</h4>
                        <p class="authors">Afroza Islam, Ikbal Ahmed, Farhana Abedin, <strong>Md Mahmudul Hoque</strong>, Auntor Chandra Das</p>
                        <p class="venue">2nd International Conference on Intelligent Systems, Blockchain, and Communication Technologies, ElSewedy University of Technology, Egypt.</p>
                        <span class="status" style="display:inline-block; padding: 2px 8px; font-size: 0.8rem;">Accepted (Springer)</span>
                    </div>
                </div>"""

pattern = re.compile(r'(<h3 class="category-title">Conference Publications</h3>\s*)<div class="publications-grid">.*?</div>(\s*</div>\s*<!-- Journal Publications -->)', re.DOTALL)
match = pattern.search(html)

if match:
    html = html[:match.start()] + match.group(1) + replacement + match.group(2) + html[match.end():]
    with codecs.open('portfolio/index.html', 'w', 'utf-8') as f:
        f.write(html)
    print("Successfully replaced.")
else:
    print("Failed to find the Conference Publications grid.")
