/**
 * IOE Engineering Subject PDF Portal
 * Core Client Logic, Search Engine & In-Browser PDF Previewer
 */

const SUBJECTS_DATA = [
  {
    id: "ecm",
    title: "Electrical Circuits & Machines",
    code: "EE 154 / ENEE 154",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    pages: "55 Pages",
    fileSize: "678 KB",
    pdfUrl: "downloads/electrical_circuits_and_machines_master_solutions.pdf",
    featured: true,
    desc: "Complete 55-page master solutions book (2083 Baishakh to 2081 Ashwin) with 10 redone Circuitikz schematics, Laplace transforms, Bode plots, Two-port networks, Transformers, and AC/DC machines.",
    tags: ["55 PAGES", "VERIFIED SOLUTIONS", "MESH & NODAL", "BODE PLOTS", "2-PORT NETWORKS", "AC/DC MACHINES"]
  },
  {
    id: "math",
    title: "Engineering Mathematics",
    code: "SH 151",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    pages: "Comprehensive Packet",
    fileSize: "PDF Ready",
    pdfUrl: "downloads/engineering_mathematics_ii_master.pdf",
    featured: false,
    desc: "Differential Equations, Partial Differential Equations, Linear Algebra, Multiple Integrals, Vector Calculus, and 3D Analytical Geometry with formula reference sheets.",
    tags: ["CALCULUS", "DIFF EQUATIONS", "LINEAR ALGEBRA", "VECTOR CALCULUS", "FORMULA SHEET"]
  },
  {
    id: "dl",
    title: "Digital Logic",
    code: "EX 152 / CT 152",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    pages: "Comprehensive Packet",
    fileSize: "PDF Ready",
    pdfUrl: "downloads/digital_logic_master.pdf",
    featured: false,
    desc: "Number Systems & Codes, Boolean Algebra & K-Maps, Combinational Logic Circuits (Mux/Demux/Encoders), Sequential Circuits, Flip-Flops, Counters, Registers, and Synchronous FSM Design.",
    tags: ["BOOLEAN ALGEBRA", "K-MAPS", "COMBINATIONAL", "SEQUENTIAL", "COUNTERS & FSM"]
  },
  {
    id: "oop",
    title: "Object Oriented Programming",
    code: "CT 153",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    pages: "Comprehensive Packet",
    fileSize: "PDF Ready",
    pdfUrl: "downloads/object_oriented_programming_master.pdf",
    featured: false,
    desc: "C++ Object Oriented Programming, Classes & Objects, Constructor Overloading, Operator Overloading, Inheritance Hierarchies, Virtual Functions, Polymorphism, Templates, and File Handling.",
    tags: ["C++ PROGRAMMING", "OPERATOR OVERLOADING", "INHERITANCE", "POLYMORPHISM", "FILE I/O"]
  },
  {
    id: "edc",
    title: "Electronic Devices & Circuits",
    code: "EX 151",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    pages: "Comprehensive Packet",
    fileSize: "PDF Ready",
    pdfUrl: "downloads/electronic_devices_and_circuits_master.pdf",
    featured: false,
    desc: "Semiconductor Physics, PN Junction Diodes, Zener Regulators, BJT Small Signal Analysis, JFET & MOSFET Amplifiers, Frequency Response, Operational Amplifiers (Op-Amps), and Feedback Oscillators.",
    tags: ["SEMICONDUCTORS", "BJT AMPLIFIERS", "MOSFET", "OP-AMPS", "FREQUENCY RESPONSE"]
  },
  {
    id: "chem",
    title: "Engineering Chemistry",
    code: "SH 153",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    pages: "Comprehensive Packet",
    fileSize: "PDF Ready",
    pdfUrl: "downloads/engineering_chemistry_master.pdf",
    featured: false,
    desc: "Electrochemistry & Batteries, Corrosion & its Prevention, Synthetic Polymers, Water Quality Parameters & Treatment, Phase Rule & Phase Diagrams, Fuels, and Instrumental Analytical Methods.",
    tags: ["ELECTROCHEMISTRY", "CORROSION", "POLYMERS", "WATER TREATMENT", "PHASE RULE"]
  }
];

let currentTheme = localStorage.getItem('ecm_portal_theme') || 'light';

document.addEventListener('DOMContentLoaded', () => {
  applyTheme(currentTheme);
  renderSubjectSlots(SUBJECTS_DATA);
  setupListeners();
});

// Render Subject Cards
function renderSubjectSlots(subjects) {
  const container = document.getElementById('subject-grid');
  const countEl = document.getElementById('slots-count');
  if (!container) return;
  
  if (countEl) countEl.innerText = `${subjects.length} SUBJECTS AVAILABLE`;
  
  if (subjects.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 3rem; text-align: center; color: var(--text-muted); font-family: var(--font-mono);">
        No subjects found matching your query.
      </div>
    `;
    return;
  }
  
  container.innerHTML = subjects.map(s => `
    <div class="subject-card ${s.featured ? 'featured' : ''}" id="card-${s.id}">
      <div>
        <div class="card-top-meta">
          <span class="course-code-badge">${s.code}</span>
          ${s.featured ? '<span class="featured-flag">55-PAGE MASTER BOOK</span>' : `<span class="mono" style="font-size:0.75rem; color:var(--text-muted);">${s.semester}</span>`}
        </div>
        
        <h2 class="subject-title">${s.title}</h2>
        <p class="subject-desc">${s.desc}</p>
        
        <div class="subject-tags">
          ${s.tags.map(t => `<span class="card-tag">${t}</span>`).join('')}
        </div>
      </div>
      
      <div class="card-actions-row">
        <a href="${s.pdfUrl}" class="btn-download-primary" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_IOE.pdf">
          <span>↓ DOWNLOAD PDF</span>
        </a>
        <button class="btn-preview-secondary" onclick="openPdfModal('${s.pdfUrl}', '${s.title} (${s.code})')" title="Preview in browser">
          <span>PREVIEW</span>
        </button>
      </div>
    </div>
  `).join('');
}

// Live Search Filter
function handleSearch(query) {
  const q = query.trim().toLowerCase();
  if (!q) {
    renderSubjectSlots(SUBJECTS_DATA);
    return;
  }
  
  const filtered = SUBJECTS_DATA.filter(s => {
    return s.title.toLowerCase().includes(q) ||
           s.code.toLowerCase().includes(q) ||
           s.desc.toLowerCase().includes(q) ||
           s.tags.some(t => t.toLowerCase().includes(q));
  });
  
  renderSubjectSlots(filtered);
}

// In-App PDF Previewer Modal
function openPdfModal(url, title) {
  const modal = document.getElementById('pdf-modal-backdrop');
  const frame = document.getElementById('pdf-iframe');
  const titleEl = document.getElementById('pdf-modal-title');
  const downloadLink = document.getElementById('modal-download-btn');
  
  if (modal && frame) {
    if (titleEl) titleEl.innerText = title;
    if (downloadLink) downloadLink.href = url;
    frame.src = url;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
}

function closePdfModal() {
  const modal = document.getElementById('pdf-modal-backdrop');
  const frame = document.getElementById('pdf-iframe');
  if (modal) {
    modal.classList.remove('open');
    if (frame) frame.src = '';
    document.body.style.overflow = '';
  }
}

// Theme Switcher
function applyTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('ecm_portal_theme', theme);
  const btnText = document.getElementById('theme-toggle-text');
  if (btnText) btnText.innerText = theme === 'dark' ? 'LIGHT MODE' : 'DARK MODE';
}

function toggleTheme() {
  applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
}

// Event Listeners & Shortcuts
function setupListeners() {
  const searchInput = document.getElementById('search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => handleSearch(e.target.value));
  }
  
  document.getElementById('theme-toggle-btn')?.addEventListener('click', toggleTheme);
  document.getElementById('close-pdf-modal-btn')?.addEventListener('click', closePdfModal);
  
  document.getElementById('pdf-modal-backdrop')?.addEventListener('click', (e) => {
    if (e.target.id === 'pdf-modal-backdrop') closePdfModal();
  });
  
  // Keyboard Shortcuts
  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      if (e.key === 'Escape') e.target.blur();
      return;
    }
    
    if (e.key === '/' || ((e.metaKey || e.ctrlKey) && e.key === 'k')) {
      e.preventDefault();
      searchInput?.focus();
    } else if (e.key === 't' || e.key === 'T') {
      toggleTheme();
    } else if (e.key === 'Escape') {
      closePdfModal();
    }
  });
}
