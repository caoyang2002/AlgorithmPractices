/* ================================================================= */
/* JavaScript代码 */
/* ================================================================= */

// 优化的导航按钮JavaScript
document.addEventListener("DOMContentLoaded", () => {
  // 检查是否有book对象
  if (!window.book) return;

  const prev = window.book.previous;
  const next = window.book.next;
  const body = document.body;

  // 创建导航容器
  const navContainer = document.createElement("div");
  navContainer.className = "bottom-nav-container";

  // 创建上一页按钮
  if (prev) {
    const prevButton = document.createElement("a");
    prevButton.href = prev.path;
    prevButton.className = "nav-button previous";
    prevButton.innerHTML = `
        <span class="chapter-label">上一章</span>
        <span class="chapter-title">${escapeHtml(prev.title)}</span>
    `;

    // 添加键盘导航支持
    prevButton.addEventListener("keydown", handleKeyDown);
    navContainer.appendChild(prevButton);
  }

  // 创建下一页按钮
  if (next) {
    const nextButton = document.createElement("a");
    nextButton.href = next.path;
    nextButton.className = "nav-button next";
    nextButton.innerHTML = `
        <span class="chapter-label">下一章</span>
        <span class="chapter-title">${escapeHtml(next.title)}</span>
    `;

    // 添加键盘导航支持
    nextButton.addEventListener("keydown", handleKeyDown);
    navContainer.appendChild(nextButton);
  }

  // 将容器添加到body
  body.appendChild(navContainer);

  // 添加键盘快捷键支持
  document.addEventListener("keydown", (e) => {
    // 避免在输入框中触发
    if (
      e.target.tagName === "INPUT" ||
      e.target.tagName === "TEXTAREA" ||
      e.target.isContentEditable
    ) {
      return;
    }

    switch (e.key) {
      case "ArrowLeft":
        if (prev && !e.ctrlKey && !e.metaKey) {
          e.preventDefault();
          window.location.href = prev.path;
        }
        break;
      case "ArrowRight":
        if (next && !e.ctrlKey && !e.metaKey) {
          e.preventDefault();
          window.location.href = next.path;
        }
        break;
    }
  });
});

// 辅助函数：转义HTML
function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

// 辅助函数：处理键盘事件
function handleKeyDown(e) {
  if (e.key === "Enter" || e.key === " ") {
    e.preventDefault();
    e.target.click();
  }
}
