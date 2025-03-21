# Dictionary pro vyhledávání slov v textu a jejich převod na kategorie.
KEYWORDS_SEARCH_TABLE = {
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
    'NÚKIB': 'kyberbezpečnost',

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
    'MAGA': 'radikalizace',  # new
    'qanon': 'radikalizace',
    'infowars': 'radikalizace',
    'trumpismus': 'radikalizace',  # new
    'extremis': 'radikalizace',  # new
    'antisemi': 'radikalizace',  # new
    'radikál': 'radikalizace',  # new

    # Muži - seximus?
    'manosféra': 'sexismus',
    'mansplaining': 'sexismus',
    'machis': 'sexismus',
    'misogyn': 'sexismus',
    'mizogyn': 'sexismus',
    'šovin': 'sexismus',

    # Terorismus
    'teroris': 'terorismus',  # new

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

NEGATIVE_KEYWORDS = ['podvodní ', 'podvodních ', 'podvodního ']

# Dictionary pro převod kategorií na verzi bez diakritiky a obráceně.
TAGS_ACCENT_TABLE = {
    "dezinformace": "dezinformace",
    "dezinformátoři": "dezinformatori",
    "fact-checking": "fact-checking",
    "hybridní hrozby": "hybridni-hrozby",
    "krajní levice": "krajni-levice",
    "krajní pravice": "krajni-pravice",
    "kyberbezpečnost": "kyberbezpecnost",
    "kyberšikana": "kybersikana",
    "mediální gramotnost": "medialni-gramotnost",
    "nenávistné komentáře": "nenavistne-komentare",
    "podvod": "podvod",
    "propaganda": "propaganda",
    "radikalizace": "radikalizace",
    "sexismus": "sexismus",
    "sociální sítě": "socialni-site",
    "strategická komunikace": "strategicka-komunikace",
    "svoboda slova": "svoboda-slova",
    "terorismus": "terorismus",
    "umělá inteligence": "umela-inteligence",
    "řetězáky": "retezaky",
}

TAGS_COLORS_TABLE = {
    # Disinformation & Propaganda (Green, Yellow)
    "dezinformace": "#A3E635",  # Bright Green
    "dezinformátoři": "#FACC15",  # Warm Yellow
    "propaganda": "#FFDD57",  # Soft Gold
    "řetězáky": "#FFB703",  # Deep Yellow-Orange

    # Fact-checking & Strategic Communication (Teal, Cyan)
    "fact-checking": "#00C49A",  # Teal Green
    "strategická komunikace": "#5CD1E5",  # Light Cyan-Blue
    "mediální gramotnost": "#00B4D8",  # Bright Sky Blue

    # Cybersecurity & Online Threats (Blue, Cyan)
    "kyberbezpečnost": "#118AB2",  # Deep Cyan
    "kyberšikana": "#06D6A0",  # Teal Green
    "sociální sítě": "#4FD1C5",  # Soft Turquoise
    "umělá inteligence": "#38BDF8",  # Electric Blue

    # Radicalization, Extremism & Hate Speech (Red, Pink)
    "radikalizace": "#D90429",  # Bold Red
    "krajní levice": "#E63946",  # Coral Red
    "krajní pravice": "#EF476F",  # Pinkish Red
    "nenávistné komentáře": "#F87171",  # Light Red

    # Fraud & Misinformation (Muted Browns, Orange)
    "podvod": "#EE9B00",  # Deep Orange
    "hybridní hrozby": "#F4A261",  # Soft Orange
    "sexismus": "#D77FA1",  # Muted Pink
    "terorismus": "#FF595E",  # Vivid Red

    # Freedom of Speech & Ethics (Gold, Beige)
    "svoboda slova": "#F2C14E",  # Rich Gold
}


def get_accented_tag(unaccented_tag):
    for tag in TAGS_ACCENT_TABLE:
        if TAGS_ACCENT_TABLE[tag] == unaccented_tag:
            return tag
    return None
