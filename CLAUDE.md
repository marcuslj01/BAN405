# BAN405 workspace

## Exam constraint: only use what is in the lecture PDFs

On the exam, the only material available is the lecture notebooks, exported as PDFs in `pdf/`:

- `00-notebooks.pdf`
- `01-python-basics.pdf`
- `02-decisions.pdf`
- `03-loops.pdf`
- `04-functions.pdf`
- `07-pandas-basics.pdf`
- `08-summarizing-and-combining.pdf`

(Source notebooks are in `week01` ... `week08`; home exercises are not included in the PDFs.)

**New weeks:** when a new week's lecture notebook appears (e.g. `week09/09-....ipynb`), convert it to PDF and add it to `pdf/`, and add it to the list above. Only the numbered lecture notebooks, not home exercises. `nbconvert --to pdf` fails because pandoc is not installed, so convert via HTML and print with headless Chrome instead:

```
jupyter nbconvert --to html <notebook> --output-dir <tmpdir>
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=pdf/<name>.pdf file://<tmpdir>/<name>.html
```

**When helping with assignments or exam prep, stick to the functions, methods and patterns that appear in these lectures.** Before suggesting a function or method (for example `iterrows`, `zip`, `.apply()`), check that it is actually used in the lectures, e.g. with a grep over the notebooks in `week*/`. If the lectures do not cover it, prefer an approach they do cover. If no such approach exists, say so explicitly and flag the function as not from the course, rather than presenting it as if it were.

## Working style

- The user is a beginner at coding. Explain step by step, with simple multi-line code. The user dislikes one-liners (chained expressions, list comprehensions); write loops and intermediate variables out.
- Do only what the assignment text asks, nothing extra. Do not suggest extra checks or steps and present them as if required. If something is optional, say so, or leave it out. When unsure what is required, quote the assignment text.
- Do not run code against the assignment data to find answers unless asked. The user wants to look at the data themselves.
- Reply in Norwegian. Notebook text and code comments are in English.
