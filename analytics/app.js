/**
 * Arya's Request Inspector & Traffic Analytics Engine
 * Real-time Auto-Polling, KPI Calculations, Category Filtering, and Live Stream Rendering
 */

let allRequests = [];
let activeCategory = 'ALL';
let searchQuery = '';
let autoPollTimer = null;
let isAutoPolling = true;
let currentTheme = localStorage.getItem('inspector_theme') || 'light';

const SUBJECT_COLORS = {
  "Digital Logic": "#059669",
  "Electronic Devices & Circuits": "#0284c7",
  "Engineering Chemistry": "#0d9488",
  "Engineering Mathematics II": "#7c3aed",
  "Electrical Circuits & Machines": "#d97706",
  "Object Oriented Programming": "#e11d48"
};

document.addEventListener('DOMContentLoaded', () => {
  applyTheme(currentTheme);
  fetchLiveRequests();
  startAutoPolling();
});

// Fetch Live Data from Server API
async function fetchLiveRequests() {
  const refreshLabel = document.getElementById('refresh-label');
  if (refreshLabel) refreshLabel.innerText = 'SYNCING...';

  try {
    const res = await fetch('/api/requests', { cache: 'no-store' });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    
    allRequests = data.requests || [];
    updateDashboardUI(data);
    fetchReviewsAnalytics();
  } catch (err) {
    console.warn('Failed to fetch from /api/requests, falling back to static log parsing...', err);
  } finally {
    if (refreshLabel) refreshLabel.innerText = 'REFRESH';
    const lastSyncEl = document.getElementById('last-updated-text');
    if (lastSyncEl) {
      const now = new Date().toLocaleTimeString();
      lastSyncEl.innerText = `Last synchronized: ${now}`;
    }
  }
}

async function fetchReviewsAnalytics() {
  try {
    const res = await fetch('/api/reviews', { cache: 'no-store' });
    if (!res.ok) return;
    const data = await res.json();
    const revCount = data.total_reviews || 0;
    const avg = data.average_rating || 5.0;

    const revTotalEl = document.getElementById('kpi-total-reviews');
    const badgeEl = document.getElementById('kpi-reviews-badge');
    const subtextEl = document.getElementById('kpi-reviews-subtext');

    if (revTotalEl) revTotalEl.innerText = revCount;
    if (badgeEl) badgeEl.innerText = `★ ${avg.toFixed(1)}`;
    if (subtextEl) subtextEl.innerText = `${revCount} verified testimonials`;
  } catch (e) {}
}

// Update KPIs, Charts, Unique Visitors, and Table
function updateDashboardUI(data) {
  // 1. KPIs
  const uniqueEl = document.getElementById('kpi-unique-visitors');
  const totalEl = document.getElementById('kpi-total-requests');
  const viewsEl = document.getElementById('kpi-page-views');
  const downloadsEl = document.getElementById('kpi-pdf-downloads');
  const successEl = document.getElementById('kpi-success-rate');
  const errorsSubEl = document.getElementById('kpi-errors-count');

  if (uniqueEl) uniqueEl.innerText = data.unique_visitors_count || 1;
  if (totalEl) totalEl.innerText = data.total_requests;
  if (viewsEl) viewsEl.innerText = data.page_views;
  if (downloadsEl) downloadsEl.innerText = data.pdf_downloads;

  const total = data.total_requests || 1;
  const errors = data.errors_count || 0;
  const successRate = Math.max(0, Math.min(100, Math.round(((total - errors) / total) * 100)));
  if (successEl) successEl.innerText = `${successRate}%`;
  if (errorsSubEl) errorsSubEl.innerText = `${errors} error${errors === 1 ? '' : 's'} logged`;

  // 2. Unique Visitors Window List
  renderUniqueVisitors(data.unique_visitors_list || [], data.unique_visitors_count || 1);

  // 3. Subject Downloads Breakdown
  renderSubjectBreakdown(data.subject_downloads || {}, data.pdf_downloads || 0);

  // 4. Traffic Composition
  renderTrafficComposition(data);

  // 5. Filter & Render Logs Table
  renderFilteredTable();
}

function renderUniqueVisitors(visitors, totalCount) {
  const container = document.getElementById('visitors-list-wrap');
  const headerCount = document.getElementById('unique-visitors-header-count');
  if (!container) return;

  if (headerCount) headerCount.innerText = `${totalCount} UNIQUE PEOPLE`;

  if (visitors.length === 0) {
    container.innerHTML = `<div class="visitor-item-card"><span class="visitor-time">No visitor records found.</span></div>`;
    return;
  }

  container.innerHTML = visitors.map(v => {
    return `
      <div class="visitor-item-card mono">
        <div class="visitor-left">
          <div class="visitor-ip-row">
            <span>👤 ${v.ip}</span>
            <span class="visitor-device-badge">${v.device}</span>
          </div>
          <span class="visitor-time">First seen: ${v.first_seen} · Last: ${v.last_seen}</span>
        </div>
        <div class="visitor-right">
          <span class="visitor-stats-tag">${v.page_views} views · ${v.downloads} dls</span>
          <span class="visitor-hits">${v.total_requests} total hits</span>
        </div>
      </div>
    `;
  }).join('');
}

function renderSubjectBreakdown(subjectMap, totalDownloads) {
  const container = document.getElementById('subject-bars-list');
  const tag = document.getElementById('total-downloads-tag');
  if (!container) return;

  if (tag) tag.innerText = `${totalDownloads} TOTAL DOWNLOADS`;

  const sortedSubjects = Object.entries(subjectMap).sort((a, b) => b[1] - a[1]);

  container.innerHTML = sortedSubjects.map(([name, count]) => {
    const percent = totalDownloads > 0 ? Math.round((count / totalDownloads) * 100) : 0;
    const color = SUBJECT_COLORS[name] || '#10b981';

    return `
      <div class="subject-bar-row">
        <div class="bar-labels-row">
          <span>${name}</span>
          <span class="mono">${count} downloads (${percent}%)</span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" style="width: ${percent}%; --bar-color: ${color};"></div>
        </div>
      </div>
    `;
  }).join('');
}

function renderTrafficComposition(data) {
  const container = document.getElementById('composition-list');
  if (!container) return;

  const total = data.total_requests || 1;
  const items = [
    { label: "PDF Documents & Solutions", count: data.pdf_downloads, color: "#7c3aed" },
    { label: "Portal Page Views", count: data.page_views, color: "#10b981" },
    { label: "Static JS/CSS Assets", count: data.assets_count, color: "#0284c7" },
    { label: "Errors / 404 Requests", count: data.errors_count, color: "#e11d48" }
  ];

  container.innerHTML = items.map(item => {
    const percent = Math.round((item.count / total) * 100);
    return `
      <div class="comp-row">
        <div class="bar-labels-row">
          <span>${item.label}</span>
          <span class="mono">${item.count} hits (${percent}%)</span>
        </div>
        <div class="bar-track">
          <div class="bar-fill" style="width: ${percent}%; --bar-color: ${item.color};"></div>
        </div>
      </div>
    `;
  }).join('');
}

// Table Filter and Render
function renderFilteredTable() {
  const tbody = document.getElementById('requests-table-body');
  const countBadge = document.getElementById('filtered-count-badge');
  if (!tbody) return;

  let filtered = allRequests;

  // Filter by category
  if (activeCategory !== 'ALL') {
    filtered = filtered.filter(r => r.category === activeCategory);
  }

  // Filter by search query
  if (searchQuery.trim()) {
    const q = searchQuery.toLowerCase();
    filtered = filtered.filter(r =>
      r.path.toLowerCase().includes(q) ||
      r.subject.toLowerCase().includes(q) ||
      r.ip.toLowerCase().includes(q) ||
      r.timestamp.toLowerCase().includes(q)
    );
  }

  if (countBadge) countBadge.innerText = `${filtered.length} ENTRIES`;

  if (filtered.length === 0) {
    tbody.innerHTML = `
      <tr>
        <td colspan="7" class="table-loading">No matching requests found.</td>
      </tr>
    `;
    return;
  }

  tbody.innerHTML = filtered.map(r => {
    return `
      <tr>
        <td><strong>#${r.id}</strong></td>
        <td>${r.timestamp}</td>
        <td><span class="method-badge">${r.method}</span></td>
        <td style="max-width: 320px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${r.path}">
          <a href="${r.path}" target="_blank" style="text-decoration: underline;">${r.path}</a>
        </td>
        <td>
          <span class="cat-badge cat-${r.category}">${r.subject}</span>
        </td>
        <td><span class="status-badge status-${r.status}">${r.status}</span></td>
        <td>${r.ip}</td>
      </tr>
    `;
  }).join('');
}

// Category Filter Switch
function setCategoryFilter(category) {
  activeCategory = category;
  document.querySelectorAll('.cat-pill').forEach(btn => {
    btn.classList.toggle('active', btn.innerText.includes(category) || (category === 'ALL' && btn.innerText === 'ALL'));
  });
  renderFilteredTable();
}

function handleFilterChange() {
  const input = document.getElementById('log-search-input');
  if (input) searchQuery = input.value;
  renderFilteredTable();
}

// Auto-Polling Interval Control
function startAutoPolling() {
  if (autoPollTimer) clearInterval(autoPollTimer);
  autoPollTimer = setInterval(fetchLiveRequests, 2000);
}

function toggleAutoPolling() {
  isAutoPolling = !isAutoPolling;
  const btn = document.getElementById('auto-poll-btn');
  const label = document.getElementById('auto-poll-text');
  const pill = document.getElementById('live-polling-text');

  if (isAutoPolling) {
    startAutoPolling();
    if (btn) btn.classList.add('active');
    if (label) label.innerText = 'AUTO (2s)';
    if (pill) pill.innerText = 'LIVE STREAMING';
  } else {
    if (autoPollTimer) clearInterval(autoPollTimer);
    if (btn) btn.classList.remove('active');
    if (label) label.innerText = 'PAUSED';
    if (pill) pill.innerText = 'PAUSED';
  }
}

// Theme Switcher
function applyTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  try { localStorage.setItem('inspector_theme', theme); } catch (e) {}
  const btnText = document.getElementById('theme-toggle-text');
  if (btnText) btnText.innerText = theme === 'light' ? 'DARK' : 'LIGHT';
}

function toggleTheme() {
  applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
}
