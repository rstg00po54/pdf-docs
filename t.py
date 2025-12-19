import os

pdf_dir = "docs/pdf"
out_dir = "docs/generated"

os.makedirs(out_dir, exist_ok=True)
pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
pdf_files.sort()

for pdf in pdf_files:
    filename = os.path.splitext(pdf)[0] + ".md"
    content = f"""# {pdf}

<iframe src="../pdfjs/web/viewer.html?file=pdf/{pdf}" width="100%" height="900px"></iframe>
"""
    with open(os.path.join(out_dir, filename), "w") as f:
        f.write(content)
