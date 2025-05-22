import json

def remove_widgets(o):
    if isinstance(o, dict):
        # 刪掉當前這層的 widgets
        if "widgets" in o:
            del o["widgets"]
        # 繼續遞迴
        for v in o.values():
            remove_widgets(v)
    elif isinstance(o, list):
        for item in o:
            remove_widgets(item)

# 讀原檔
fn = "Semantic_search_demo.ipynb"
with open(fn, "r", encoding="utf-8") as f:
    nb = json.load(f)

# 遞迴刪除所有 widgets
remove_widgets(nb)

# 寫回原檔（覆蓋）
with open(fn, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("✅ 已遞迴移除所有 metadata.widgets，請再 git add, commit, push")
