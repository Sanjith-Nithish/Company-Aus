import re

# 1. Update index.html to add previews
with open('docs/index.html', 'r', encoding='utf-8') as f:
    idx_html = f.read()

preview_html = """
<!-- PREVIEWS -->
<section class="section" style="background:var(--ink)">
  <div class="wrap" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:3rem">
    
    <div style="background:var(--deep);border:1px solid var(--border);border-radius:2px;padding:2rem">
      <div style="width:50px;height:50px;background:var(--gold);color:var(--ink);display:flex;align-items:center;justify-content:center;font-size:1.5rem;border-radius:2px;margin-bottom:1.5rem">ΓÜÖ∩╕Å</div>
      <h3 style="font-family:'Barlow Condensed',sans-serif;font-size:1.8rem;color:var(--white);margin-bottom:1rem">About Inlec</h3>
      <p style="color:var(--fog);line-height:1.7;margin-bottom:2rem">We are a distinguished analytical devices engineering services firm, boasting 60+ years of combined experience across process industries globally.</p>
      <a href="about.html" class="btn-line" style="font-size:0.85rem;padding:0.6rem 1.4rem">Read Our Story ΓåÆ</a>
    </div>

    <div style="background:var(--deep);border:1px solid var(--border);border-radius:2px;padding:2rem">
      <div style="width:50px;height:50px;background:rgba(26,127,168,0.3);color:var(--sky);display:flex;align-items:center;justify-content:center;font-size:1.5rem;border-radius:2px;border:1px solid var(--sky);margin-bottom:1.5rem">≡ƒö¼</div>
      <h3 style="font-family:'Barlow Condensed',sans-serif;font-size:1.8rem;color:var(--white);margin-bottom:1rem">Our Services</h3>
      <p style="color:var(--fog);line-height:1.7;margin-bottom:2rem">From design and FAT through to site commissioning, traceable calibration, and ongoing sample system troubleshooting.</p>
      <a href="services.html" class="btn-line" style="font-size:0.85rem;padding:0.6rem 1.4rem">View Services ΓåÆ</a>
    </div>

    <div style="background:var(--deep);border:1px solid var(--border);border-radius:2px;padding:2rem">
      <div style="width:50px;height:50px;background:rgba(200,136,10,0.15);color:var(--gold);display:flex;align-items:center;justify-content:center;font-size:1.5rem;border-radius:2px;border:1px solid var(--gold);margin-bottom:1.5rem">≡ƒîí∩╕Å</div>
      <h3 style="font-family:'Barlow Condensed',sans-serif;font-size:1.8rem;color:var(--white);margin-bottom:1rem">Area of Expertise</h3>
      <p style="color:var(--fog);line-height:1.7;margin-bottom:2rem">Extensive technical depth across Gas Chromatographs, In-Situ, Extractive, CEMS, Water Quality, and Petrochemical property analyzers.</p>
      <a href="expertise.html" class="btn-line" style="font-size:0.85rem;padding:0.6rem 1.4rem">Explore Expertise ΓåÆ</a>
    </div>

  </div>
</section>
"""

if "<!-- PREVIEWS -->" not in idx_html:
    idx_html = re.sub(r'(<div id="trust">.*?</div>)', r'\1\n' + preview_html, idx_html, flags=re.DOTALL)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(idx_html)


# 2. Expand About.html with an infographic and more info
with open('docs/about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

about_expansion = """
<!-- INFOGRAPHIC SECTION -->
<section class="section" style="background:var(--ink);border-top:1px solid var(--border2)">
  <div class="wrap">
    <div class="eyebrow">Our Legacy in Data</div>
    <span class="rule"></span>
    <h2 style="font-size:clamp(2rem,4vw,3rem);color:var(--white);margin-bottom:3rem">The Inlec Blueprint</h2>
    
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center;">
      <div>
        <h3 style="font-family:'Barlow Condensed';font-size:1.5rem;color:var(--gold2);margin-bottom:1rem">Decades of Cumulative Insight</h3>
        <p style="color:var(--fog);line-height:1.8;margin-bottom:1.5rem">When we say we have 60+ years of combined experience, we mean deep-trench, front-line involvement in some of the most complex analyzer migrations in the Southern Hemisphere. We don't just read manuals; we write the procedures that manufacturers adopt.</p>
        <p style="color:var(--fog);line-height:1.8">Our approach is built on a foundation of measurable, data-driven outcomes. Every calibration, every commissioning phase, and every maintenance cycle is documented, analyzed, and optimized.</p>
      </div>
      
      <!-- CSS Infographic -->
      <div style="background:var(--deep);border:1px solid var(--border);padding:2rem;border-radius:2px;position:relative;overflow:hidden">
        <div style="position:absolute;top:0;right:0;width:150px;height:150px;background:radial-gradient(circle,rgba(200,136,10,0.1),transparent);filter:blur(20px)"></div>
        <h4 style="font-family:'Oswald';color:var(--white);font-size:1.2rem;margin-bottom:1.5rem;display:flex;justify-content:space-between"><span>System Reliability Index</span><span style="color:var(--gold)">99.8%</span></h4>
        
        <div style="display:flex;align-items:flex-end;gap:15px;height:180px;border-bottom:1px solid rgba(255,255,255,0.1);padding-bottom:10px;margin-bottom:10px">
          <!-- Bars -->
          <div style="flex:1;background:rgba(26,127,168,0.4);height:30%;border-top:2px solid var(--sky)"></div>
          <div style="flex:1;background:rgba(26,127,168,0.5);height:45%;border-top:2px solid var(--sky)"></div>
          <div style="flex:1;background:rgba(26,127,168,0.6);height:60%;border-top:2px solid var(--sky)"></div>
          <div style="flex:1;background:rgba(26,127,168,0.8);height:85%;border-top:2px solid var(--sky)"></div>
          <div style="flex:1;background:var(--gold);height:100%;box-shadow:0 0 20px rgba(200,136,10,0.4)"></div>
        </div>
        
        <div style="display:flex;justify-content:space-between;color:rgba(255,255,255,0.4);font-family:'Barlow Condensed';font-size:0.8rem">
          <span>2021</span><span>2022</span><span>2023</span><span>2024</span><span style="color:var(--gold2)">2025 Projected</span>
        </div>
      </div>
    </div>
  </div>
</section>
"""

if "<!-- INFOGRAPHIC SECTION -->" not in about_html:
    about_html = about_html.replace('</section>\n<footer>', '</section>\n' + about_expansion + '\n<footer>')
    with open('docs/about.html', 'w', encoding='utf-8') as f:
        f.write(about_html)


# 3. Expand Services.html with big graphic wrapper
with open('docs/services.html', 'r', encoding='utf-8') as f:
    srv_html = f.read()

srv_expansion = """
<div class="wrap" style="margin-bottom:4rem">
  <!-- Dynamic Image Placeholder -->
  <div style="width:100%;height:400px;background:url('https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?auto=format&fit=crop&q=80&w=1600') center/cover;position:relative;border-radius:2px;overflow:hidden;border:1px solid var(--border)">
    <div style="position:absolute;inset:0;background:linear-gradient(to right, rgba(8,15,24,0.95) 0%, rgba(8,15,24,0.4) 100%)"></div>
    <div style="position:absolute;top:50%;transform:translateY(-50%);left:clamp(2rem,5vw,5rem);max-width:500px">
       <span class="pill" style="margin-bottom:1rem">Comprehensive Capability</span>
       <h2 style="font-family:'Oswald';font-size:clamp(2.5rem,5vw,4rem);color:var(--white);line-height:1.1;margin-bottom:1rem">Engineered<br><span style="color:var(--gold)">To Perform.</span></h2>
       <p style="color:var(--fog);font-size:1.1rem;line-height:1.6">We mitigate risk and maximize uptime by offering a continuous lifecycle of analytical support. Dive deep into our core offerings below.</p>
    </div>
  </div>
</div>
"""

if "Dynamic Image Placeholder" not in srv_html:
    srv_html = srv_html.replace('<div class="services-header r">', srv_expansion + '\n<div class="services-header r">')
    with open('docs/services.html', 'w', encoding='utf-8') as f:
        f.write(srv_html)


print("Content expansions injected!")
