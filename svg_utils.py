def add_block(x, y, text, couleur, titre,  url = "", largeur_globale = 208, couleur_tour=""):
    """
    
    """
    hauteur = 47
    largeur = largeur_globale#208
    couleur_txt = "black"
    taille_txt = 15
    corr_hauteur_txt = 0
    
    if couleur_tour == "":
        couleur_tour = "rgb(0,0,0)"
    
    if couleur == "titre":
        couleur = "rgb(52,108,169)"
    elif couleur == "fond":
        couleur = "rgb(237,241,247)"
        
    if titre:
        hauteur = 29
        corr_hauteur_txt = 7
        couleur_txt = "white"
        
    if url == "":
        return f'<g>\n    <rect x="{x}" y="{y}" width="{largeur}" height="{hauteur}" style="fill:{couleur};stroke-width:2;stroke:{couleur_tour}" ></rect>\n    <text x="{x+15}" y="{y+hauteur-15+corr_hauteur_txt}" font-family="Verdana" font-size="{taille_txt}" font-weight="bold" fill="{couleur_txt}">{text}</text>\n  </g>'
    else:
        if "\n" in text:
            txt1 = text.split("\n")[0]
            txt2 = text.split("\n")[1][1:]
            return f'<g>\n    <rect x="{x}" y="{y}" width="{largeur}" height="{hauteur}" style="fill:{couleur};stroke-width:2;stroke:{couleur_tour}" ></rect>\n    <text x="{x+15}" y="{y+hauteur-25+corr_hauteur_txt}" font-family="Verdana" font-size="{taille_txt}" font-weight="bold" fill="{couleur_txt}"><a href="{url}">{txt1}<tspan x="{x+15}" y="{y+hauteur-10+corr_hauteur_txt}">{txt2}</tspan></a></text>\n  </g>'
        else:    
            return f'<g>\n    <rect x="{x}" y="{y}" width="{largeur}" height="{hauteur}" style="fill:{couleur};stroke-width:2;stroke:{couleur_tour}" ></rect>\n    <text x="{x+15}" y="{y+hauteur-15+corr_hauteur_txt}" font-family="Verdana" font-size="{taille_txt}" font-weight="bold" fill="{couleur_txt}"><a href="{url}">{text}</a></text>\n  </g>'
            

def section(x, y, titre, elements, largeur_globale, couleur_titre = "titre"):
    """
    
    """
    html = add_block(x=x, y=y, text=titre, couleur= couleur_titre, titre=True)
    for i, e in enumerate(elements):
        try:
            html += add_block(x=x, y=y+29+47*i, text=e["titre"], couleur="fond", titre=False, url=e["url"], largeur_globale = largeur_globale, couleur_tour=e["couleur_tour"])
        except KeyError:
            html += add_block(x=x, y=y+29+47*i, text=e["titre"], couleur="fond", titre=False,  url=e["url"], largeur_globale = largeur_globale)
    return html

def add_column(x, i, largeur_globale, liste_sections):
    """
    
    """
    html = ""
    y=5
    for isec, sec in enumerate(liste_sections):
        try:
            html += section(x + i * largeur_globale + 19*i, y = y  , titre = sec["titre"], elements = sec["elements"], largeur_globale = largeur_globale, couleur_titre =sec["couleur_titre"])
        except KeyError:
            html += section(x + i * largeur_globale + 19*i, y = y  , titre = sec["titre"], elements = sec["elements"], largeur_globale = largeur_globale, couleur_titre ="titre")
        y += 29 + len(sec["elements"])*47 + 19
    
    return html

def hauteur_max(colonnes):
    """
    
    """
    maxhauteur = 0
    for c in colonnes:
        hauteur = 0
        for s in c:
            hauteur += len(s["elements"])*47 + 29
        hauteur += 19
        maxhauteur = max(maxhauteur, hauteur)
    return maxhauteur