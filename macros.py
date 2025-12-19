import os

def define_env(env):
    pdf_dir = os.path.join(env.project_dir, "docs", "pdf")
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith(".pdf")]
    pdf_files.sort()
    env.variables['pdf_files'] = pdf_files
