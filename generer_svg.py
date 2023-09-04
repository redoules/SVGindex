#%%
import json
from svg_utils import max_height, add_column
import argparse


# %%
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json",
        type=str,
        help="Json file containing the different sections and links",
    )
    args = parser.parse_args()
    file = args.json

    if file is None:
        file = "data.json"

    print(file)
    with open(file, "r", encoding="utf-8") as f:
        columns = json.load(f)

        global_width = columns.pop(0)[0]["width"]

        html = "<!-- In order to generate the svg, use the following repo : \n"
        html += "https://github.com/redoules/SVGindex\n"
        html += "with a json file containing the following content : \n"
        f.seek(0)
        html += f.read()
        html += "\n-->\n"

        html += f"<svg width='{len(columns)*(global_width+19)}' height='{max_height(columns)+50}'>"
        for ic, column in enumerate(columns):
            html += add_column(
                x=5, i=ic, global_width=global_width, list_sections=column
            )
        html += "</svg>"
        with open("visu_demo.html", "w") as f:
            f.write(html)
