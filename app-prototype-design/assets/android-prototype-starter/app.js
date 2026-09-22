const PRIMARY_ROUTES = new Set(["home", "projects", "stats", "profile"]);

function initialisePrototype(instance) {
  const template = document.querySelector("#app-shell-template");
  const root = instance.querySelector("[data-app-root]");
  root.append(template.content.cloneNode(true));

  let route = instance.dataset.startScreen || "home";
  const shell = root.querySelector(".app-shell");
  const toast = root.querySelector(".toast");
  let toastTimer;

  function showToast(message) {
    clearTimeout(toastTimer);
    toast.textContent = message;
    toast.hidden = false;
    toastTimer = setTimeout(() => { toast.hidden = true; }, 1800);
  }

  function renderRoute(nextRoute) {
    route = nextRoute;
    root.querySelectorAll("[data-screen]").forEach((screen) => {
      screen.hidden = screen.dataset.screen !== route;
    });
    root.querySelectorAll("[data-nav-item]").forEach((item) => {
      const active = item.dataset.routeTo === route;
      item.classList.toggle("active", active);
      item.setAttribute("aria-current", active ? "page" : "false");
    });
    root.querySelector(".app-bottom-nav").hidden = !PRIMARY_ROUTES.has(route);
  }

  root.addEventListener("click", (event) => {
    const routeControl = event.target.closest("[data-route-to]");
    const backControl = event.target.closest("[data-back-to]");
    const modalOpen = event.target.closest("[data-modal-open]");
    const modalClose = event.target.closest("[data-modal-close]");
    const feedback = event.target.closest("[data-prototype-feedback]");
    const tab = event.target.closest("[data-tab-value]");

    if (routeControl) renderRoute(routeControl.dataset.routeTo);
    if (backControl) renderRoute(backControl.dataset.backTo);
    if (modalOpen) root.querySelector(`[data-modal="${modalOpen.dataset.modalOpen}"]`).hidden = false;
    if (modalClose) root.querySelector(`[data-modal="${modalClose.dataset.modalClose}"]`).hidden = true;
    if (feedback) showToast(feedback.dataset.prototypeFeedback);
    if (tab) {
      root.querySelectorAll("[data-tab-value]").forEach((item) => {
        const active = item === tab;
        item.classList.toggle("active", active);
        item.setAttribute("aria-selected", String(active));
      });
      root.querySelector("[data-total]").textContent = tab.dataset.tabValue === "week" ? "¥1,120" : "¥4,360";
    }
    if (event.target.matches("[data-modal]")) event.target.hidden = true;
  });

  root.querySelector("[data-reminder]").addEventListener("change", (event) => {
    root.querySelector("[data-reminder-state]").textContent = event.target.checked ? "每天 21:00" : "已关闭";
    showToast(event.target.checked ? "提醒已开启" : "提醒已关闭");
  });

  root.querySelector("[data-entry-form]").addEventListener("submit", (event) => {
    event.preventDefault();
    const form = event.currentTarget;
    const amount = Number(form.elements.amount.value);
    const error = form.querySelector("[data-amount-error]");
    if (!Number.isFinite(amount) || amount <= 0) {
      error.textContent = "请输入大于 0 的金额";
      form.elements.amount.focus();
      return;
    }
    error.textContent = "";
    const category = new FormData(form).get("category");
    root.querySelector("[data-transaction-list]").insertAdjacentHTML(
      "afterbegin",
      `<li><span>${category.slice(0, 1)}</span><div><strong>${category}</strong><small>刚刚</small></div><b>- ¥${amount.toFixed(2)}</b></li>`
    );
    renderRoute("detail");
    showToast("记录已保存");
    form.reset();
  });

  renderRoute(route);
  shell.dataset.ready = "true";
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-prototype-instance]").forEach(initialisePrototype);
});

