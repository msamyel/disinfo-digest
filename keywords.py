# Dictionary pro vyhledávání slov v textu a jejich převod na kategorie.
KEYWORDS_SEARCH_TABLE = {
    # dezinformace
    'dezinform': 'dezinformace',
    'misinform': 'dezinformace',
    'malinforma': 'dezinformace',
    'hoax': 'dezinformace',
    'konspir': 'dezinformace',
    'fake news': 'dezinformace',
    'postfakt': 'dezinformace',
    'pseudověd': 'dezinformace',
    'pseudoved': 'dezinformace',
    'chemtrails': 'dezinformace',
    'mystifika': 'dezinformace',
    'manipulace': 'dezinformace',
    'narativ': 'dezinformace',

    # propaganda
    'propagand': 'propaganda',
    'spamouflage': 'propaganda',
    'dragonbridge': 'propaganda',
    'storm 1376': 'propaganda',
    'false flag': 'propaganda',
    'falešnou vlajk': 'propaganda',
    'falešná vlajk': 'propaganda',

    # sociální sítě - možná bych vypustil
    # 'twitter': 'sociální sítě',
    # 'Meta': 'sociální sítě',
    # 'musk': 'Elon Musk',
    # 'tik tok': 'sociální sítě',
    # 'sociální sítě': 'sociální sítě',
    'algoritm': 'sociální sítě',
    'nenávistný komentář': 'nenávistné komentáře',
    'nenávistných komentář': 'nenávistné komentáře',
    'nenávistnými komentář': 'nenávistné komentáře',
    'nenávistné komentář': 'nenávistné komentáře',

    # Jména dezinformátorů - https://www.seznamzpravy.cz/clanek/domaci-kauzy-kdo-v-cesku-vydelava-na-strachu-lidi-232386
    'Tomáš Čermák': 'dezinformátoři',
    'Lubomír Volný': 'dezinformátoři',
    'Patrik Tušl': 'dezinformátoři',
    'Jan Macháček': 'dezinformátoři',
    'Petr Bílý': 'dezinformátoři',
    'Jakub Netík': 'dezinformátoři',
    'Pavel Zítko': 'dezinformátoři',
    'Ladislav Vrabel': 'dezinformátoři',
    'Vladimír Kapal': 'dezinformátoři',
    'Jana Peterková': 'dezinformátoři',
    'Jindřich Rajchl': 'dezinformátoři',
    'Žarko Jovanovič': 'dezinformátoři',
    'Ivan Smetana': 'dezinformátoři',
    'Petr Hájek': 'dezinformátoři',
    'Marek Pešl': 'dezinformátoři',
    'Ondřej Geršl': 'dezinformátoři',
    'Ondřej Thor': 'dezinformátoři',
    'Raptor-TV': 'dezinformátoři',
    'Aeronet': 'dezinformátoři',
    'Aliance pro rodinu': 'dezinformátoři',

    # AI
    'umělá intelig': 'umělá inteligence',
    'umělé intelig': 'umělá inteligence',
    'umělou intelig': 'umělá inteligence',
    'deepfake': 'umělá inteligence',
    'AI': 'umělá inteligence',

    # Kyberbezpečnost
    'phishing': 'kyberbezpečnost',
    'kyber': 'kyberbezpečnost',
    'botnet': 'kyberbezpečnost',
    'ddos': 'kyberbezpečnost',
    'scam': 'kyberbezpečnost',
    'smishing': 'kyberbezpečnost',
    'vishing': 'kyberbezpečnost',
    'hack': 'kyberbezpečnost',
    'phreak': 'kyberbezpečnost',
    'ransomware': 'kyberbezpečnost',
    'sociální inženýr': 'kyberbezpečnost',
    'únik dat': 'kyberbezpečnost',
    'zero-day': 'kyberbezpečnost',
    'zero day': 'kyberbezpečnost',
    'krádež identity': 'kyberbezpečnost',
    'malware': 'kyberbezpečnost',
    'hijacking': 'kyberbezpečnost',
    
    # Podvodné praktiky
    'podvod': 'podvod',
    'spam': 'podvod',
    'sociální inženýrství': 'podvod',

    # Kyberšikana
    'kyberšikan': 'kyberšikana',
    'doxx': 'kyberšikana',
    'doxing': 'kyberšikana',
    'brigading': 'kyberšikana',
    'stalkgin': 'kyberšikana',
    'sextortion': 'kyberšikana',
    'troll': 'kyberšikana',
    'gaslighting': 'kyberšikana',

    # Mediální gramotnost
    'mediální gramotnost': 'mediální gramotnost',
    'clickbait': 'mediální gramotnost',
    'konfirmačn': 'mediální gramotnost',
    'kritické myšlení': 'mediální gramotnost',
    'informační gramotnost': 'mediální gramotnost',

    # Řetězové zprávy
    'řetězový email': 'řetězáky',
    'řetězové email': 'řetězáky',
    'řetězák': 'řetězáky',

    # Svoboda slova
    'svoboda slova': 'svoboda slova',
    'cenzúr': 'svoboda slova',
    'cenzur': 'svoboda slova',
    'newspeak': 'svoboda slova',

    # Fact-checking
    'fact-checking': 'fact-checking',
    'overovanie faktov': 'fact-checking',
    'ověřování faktů': 'fact-checking',
    'prebunking': 'fact-checking',
    'debunking': 'fact-checking',

    # Krajní pravice/levice
    'krajní pravic': 'krajní pravice',
    'krajně pravic': 'krajní pravice',
    'extrémní pravic': 'krajní pravice',
    'extrémně pravic': 'krajní pravice',
    'krajně levic': 'krajní levice',
    'krajní levic': 'krajní levice',
    'extrémní levic': 'krajní levice',
    'extrémně levic': 'krajní levice',

    # Radikalizace
    'redpilling': 'radikalizace',
    'radikali': 'radikalizace',
    'weaponiz': 'radikalizace',
    'MAGA': 'radikalizace', #new
    'qanon': 'radikalizace',
    'infowars': 'radikalizace',
    'trumpismus': 'radikalizace', #new
    'extremis': 'radikalizace', #new
    'antisemi': 'radikalizace', #new
    'radikál': 'radikalizace', #new

    # Muži - seximus?
    'manosféra': 'sexismus',
    'mansplaining': 'sexismus',
    'machis': 'sexismus',
    'misogyn': 'sexismus',
    'mizogyn': 'sexismus',
    'šovin': 'sexismus',

    # Terorismus
    'teroris': 'terorismus', #new

    # Hybridní hrozby
    'hybridní hrozb': 'hybridní hrozby',
    'hybridní kampaň': 'hybridní hrozby',
    'informační válk': 'hybridní hrozby',
    'informační operac': 'hybridní hrozby',

    # strategická komunikace
    'strategická komunik': 'strategická komunikace',
    'stratcom': 'strategická komunikace',

    # Out - nikdo nehleda
    # 'gerrymandering': 'gerrymandering',
    # 'overton': 'overtonovo okno',
    # 'himpatie': 'himpathy',
}

# Dictionary pro převod kategorií na verzi bez diakritiky a obráceně.
TAGS_ACCENT_TABLE = {
    "dezinformace": "dezinformace",
    "propaganda": "propaganda",
    "sociální sítě": "socialni-site",
    "nenávistné komentáře": "nenavistne-komentare",
    "dezinformátoři": "dezinformatori",
    "umělá inteligence": "umela-inteligence",
    "kyberbezpečnost": "kyberbezpecnost",
    "podvod": "podvod",
    "kyberšikana": "kybersikana",
    "mediální gramotnost": "medialni-gramotnost",
    "řetězáky": "retezaky",
    "svoboda slova": "svoboda-slova",
    "fact-checking": "fact-checking",
    "krajní pravice": "krajni-pravice",
    "krajní levice": "krajni-levice",
    "radikalizace": "radikalizace",
    "sexismus": "sexismus",
    "terorismus": "terorismus",
    "hybridní hrozby": "hybridni-hrozby",
    "strategická komunikace": "strategicka-komunikace",
}


def get_accented_tag(unaccented_tag):
    for tag in TAGS_ACCENT_TABLE:
        if TAGS_ACCENT_TABLE[tag] == unaccented_tag:
            return tag
    return None