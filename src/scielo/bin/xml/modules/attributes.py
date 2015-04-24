# coding=utf-8
DOCTOPIC = {
                'research-article': 'oa',
                'editorial': 'ed',
                'abstract': 'ab',
                'announcement': 'an',
                'article-commentary': 'co',
                'case-report': 'cr',
                'letter': 'le',
                'review-article': 'ra',
                'rapid-communication': 'sc',
                'addendum': 'zz',
                'book-review': 'rc',
                'books-received': 'zz',
                'brief-report': 'rn',
                'calendar': 'zz',
                'clinical-trial': 'ct',
                'collection': 'zz',
                'correction': 'er',
                'discussion': 'em',
                'dissertation': 'em',
                'editorial-material': 'em',
                'in-brief': 'pr',
                'introduction': 'em',
                'meeting-report': 'zz',
                'news': 'zz',
                'obituary': 'zz',
                'oration': 'zz',
                'partial-retraction': 're',
                'product-review': 'rc',
                'reply': 'zz',
                'reprint': 'zz',
                'retraction': 're',
                'translation': 'zz',
                'other': 'zz',
}

DOCTOPIC_IN_USE = [
    'abstract', 
    'announcement', 
    'article-commentary', 
    'book-review', 
    'brief-report', 
    'case-report', 
    'clinical-trial', 
    'correction', 
    'editorial', 
    'editorial-material', 
    'in-brief', 
    'letter', 
    'other', 
    'rapid-communication', 
    'research-article', 
    'retraction', 
    'review-article', 
    'technical-report', 
    ]


TOC_SECTIONS = { u'carta': u'letter', u'revisão': u'review', u'origin': u'research', u'informe': u'report', u'revisión': u'review', u'relato': u'report', u'artigo': u'article', u'artículo': u'article', u'errata': u'correction', u'erratum': u'correction'}

ROLE = {
    'author': 'ND',
    'editor': 'ED',
    'assignee': 'assignee',
    'compiler': 'compiler',
    'director': 'director',
    'guest-editor': 'guest-editor',
    'inventor': 'inventor',
    'transed': 'transed',
    'translator': 'TR',    
}


PUBLICATION_TYPE = []
PUBLICATION_TYPE.append('journal')
PUBLICATION_TYPE.append('book')
PUBLICATION_TYPE.append('thesis')
PUBLICATION_TYPE.append('patent')
PUBLICATION_TYPE.append('report')
PUBLICATION_TYPE.append('software')
PUBLICATION_TYPE.append('webpage')
PUBLICATION_TYPE.append('database')
PUBLICATION_TYPE.append('confproc')
PUBLICATION_TYPE.append('legal-doc')
PUBLICATION_TYPE.append('other')


REFERENCE_REQUIRED_SUBELEMENTS = {}
REFERENCE_REQUIRED_SUBELEMENTS['journal'] = ['article-title']
REFERENCE_REQUIRED_SUBELEMENTS['confproc'] = ['conf-name']
REFERENCE_REQUIRED_SUBELEMENTS['webpage'] = ['ext-link', 'date-in-citation[@content-type="access-date"]']


REFERENCE_NOT_ALLOWED_SUBELEMENTS = {}
REFERENCE_NOT_ALLOWED_SUBELEMENTS['journal'] = ['chapter-title']
REFERENCE_NOT_ALLOWED_SUBELEMENTS['book'] = ['article-title']


def is_required(publication_type, label):
    return label in REFERENCE_REQUIRED_SUBELEMENTS.get(publication_type, [])


def is_allowed_element(publication_type, label):
    if is_required(publication_type, label):
        r = True
    else:
        r = not label in REFERENCE_NOT_ALLOWED_SUBELEMENTS.get(publication_type, [])
    return r


def validate_element(publication_type, label, value):
    problem = ''
    if value is None or value == '':
        if is_required(publication_type, label):
            problem = label + ' is required for @publication-type=' + publication_type
    else:
        if not is_allowed_element(publication_type, label):
            problem = label + ' is not allowed for @publication-type=' + publication_type
    return problem


def doctopic_label(code):
    label = [k for k, v in DOCTOPIC.items() if v == code]
    if len(label) == 0:
        label = None
    else:
        label = label[0]
    return label


def normalize_section_title(article_toc_section):
    if article_toc_section is None:
        article_toc_section = ''
    section = article_toc_section.lower().replace(' de ', ' ').replace('-', ' ')
    section = ' '.join([item for item in sorted(section.split(' '))])
    if section is not None:
        for term, transl in TOC_SECTIONS.items():
            section = section.replace(term, transl)
    return section
 
