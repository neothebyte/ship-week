# Builds the game from src/:
#   ../index.html   standalone page: open from disk or serve with GitHub Pages (doctype + UTF-8 head)
#   artifact.html   page body for publishing as a claude.ai Artifact (the platform adds the head)
import json, base64, pathlib

src = pathlib.Path(__file__).resolve().parent
tpl = (src / 'game.tpl.html').read_text(encoding='utf-8')
data = json.loads((src / 'guide.json').read_text(encoding='utf-8'))

rng = 'U+1000-109F,U+A9E0-A9FF,U+AA60-AA7F,U+200B-200D,U+25CC'
faces = []
for weight, style in ((400, 'Regular'), (700, 'Bold')):
    b64 = base64.b64encode((src / 'fonts' / f'Pyidaungsu-2.5.3_{style}.ttf').read_bytes()).decode()
    faces.append('@font-face{font-family:"Pyidaungsu";font-weight:%d;font-style:normal;font-display:swap;'
                 'unicode-range:%s;src:url(data:font/ttf;base64,%s) format("truetype")}' % (weight, rng, b64))

body = (tpl.replace('__DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
           .replace('__FONTFACE__', '\n'.join(faces)))

(src / 'artifact.html').write_text(body, encoding='utf-8')
head = ('<!doctype html>\n<html lang="my">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<style>body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n')
(src.parent / 'index.html').write_text(head + body + '\n</body>\n</html>\n', encoding='utf-8')
print('built index.html and src/artifact.html')
