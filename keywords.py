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
    'clickbait': 'clickbait',
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

    # Kritické myšlení
    'konfirmačn': 'konfirmační bias',
    'kritické myšlení': 'kritické myšlení',

    # Hybridní hrozby
    'hybridní hrozb': 'hybridní hrozby',
    'hybridní kampaň': 'hybridní hrozby',
    'informační válk': 'hybridní hrozby',
    'informační operac': 'hybridní hrozby',

    # strategická komunikace
    'strategická komunik': 'strategická komunikace',
    'stratcom': 'strategická komunikace',

    # Ostatní
    'manipulace': 'manipulace',
    'narativ': 'narativ',
    'mystifika': 'mystifikace',

    # Out - nikdo nehleda
    # 'gerrymandering': 'gerrymandering',
    # 'overton': 'overtonovo okno',
    # 'himpatie': 'himpathy',
}

# Dictionary pro převod kategorií na verzi bez diakritiky a obráceně.
CATEGORIES_ACCENT_TABLE = {
    'dezinformace': 'dezinformace',
    'misinformace': 'misinformace',
    'malinformace': 'malinformace',
    'hoax': 'hoax',
    'propaganda': 'propaganda',
    'podvod': 'podvod',
    'twitter': 'twitter',
    'facebook': 'facebook',
    'umela-inteligence': 'AI',
    'elon-musk': 'Elon Musk',
    'tik-tok': 'tik tok',
    'konspirace': 'konspirace',
    'deepfake': 'deepfake',
    'botnet': 'botnet',
    'ddos': 'ddos',
    'troll': 'troll',
    'socialni-inzenyrstvi': 'sociální inženýrství',
    'clickbait': 'clickbait',
    'kyberbezpecnost': 'kyberbezpečnost',
    'socialni-site': 'sociální sítě',
    'medialni-gramotnost': 'mediální gramotnost',
    'retezovy-email': 'řetězový email',
    'retezak': 'řetězák',
    'svoboda-slova': 'svoboda slova',
    'fact-checking': 'fact-checking',
    'cenzura': 'cenzura',
    'algoritmus': 'algoritmus',
    'spamouflage': 'spamouflage',
    'spam': 'spam',
    'dragonbridge': 'dragonbridge',
    'storm-1376': 'storm 1376',
    'prebunking': 'prebunking',
    'debunking': 'debunking',
    'fake-news': 'fake news',
    'qanon': 'qanon',
    'infoWars': 'infoWars',
    'doxx': 'doxx',
    'doxing': 'doxing',
    'gaslighting': 'gaslighting',
    'postfakt': 'postfakt',
    'brigading': 'brigading',
    'phishing': 'phishing',
    'scam': 'scam',
    'smishing': 'smishing',
    'gerrymandering': 'gerrymandering',
    'vishing': 'vishing',
    'manosfera': 'manosféra',
    'redpilling': 'redpilling',
    'krajni-pravice': 'krajní pravice',
    'false-flag': 'false flag',
    'hybridni-hrozba': 'hybridní hrozba',
    'hijacking': 'hijacking',
    'informacni-valka': 'informační válka',
    'konfirmacni': 'konfirmační',
    'kriticke-mysleni': 'kritické myšlení',
    'mystifikace': 'mystifikace',
    'narativ': 'narativ',
    'newspeak': 'newspeak',
    'hack': 'hack',
    'phreak': 'phreak',
    'radikalismus': 'radikalismus',
    'pseudoveda': 'pseudověda',
    'overton': 'overton',
    'sextortion': 'sextortion',
    'strategicka-komunikace': 'strategická komunikace',
    'stratcom': 'stratcom',
    'weaponizace': 'weaponizace'
}