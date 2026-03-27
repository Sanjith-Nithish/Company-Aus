import re, os

with open('docs/index_base.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update navigation links in the HTML globally
# Original: <a href="#about">About</a> -> New: <a href="about.html">About</a>
nav_links = {
    '#about': 'about.html',
    '#services': 'services.html',
    '#expertise': 'expertise.html',
    '#industries': 'industries.html',
    '#team': 'team.html',
    '#contact': 'contact.html'
}

for old_link, new_link in nav_links.items():
    html = html.replace(f'href="{old_link}"', f'href="{new_link}"')

# Also fix the logo link to go to index.html
html = html.replace('href="#" class="logo-wrap"', 'href="index.html" class="logo-wrap"')

# 2. Extract Head + Nav (Everything before <section id="hero">)
hero_match = re.search(r'<section id="hero">', html)
if not hero_match:
    print("Could not find hero section")
    exit(1)

head_nav = html[:hero_match.start()]

# 3. Extract Footer
footer_match = re.search(r'<footer>', html)
if not footer_match:
    print("Could not find footer")
    exit(1)

footer = html[footer_match.start():]

# 4. Extract sections
sections = {}
section_ids = ['hero', 'about', 'services', 'expertise', 'industries', 'team', 'contact']
# Extract trust bar specifically
trust_match = re.search(r'<div id="trust">.*?</div>\n\n<!--', html, flags=re.DOTALL)
trust_html = trust_match.group(0).rsplit('<!--', 1)[0] if trust_match else ""

for s_id in section_ids:
    if s_id == 'trust': continue
    pattern = rf'<section id="{s_id}"(.*?</section>)'
    if s_id == 'contact':
        # Contact is not a <section>? Oh wait, it is a section or div? Let's check regex with <section or <div
        pattern = rf'<(section|div) id="{s_id}"(.*?</\1>)'
    
    match = re.search(pattern, html, flags=re.DOTALL)
    if match:
        sections[s_id] = match.group(0)
    else:
        print(f"Could not find section {s_id}")

# 5. Build individual pages
pages = {
    'index.html': sections.get('hero', '') + '\n' + trust_html,
    'about.html': sections.get('about', ''),
    'services.html': sections.get('services', ''),
    'expertise.html': sections.get('expertise', ''),
    'industries.html': sections.get('industries', ''),
    'team.html': sections.get('team', ''),
    'contact.html': sections.get('contact', '').replace('href="contact.html"', 'href="#contact"') # wait, contact forms have #contact perhaps
}

for page, content in pages.items():
    if not content: continue
    
    # We add a generic spacing div if it's not the homepage so the nav doesn't overlap
    padding = '\n<div style="padding-top: 80px;"></div>\n' if page != 'index.html' else ''
    
    full_page = head_nav + padding + content + '\n' + footer
    with open(f'docs/{page}', 'w', encoding='utf-8') as f:
        f.write(full_page)

print("Pages split successfully!")
