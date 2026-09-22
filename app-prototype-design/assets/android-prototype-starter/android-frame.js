class AndroidFrame extends HTMLElement {
  connectedCallback() {
    if (this.shadowRoot) return;

    const root = this.attachShadow({ mode: "open" });
    const time = this.getAttribute("time") || "09:41";
    root.innerHTML = `
      <style>
        :host {
          --android-frame-width: 360px;
          --android-frame-height: 780px;
          --android-frame-radius: 38px;
          --android-frame-border: 8px;
          display: block;
          width: min(100%, var(--android-frame-width));
          height: var(--android-frame-height);
          color: #21191d;
        }
        .hardware {
          box-sizing: border-box;
          position: relative;
          width: 100%;
          height: 100%;
          overflow: hidden;
          border: var(--android-frame-border) solid #1f1a1d;
          border-radius: var(--android-frame-radius);
          background: #f9f6f4;
          box-shadow: 0 24px 60px rgba(43, 22, 31, 0.2), 0 4px 12px rgba(43, 22, 31, 0.12);
        }
        .status {
          box-sizing: border-box;
          position: absolute;
          z-index: 10;
          inset: 0 0 auto;
          height: 30px;
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: 0 16px 0 18px;
          font: 700 11px/1 system-ui, sans-serif;
          background: color-mix(in srgb, var(--app-surface, #f9f6f4) 92%, transparent);
          backdrop-filter: blur(12px);
        }
        .camera {
          position: absolute;
          left: 50%;
          top: 8px;
          width: 8px;
          height: 8px;
          border-radius: 50%;
          transform: translateX(-50%);
          background: #282125;
          box-shadow: inset 0 0 0 2px #3d3439;
        }
        .signals { display: flex; align-items: center; gap: 4px; }
        .signal { font-size: 10px; letter-spacing: -2px; }
        .wifi { font-size: 10px; transform: rotate(90deg); }
        .battery {
          width: 16px;
          height: 8px;
          border: 1.5px solid currentColor;
          border-radius: 2px;
          position: relative;
        }
        .battery::before { content: ""; position: absolute; inset: 1px 3px 1px 1px; background: currentColor; }
        .battery::after { content: ""; position: absolute; right: -3px; top: 2px; width: 2px; height: 4px; background: currentColor; }
        .viewport { position: absolute; inset: 30px 0 20px; overflow: hidden; }
        ::slotted([data-app-root]) { display: block; width: 100%; height: 100%; }
        .system-nav {
          position: absolute;
          z-index: 10;
          inset: auto 0 0;
          height: 20px;
          display: grid;
          place-items: center;
          background: var(--app-surface, #f9f6f4);
        }
        .gesture { width: 108px; height: 4px; border-radius: 999px; background: #21191d; opacity: 0.82; }
      </style>
      <div class="hardware">
        <div class="status" aria-hidden="true">
          <span>${time}</span>
          <span class="camera"></span>
          <span class="signals"><span class="signal">▂▄▆</span><span class="wifi">◔</span><span class="battery"></span></span>
        </div>
        <div class="viewport"><slot></slot></div>
        <div class="system-nav" aria-hidden="true"><span class="gesture"></span></div>
      </div>
    `;
  }
}

customElements.define("android-frame", AndroidFrame);

