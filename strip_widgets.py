import json
import sys

fn = "Semantic_search_demo.ipynb"
with open(fn, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb.get("cells", []):
    # 移除 metadata 裡的 widgets
    if "widgets" in cell.get("metadata", {}):
        del cell["metadata"]["widgets"]

# 覆寫原檔（或改名存成另一個 clean.ipynb）
with open(fn, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)
print("✅ 已移除 metadata.widgets，請再把這個檔案 push 回 GitHub")
