"""Builds the static multi-page site for Faraz Abdul Razzak & Co.
Run: python3 build.py   (writes the .html files next to this script)"""
import os, sys
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

FIRM = "Faraz Abdul Razzak & Co."
CONTACT = "Ms. Aysha Mehmood"            # website contact person (call + WhatsApp)
PHONE, PHONE_INTL = "0330-3937036", "+923303937036"
FARAZ_PHONE, FARAZ_INTL = "0333-2661981", "+923332661981"
EMAIL = "farazrazzakcompany@gmail.com"
WA = "https://wa.me/923303937036?text=Enquiry%20from%20website"
ADDRESS = "142, 1st Floor, Al-Amna Plaza, opposite Capri Cinema, M.A. Jinnah Road, Karachi, Pakistan"
MAPS = "https://www.google.com/maps/search/?api=1&query=Al-Amna+Plaza+M.A.+Jinnah+Road+Karachi"

LOGO = """<svg viewBox="0 0 48 48" aria-hidden="true"><rect width="48" height="48" rx="10" fill="#12305a"/>
<rect x="9" y="28" width="7" height="11" rx="1.5" fill="#7fb0ec"/><rect x="19" y="22" width="7" height="17" rx="1.5" fill="#4d8fd8"/>
<rect x="29" y="15" width="7" height="24" rx="1.5" fill="#2a6db5"/>
<path d="M10 24 L30 9" stroke="#e2bd6c" stroke-width="2.4" stroke-linecap="round" fill="none"/>
<path d="M24 8.5 L31.5 8 L30 15" stroke="#e2bd6c" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>"""

WA_ICON = """<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6a2.8 2.8 0 0 0 1.8-1.3 2.3 2.3 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3z"/></svg>"""
PHONE_ICON = """<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.2 11.4 11.4 0 0 0 3.6.6 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .6 3.6 1 1 0 0 1-.3 1z"/></svg>"""

ICONS = {  # simple line icons for service cards
 "audit": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 11l2 2 4-4"/><rect x="4" y="3" width="16" height="18" rx="2"/></svg>',
 "internal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/></svg>',
 "secp": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21h18M5 21V10l7-5 7 5v11M9 21v-6h6v6"/></svg>',
 "tax": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 5L5 19"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/></svg>',
 "accounting": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M16 11h0M8 15h2M12 15h2M8 18h8"/></svg>',
}

NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("insights.html", "Insights"), ("contact.html", "Contact")]

SERVICES = [
    ("audit-assurance.html", "Audit & Assurance", "audit",
     "Statutory audit of eligible private companies, and audit of trusts, NGOs, individuals, sole proprietors and AOPs."),
    ("internal-audit.html", "Internal Audit, Risk & Advisory", "internal",
     "Internal audit, review of internal controls and risks, and practical business advice."),
    ("corporate-secp.html", "Corporate & SECP Compliance", "secp",
     "Company incorporation, secretarial work and statutory filings with the SECP."),
    ("tax-advisory.html", "Tax Advisory & Filing", "tax",
     "Income tax and sales tax returns, tax advice, and matters before the FBR and SRB."),
    ("accounting.html", "Accounting & Financial Statements", "accounting",
     "Bookkeeping, preparation of financial statements, and cost and management accounting."),
]


def section_of(fname):
    if fname in [s[0] for s in SERVICES]:
        return "services.html"
    if fname.startswith("article"):
        return "insights.html"
    return fname


def page(fname, title, description, body):
    cur = section_of(fname)
    nav = "".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a></li>' for h, t in NAV)
    services_links = "".join(f'<li><a href="{s[0]}">{escape(s[1])}</a></li>' for s in SERVICES)
    full_title = f"{title} | {FIRM}" if fname != "index.html" else f"{FIRM} | Chartered Management Accountants, Karachi"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600&family=Source+Serif+4:opsz,wght@8..60,600&display=swap">
<link rel="stylesheet" href="css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap">
  <div><span>Karachi, Pakistan</span><span class="hide-sm">Open Monday to Saturday</span></div>
  <div><span>WhatsApp: <a href="{WA}">{PHONE}</a></span><span class="hide-sm">Mr. Faraz Abdul Razzak: <a href="tel:{FARAZ_INTL}">{FARAZ_PHONE}</a></span></div>
</div></div>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html">{LOGO}<span><span class="brand-name">{escape(FIRM)}</span><span class="brand-sub">Chartered Management Accountants</span></span></a>
    <button class="menu-btn" id="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main"><ul>{nav}</ul><a class="btn btn-primary" href="{WA}">{WA_ICON} WhatsApp</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <h3>{escape(FIRM)}</h3>
        <p>Chartered Management Accountants<br>Partner: Fellow member of ICMA Pakistan</p>
        <p style="margin-top:10px">{escape(ADDRESS)}</p>
      </div>
      <div>
        <h3>Contact</h3>
        <ul>
          <li>{CONTACT}: <a href="tel:{PHONE_INTL}">{PHONE}</a> (call and WhatsApp)</li>
          <li>Mr. Faraz Abdul Razzak: <a href="tel:{FARAZ_INTL}">{FARAZ_PHONE}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Open Monday to Saturday</li>
        </ul>
      </div>
      <div>
        <h3>Services</h3>
        <ul>{services_links}</ul>
      </div>
    </div>
    <div class="base">
      <span>&copy; 2026 {escape(FIRM)}</span>
      <span><a href="privacy.html">Privacy Notice</a></span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA}" aria-label="Message {CONTACT} on WhatsApp">{WA_ICON}</a>
<div class="call-bar"><a href="tel:{PHONE_INTL}">Call {PHONE}</a><a href="{WA}">WhatsApp</a></div>
<script>
(function () {{
  var b = document.getElementById('menu-btn'), n = document.getElementById('site-nav');
  b.addEventListener('click', function () {{
    var open = n.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
  var r = document.querySelector('.rotator span');
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (r && !still) {{
    var words = JSON.parse(r.parentNode.getAttribute('data-words')), i = 0;
    setInterval(function () {{
      r.classList.add('out');
      setTimeout(function () {{
        i = (i + 1) % words.length; r.textContent = words[i];
        r.classList.remove('out'); r.classList.add('in');
        void r.offsetWidth; r.classList.remove('in');
      }}, 450);
    }}, 2600);
  }}
}})();
</script>
</body>
</html>
"""


def cta(heading="Discuss your requirements", text=f"Call or WhatsApp {CONTACT} on {PHONE}. We are open Monday to Saturday."):
    return f"""<section class="cta"><div class="wrap">
  <div><h2>{heading}</h2><p>{text}</p></div>
  <div class="hero-actions" style="margin-top:0">
    <a class="btn btn-primary" href="tel:{PHONE_INTL}">{PHONE_ICON} Call {PHONE}</a>
    <a class="btn btn-ghost" href="{WA}">{WA_ICON} WhatsApp</a>
  </div>
</div></section>"""


def cards():
    return '<div class="cards">' + "".join(
        f'<a class="card" href="{h}"><span class="icon">{ICONS[k]}</span><h3>{escape(t)}</h3><p>{escape(d)}</p><span class="go">Explore service &rarr;</span></a>'
        for h, t, k, d in SERVICES) + "</div>"


def ticker():
    items = ["Statutory audit", "Audit of trusts and NGOs", "Income tax returns", "Sales tax returns (FBR and SRB)",
             "SECP filings", "Company incorporation", "Internal audit", "Financial statements", "Cost and management accounting"]
    row = "".join(f"<span>{i}</span>" for i in items)
    return f'<div class="ticker" aria-hidden="true"><div class="ticker-track">{row}{row}</div></div>'


schedule = cards  # inner pages call schedule()

PAGES = {}

from articles import ARTICLES, article_cards  # noqa: E402

ROT = ["audit", "tax filing", "SECP compliance", "internal audit", "accounting"]
PAGES["index.html"] = ("Home",
  "Chartered Management Accountants in Karachi: audit, tax, SECP compliance, internal audit and accounting.",
  f"""<section class="hero"><div class="wrap">
  <div>
    <h1 class="rise">Partner-led <span class="rotator" data-words='{escape(str(ROT).replace("'", '"'))}'><span>{ROT[0]}</span></span><br>for businesses and non-profits in Karachi</h1>
    <p class="lead rise rise-2">{escape(FIRM)} is a firm of Chartered Management Accountants led by Faraz Abdul Razzak, FCMA. We help private companies, trusts, NGOs, individuals and AOPs keep accurate books, file on time and meet their legal obligations.</p>
    <div class="hero-actions rise rise-3">
      <a class="btn btn-primary" href="tel:{PHONE_INTL}">{PHONE_ICON} Call {PHONE}</a>
      <a class="btn btn-ghost" href="{WA}">{WA_ICON} WhatsApp {CONTACT}</a>
    </div>
    <div class="badges"><span>Partner-led</span><span>Grounded in the law</span><span>Confidential</span></div>
  </div>
  <dl class="credentials rise rise-2">
    <div><dt>Led by</dt><dd>Faraz Abdul Razzak, FCMA</dd></div>
    <div><dt>Professional body</dt><dd>Institute of Cost and Management Accountants of Pakistan</dd></div>
    <div><dt>Experience</dt><dd>22 years in finance, governance, compliance and internal audit</dd></div>
    <div><dt>Contact</dt><dd>{CONTACT} &middot; {PHONE} (WhatsApp)<br>Mr. Faraz Abdul Razzak &middot; {FARAZ_PHONE}</dd></div>
  </dl>
</div></section>
{ticker()}

<section class="section"><div class="wrap">
  <div class="section-head"><span class="label">Services</span><h2>Five areas of practice</h2>
  <p class="muted">Each engagement is overseen by the partner, with a clear scope and fee agreed before work begins.</p></div>
  {cards()}
</div></section>

<section class="section alt"><div class="wrap two-col">
  <div class="section-head" style="margin:0"><span class="label">Why work with us</span><h2>Qualified, direct and confidential</h2>
  <p class="muted">A small practice means your work is overseen by the qualified professional who signs it.</p></div>
  <ul class="points">
    <li><strong>Partner-level attention</strong><span class="muted">Faraz personally oversees every engagement.</span></li>
    <li><strong>Grounded in the law</strong><span class="muted">Advice references the Income Tax Ordinance, Sales Tax Act, Companies Act 2017 and current SECP, FBR and SRB notifications.</span></li>
    <li><strong>Confidential by default</strong><span class="muted">Client information is never shared or named without written consent.</span></li>
    <li><strong>Deadlines tracked</strong><span class="muted">We plan your filings around their due dates.</span></li>
  </ul>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="label">How it works</span><h2>Four steps to get started</h2></div>
  <ol class="how">
    <li><strong>Get in touch</strong><span class="muted">Call or WhatsApp {CONTACT} with a short description of what you need.</span></li>
    <li><strong>Share your records</strong><span class="muted">Send last year's documents so we can assess the work.</span></li>
    <li><strong>Agree scope and fee</strong><span class="muted">We confirm scope, timeline and fee in an engagement letter.</span></li>
    <li><strong>Work delivered</strong><span class="muted">One point of contact from start to finish.</span></li>
  </ol>
</div></section>

<section class="section alt"><div class="wrap">
  <blockquote class="quote">Clients get partner-level attention, practical advice and work delivered to professional standards.<cite>Faraz Abdul Razzak, FCMA, Partner &amp; CEO</cite></blockquote>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><span class="label">Insights</span><h2>Latest updates</h2></div>
  <div class="articles">{article_cards(ARTICLES[:3])}</div>
  <p style="margin-top:24px"><a href="insights.html">All insights &rarr;</a></p>
</div></section>
{cta()}""")


def build():
    for fname, (title, desc, body) in PAGES.items():
        with open(os.path.join(ROOT, fname), "w", encoding="utf-8") as f:
            f.write(page(fname, title, desc, body))
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    exec(open(os.path.join(ROOT, "pages_inner.py"), encoding="utf-8").read())
    build()
