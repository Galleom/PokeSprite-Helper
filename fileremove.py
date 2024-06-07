# removes unecessary images
from pathlib import Path
path = "images/"

for p in Path(path).glob("*-shiny-*.png"):
    p.unlink()
for p in Path(path).glob("*-shiny.png"):
    p.unlink()
for p in Path(path).glob("*-legends_arceus.png"):
    p.unlink()
for p in Path(path).glob("*-legends_arceus-hisui.png"):
    p.unlink()
for p in Path(path).glob("*-legends_arceus-alola.png"):
    p.unlink()
for p in Path(path).glob("*-gigantamax.png"):
    p.unlink()
for p in Path(path).glob("*-mega.png"):
    p.unlink()
for p in Path(path).glob("*-mega-x.png"):
    p.unlink()
for p in Path(path).glob("*-mega-y.png"):
    p.unlink()
for p in Path(path).glob("*-noble.png"):
    p.unlink()
    