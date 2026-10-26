# Ship Week

A seven-day simulation game for vibe coders: ship the Study Notes sample app with an AI agent. Each day practises one part of vibe coding — planning a spec, writing prompts, committing and reverting in a terminal, debugging with a fresh chat, reviewing a PR, handling leaked keys, and testing before launch. UI text is in Burmese.

- Play: open `index.html`, or the GitHub Pages site for this repo.
- Edit: change `src/game.tpl.html` or `src/guide.json`, then run `python3 src/build.py` to regenerate `index.html` and `src/artifact.html`.
- Progress is saved in the browser (localStorage), per device.
- Burmese text uses Pyidaungsu 2.5.3 by the Myanmar Computer Federation, from https://github.com/mcfnlp/Pyidaungsu.
