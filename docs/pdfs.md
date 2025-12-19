# PDF 文档集

{% set pdf_files = [
    'LubanCat4CB_EBF410133V1R0_SCH_20250728.pdf',
    'LubanCat4IOB_EBF410134V1R0_SCH_20250728.pdf'
] %}

{% for pdf in pdf_files %}
## {{ pdf }}
<!-- <iframe src="pdfjs/web/viewer.html?file=pdf/{{ pdf }}" width="100%" height="900px"></iframe> -->
<div class="pdf-outer">
<iframe
  class="pdf-frame"
  src="/pdf-docs/pdfjs/web/viewer.html?file=/pdf-docs/pdf/AMOLED/Amoled-5.99/PCB_PCB1_2025-12-09.pdf#zoom=page-width"
  loading="lazy">
</iframe>
</div>

{% endfor %}
