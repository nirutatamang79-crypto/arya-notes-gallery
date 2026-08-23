/**
 * IOE Engineering Subject Resource Portal
 * Core Client Logic, Categorized PDF Downloads & In-Browser Previewer
 */

const SUBJECTS_DATA = [
  {
    id: "ecm",
    title: "Electrical Circuits & Machines",
    code: "EE 154 / ENEE 154",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    solutionsPdf: "downloads/ecm/ecm_master_solutions_55_pages.pdf",
    questionsPdf: "downloads/ecm/ecm_questions.pdf",
    syllabusPdf: "downloads/ecm/ecm_syllabus.pdf",
    featured: true,
    solutionsLabel: "55-Page Master Book (Verified)",
    desc: "Complete 55-page master solutions book (2083 Baishakh to 2081 Ashwin) with 10 redone Circuitikz schematics, Laplace transforms, Bode plots, Two-port networks, Transformers, and AC/DC machines.",
    tags: ["55-PAGE MASTER BOOK", "VERIFIED SCHEMATICS", "LAPLACE TRANSFORMS", "BODE PLOTS", "AC/DC MACHINES"]
  },
  {
    id: "math",
    title: "Engineering Mathematics",
    code: "SH 151",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    solutionsPdf: "downloads/math/math_solutions.pdf",
    questionsPdf: "downloads/math/math_questions.pdf",
    syllabusPdf: "downloads/math/math_syllabus.pdf",
    featured: false,
    solutionsLabel: "Math Solutions PDF",
    desc: "Ordinary Differential Equations, Partial Differential Equations, Linear Algebra, Multiple Integrals, Vector Calculus, and 3D Analytical Geometry with step-by-step solutions.",
    tags: ["CALCULUS", "DIFF EQUATIONS", "LINEAR ALGEBRA", "VECTOR CALCULUS", "FORMULA SHEETS"]
  },
  {
    id: "dl",
    title: "Digital Logic",
    code: "EX 152 / CT 152",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    solutionsPdf: "downloads/dl/digital_logic_solutions.pdf",
    questionsPdf: "downloads/dl/digital_logic_questions.pdf",
    syllabusPdf: "downloads/dl/digital_logic_syllabus.pdf",
    featured: false,
    solutionsLabel: "Digital Logic Solutions PDF",
    desc: "Number Systems & Codes, Boolean Algebra & K-Maps, Combinational Logic Circuits (Mux/Demux/Encoders), Sequential Circuits, Flip-Flops, Counters, Registers, and Synchronous FSM Design.",
    tags: ["BOOLEAN ALGEBRA", "K-MAPS", "COMBINATIONAL", "SEQUENTIAL", "COUNTERS & FSM"]
  },
  {
    id: "oop",
    title: "Object Oriented Programming",
    code: "CT 153",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    solutionsPdf: "downloads/oop/oop_solutions.pdf",
    questionsPdf: "downloads/oop/oop_questions.pdf",
    syllabusPdf: "downloads/oop/oop_syllabus.pdf",
    featured: false,
    solutionsLabel: "OOP (C++) Solutions PDF",
    desc: "C++ Object Oriented Programming, Classes & Objects, Constructor Overloading, Operator Overloading, Inheritance Hierarchies, Virtual Functions, Polymorphism, Templates, and File Handling.",
    tags: ["C++ OOP", "OPERATOR OVERLOADING", "INHERITANCE", "POLYMORPHISM", "FILE STREAMS"]
  },
  {
    id: "edc",
    title: "Electronic Devices & Circuits",
    code: "EX 151",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    solutionsPdf: "downloads/edc/edc_solutions.pdf",
    questionsPdf: "downloads/edc/edc_questions.pdf",
    syllabusPdf: "downloads/edc/edc_syllabus.pdf",
    featured: false,
    solutionsLabel: "EDC Solutions PDF",
    desc: "Semiconductor Physics, PN Junction Diodes, Zener Regulators, BJT Small Signal Analysis, JFET & MOSFET Amplifiers, Frequency Response, Operational Amplifiers (Op-Amps), and Oscillators.",
    tags: ["SEMICONDUCTORS", "BJT AMPLIFIERS", "MOSFET", "OP-AMPS", "FREQUENCY RESPONSE"]
  },
  {
    id: "chem",
    title: "Engineering Chemistry",
    code: "SH 153",
    semester: "Semester I/II",
    marks: "80 Marks Weightage",
    solutionsPdf: "downloads/chem/chemistry_solutions.pdf",
    questionsPdf: "downloads/chem/chemistry_questions.pdf",
    syllabusPdf: "downloads/chem/chemistry_syllabus.pdf",
    featured: false,
    solutionsLabel: "Chemistry Solutions PDF",
    desc: "Electrochemistry & Batteries, Corrosion & its Prevention, Synthetic Polymers, Water Quality Parameters & Treatment, Phase Rule & Phase Diagrams, Fuels, and Analytical Methods.",
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
          <span class="mono" style="font-size:0.75rem; color:var(--text-muted); font-weight:600;">${s.semester}</span>
        </div>
        
        <h2 class="subject-title">${s.title}</h2>
        <p class="subject-desc">${s.desc}</p>
        
        <div class="subject-tags">
          ${s.tags.map(t => `<span class="card-tag">${t}</span>`).join('')}
        </div>
      </div>
      
      <!-- Multi-Download Action Row -->
      <div class="card-actions-wrapper">
        <div class="primary-download-row">
          <a href="${s.solutionsPdf}" class="btn-download-primary" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_Solutions_IOE.pdf">
            <span>↓ DOWNLOAD SOLUTIONS</span>
          </a>
          <button class="btn-preview-secondary" onclick="openPdfModal('${s.solutionsPdf}', '${s.title} — Solutions')" title="Preview Solutions in browser">
            <span>PREVIEW</span>
          </button>
        </div>
        
        <div class="secondary-download-row">
          <a href="${s.questionsPdf}" class="btn-sub-link" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_Questions_IOE.pdf">
            <span>📄 Questions PDF</span>
          </a>
          <a href="${s.syllabusPdf}" class="btn-sub-link" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_Syllabus_IOE.pdf">
            <span>📋 Syllabus PDF</span>
          </a>
        </div>
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

// Modal for Ready PDF Preview
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
