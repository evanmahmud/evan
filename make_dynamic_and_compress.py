import codecs
import re
import os
import subprocess
import shutil

# --- 1. Update script.js for Dynamic Text ---
with codecs.open('portfolio/script.js', 'r', 'utf-8') as f:
    js = f.read()

# Make all text elements dynamic
if "document.querySelectorAll('h1, h2, h3, h4, p," not in js:
    js = js.replace(
        "const elementsToAnimate = document.querySelectorAll('.publication-card, .timeline-item, .skill-category, .contact-item');",
        "const elementsToAnimate = document.querySelectorAll('h1, h2, h3, h4, p, .publication-card, .project-card, .reviewer-card, .timeline-item, .skill-category, .contact-item');"
    )
    with codecs.open('portfolio/script.js', 'w', 'utf-8') as f:
        f.write(js)
    print("Updated script.js for text animations.")

# --- 2. Update styles.css for animations ---
with codecs.open('portfolio/styles.css', 'r', 'utf-8') as f:
    css = f.read()

if '.fade-in {' not in css:
    css += """
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}
"""
    with codecs.open('portfolio/styles.css', 'w', 'utf-8') as f:
        f.write(css)
    print("Updated styles.css with fade-in animations.")
else:
    # If fade-in exists in original, ensure it's robust
    if "transform: translateY(30px);" not in css:
        css += """
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.165, 0.84, 0.44, 1), transform 0.8s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}
"""
        with codecs.open('portfolio/styles.css', 'w', 'utf-8') as f:
            f.write(css)
        print("Appended robust fade-in animations to styles.css.")


# --- 3. Compress the 193MB Video for GitHub (Limit is 100MB) ---
video_path = "portfolio/background-video.mp4"
compressed_path = "portfolio/bg-compressed.mp4"
if os.path.exists(video_path):
    size_mb = os.path.getsize(video_path) / (1024 * 1024)
    print(f"Current video size: {size_mb:.2f} MB")
    
    if size_mb > 50:
        print("Video is too large for GitHub (>100MB risk), compressing...")
        ffmpeg_path = shutil.which("ffmpeg")
        
        if not ffmpeg_path:
            try:
                import imageio_ffmpeg
                ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
            except ImportError as e:
                print("imageio-ffmpeg not found, skipping compression.", e)
        
        if ffmpeg_path:
            try:
                # -an removes audio, -crf 32 reduces quality heavily (good for background), -preset fast speeds it up
                subprocess.run([ffmpeg_path, "-y", "-i", video_path, "-vcodec", "libx264", "-crf", "32", "-preset", "fast", "-an", compressed_path], check=True)
                if os.path.exists(compressed_path):
                    new_size = os.path.getsize(compressed_path) / (1024 * 1024)
                    os.replace(compressed_path, video_path)
                    print(f"Compression successful! New size: {new_size:.2f} MB")
            except Exception as e:
                print("FFmpeg compression failed:", e)
    else:
        print("Video is already small enough.")
else:
    print("Video file not found!")
