#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate pre-Week 19 album table: fill dates, strip 约, compute math expressions."""
import json, re, collections

SRC = "/workspace/.uploads/_album_table_weeks1_18.md"
OUT = "/workspace/.uploads/_album_table_weeks1_18.md"

# ---------- date overrides: manual verified (priority) ----------
D = {}
def add(w, t, d): D[(w, t)] = d

# Week 2
add(2, "All For You", "2012-08-22")
add(2, "周杰倫的床邊故事", "2016-06-24")
add(2, "最偉大的作品", "2022-07-15")
add(2, "不良少年", "2011-12-26")
add(2, "F.I.R.", "2004-04-23")
add(2, "花花宇宙", "2000-05-26")
add(2, "Red Liberation", "2023-10-11")
add(2, "マイクロレボリューション", "2024-08-07")
add(2, "君じゃなきゃダメみたい", "2014-08-27")
add(2, "ウラオモテ・フォーチュン", "2014-08-27")
add(2, "動く、動く", "2017-11-29")
add(2, "More One Night", "2017-11-29")
add(2, "ブループリント", "2024-07-13")
add(2, "HARDCORE SYNDROME 14", "2020-08-19")
add(2, "HARDCORE SYNDROME 15", "2021-08-18")
add(2, "HARDCORE SYNDROME 16", "2022-08-13")
add(2, "HARDCORE SYNDROME 17", "2023-08-13")
add(2, "HARDCORE SYNDROME 18", "2024-10-27")
# Week 3
add(3, "ブループリント (Special Edition)", "2024-08-21")
add(3, "Daydream café", "2014-05-28")
add(3, "ぽっぴんジャンプ♪", "2014-05-28")
add(3, "ノーポイッ!", "2015-11-11")
add(3, "ときめきポポロン♪", "2015-11-11")
add(3, "天空カフェテリア", "2020-10-28")
add(3, "なかよし！○！なかよし！", "2020-10-28")
add(3, "セカイがカフェになっちゃった!", "2017-11-11")
add(3, "しんがーそんぐぱやぽやメロディー", "2019-09-26")
add(3, "ふ･れ･ん･ど･し･た･い", "2015-07-29")
add(3, "ハーモナイズ・クローバー/アフターグロウ", "2015-08-19")
add(3, "TVアニメ「がっこうぐらし!」キャラクターソング①", "2015-08-26")
add(3, "TVアニメ「がっこうぐらし!」キャラクターソング②", "2015-08-26")
add(3, "TVアニメ「がっこうぐらし!」キャラクターソング③", "2015-09-26")
add(3, "TVアニメ「がっこうぐらし!」キャラクターソング④", "2015-09-26")
add(3, "HARDCORE SYNDROME 19", "2025-10-26")
add(3, "IRREGULAR NATION 2", "2016-04-24")
add(3, "IRREGULAR NATION 3", "2017-04-30")
add(3, "IRREGULAR NATION 4", "2018-04-29")
add(3, "魔法少女ノ魔女裁判 コンプリートオリジナルサウンドトラック", "2025-07-18")
add(3, "NOIR ORIGINAL SOUNDTRACK I", "2001-06-21")
add(3, "NOIR ORIGINAL SOUNDTRACK II", "2001-10-03")
add(3, "「NOIR」blanc dans NOIR～黒の中の白～", "2001-11-07")
add(3, "ぼっち・ざ・ろっく! オリジナルサウンドトラックvol.1", "2022-12-28")
add(3, "ぼっち・ざ・ろっく! オリジナルサウンドトラックvol.2", "2023-01-25")
# Week 4
add(4, "初音ミクの消失", "2010-08-04")
add(4, "少女と夢人形", "2004-10-09")
add(4, "staple stable & あとがたり", "2009-09-30")
add(4, "帰り道 & あとがたり", "2009-10-28")
add(4, "ambivalent world & あとがたり", "2009-11-25")
add(4, "恋愛サーキュレーション & あとがたり", "2009-12-23")
add(4, "月光/街", "2023-06-21")
add(4, "STAGE OF SEKAI/Peaky Peaky", "2023-07-05")
add(4, "オーダーメイド/てらてら", "2023-07-05")
add(4, "イフ/パラソルサイダー", "2023-07-19")
add(4, "88☆彡/星空のメロディー", "2023-08-02")
add(4, "虚ろを扇ぐ/仮死化", "2023-08-16")
add(4, "Voices/the WALL", "2023-08-30")
add(4, "DREAM PLACE/フロート・プランナー", "2023-09-13")
add(4, "君の夜をくれ/Iなんです", "2023-09-27")
add(4, "どんな結末がお望みだい？/星空オーケストラ", "2023-10-11")
add(4, "からかい上手の高木さん Cover Song Collection", "2018-03-28")
add(4, "からかい上手の高木さん2 Cover Song Collection", "2019-09-25")
add(4, "IRREGULAR NATION 5", "2019-04-28")
add(4, "IRREGULAR NATION 6", "2020-03-01")
# Week 5
add(5, "IRREGULAR NATION 7", "2021-04-25")
add(5, "IRREGULAR NATION 8", "2022-06-27")
add(5, "IRREGULAR NATION 9", "2023-04-30")
add(5, "Aladdin: Original Motion Picture Soundtrack", "1992-10-31")
# Week 6
add(6, "Relay - ghostpia Season One Original Soundtrack", "2023-08-22")
add(6, "Cytus II-Paff Original Soundtrack", "2018-07-10")
add(6, "Cytus II-Neko Original Soundtrack", "2018-08-08")
add(6, "Cytus II-Robo_head Original Soundtrack", "2018-09-19")
add(6, "Cytus II-Ivy Original Soundtrack", "2020-01-18")
add(6, "Cytus II-Vanessa Original Soundtrack", "2020-07-10")
add(6, "Cytus II-Xenon Original Soundtrack", "2018-12-28")
add(6, "Cytus II-Cherry Original Soundtrack", "2025-09-08")
add(6, "Cytus II-ConneR Original Soundtrack", "2018-07-12")
add(6, "Cytus II-Joe Original Soundtrack", "2025-09-08")
add(6, "Cytus II-Sagar Original Soundtrack", "2025-09-08")
add(6, "Cytus II-Rin Original Soundtrack", "2025-09-08")
add(6, "Cytus II-Ilka Original Soundtrack", "2025-09-08")
add(6, "After the End", "2014-10")
# Week 7
add(7, "ULTIMATE HAPPY CARNIVAL", "2021-01-04")
add(7, "HARDCORE UTOPIA", "2019-10-28")
add(7, "HARDCORE UTOPIA 2", "2020-08-14")
add(7, "HARDCORE UTOPIA 3", "2021-07-02")
add(7, "HARDCORE UTOPIA 4", "2022-09-02")
# Week 8
add(8, "VSQ Performs Lady Gaga", "2010-07-27")
add(8, "Selentia", "2012-08-11")
add(8, "L'aventale", "2013-08-12")
add(8, "fairythm", "2014-12-30")
# Week 9
add(9, "相愛性理論", "2010-04-21")
add(9, "The Romantic", "2026-02-27")
add(9, "FREE YOUR MIND", "2016-11-02")
# Week 14
for n, d in [(1, "2019-09-25"), (2, "2019-10-09"), (3, "2019-10-23"), (4, "2019-11-06"), (5, "2019-11-20"),
             (6, "2019-12-04"), (7, "2019-12-11"), (8, "2019-12-25"), (9, "2020-01-15"), (10, "2020-01-29")]:
    add(14, f"TVアニメ『アズールレーン』キャラクターソングシングル Vol.{n}", d)
for n, d in [(1, "2020-02-12"), (2, "2020-02-26"), (3, "2020-03-11"), (4, "2020-03-25"), (5, "2020-04-08")]:
    add(14, f"TVアニメ『アズールレーン』バディキャラクターソングシングル Vol.{n}", d)
add(14, "Diverse Style from \"B\"", "2000")
add(14, "Diverse Style from \"B\" 2nd style.", "2000-12-30")
add(14, "Diverse Style from \"B\" 1st & 2nd", "2001")
add(14, "Diverse Style from \"B\" 3rd style [Normal]", "2001-08-21")
add(14, "Diverse Style from \"B\" 3rd style [Versus]", "2001-08-12")
add(14, "Diverse Style from \"B\" 4th style", "2001-12-30")
add(14, "Diverse Style from \"B\" 5th style", "2002-08-11")
add(14, "Diverse Style from \"B\" 6th style", "2002-12")
add(14, "Dear,Mr.180", "2001-12-30")
add(14, "Side-C", "2001-08-11")
add(14, "Diverse System Original ＃1", "2002-04-28")
add(14, "Diverse System Original ＃2", "2002-08-10")
add(14, "Diverse System Original ＃3", "2003-12-19")
add(14, "IRREGULAR NATION 10", "2024-04-28")
add(14, "IRREGULAR NATION 11", "2025-08-17")
add(14, "Bright Colors 3", "2015-12-31")
add(14, "Bright Colors 4", "2017-12-29")
add(14, "Bright Colors 5", "2020-05-05")
add(14, "Bright Colors 6", "2022-04-24")
add(14, "最高", "2026-03-03")
add(14, "Dinosaur", "2000-05-02")
add(14, "化物語 音楽全集 Songs & Soundtracks", "2011-12-21")
add(14, "fiction", "2024-09-11")
add(14, "「からかい上手の高木さん３＆劇場版」Cover Song Collection", "2022-07-13")
# Week 17
add(17, "恋のビギナーなんです (T_T)", "2012-04-25")
add(17, "塞尘のパンドラ", "2009-08-05")

# ---------- Artist fill: verified (2026-09) ----------
ARTIST = {
    "魔法少女ノ魔女裁判 コンプリートオリジナルサウンドトラック": "近藤祐輔",
    "NOIR ORIGINAL SOUNDTRACK I": "梶浦由記",
    "NOIR ORIGINAL SOUNDTRACK II": "梶浦由記",
    "「NOIR」blanc dans NOIR～黒の中の白～": "梶浦由記",
    "ぼっち・ざ・ろっく! オリジナルサウンドトラックvol.1": "菊谷知樹",
    "ぼっち・ざ・ろっく! オリジナルサウンドトラックvol.2": "菊谷知樹",
    "staple stable & あとがたり": "戦場ヶ原ひたぎ（CV.斎藤千和）",
    "帰り道 & あとがたり": "八九寺真宵（CV.加藤英美里）",
    "ambivalent world & あとがたり": "神原駿河（CV.沢城みゆき）",
    "恋愛サーキュレーション & あとがたり": "千石撫子（CV.花澤香菜）",
    "Aladdin: Original Motion Picture Soundtrack": "Alan Menken",
    "Relay - ghostpia Season One Original Soundtrack": "Hiromu Takano",
    "Cytus II-Paff Original Soundtrack": "Rayark",
    "Cytus II-Neko Original Soundtrack": "Rayark",
    "Cytus II-Robo_head Original Soundtrack": "Rayark",
    "Cytus II-Ivy Original Soundtrack": "Rayark",
    "Cytus II-Vanessa Original Soundtrack": "Rayark",
    "Cytus II-Xenon Original Soundtrack": "Rayark",
    "Cytus II-Cherry Original Soundtrack": "Rayark",
    "Cytus II-ConneR Original Soundtrack": "Rayark",
    "Cytus II-Joe Original Soundtrack": "Rayark",
    "Cytus II-Sagar Original Soundtrack": "Rayark",
    "Cytus II-Rin Original Soundtrack": "Rayark",
    "Cytus II-Ilka Original Soundtrack": "Rayark",
    "HARDCORE UTOPIA": "Kara (43)",
    "HARDCORE UTOPIA 2": "Kara (43)",
    "HARDCORE UTOPIA 3": "Kara (43)",
    "HARDCORE UTOPIA 4": "Kara (43)",
    "HARDCORE UTOPIA 5": "Kara (43)",
    "化物語 音楽全集 Songs & Soundtracks": "神前暁",
}

# ---------- length expression evaluation ----------
FRACS = {"½": 1/2, "⅓": 1/3, "⅔": 2/3, "¼": 1/4, "¾": 3/4,
         "⅕": 1/5, "⅖": 2/5, "⅗": 3/5, "⅘": 4/5,
         "⅙": 1/6, "⅚": 5/6,
         "⅐": 1/7, "⅛": 1/8, "⅑": 1/9, "⅒": 1/10}

def eval_expr(s):
    """Evaluate math expression like '(37+⅚+⅒)min' to minutes float, or None."""
    s = s.strip()
    m = re.match(r"^\((.+)\)(?:min|分)?$", s)
    if not m:
        return None
    expr = m.group(1)
    # translate fraction chars
    def repl(fr):
        return f"({FRACS[fr]})"
    expr = re.sub("|".join(map(re.escape, FRACS)), lambda mo: repl(mo.group(0)), expr)
    expr = expr.replace("·", "*").replace("×", "*")
    try:
        val = eval(expr)
        if isinstance(val, (int, float)):
            return val
    except Exception:
        return None
    return None

def fmt_len(minutes):
    total = int(round(minutes * 60))
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"

def proc_len(raw):
    raw = raw.strip()
    raw = raw.replace("约", "").replace("約", "")
    if not raw:
        return raw
    mval = eval_expr(raw)
    if mval is not None:
        return fmt_len(mval)
    return raw

# ---------- apply ----------
with open(SRC, encoding="utf-8") as f:
    lines = f.read().splitlines()

out = []
week = None
fixed_dates, fixed_lens = 0, 0
for line in lines:
    wm = re.match(r"^### Week (\d+)$", line)
    if wm:
        week = int(wm.group(1))
        out.append(line)
        continue
    if not line.startswith("|") or line.startswith("| :"):
        out.append(line)
        continue
    if line.strip().startswith("| Type |"):
        out.append(line)
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    # Type | Format | Title | Artist | Released | Tracks | Length | Week
    typ, fmt, title, artist, released, tracks, length, wk = cells
    # exact match, then prefix match (azurlane Vol.N titles carry character names)
    date = D.get((week, title))
    if date is None:
        for (w, t), d in D.items():
            if w == week and (title == t or title.startswith(t + " ")):
                date = d
                break
    if date and released != date:
        released = date
        fixed_dates += 1
    if artist == "待核实" and title in ARTIST:
        artist = ARTIST[title]
    if tracks == "待核实":
        if title == "塞尘のパンドラ":
            tracks, length = "4", "18:54"
    if length == "待核实" and title == "After the End":
        length = "24:08"
    new_len = proc_len(length)
    if new_len != length:
        fixed_lens += 1
    length = new_len
    out.append(f"| {typ} | {fmt} | {title} | {artist} | {released} | {tracks} | {length} | {wk} |")

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(out) + "\n")

# ---------- report ----------
remain = [l for l in out if l.startswith("|") and "待核实" in l if not l.startswith("| :") and "| Type |" not in l]
print("dates filled:", fixed_dates)
print("lengths fixed:", fixed_lens)
print("remaining 待核实 rows:", len(remain))
for r in remain:
    print("  ", r)