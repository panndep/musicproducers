from flask import Flask, render_template
import sqlite3
from pathlib import Path

app = Flask(__name__)

DB_PATH = Path(__file__).parent / "footer.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS site_info (
        id INTEGER PRIMARY KEY,
        footer_text TEXT
    )
    ''')
    
    cursor.execute('SELECT COUNT(*) FROM site_info')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
        INSERT INTO site_info (footer_text)
        VALUES ("2025 Music Producers")
        ''')
    
    conn.commit()
    conn.close()

init_db()

def get_footer_text():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT footer_text FROM site_info LIMIT 1')
    text = cursor.fetchone()[0]
    conn.close()
    return text

producers_data = {
    "filty": {
        "name": "Filty",
        "full_name": "Filthy Johnson",
        "birth_date": "1990-05-15",
        "origin": "Атланта, Джорджия, США",
        "genres": ["Trap", "Hip-Hop", "Rap"],
        "active_years": "2013 - настоящее время",
        "popular_tracks": [
            "Playboi Carti - Magnolia",
            "Lil Uzi Vert - XO Tour Llif3",
            "Playboi Carti - Shoota (feat. Lil Uzi Vert)",
            "Lil Yachty - One Night",
            "Playboi Carti - R.I.P."
        ],
        "collaborations": [
            "Playboi Carti",
            "Lil Uzi Vert",
            "Lil Yachty",
            "ASAP Rocky",
            "Young Thug"
        ],
        "bio": "Filty - один из самых влиятельных продюсеров в современном трэпе. Начал свою карьеру в Атланте, работая с местными артистами. Его минималистичный, но агрессивный звук стал визитной карточкой лейбла Opium и таких артистов как Playboi Carti. Filty известен своим умением создавать харизматичные биты с запоминающимися мелодиями."
    },
    "mafia808": {
        "name": "808 Mafia",
        "members": ["Southside", "TM88", "DY", "Tarentino", "Fuse"],
        "formation": "2010",
        "origin": "Атланта, Джорджия, США",
        "genres": ["Trap", "Hip-Hop", "Rap"],
        "popular_tracks": [
            "Future - March Madness",
            "Gucci Mane - First Day Out Tha Feds",
            "Young Thug - With That",
            "Lil Uzi Vert - You Was Right",
            "21 Savage - Bank Account"
        ],
        "collaborations": [
            "Future",
            "Gucci Mane",
            "Young Thug",
            "21 Savage",
            "Lil Uzi Vert",
            "Drake"
        ],
        "bio": "808 Mafia - коллектив продюсеров из Атланты, сформированный Southside и TM88. Коллектив стал одним из самых влиятельных в жанре трэп, создав звучание для множества хитов. 808 Mafia работали практически со всеми крупнейшими артистами современного хип-хопа и продолжают задавать тренды в производстве битов."
    },
    "lucian": {
        "name": "Lucian",
        "full_name": "Lucian Piane",
        "birth_date": "1984-04-12",
        "origin": "Нью-Йорк, США",
        "genres": ["Pop", "Electronic", "Hip-Hop"],
        "active_years": "2006 - настоящее время",
        "popular_tracks": [
            "Lady Gaga - Bad Romance",
            "Lady Gaga - Poker Face",
            "Britney Spears - Work Bitch",
            "Rihanna - Pon de Replay",
            "Miley Cyrus - We Can't Stop"
        ],
        "collaborations": [
            "Lady Gaga",
            "Britney Spears",
            "Rihanna",
            "Miley Cyrus",
            "Beyoncé"
        ],
        "bio": "Lucian - продюсер и композитор, известный своей работой с Lady Gaga и другими поп-звездами. Его стиль сочетает элементы электронной музыки, поп и хип-хопа. Lucian имеет классическое музыкальное образование, что позволяет ему создавать сложные аранжировки и запоминающиеся мелодии."
    },
    "whitearmor": {
        "name": "Whitearmor",
        "full_name": "Joakim Benon",
        "birth_date": "1991-08-10",
        "origin": "Стокгольм, Швеция",
        "genres": ["Cloud Rap", "Alternative", "Electronic"],
        "active_years": "2010 - настоящее время",
        "popular_tracks": [
            "Yung Lean - Ginseng Strip 2002",
            "Bladee - Obedient",
            "Ecco2k - Peroxide",
            "Yung Lean - Kyoto",
            "Thaiboy Digital - Legendary Member"
        ],
        "collaborations": [
            "Yung Lean",
            "Bladee",
            "Ecco2k",
            "Thaiboy Digital",
            "Gud"
        ],
        "bio": "Whitearmor - шведский продюсер и участник Drain Gang, известный своим меланхоличным, атмосферным звучанием. Его работы с Yung Lean помогли сформировать облачный рэп как жанр. Whitearmor также продюсировал треки для лейбла Opium, создавая уникальное звучание на стыке трэпа и экспериментальной электроники."
    },
    "jetsonmade": {
        "name": "JetsonMade",
        "full_name": "Jetson Davis",
        "birth_date": "1996-07-22",
        "origin": "Южная Каролина, США",
        "genres": ["Trap", "Drill", "Hip-Hop"],
        "active_years": "2016 - настоящее время",
        "popular_tracks": [
            "DaBaby - Suge",
            "Roddy Ricch - The Box",
            "Jack Harlow - What's Poppin",
            "Lil Yachty - Poland",
            "Playboi Carti - Stop Breathing"
        ],
        "collaborations": [
            "DaBaby",
            "Roddy Ricch",
            "Jack Harlow",
            "Lil Yachty",
            "Playboi Carti"
        ],
        "bio": "JetsonMade - молодой, но уже крайне влиятельный продюсер, известный своими работами с DaBaby и другими артистами новой волны. Его биты отличаются агрессивными басами и минималистичными, но эффективными аранжировками. JetsonMade также работал с артистами лейбла Opium, привнося в их звучание элементы дрилла."
    }
}
@app.route('/')
def index():
    footer_text = get_footer_text()
    return render_template('index.html', 
                         producers=producers_data,
                         footer_text=footer_text)

@app.route('/producer/<producer_name>')
def producer(producer_name):
    producer_info = producers_data.get(producer_name.lower())
    if not producer_info:
        return "Producer not found", 404
        
    footer_text = get_footer_text()
    return render_template(f'{producer_name}.html', 
                         producer=producer_info,
                         footer_text=footer_text)

if __name__ == '__main__':
    app.run(debug=True)