# Dictionary pro vyhledávání slov v textu a jejich převod na kategorie.
KEYWORDS_SEARCH_TABLE = {
    #dezinformace
    'dezinform': 'dezinformace',
    'misinform': 'misinformace',
    'malinforma': 'malinformace',
    'hoax': 'hoax',
    'konspir': 'konspirace',
    'manipulace': 'manipulace',
    'fake news': 'fake news',
    'postfakt': 'doba postfaktická',
    'pseudověd': 'pseudověda',

    #strategická komunikace
    'strategická komunik': 'strategická komunikace',
    'stratcom': 'strategická komunikace',

    #propaganda
    'propagand': 'propaganda',
    'sociální inženýrství': 'sociální inženýrství',
    'dragonbridge': 'dragonbridge',
    'storm 1376': 'storm 1376',
    'qanon': 'qanon',
    'infowars': 'infoWars',
    'false flag': 'false flag',
    'hybridní hrozb': 'hybridní hrozba',
    'informační válk': 'informační válka',
    'narativ': 'narativ',
    'mystifika': 'mystifikace',

    #sociální sítě
    'twitter': 'x.com',
    'facebook': 'facebook',
    'musk': 'Elon Musk',
    'tik tok': 'tik tok',
    'sociální sítě': 'sociální sítě',
    'algoritm': 'algoritmus',
    'gaslighting': 'gaslighting',

    #AI
    'umělá inteligence': 'AI',
    'deepfake': 'deepfake',
    'AI': 'AI',

    #Podvodné praktiky
    'podvod': 'podvod',
    'clickbait': 'clickbait',
    'botnet': 'botnet',
    'ddos': 'ddos',
    'troll': 'troll',
    'kyber': 'kyberbezpečnost',
    'spamouflage': 'spamouflage',
    'spam': 'spam',
    'doxx': 'doxxing',
    'doxing': 'doxxing',
    'brigading': 'brigading',
    'phishing': 'phishing',
    'scam': 'scam',
    'smishing': 'smishing',
    'vishing': 'vishing',
    'hack': 'hacking',
    'phreak': 'phreaking',
    'sextortion': 'sextortion',
    'gerrymandering': 'gerrymandering',
    'hijacking': 'hijacking',

    #Mediální gramotnost
    'mediální gramotnost': 'mediální gramotnost',

    #Řetězové zprávy
    'řetězový email': 'řetězáky',
    'řetězové email': 'řetězáky',
    'řetězák': 'řetězáky',

    #Svoboda slova
    'svoboda slova': 'svoboda slova',
    'cenzúr': 'cenzura',
    'cenzur': 'cenzura',
    'newspeak': 'newspeak',

    #Fact-checking
    'fact-checking': 'fact-checking',
    'overovanie faktov': 'fact-checking',
    'ověřování faktů': 'fact-checking',
    'prebunking': 'prebunking',
    'debunking': 'debunking',

    #Radikalizace
    'manosféra': 'manosféra',
    'redpilling': 'redpilling',
    'radikali': 'radikalismus',
    'krajní pravice': 'krajní pravice',
    'overton': 'overtonovo okno',
    'weaponiz': 'weaponizace',

    #Kritické myšlení
    'konfirmačn': 'konfirmační bias',
    'kritické myšlení': 'kritické myšlení',
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