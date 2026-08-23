/**
 * IOE Electrical Circuits & Machines - Minimalist Monochrome Web App
 * Core Application Engine, Sidebar Drawer, and KaTeX Pipeline
 */

let appData = null;
let currentQuestionId = null;
let currentYearFilter = "ALL";
let bookmarks = new Set(JSON.parse(localStorage.getItem('ecm_bookmarks') || '[]'));
let currentTheme = localStorage.getItem('ecm_theme') || 'light';

// Clean Topic Map
const CHAPTER_TOPICS = {
  1: "DC Network Analysis (Mesh & Nodal)",
  2: "First-Order Transients (RL & RC)",
  3: "Second-Order Transients (RLC)",
  4: "Laplace Transform Applications",
  5: "Bode Plots & Frequency Response",
  6: "Two-Port Network Parameters",
  7: "Electromagnetism & Magnetic Circuits",
  8: "Transformers (1-Phase & 3-Phase)",
  9: "DC & Induction Machines",
  10: "Grading Pitfalls & Short Notes"
};

// Engineering Formula Database
const FORMULA_SHEET = {
  "Laplace Transform Pairs & Models": [
    { name: "Step Function", formula: "\\mathcal{L}\\{u(t)\\} = \\frac{1}{s}" },
    { name: "Exponential Decay", formula: "\\mathcal{L}\\{e^{-at}\\} = \\frac{1}{s+a}" },
    { name: "Sinusoid Wave", formula: "\\mathcal{L}\\{\\sin(\\omega t)\\} = \\frac{\\omega}{s^2 + \\omega^2}" },
    { name: "Cosinusoid Wave", formula: "\\mathcal{L}\\{\\cos(\\omega t)\\} = \\frac{s}{s^2 + \\omega^2}" },
    { name: "Damped Sinusoid", formula: "\\mathcal{L}\\{e^{-at}\\sin(\\omega t)\\} = \\frac{\\omega}{(s+a)^2 + \\omega^2}" },
    { name: "Damped Cosinusoid", formula: "\\mathcal{L}\\{e^{-at}\\cos(\\omega t)\\} = \\frac{s+a}{(s+a)^2 + \\omega^2}" },
    { name: "Inductor s-Domain Model", formula: "V_L(s) = sL I(s) - L i(0^+)" },
    { name: "Capacitor s-Domain Model", formula: "V_C(s) = \\frac{1}{sC} I(s) + \\frac{v_C(0^+)}{s}" }
  ],
  "Two-Port Network Matrices": [
    { name: "Z-Parameters (Open-Circuit)", formula: "\\begin{bmatrix} V_1 \\\\ V_2 \\end{bmatrix} = \\begin{bmatrix} Z_{11} & Z_{12} \\\\ Z_{21} & Z_{22} \\end{bmatrix} \\begin{bmatrix} I_1 \\\\ I_2 \\end{bmatrix}" },
    { name: "Y-Parameters (Short-Circuit)", formula: "\\begin{bmatrix} I_1 \\\\ I_2 \\end{bmatrix} = \\begin{bmatrix} Y_{11} & Y_{12} \\\\ Y_{21} & Y_{22} \\end{bmatrix} \\begin{bmatrix} V_1 \\\\ V_2 \\end{bmatrix}" },
    { name: "ABCD Transmission Parameters", formula: "\\begin{bmatrix} V_1 \\\\ I_1 \\end{bmatrix} = \\begin{bmatrix} A & B \\\\ C & D \\end{bmatrix} \\begin{bmatrix} V_2 \\\\ -I_2 \\end{bmatrix}" },
    { name: "Reciprocity Conditions", formula: "Z_{12} = Z_{21}, \\quad Y_{12} = Y_{21}, \\quad AD - BC = 1" },
    { name: "Symmetry Conditions", formula: "Z_{11} = Z_{22}, \\quad Y_{11} = Y_{22}, \\quad A = D" }
  ],
  "Electrical Machines & Magnetics": [
    { name: "DC Motor Torque", formula: "T = \\frac{1}{2\\pi} \\left(\\frac{P Z}{A}\\right) \\Phi I_a = k_t \\Phi I_a" },
    { name: "DC Generator Back EMF", formula: "E_b = \\frac{P \\Phi N Z}{60 A}" },
    { name: "Induction Motor Slip", formula: "s = \\frac{N_s - N}{N_s}, \\quad N_s = \\frac{120 f}{P}" },
    { name: "Rotor Frequency & EMF", formula: "f_r = s f, \\quad E_{2s} = s E_2" },
    { name: "Maximum Torque Condition", formula: "s_{mT} = \\frac{R_2}{X_2}, \\quad T_{\\max} = \\frac{3}{2\\omega_s} \\frac{V^2}{2 X_2}" },
    { name: "Magnetic Core Reluctance", formula: "\\mathcal{R} = \\frac{l}{\\mu_0 \\mu_r A}, \\quad \\text{MMF} = N I = \\Phi \\mathcal{R}" }
  ]
};

// Application Bootstrapping
document.addEventListener('DOMContentLoaded', async () => {
  applyTheme(currentTheme);
  await loadDatabase();
  setupEventListeners();
  setupKeyboardShortcuts();
  
  // Handle initial URL Hash Routing
  const hash = window.location.hash.replace('#', '');
  if (hash && findQuestionById(hash)) {
    navigateToQuestion(hash);
  } else if (appData && appData.chapters[0]?.questions[0]) {
    navigateToQuestion(appData.chapters[0].questions[0].id);
  }
});

// Load Question Database JSON
async function loadDatabase() {
  try {
    const res = await fetch('questions_data.json');
    if (!res.ok) throw new Error('Database load failed');
    appData = await res.json();
    renderSidebar();
    renderFormulaModal();
  } catch (err) {
    console.error(err);
    document.getElementById('main-content').innerHTML = `
      <div style="padding: 3rem; text-align: center;">
        <h2 style="font-size: 1.25rem; font-weight: 700; margin-bottom: 0.5rem;">Database Connection Error</h2>
        <p style="color: var(--text-muted);">Please verify that the local HTTP server is running (e.g. <code>python3 -m http.server 8080</code>).</p>
      </div>
    `;
  }
}

// Render Sidebar Navigation
function renderSidebar() {
  const navContainer = document.getElementById('sidebar-nav-list');
  if (!navContainer || !appData) return;
  
  navContainer.innerHTML = '';
  
  appData.chapters.forEach(ch => {
    // Filter questions based on selected year
    const filteredQuestions = ch.questions.filter(q => {
      if (currentYearFilter === 'ALL') return true;
      return q.exam_year.toUpperCase().includes(currentYearFilter);
    });
    
    if (filteredQuestions.length === 0 && currentYearFilter !== 'ALL') return;
    
    const isCurrentChapter = ch.questions.some(q => q.id === currentQuestionId);
    const chapterTopic = CHAPTER_TOPICS[ch.chapter_num] || ch.chapter_title;
    
    const chapterItem = document.createElement('div');
    chapterItem.className = 'nav-chapter-item';
    
    chapterItem.innerHTML = `
      <button class="nav-chapter-header ${isCurrentChapter ? 'active' : ''}" data-ch="${ch.chapter_num}">
        <span>Q${ch.chapter_num}: ${chapterTopic}</span>
        <span class="chapter-count-tag">${filteredQuestions.length}</span>
      </button>
      <div class="nav-sub-list" id="sub-list-ch${ch.chapter_num}" style="display: ${isCurrentChapter ? 'flex' : 'none'};">
        ${filteredQuestions.map(q => {
          const isBookmarked = bookmarks.has(q.id);
          const isActive = q.id === currentQuestionId;
          return `
            <button class="nav-sub-btn ${isActive ? 'active' : ''}" data-id="${q.id}">
              <span>
                ${isBookmarked ? '★ ' : ''}${q.exam_year}
              </span>
              <span class="nav-sub-badge">[${q.marks || q.q_num}]</span>
            </button>
          `;
        }).join('')}
      </div>
    `;
    
    navContainer.appendChild(chapterItem);
  });
  
  // Attach Chapter Header Click Handlers
  navContainer.querySelectorAll('.nav-chapter-header').forEach(btn => {
    btn.addEventListener('click', () => {
      const chNum = parseInt(btn.getAttribute('data-ch'), 10);
      const subList = document.getElementById(`sub-list-ch${chNum}`);
      const ch = appData.chapters.find(c => c.chapter_num === chNum);
      
      // Toggle Sub-list
      if (subList) {
        const isHidden = subList.style.display === 'none';
        subList.style.display = isHidden ? 'flex' : 'none';
      }
      
      // If clicking chapter, navigate directly to first question of chapter
      if (ch && ch.questions.length > 0) {
        navigateToQuestion(ch.questions[0].id);
      }
    });
  });
  
  // Attach Sub-question Click Handlers
  navContainer.querySelectorAll('.nav-sub-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const qId = btn.getAttribute('data-id');
      navigateToQuestion(qId);
      closeSidebarDrawer();
    });
  });
}

// Navigate to Specific Question
function navigateToQuestion(qId) {
  currentQuestionId = qId;
  window.location.hash = qId;
  
  const question = findQuestionById(qId);
  if (!question) return;
  
  renderSidebar();
  renderQuestionArticle(question);
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Render Main Question View
function renderQuestionArticle(q) {
  const main = document.getElementById('main-content');
  if (!main) return;
  
  const topicTitle = CHAPTER_TOPICS[q.ch_num] || `Question ${q.ch_num}`;
  const isBookmarked = bookmarks.has(q.id);
  
  // Calculate Prev / Next
  const allQs = [];
  appData.chapters.forEach(ch => ch.questions.forEach(item => allQs.push(item)));
  const currentIndex = allQs.findIndex(item => item.id === q.id);
  const prevQ = currentIndex > 0 ? allQs[currentIndex - 1] : null;
  const nextQ = currentIndex < allQs.length - 1 ? allQs[currentIndex + 1] : null;
  
  main.innerHTML = `
    <!-- Minimalist Breadcrumb -->
    <div class="breadcrumb-trail">
      <span>Question ${q.ch_num}</span>
      <span>/</span>
      <span>${q.exam_year}</span>
      <span>/</span>
      <span class="active">${q.q_num}</span>
    </div>
    
    <!-- Question Header -->
    <header class="article-header">
      <h1 class="article-title">${q.sub_header || `${q.exam_year} — ${q.q_num}`}</h1>
      <div class="article-tags-row">
        <div class="meta-tags">
          <span class="tag-badge">[${q.exam_year.toUpperCase()}]</span>
          <span class="tag-badge">[${q.marks.toUpperCase() || 'FULL WEIGHTAGE'}]</span>
          <span class="tag-badge">[${topicTitle.toUpperCase()}]</span>
        </div>
        <div class="article-actions">
          <button class="icon-action-btn" id="bookmark-btn" title="${isBookmarked ? 'Remove Bookmark' : 'Bookmark Question'}">
            ${isBookmarked ? '★' : '☆'}
          </button>
          <button class="icon-action-btn" id="copy-btn" title="Copy Direct URL">
            ⎘
          </button>
          <button class="icon-action-btn" id="print-btn" title="Print Problem & Solution">
            ⎙
          </button>
        </div>
      </div>
    </header>
    
    <!-- Problem Statement (Minimalist Academic Frame) -->
    <section class="problem-card">
      <div class="problem-card-label">
        <span>Problem Statement</span>
        <span>${q.marks || ''}</span>
      </div>
      <div class="problem-card-text">
        ${q.problem_statement_html || q.problem_statement}
      </div>
      
      <!-- Circuit Diagram Schematic -->
      ${q.circuit_image ? `
        <div class="diagram-frame" onclick="openLightbox('${q.circuit_image}', 'Circuit Diagram: ${q.exam_year} ${q.q_num}')">
          <img src="${q.circuit_image}" alt="Circuit Schematic" class="diagram-image" />
          <div class="diagram-caption-text">[CLICK SCHEMATIC TO ZOOM]</div>
        </div>
      ` : ''}
      
      <!-- Vector Plot -->
      ${q.figure_image ? `
        <div class="diagram-frame" onclick="openLightbox('${q.figure_image}', 'Characteristic Curve: ${q.exam_year} ${q.q_num}')">
          <img src="${q.figure_image}" alt="Vector Characteristic Plot" class="diagram-image" />
          <div class="diagram-caption-text">[CLICK PLOT TO ZOOM]</div>
        </div>
      ` : ''}
    </section>
    
    <!-- Step-by-Step Solution -->
    <section class="solution-section">
      <h2 class="solution-section-title">Step-by-Step Derivation</h2>
      <div class="solution-body">
        ${q.solution_html || q.raw_solution}
      </div>
      
      <!-- Boxed Final Result -->
      ${q.final_answer ? `
        <div class="boxed-final-answer">
          <div class="boxed-final-answer-label">Final Verified Result</div>
          <div class="boxed-final-answer-content">
            ${q.final_answer_html || `$$${q.final_answer}$$`}
          </div>
        </div>
      ` : ''}
    </section>
    
    <!-- Bottom Pagination -->
    <nav class="bottom-pagination">
      <button class="page-btn" id="prev-btn" ${!prevQ ? 'disabled' : ''}>
        ← Prev (${prevQ ? prevQ.exam_year : 'Start'})
      </button>
      <button class="page-btn" id="next-btn" ${!nextQ ? 'disabled' : ''}>
        Next (${nextQ ? nextQ.exam_year : 'End'}) →
      </button>
    </nav>
  `;
  
  // Attach Action Button Listeners
  document.getElementById('bookmark-btn')?.addEventListener('click', () => toggleBookmark(q.id));
  document.getElementById('copy-btn')?.addEventListener('click', copyDirectLink);
  document.getElementById('print-btn')?.addEventListener('click', () => window.print());
  
  document.getElementById('prev-btn')?.addEventListener('click', () => {
    if (prevQ) navigateToQuestion(prevQ.id);
  });
  document.getElementById('next-btn')?.addEventListener('click', () => {
    if (nextQ) navigateToQuestion(nextQ.id);
  });
  
  // Run KaTeX Typesetting on Newly Inserted Math
  typesetMath();
}

// KaTeX Typesetting Engine
function typesetMath() {
  if (window.renderMathInElement) {
    window.renderMathInElement(document.getElementById('main-content'), {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false }
      ],
      throwOnError: false
    });
  }
}

// Find Question Object by ID
function findQuestionById(id) {
  if (!appData) return null;
  for (const ch of appData.chapters) {
    for (const q of ch.questions) {
      if (q.id === id) return q;
    }
  }
  return null;
}

// Bookmark Toggle
function toggleBookmark(qId) {
  if (bookmarks.has(qId)) {
    bookmarks.delete(qId);
    showToast('Removed from bookmarks');
  } else {
    bookmarks.add(qId);
    showToast('Question bookmarked');
  }
  localStorage.setItem('ecm_bookmarks', JSON.stringify(Array.from(bookmarks)));
  renderSidebar();
  const btn = document.getElementById('bookmark-btn');
  if (btn) {
    btn.innerHTML = bookmarks.has(qId) ? '★' : '☆';
  }
}

// Copy Direct URL
function copyDirectLink() {
  navigator.clipboard.writeText(window.location.href);
  showToast('Direct link copied to clipboard');
}

// Toast Alert
function showToast(text) {
  let shelf = document.querySelector('.toast-shelf');
  if (!shelf) {
    shelf = document.createElement('div');
    shelf.className = 'toast-shelf';
    document.body.appendChild(shelf);
  }
  const pill = document.createElement('div');
  pill.className = 'toast-pill';
  pill.innerText = text;
  shelf.appendChild(pill);
  setTimeout(() => pill.remove(), 2500);
}

// Theme Engine (Pure Black & White)
function applyTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('ecm_theme', theme);
  const icon = document.getElementById('theme-icon');
  if (icon) icon.innerText = theme === 'dark' ? 'LIGHT' : 'DARK';
}

function toggleTheme() {
  applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
}

// Sidebar Drawer Control (Robust Mobile & Desktop)
function openSidebarDrawer() {
  document.getElementById('app-sidebar')?.classList.add('open');
  document.getElementById('sidebar-backdrop')?.classList.add('active');
  document.body.classList.add('no-scroll');
}

function closeSidebarDrawer() {
  document.getElementById('app-sidebar')?.classList.remove('open');
  document.getElementById('sidebar-backdrop')?.classList.remove('active');
  document.body.classList.remove('no-scroll');
}

function toggleSidebarDrawer() {
  const sidebar = document.getElementById('app-sidebar');
  if (sidebar?.classList.contains('open')) {
    closeSidebarDrawer();
  } else {
    openSidebarDrawer();
  }
}

// Event Listeners Setup
function setupEventListeners() {
  // Sidebar Toggle Buttons
  document.getElementById('sidebar-toggle-btn')?.addEventListener('click', toggleSidebarDrawer);
  document.getElementById('mobile-menu-btn')?.addEventListener('click', toggleSidebarDrawer);
  document.getElementById('sidebar-close-btn')?.addEventListener('click', closeSidebarDrawer);
  document.getElementById('sidebar-backdrop')?.addEventListener('click', closeSidebarDrawer);
  
  // Year Filter Chips
  document.querySelectorAll('.filter-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
      chip.classList.add('active');
      currentYearFilter = chip.getAttribute('data-year');
      renderSidebar();
    });
  });
  
  // Theme Switcher
  document.getElementById('theme-toggle-btn')?.addEventListener('click', toggleTheme);
  
  // Search Modal
  document.getElementById('search-trigger-btn')?.addEventListener('click', openSearchModal);
  document.getElementById('mobile-search-btn')?.addEventListener('click', openSearchModal);
  document.getElementById('search-close-btn')?.addEventListener('click', closeSearchModal);
  document.getElementById('search-modal-backdrop')?.addEventListener('click', (e) => {
    if (e.target.id === 'search-modal-backdrop') closeSearchModal();
  });
  document.getElementById('search-input-field')?.addEventListener('input', handleSearchQuery);
  
  // Formula Modal
  document.getElementById('formula-trigger-btn')?.addEventListener('click', openFormulaModal);
  document.getElementById('mobile-formula-btn')?.addEventListener('click', openFormulaModal);
  document.getElementById('formula-close-btn')?.addEventListener('click', closeFormulaModal);
  document.getElementById('formula-modal-backdrop')?.addEventListener('click', (e) => {
    if (e.target.id === 'formula-modal-backdrop') closeFormulaModal();
  });
  
  // Lightbox Close
  document.getElementById('lightbox-backdrop')?.addEventListener('click', (e) => {
    if (e.target.id === 'lightbox-backdrop' || e.target.id === 'lightbox-close-btn') {
      document.getElementById('lightbox-backdrop').classList.remove('active');
    }
  });
  
  // Mobile Bottom Bar Pagination
  document.getElementById('mobile-prev-btn')?.addEventListener('click', () => {
    document.getElementById('prev-btn')?.click();
  });
  document.getElementById('mobile-next-btn')?.addEventListener('click', () => {
    document.getElementById('next-btn')?.click();
  });
}

// Keyboard Shortcuts
function setupKeyboardShortcuts() {
  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
    
    if (e.key === '/' || ((e.metaKey || e.ctrlKey) && e.key === 'k')) {
      e.preventDefault();
      openSearchModal();
    } else if (e.key === 't') {
      toggleTheme();
    } else if (e.key === 'f') {
      openFormulaModal();
    } else if (e.key === 'm') {
      toggleSidebarDrawer();
    } else if (e.key === 'Escape') {
      closeSearchModal();
      closeFormulaModal();
      closeSidebarDrawer();
      document.getElementById('lightbox-backdrop')?.classList.remove('active');
    } else if (e.key === 'j' || e.key === 'ArrowRight') {
      document.getElementById('next-btn')?.click();
    } else if (e.key === 'k' || e.key === 'ArrowLeft') {
      document.getElementById('prev-btn')?.click();
    }
  });
}

// Search Modal Functionality
function openSearchModal() {
  const modal = document.getElementById('search-modal-backdrop');
  if (modal) {
    modal.classList.add('active');
    const input = document.getElementById('search-input-field');
    input.value = '';
    input.focus();
    renderSearchResults('');
  }
}

function closeSearchModal() {
  document.getElementById('search-modal-backdrop')?.classList.remove('active');
}

function handleSearchQuery(e) {
  renderSearchResults(e.target.value.trim().toLowerCase());
}

function renderSearchResults(query) {
  const container = document.getElementById('search-results-list');
  if (!container || !appData) return;
  
  if (!query) {
    container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 1.5rem; font-size: 0.85rem;">Type topic, year, formula, or question keyword...</div>`;
    return;
  }
  
  const matches = [];
  appData.chapters.forEach(ch => {
    ch.questions.forEach(q => {
      const matchHeader = q.sub_header.toLowerCase().includes(query);
      const matchYear = q.exam_year.toLowerCase().includes(query);
      const matchProblem = q.problem_statement.toLowerCase().includes(query);
      const matchSolution = q.raw_solution.toLowerCase().includes(query);
      const matchTopic = (CHAPTER_TOPICS[q.ch_num] || '').toLowerCase().includes(query);
      
      if (matchHeader || matchYear || matchProblem || matchSolution || matchTopic) {
        matches.push(q);
      }
    });
  });
  
  if (matches.length === 0) {
    container.innerHTML = `<div style="text-align: center; color: var(--text-muted); padding: 1.5rem; font-size: 0.85rem;">No results found for "${query}"</div>`;
    return;
  }
  
  container.innerHTML = matches.slice(0, 10).map(q => `
    <div class="search-result-row" onclick="navigateToQuestion('${q.id}'); closeSearchModal();">
      <div class="search-row-title">${q.sub_header}</div>
      <div class="search-row-meta">${CHAPTER_TOPICS[q.ch_num] || ''} · [${q.marks || ''}]</div>
    </div>
  `).join('');
}

// Formula Reference Modal Functionality
function openFormulaModal() {
  const modal = document.getElementById('formula-modal-backdrop');
  if (modal) {
    modal.classList.add('active');
    if (window.renderMathInElement) {
      window.renderMathInElement(modal, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false }
        ],
        throwOnError: false
      });
    }
  }
}

function closeFormulaModal() {
  document.getElementById('formula-modal-backdrop')?.classList.remove('active');
}

function renderFormulaModal() {
  const body = document.getElementById('formula-modal-body');
  if (!body) return;
  
  let html = '';
  for (const [section, items] of Object.entries(FORMULA_SHEET)) {
    html += `
      <h3 style="font-size: 0.95rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; font-family: var(--font-mono); margin: 1.25rem 0 0.5rem; border-bottom: 1px solid var(--border-light); padding-bottom: 0.25rem;">
        ${section}
      </h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0.6rem; margin-bottom: 1.25rem;">
        ${items.map(f => `
          <div style="border: 1px solid var(--border-light); padding: 0.75rem; border-radius: 4px; background: var(--bg-subtle);">
            <div style="font-size: 0.75rem; font-family: var(--font-mono); font-weight: 700; color: var(--text-muted); margin-bottom: 0.25rem;">${f.name}</div>
            <div style="font-size: 0.9rem;">$$${f.formula}$$</div>
          </div>
        `).join('')}
      </div>
    `;
  }
  body.innerHTML = html;
}

// Lightbox Zoom Functionality
function openLightbox(src, title) {
  const backdrop = document.getElementById('lightbox-backdrop');
  const img = document.getElementById('lightbox-image');
  const cap = document.getElementById('lightbox-caption');
  if (backdrop && img) {
    img.src = src;
    if (cap) cap.innerText = title;
    backdrop.classList.add('active');
  }
}
