# Inner pages. Executed inside build.py's namespace (see build.py __main__).

def head(title, lead, crumb=None):
    c = f'<p class="crumb"><a href="index.html">Home</a> / {crumb}</p>' if crumb else ""
    return f'<section class="page-head"><div class="wrap">{c}<h1 class="rise">{title}</h1><p class="lead rise rise-2">{lead}</p></div></section>'


def service_page(fname, title, lead, what, who, included, steps, note=""):
    inc = "".join(f"<li>{i}</li>" for i in included)
    st = "".join(f"<li><span>{s}</span></li>" for s in steps)
    others = "".join(f'<li><a href="{h}">{escape(t)}</a></li>' for h, t, *_ in SERVICES if h != fname)
    note_html = f'<p class="note">{note}</p>' if note else ""
    body = f"""{head(escape(title), lead, '<a href="services.html">Services</a> / ' + escape(title))}
<section class="section"><div class="wrap two-col">
  <div class="prose"><h2>What it is</h2>{what}{note_html}</div>
  <div class="prose"><h2>Who it is for</h2>{who}</div>
</div></section>
<section class="section"><div class="wrap">
  <div class="section-head"><h2>What is included</h2></div>
  <ul class="included">{inc}</ul>
</div></section>
<section class="section"><div class="wrap two-col">
  <div class="prose"><h2>How to get started</h2><ol class="steps">{st}</ol></div>
  <div class="prose"><h2>Other services</h2><ul>{others}</ul></div>
</div></section>
{cta("Discuss " + title.lower().replace("&", "and"), f"Call or WhatsApp {CONTACT} on {PHONE} to agree the scope and fee before any work begins.")}"""
    PAGES[fname] = (title, lead, body)


STEPS = [f"Call or WhatsApp {CONTACT} on {PHONE} with a short description of your entity and what you need.",
         "Share last year's documents so we can assess the work involved.",
         "We confirm the scope, timeline and fee in an engagement letter.",
         "Work begins, with one point of contact throughout."]

# ---------------- About ----------------
PAGES["about.html"] = ("About & Team",
  "A Karachi practice of Chartered Management Accountants, established in January 2026, led by Faraz Abdul Razzak, FCMA.",
  f"""{head("About the firm", "Faraz Abdul Razzak &amp; Co. is a practice of Chartered Management Accountants in Karachi, established in January 2026 to serve private companies, non-profits and individuals.", "About")}
<section class="section"><div class="wrap two-col">
  <div class="prose">
    <span class="label">Our practice</span>
    <h2>Finance, governance and compliance under one roof</h2>
    <p>The firm brings together long experience in audit, accounting, tax and corporate compliance. We work with owner-managed companies, trusts and NGOs, sole proprietors, individuals and associations of persons.</p>
    <p>Our work is grounded in the Companies Act 2017, the Income Tax Ordinance 2001, the Sales Tax Act 1990 and the regulations of the SECP, FBR and Sindh Revenue Board.</p>
    <p class="note">ICMA Pakistan practice registration number: to be added.</p>
  </div>
  <div class="prose">
    <span class="label">How we work</span>
    <ul class="points">
      <li><strong>Integrity</strong><span class="muted">We report what the records show, clearly and without bias.</span></li>
      <li><strong>Confidentiality</strong><span class="muted">Client information stays with us unless you consent in writing.</span></li>
      <li><strong>Timeliness</strong><span class="muted">We plan around your statutory deadlines, not after them.</span></li>
    </ul>
  </div>
</div></section>
<section class="section alt"><div class="wrap">
  <div class="section-head"><span class="label">Our team</span><h2>The people you will work with</h2></div>

  <article class="person" id="faraz">
    <div class="avatar" aria-hidden="true">FR</div>
    <div class="info">
      <div><h3>Mr. Faraz Abdul Razzak, FCMA</h3><p class="role">Partner &amp; CEO</p></div>
      <p>Faraz Abdul Razzak is the Partner and Chief Executive of Faraz Abdul Razzak &amp; Co., Chartered Management Accountants, Karachi. He is a Fellow member of the Institute of Cost and Management Accountants of Pakistan (ICMAP) and brings 22 years of hands-on experience across financial management, corporate secretarial practice, regulatory compliance and internal audit.</p>
      <p>His career has been built largely in Pakistan's insurance industry, a sector with demanding regulatory and reporting standards. At Alpha Insurance he served as Chief Financial Officer, Company Secretary and Acting Head of IT, and earlier as Chief Internal Auditor. Since September 2023 he has served as Company Secretary &amp; Compliance Officer at an insurance company in Karachi.</p>
      <p>This mix of finance, governance, audit and technology gives Faraz an end-to-end view of how a business is run and controlled. He works closely with business owners and boards to prepare reliable financial statements, strengthen internal controls, meet SECP and tax obligations, and build systems that support growth.</p>
      <p>At the firm, Faraz personally oversees every engagement, so clients get partner-level attention, practical advice and work delivered to professional standards.</p>
      <h4>Qualifications &amp; memberships</h4>
      <ul class="chips"><li>FCMA, Fellow Member, ICMAP</li></ul>
      <h4>Career highlights</h4>
      <div class="tbl-wrap"><table class="career"><tbody>
        <tr><td>Jan 2026 &ndash; present</td><td>Partner &amp; CEO, {escape(FIRM)}</td></tr>
        <tr><td>Sep 2023 &ndash; present</td><td>Company Secretary &amp; Compliance Officer, insurance company, Karachi</td></tr>
        <tr><td>Earlier</td><td>Chief Financial Officer, Company Secretary &amp; Acting Head of IT, Alpha Insurance</td></tr>
        <tr><td>Earlier</td><td>Chief Internal Auditor, Alpha Insurance</td></tr>
      </tbody></table></div>
      <h4>Areas of expertise</h4>
      <ul class="chips"><li>Financial statements and annual accounts</li><li>Corporate secretarial and SECP compliance</li><li>Regulatory compliance and corporate governance</li><li>Internal audit and internal controls</li><li>Financial management and CFO-level advisory</li><li>Taxation support and statutory filings</li></ul>
      <p><strong>Call:</strong> <a href="tel:{FARAZ_INTL}">{FARAZ_PHONE}</a></p>
    </div>
  </article>

  <article class="person" id="aysha">
    <div class="avatar" aria-hidden="true">AM</div>
    <div class="info">
      <div><h3>{CONTACT}, MBA</h3><p class="role">Associate &middot; Client contact</p></div>
      <p>Aysha is an Associate at Faraz Abdul Razzak &amp; Co. and has been with the firm since its inception in January 2026. She holds an MBA and has worked in professional practice since 1998.</p>
      <p>From 1998 to 2025 she worked at Mehmood Zubari &amp; Co., Chartered Accountants, where she gained broad experience in maintaining accounts, preparing financial statements and handling tax matters for a wide range of clients.</p>
      <p>At the firm, Aysha works on clients' accounting records, income tax returns and sales tax filings. Her long practical experience helps clients stay compliant and meet their deadlines. She is also the firm's first point of contact for new enquiries.</p>
      <h4>Qualifications</h4>
      <ul class="chips"><li>MBA</li></ul>
      <h4>Experience</h4>
      <div class="tbl-wrap"><table class="career"><tbody>
        <tr><td>Jan 2026 &ndash; present</td><td>Associate, {escape(FIRM)}</td></tr>
        <tr><td>1998 &ndash; 2025</td><td>Mehmood Zubari &amp; Co., Chartered Accountants</td></tr>
      </tbody></table></div>
      <h4>Areas of expertise</h4>
      <ul class="chips"><li>Accounting and bookkeeping</li><li>Financial statements</li><li>Income tax returns and compliance</li><li>Sales tax registration, returns and compliance</li></ul>
      <p><strong>Call or WhatsApp:</strong> <a href="tel:{PHONE_INTL}">{PHONE}</a></p>
    </div>
  </article>
</div></section>
{cta()}""")


# ---------------- Services overview ----------------
PAGES["services.html"] = ("Services",
  "Audit, internal audit, SECP compliance, tax and accounting services in Karachi.",
  f"""{head("Services", "Five areas of practice for companies, non-profits and individuals. Each engagement has an agreed scope and fee before work begins.", "Services")}
<section class="section"><div class="wrap">{schedule()}</div></section>
{cta()}""")

service_page("audit-assurance.html", "Audit & Assurance",
  "Independent audit of financial statements for eligible private companies, trusts, NGOs, individuals, sole proprietors and AOPs.",
  "<p>An audit gives owners, donors, banks and regulators independent assurance that the financial statements are fairly presented. We plan each audit around the risks in your business and report our findings clearly to management.</p>",
  "<p>We audit:</p><ul><li>Private limited companies whose paid-up capital is within the limit permitted to Cost and Management Accountants under section 247 of the Companies Act, 2017</li><li>Trusts, NGOs and not-for-profit organisations</li><li>Individuals, sole proprietors and associations of persons (AOPs)</li></ul>",
  ["Audit planning and risk assessment", "Testing of income, expenses, assets and liabilities",
   "Audit report on the financial statements", "Management letter on control weaknesses found",
   "Audits required by donors or funding agencies", "Guidance on the documents and schedules auditors need"],
  STEPS, "Not sure whether your company is eligible? Tell us its paid-up capital and we will confirm.")

service_page("internal-audit.html", "Internal Audit, Risk & Advisory",
  "Outsourced internal audit, reviews of internal controls and risks, and practical advice for management.",
  "<p>Internal audit checks that your controls work as intended: that payments are authorised, stock is protected, revenue is complete and records are reliable. We report what we find in plain terms, with recommendations your team can act on.</p>",
  "<p>Owner-managed businesses that have outgrown informal controls, companies preparing for an external audit or a bank review, and boards that want independent assurance without a full-time internal audit department.</p>",
  ["Outsourced or co-sourced internal audit", "Review of internal controls over key processes",
   "Risk assessment and risk register", "Standard operating procedures and policies",
   "Fraud risk and segregation of duties review", "Management reporting and business advice"],
  STEPS)

service_page("corporate-secp.html", "Corporate & SECP Compliance",
  "Company incorporation, secretarial services and statutory filings under the Companies Act, 2017.",
  "<p>Every company registered with the Securities and Exchange Commission of Pakistan (SECP) must keep statutory records and file returns on time. Late or missing filings lead to penalties. We handle the paperwork so you can focus on the business.</p>",
  "<p>New businesses incorporating a private limited company, and existing companies that want their statutory records, meetings and SECP filings kept up to date.</p>",
  ["Incorporation of private limited and single-member companies", "Annual return and other statutory filings with the SECP",
   "Changes of directors, registered office or share capital", "Board and general meeting minutes and resolutions",
   "Maintenance of statutory registers", "Compliance calendar with filing reminders"],
  STEPS)

service_page("tax-advisory.html", "Tax Advisory & Filing",
  "Income tax and sales tax returns, tax advice, and representation in matters before the FBR and Sindh Revenue Board.",
  "<p>We prepare and file returns, keep your withholding and sales tax obligations in order, and respond to notices from the tax authorities. In Pakistan the normal tax year runs from 1 July to 30 June, so we plan the year's filings around that calendar.</p>",
  "<p>Salaried individuals with other income, business owners, AOPs, companies, and businesses registered for federal sales tax with the FBR or for sales tax on services with the Sindh Revenue Board.</p>",
  ["Income tax returns and wealth statements", "Withholding tax statements",
   "Federal sales tax returns (FBR)", "Sindh sales tax on services returns (SRB)",
   "Replies to notices and assessment matters", "Tax planning within the law"],
  STEPS)

service_page("accounting.html", "Accounting & Financial Statements",
  "Bookkeeping, financial statements and cost and management accounting that give owners reliable numbers.",
  "<p>Accurate books are the base for tax returns, audits, bank finance and good decisions. We keep your records up to date and prepare financial statements under the reporting framework that applies to your entity.</p>",
  "<p>Small and medium businesses without a full accounts team, non-profits that report to donors, and owners who want regular management accounts to run the business.</p>",
  ["Monthly bookkeeping and bank reconciliations", "Annual financial statements",
   "Management accounts and MIS reports", "Product and service costing",
   "Budgets and cash flow forecasts", "Setting up or improving accounting systems"],
  STEPS)

# ---------------- Insights ----------------
cats = sorted({a["cat"] for a in ARTICLES} | {"Sales Tax", "Budget Updates"})
filt = '<button type="button" aria-pressed="true" data-f="all">All</button>' + "".join(
    f'<button type="button" aria-pressed="false" data-f="{escape(c)}">{escape(c)}</button>' for c in
    ["Income Tax", "Sales Tax", "Corporate & SECP", "Audit & Accounting", "Budget Updates"])
PAGES["insights.html"] = ("Insights",
  "Updates on income tax, sales tax, SECP compliance, audit and the federal and Sindh budgets.",
  f"""{head("Insights", "Short, sourced updates on tax, SECP compliance and audit. Each article shows its publish date and the law or notification it relies on.", "Insights")}
<section class="section"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter by category">{filt}</div>
  <div class="articles" id="list">{article_cards(ARTICLES)}</div>
  <p class="muted" id="empty" hidden>No articles in this category yet.</p>
</div></section>
<script>
(function () {{
  var btns = document.querySelectorAll('.filters button'), cards = document.querySelectorAll('#list .article-card'), empty = document.getElementById('empty');
  btns.forEach(function (b) {{ b.addEventListener('click', function () {{
    var f = b.getAttribute('data-f'), shown = 0;
    btns.forEach(function (x) {{ x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }});
    cards.forEach(function (c) {{ var ok = f === 'all' || c.getAttribute('data-cat') === f; c.hidden = !ok; if (ok) shown++; }});
    empty.hidden = shown > 0;
  }}); }});
}})();
</script>
{cta()}""")

PAGES["article-sample.html"] = ("Sample article",
  "Sample article layout for the Insights section.",
  f"""{head("Annual filing reminders for private companies", '<span class="tag">Corporate &amp; SECP</span> &nbsp; By Faraz Abdul Razzak, FCMA &middot; Publish date to be added', '<a href="insights.html">Insights</a> / Article')}
<section class="section"><div class="wrap">
  <div class="article-body">
    <p class="note">This is a sample showing how articles will look. The final text will be written from the official source and approved by Faraz before publishing.</p>
    <p class="lead">Summary: a two-line summary of the update appears here, telling the reader who is affected and what they need to do.</p>
    <h2>What has changed</h2>
    <p>The body of the article explains the change in plain language, in 300 to 800 words, with any dates and amounts checked against the official source.</p>
    <h2>Who is affected</h2>
    <p>This section names the types of taxpayer or company the update applies to.</p>
    <h2>What you should do</h2>
    <p>Practical steps and deadlines for the reader.</p>
    <p class="source"><strong>Source:</strong> the Act and section, SRO, circular or notification, with its date.<br>
    This update is for general information only and is not professional advice. Please contact us before acting on it.</p>
    <p>Share: <a href="https://wa.me/?text=Annual%20filing%20reminders%20for%20private%20companies">WhatsApp</a> &middot; <a href="https://www.linkedin.com/">LinkedIn</a></p>
  </div>
</div></section>
{cta()}""")

# ---------------- Contact ----------------
PAGES["contact.html"] = ("Contact",
  "Call or WhatsApp Ms. Aysha Mehmood, or visit Faraz Abdul Razzak & Co. on M.A. Jinnah Road, Karachi. Open Monday to Saturday.",
  f"""{head("Contact us", f"Call or WhatsApp {CONTACT} on {PHONE}. We are open Monday to Saturday.", "Contact")}
<section class="section"><div class="wrap contact-grid">
  <ul class="contact-list">
    <li><span class="k">{CONTACT}</span><span>Associate<br>Call: <a href="tel:{PHONE_INTL}">{PHONE}</a></span></li>
    <li><span class="k">Mr. Faraz Abdul Razzak</span><span>Partner &amp; CEO<br>Call: <a href="tel:{FARAZ_INTL}">{FARAZ_PHONE}</a></span></li>
    <li><span class="k">WhatsApp</span><span><a href="{WA}">Message {PHONE}</a></span></li>
    <li><span class="k">Email</span><span><a href="mailto:{EMAIL}">{EMAIL}</a></span></li>
    <li><span class="k">Office days</span><span>Monday to Saturday</span></li>
  </ul>
  <div class="map-card">
    <h2>Visit the office</h2>
    <p>{escape(ADDRESS)}</p>
    <p class="muted">Opposite Capri Cinema, on M.A. Jinnah Road.</p>
    <p><a class="btn btn-blue" href="{MAPS}">Get directions on Google Maps</a></p>
    <p class="muted" style="font-size:.9rem">An embedded map will be added on the live site.</p>
  </div>
</div></section>""")


PAGES["privacy.html"] = ("Privacy Notice",
  "How Faraz Abdul Razzak & Co. handles information from website visitors.",
  f"""{head("Privacy Notice", "How we handle information when you visit this website or contact us.", "Privacy Notice")}
<section class="section"><div class="wrap"><div class="prose">
  <h2>What we collect</h2>
  <p>This website has no forms and no logins. We use anonymous visitor statistics, such as pages viewed and the type of device, to understand how the site is used. These statistics do not identify you.</p>
  <h2>When you contact us</h2>
  <p>If you call, email or message us on WhatsApp, we use your name, number and message only to reply and, if you become a client, to provide our services. We do not sell or share it.</p>
  <h2>Client confidentiality</h2>
  <p>Information about clients is kept confidential in line with our professional obligations, and no client is named on this website without written consent.</p>
  <h2>Questions</h2>
  <p>Contact us at <a href="mailto:{EMAIL}">{EMAIL}</a> or call {CONTACT} on {PHONE}.</p>
  <p class="muted">Last updated: November 2026</p>
</div></div></section>""")

PAGES["404.html"] = ("Page not found",
  "The page you were looking for could not be found.",
  f"""{head("Page not found", "The address may be mistyped or the page may have moved. Use the menu above, or one of these links.")}
<section class="section"><div class="wrap"><div class="prose"><ul>
  <li><a href="index.html">Home</a></li><li><a href="services.html">Our services</a></li>
  <li><a href="contact.html">Contact us</a>: {CONTACT}, {PHONE}</li></ul></div></div></section>""")
