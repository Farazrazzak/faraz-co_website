"""Insights articles. The three launch articles are placeholders until Faraz supplies
sourced, approved content (Spec 02, articles workflow)."""
from html import escape

ARTICLES = [
    {"slug": "article-sample.html", "cat": "Corporate & SECP",
     "title": "Annual filing reminders for private companies",
     "summary": "Sample article showing the layout. The final text will list the SECP returns a private company files each year and their due dates."},
    {"slug": "article-sample.html", "cat": "Income Tax",
     "title": "Preparing for your income tax return",
     "summary": "Sample article showing the layout. The final text will set out the records to gather before the return deadline."},
    {"slug": "article-sample.html", "cat": "Audit & Accounting",
     "title": "What trusts and NGOs need for their annual audit",
     "summary": "Sample article showing the layout. The final text will explain the documents and schedules auditors ask for."},
]


def article_cards(items):
    out = []
    for a in items:
        out.append(
            f'<article class="article-card" data-cat="{escape(a["cat"])}">'
            f'<span class="tag">{escape(a["cat"])}</span>'
            f'<h3><a href="{a["slug"]}">{escape(a["title"])}</a></h3>'
            f'<p class="muted">{escape(a["summary"])}</p>'
            f'<span class="meta">Sample &middot; date to be added on publishing</span></article>')
    return "".join(out)
