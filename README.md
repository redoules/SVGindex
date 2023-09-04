# SVGindex
Generation of table of content with embedded links in a svg. Ideal to use with Sharepoint as a smart art.

## Input

The program takes a json file as an input.

you can find a sample json file named "data.json" in the repo.

The json contains lists :
 * the fist list contains a unique element "{"width": 208}" describing the global width of the elements in the svg
 * the following list represent a columns and contains a list of sections.

A section is a dict containing a "title", and a list of "elements". A section can optionnaly contain a "title_color" and "border_color".

Finally, an element contains a "title" and a "url".


## Ouput

The output is a svg element stored in the visu_demo.html file.
![Sample output](https://raw.githubusercontent.com/redoules/SVGindex/master/out.svg?sanitize=true)

## How to run?

```bash
python generer_svg.py --json data.json
```
