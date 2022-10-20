from urllib.parse import urlsplit

IGNORE = ['THE', 'OF', 'IN', 'FROM', 'BY', 'WITH', 'AND', 'OR', 'FOR', 'TO', 'AT', 'A']


def generate_bc(url, separator):
    def acronym(crumb):
        crumb = crumb.upper()
        if crumb == '':
            return 'HOME'
        elif len(crumb) <= 30 or crumb.count('-') == 0:
            return crumb.replace('-', ' ').split('.')[0]

        return ''.join([word[0].split('.')[0] for word in crumb.split('-') if word not in IGNORE])

    def html_code(link_level, crumb, site_path):
        if link_level == len(site_path) - 1:
            return f'<span class="active">{acronym(crumb)}</span>'
        return f'<a href="{"/".join(site[:(link_level + 1)] + [""])}">{acronym(crumb)}</a>'

    # print(f"('{url}', '{separator}')")
    site = [''] + urlsplit(url).path.split('/')[1:]
    if 'index' in site[-1].lower() or (len(site) > 1 and site[-1]) == '':
        site.pop()

    return separator.join([html_code(i, crumb, site) for i, crumb in enumerate(site)])
