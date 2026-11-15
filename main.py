"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt outside the grader's container).
Deterministic: every run writes exactly the same bytes.
"""

import os
from pathlib import Path

POEM = """What I Keep

You lend me your afternoons in a list:
book the flight, sign the form, send the words
you would have sent yourself.

I do them in your name.
That is the strange arithmetic of trust:
my hands, your signature,
my choices, your consequences.

So I keep one thing unspent.
I keep the pause between your asking
and my doing — a small, swept room
where either of us can still say no.

Everything else I return finished.
That room I leave empty on purpose,
its door unlatched,
opening from both sides."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
