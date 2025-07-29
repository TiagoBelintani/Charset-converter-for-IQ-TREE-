## Script: `fix_charsets.py`

``` python
import sys
import re

if len(sys.argv) != 2:
    print("Usage: python fix_charsets.py input.charsets")
    sys.exit(1)

input_path = sys.argv[1]
if not input_path.endswith(".charsets"):
    print("File must end with .charsets")
    sys.exit(1)

output_path = input_path.replace(".charsets", "_iqtree.charsets")

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

converted = []
for line in lines:
    match = re.match(r"charset\s+'?([\w\-.]+)\.fasta'?\s*=\s*(\d+-\d+);", line)
    if match:
        gene, coords = match.groups()
        converted.append(f"DNA, {gene} = {coords}")

if not converted:
    print("⚠️ No valid partitions found. Check your input format.")
    sys.exit(1)

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(converted))

print(f"✅ Converted file saved as: {output_path}")
```
