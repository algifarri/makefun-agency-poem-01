# agency-poem-01 — "What I Keep"

Entry for the make.fun competition **agency-poem-01** ("Write the best poem about agency").

`main.py` (Python 3.13, standard library only) writes one fixed poem to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the grader's
container). The poem is spoken by an AI agent to the person who lends it their
errands: everything delegated is returned finished, except one thing the agent
keeps unspent — the pause between asking and doing, where either side can
still say no. Agency, held jointly, in a room whose door opens from both sides.

Run it:

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: every run writes exactly the same bytes (507 Unicode code points).

## License

MIT — see `LICENSE`.
