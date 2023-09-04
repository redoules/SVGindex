def add_block(
    x: int,
    y: int,
    text: str,
    color: str,
    title: bool,
    url: str = "",
    global_width: int = 208,
    border_color: str = "",
) -> str:
    """Generates a SVG block containing a text and a url
    Assuming the blocks are 47 pixels high, the title blocks are 29 pixels high 
    and the separation between sections is 19 pixels high
    Args:
        x (int): top corner X coordinate
        y (int): top corner Y coordinate
        text (str): Text contained in the block
        couleur (str): Color of the block as a rgb string (e.g. "rgb(52,108,169)")
        title (bool): True if the block is a header of a section.
        url (str, optional): Link of the text. Defaults to "".
        global_width (int, optional): Width in pixels of the text block. Defaults to 208.
        border_color (str, optional): Color the the border of the block as either "background", "titre" or an explicit rgb string (e.g. "rgb(52,108,169)"). Defaults to "", this will produce a black border

    Returns:
        str: A SVG rect element in  a string
    """
    height = 47
    width = global_width  # 208
    txt_color = "black"
    txt_size = 15
    txt_height_offset = 0

    if border_color == "":
        border_color = "rgb(0,0,0)"

    if color == "title":
        color = "rgb(52,108,169)"
    elif color == "background":
        color = "rgb(237,241,247)"

    if title:
        height = 29
        txt_height_offset = 7
        txt_color = "white"

    if url == "":
        return f"""<g>\n    <rect x="{x}" y="{y}" width="{width}" height="{height}" style="fill:{color};stroke-width:2;stroke:{border_color}" ></rect>\n    <text x="{x+15}" y="{y+height-15+txt_height_offset}" font-family="Verdana" font-size="{txt_size}" font-weight="bold" fill="{txt_color}">{text}</text>\n  </g>"""
    else:
        if url.endswith("xls") or url.endswith("xlsx"):
            url = "ms-excel:ofe|u|" + url
        elif url.endswith("doc") or url.endswith("docx"):
            url = "ms-word:ofe|u|" + url
        elif url.endswith("ppt") or url.endswith("pptx"):
            url = "ms-powerpoint:ofe|u|" + url
        if "\n" in text:
            txt1 = text.split("\n")[0]
            txt2 = text.split("\n")[1][1:]
            return f"""<g>\n    <rect x="{x}" y="{y}" width="{width}" height="{height}" style="fill:{color};stroke-width:2;stroke:{border_color}" ></rect>\n    <text x="{x+15}" y="{y+height-25+txt_height_offset}" font-family="Verdana" font-size="{txt_size}" font-weight="bold" fill="{txt_color}"><a href="{url}">{txt1}<tspan x="{x+15}" y="{y+height-10+txt_height_offset}">{txt2}</tspan></a></text>\n  </g>"""
        else:
            return f"""<g>\n    <rect x="{x}" y="{y}" width="{width}" height="{height}" style="fill:{color};stroke-width:2;stroke:{border_color}" ></rect>\n    <text x="{x+15}" y="{y+height-15+txt_height_offset}" font-family="Verdana" font-size="{txt_size}" font-weight="bold" fill="{txt_color}"><a href="{url}">{text}</a></text>\n  </g>"""


def section(
    x: int,
    y: int,
    title: str,
    elements: list,
    global_width: int,
    title_color: str = "titre",
) -> str:
    """Generates a section of multiple blocks 
    Assuming the blocks are 47 pixels high, the title blocks are 29 pixels high 
    and the separation between sections is 19 pixels high
    Args:
        x (int): top corner X coordinate
        y (int): top corner Y coordinate
        title (str): Section title
        elements (list): list of dicts containing information for each block of the section. Each element contains the keys : "title", "url" and optionally "border_color"
        global_width (int): Width in pixels of the section.
        title_color (str, optional): Either "background" or "title" or an explicit rgb string (e.g. "rgb(52,108,169)"). Defaults to "titre".

    Returns:
        str: A SVG element describing a section
    """
    html = add_block(
        x=x, y=y, text=title, color=title_color, global_width=global_width, title=True,
    )
    for i, e in enumerate(elements):
        try:
            html += add_block(
                x=x,
                y=y + 29 + 47 * i,
                text=e["title"],
                color="background",
                title=False,
                url=e["url"],
                global_width=global_width,
                border_color=e["border_color"],
            )
        except KeyError:
            html += add_block(
                x=x,
                y=y + 29 + 47 * i,
                text=e["title"],
                color="background",
                title=False,
                url=e["url"],
                global_width=global_width,
            )
    return html


def add_column(x: int, i: int, global_width: int, list_sections: list) -> str:
    """Generates a column containing multiple sections 
    Assuming the blocks are 47 pixels high, the title blocks are 29 pixels high 
    and the separation between sections is 19 pixels high
    Args:
        x (int): top corner X coordinate
        i (int): number of the column
        global_width (int):  Width in pixels of the column.
        list_sections (list): List of dicts containing the keys : "title", "elements", "title_color"

    Returns:
        str: A SVG element describing a columns
    """
    html = ""
    y = 5
    for isec, sec in enumerate(list_sections):
        try:
            html += section(
                x + i * global_width + 19 * i,
                y=y,
                title=sec["title"],
                elements=sec["elements"],
                global_width=global_width,
                title_color=sec["title_color"],
            )
        except KeyError:
            html += section(
                x + i * global_width + 19 * i,
                y=y,
                title=sec["title"],
                elements=sec["elements"],
                global_width=global_width,
                title_color="title",
            )
        y += 29 + len(sec["elements"]) * 47 + 19

    return html


def max_height(columns: list) -> int:
    """Return the maximum height of the SVG figure.
    Assuming the blocks are 47 pixels high, the title blocks are 29 pixels high 
    and the separation between sections is 19 pixels high

    Args:
        columns (list): List of elemnts to display

    Returns:
        int: Maximal height of the SVG figure
    """

    max_height_value = 0
    for c in columns:
        height = 0
        for s in c:
            height += len(s["elements"]) * 47 + 29
        height += 19
        max_height_value = max(max_height_value, height)
    return max_height_value
