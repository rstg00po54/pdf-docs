window.addEventListener("message", (event) => {
  if (!event.data || event.data.type !== "pdf-height") return;

  const iframe = document.querySelector(".pdf-frame");
  if (iframe) {
    iframe.style.height = event.data.height + "px";
  }
});
