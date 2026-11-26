import os

LINE = "Stapler, c. 1997. Pressed steel and quiet resentment. Used to bind quarterly reports. Donated by the Accounts Department, who never got it back."

LIMIT = 180
if len(LINE) != 144 or len(LINE) > LIMIT:
    raise SystemExit(f"placard line must be 144 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
