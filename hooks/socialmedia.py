from textwrap import dedent
import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_share = "https://www.facebook.com/sharer/sharer.php"

def on_page_markdown(markdown,**kwargs):
    page= kwargs['page']
    config= kwargs['config']
    if page.meta.get('template') != 'blog-post.html':
        return markdown
    
    page_url = config.site_url + page.url
    page_title = urllib.parse.quote(page.title +'\n')

    return markdown + dedent(f"""
         <div style="display: flex; justify-content: center; gap: 20px; align-items: center; margin: 2em 0;">
        <a href="{x_intent}?text={page_title}&url={page_url}" target="_blank" rel="noopener noreferrer" title="Share on X"
           style="display:inline-flex; align-items:center; gap:10px; padding:8px 18px; border:2px solid #1da1f2; color:#1da1f2; border-radius:4px; text-decoration:none; font-weight:500; background:transparent; transition:background 0.2s, color 0.2s;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" style="display:inline-block;vertical-align:middle;">
                <path d="M17.53 3.25h3.92l-8.56 9.77 10.09 11.73h-7.94l-6.26-7.28-7.16 7.28H1.09l9.13-10.41L.25 3.25h8.13l5.7 6.63 6.45-6.63zm-1.36 18.09h2.18L6.62 5.03H4.3l11.87 16.31z" fill="#1da1f2"/>
            </svg>
            <span style="color:#1da1f2;">Share on X</span>
        </a>
        <a href="{fb_share}?u={page_url}" target="_blank" rel="noopener noreferrer" title="Share on Facebook"
           style="display:inline-flex; align-items:center; gap:10px; padding:8px 18px; border:2px solid #1877f3; color:#1877f3; border-radius:4px; text-decoration:none; font-weight:500; background:transparent; transition:background 0.2s, color 0.2s;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" style="display:inline-block;vertical-align:middle;">
                <path d="M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073c0 6.019 4.388 10.995 10.125 11.854v-8.385H7.078v-3.47h3.047V9.413c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953h-1.513c-1.491 0-1.953.926-1.953 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.068 24 18.092 24 12.073z" fill="#1877f3"/>
            </svg>
            <span style="color:#1877f3;">Share on Facebook</span>
        </a>
    </div>
        """)