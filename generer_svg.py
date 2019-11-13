import json
from svg_utils import hauteur_max, add_column
with open('sharepoint.json', 'r', encoding='utf-8') as f:
    colonnes = json.load(f)
    
    largeur_globale = 208
    
    html = f"<svg width='{len(colonnes)*(largeur_globale+19)}' height='{hauteur_max(colonnes)}'>"
    for ic, colonne in enumerate(colonnes):
        html += add_column(x = 5, i = ic, largeur_globale=largeur_globale, liste_sections=colonne)
    html+="</svg>"
    with open("visu_demo.html", "w") as f:
        f.write(html)