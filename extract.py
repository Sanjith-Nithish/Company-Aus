import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract styles
style_match = re.search(r'<style>(.*?)</style>', html, flags=re.DOTALL)
if style_match:
    with open('docs/styles.css', 'w', encoding='utf-8') as f:
        f.write(style_match.group(1).strip())
    html = html[:style_match.start()] + '<link rel=\"stylesheet\" href=\"styles.css\">\n' + html[style_match.end():]

# Extract scripts
script_match = re.search(r'<script>(.*?)</script>', html, flags=re.DOTALL)
if script_match:
    with open('docs/script.js', 'w', encoding='utf-8') as f:
        f.write(script_match.group(1).strip())
    html = html[:script_match.start()] + '<script src=\"script.js\"></script>\n' + html[script_match.end():]

with open('docs/index_base.html', 'w', encoding='utf-8') as f:
    f.write(html)
