from urllib.parse import urlsplit

IGNORE = ['THE', 'OF', 'IN', 'FROM', 'BY', 'WITH', 'AND', 'OR', 'FOR', 'TO', 'AT', 'A']


def generate_bc(url, separator):
    def html_code(link_level, crumb, site_path):
        acro = crumb.upper()
        if acro == '':
            acro = 'HOME'
        elif len(acro) <= 30 or acro.count('-') == 0:
            acro = acro.replace('-', ' ').split('.')[0]
        else:
            acro = ''.join([word[0].split('.')[0] for word in acro.split('-') if word not in IGNORE])

        if link_level == len(site_path) - 1:
            return f'<span class="active">{acro}</span>'
        return f'<a href="{"/".join(site[:(link_level + 1)] + [""])}">{acro}</a>'

    site = [''] + urlsplit(url).path.split('/')[1:]
    if 'index' in site[-1].lower() or (len(site) > 1 and site[-1]) == '':
        site.pop()

    return separator.join([html_code(i, crumb, site) for i, crumb in enumerate(site)])
