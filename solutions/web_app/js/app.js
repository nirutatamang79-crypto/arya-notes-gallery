/**
 * Arya's Notes Gallery & BCT Exam Countdown Timer Engine
 * iPhone Taptic Engine & Samsung One UI Haptic Sound System
 * Features: Authentic Haptic Taps, Water/Pop Clicks, Hardware Vibration API,
 * Dynamic Theme Whoosh, and Tactile Haptic Scroll Ticks.
 */

// 6 Subject Materials Data — BCT 4th Semester
const SUBJECTS_DATA = [
  {
    id: "ecm",
    title: "Electrical Circuits & Machines",
    tag: "EE",
    code: "ENEE 154",
    accent: "var(--accent-ecm)",
    accentHex: "#d97706",
    pages: "55 Pages",
    fileSize: "687 KB",
    baseDownloads: 248,
    solutionsPdf: "downloads/ecm/ECM Solutions.pdf",
    questionsPdf: "downloads/ecm/ecm_questions.pdf",
    syllabusPdf: "downloads/ecm/ecm_syllabus.pdf"
  },
  {
    id: "edc",
    title: "Electronic Devices & Circuits",
    tag: "EDC",
    code: "ENEX 151",
    accent: "var(--accent-edc)",
    accentHex: "#0284c7",
    pages: "56 Pages",
    fileSize: "570 KB",
    baseDownloads: 214,
    solutionsPdf: "downloads/edc/EDC Solutions.pdf",
    questionsPdf: "downloads/edc/edc_questions.pdf",
    syllabusPdf: "downloads/edc/edc_syllabus.pdf"
  },
  {
    id: "dl",
    title: "Digital Logic",
    tag: "LOGIC",
    code: "ENEX 152",
    accent: "var(--accent-dl)",
    accentHex: "#059669",
    pages: "61 Pages",
    fileSize: "535 KB",
    baseDownloads: 312,
    solutionsPdf: "downloads/dl/Digital Logic Solutions.pdf",
    questionsPdf: "downloads/dl/digital_logic_questions.pdf",
    syllabusPdf: "downloads/dl/digital_logic_syllabus.pdf"
  },
  {
    id: "math",
    title: "Engineering Mathematics",
    tag: "MATH",
    code: "ENSH 151",
    accent: "var(--accent-math)",
    accentHex: "#7c3aed",
    pages: "42 Pages",
    fileSize: "362 KB",
    baseDownloads: 195,
    solutionsPdf: "downloads/math/Math Solutions.pdf",
    questionsPdf: "downloads/math/math_questions.pdf",
    syllabusPdf: "downloads/math/math_syllabus.pdf"
  },
  {
    id: "oop",
    title: "Object Oriented Programming",
    tag: "OOP",
    code: "ENCT 151",
    accent: "var(--accent-oop)",
    accentHex: "#e11d48",
    pages: "38 Pages",
    fileSize: "311 KB",
    baseDownloads: 182,
    solutionsPdf: "downloads/oop/OOP Solutions.pdf",
    questionsPdf: "downloads/oop/oop_questions.pdf",
    syllabusPdf: "downloads/oop/oop_syllabus.pdf"
  },
  {
    id: "chem",
    title: "Engineering Chemistry",
    tag: "CHEM",
    code: "ENSH 153",
    accent: "var(--accent-chem)",
    accentHex: "#0d9488",
    pages: "45 Pages",
    fileSize: "344 KB",
    baseDownloads: 164,
    solutionsPdf: "downloads/chem/Chemistry Solutions.pdf",
    questionsPdf: "downloads/chem/chemistry_questions.pdf",
    syllabusPdf: "downloads/chem/chemistry_syllabus.pdf"
  }
];

// BCT 2083 Exam Schedule (1:00 PM NPT, Asia/Kathmandu, UTC+5:45) - Revised as of 2083-06-01
const EXAM_SCHEDULE = [
  {
    id: 'ensh151',
    subjectId: 'math',
    code: 'ENSH 151',
    name: 'Engineering Mathematics II',
    dateBS: '2083-05-31',
    dateAD: 'September 16, 2026',
    targetDateStr: '2026-09-16T13:00:00+05:45',
    endDateStr: '2026-09-16T16:00:00+05:45',
    accent: 'var(--accent-math)',
    accentHex: '#7c3aed'
  },
  {
    id: 'enex151',
    subjectId: 'edc',
    code: 'ENEX 151',
    name: 'Electronic Devices & Circuits',
    dateBS: '2083-06-04',
    dateAD: 'September 20, 2026',
    targetDateStr: '2026-09-20T13:00:00+05:45',
    endDateStr: '2026-09-20T16:00:00+05:45',
    accent: 'var(--accent-edc)',
    accentHex: '#0284c7'
  },
  {
    id: 'ensh153',
    subjectId: 'chem',
    code: 'ENSH 153',
    name: 'Engineering Chemistry',
    dateBS: '2083-06-08',
    dateAD: 'September 24, 2026',
    targetDateStr: '2026-09-24T13:00:00+05:45',
    endDateStr: '2026-09-24T16:00:00+05:45',
    accent: 'var(--accent-chem)',
    accentHex: '#0d9488'
  },
  {
    id: 'enct151',
    subjectId: 'oop',
    code: 'ENCT 151',
    name: 'Object Oriented Programming',
    dateBS: '2083-06-12',
    dateAD: 'September 28, 2026',
    targetDateStr: '2026-09-28T13:00:00+05:45',
    endDateStr: '2026-09-28T16:00:00+05:45',
    accent: 'var(--accent-oop)',
    accentHex: '#e11d48'
  },
  {
    id: 'enex152',
    subjectId: 'dl',
    code: 'ENEX 152',
    name: 'Digital Logic',
    dateBS: '2083-06-16',
    dateAD: 'October 2, 2026',
    targetDateStr: '2026-10-02T13:00:00+05:45',
    endDateStr: '2026-10-02T16:00:00+05:45',
    accent: 'var(--accent-dl)',
    accentHex: '#059669'
  },
  {
    id: 'enee154',
    subjectId: 'ecm',
    code: 'ENEE 154',
    name: 'Electrical Circuits & Machines',
    dateBS: '2083-06-20',
    dateAD: 'October 6, 2026',
    targetDateStr: '2026-10-06T13:00:00+05:45',
    endDateStr: '2026-10-06T16:00:00+05:45',
    accent: 'var(--accent-ecm)',
    accentHex: '#d97706'
  }
];

// ==============================================================================
// iPhone Taptic & Samsung One UI Haptic Sound Engine
// ==============================================================================
class SoundFXEngine {
  constructor() {
    this.ctx = null;
    this.enabled = localStorage.getItem('arya_sfx_enabled') !== 'false';
    this.lastScrollTick = 0;
    this.lastScrollY = window.scrollY || 0;
  }

  init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  // Trigger real mobile hardware vibration (if device supports)
  triggerHaptic(type = 'light') {
    try {
      if (navigator && typeof navigator.vibrate === 'function') {
        if (type === 'light') navigator.vibrate(8);
        else if (type === 'medium') navigator.vibrate(15);
        else if (type === 'double') navigator.vibrate([10, 25, 12]);
      }
    } catch (e) {}
  }

  toggle() {
    this.enabled = !this.enabled;
    localStorage.setItem('arya_sfx_enabled', this.enabled ? 'true' : 'false');
    const btnText = document.getElementById('sound-toggle-text');
    if (btnText) btnText.innerText = this.enabled ? 'SFX: ON' : 'SFX: OFF';
    if (this.enabled) this.playHapticTap();
    showToast(this.enabled ? 'Haptic Sound FX Enabled' : 'Sound FX Muted');
  }

  // 1. iPhone Taptic Engine / Samsung One UI Key Tap Sound
  playHapticTap() {
    this.triggerHaptic('light');
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    // Transient crisp high-frequency chirp (iPhone lock/tap click)
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(1900, now);
    osc.frequency.exponentialRampToValueAtTime(700, now + 0.012);
    gain.gain.setValueAtTime(0.32, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.012);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.012);

    // Warm taptic low-end impulse
    const subOsc = this.ctx.createOscillator();
    const subGain = this.ctx.createGain();
    subOsc.type = 'triangle';
    subOsc.frequency.setValueAtTime(160, now);
    subOsc.frequency.exponentialRampToValueAtTime(50, now + 0.02);
    subGain.gain.setValueAtTime(0.35, now);
    subGain.gain.exponentialRampToValueAtTime(0.001, now + 0.02);
    subOsc.connect(subGain);
    subGain.connect(this.ctx.destination);
    subOsc.start(now);
    subOsc.stop(now + 0.02);
  }

  // 2. Samsung One UI Pleasant Bubble/Waterdrop Pop Sound (for Downloads)
  playHapticPop() {
    this.triggerHaptic('medium');
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    // Smooth ascending pop
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(560, now);
    osc.frequency.exponentialRampToValueAtTime(1420, now + 0.035);
    gain.gain.setValueAtTime(0.38, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.045);
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.045);

    // Soft resonant harmonic ring
    const ring = this.ctx.createOscillator();
    const ringGain = this.ctx.createGain();
    ring.type = 'sine';
    ring.frequency.setValueAtTime(1420, now + 0.01);
    ringGain.gain.setValueAtTime(0.18, now + 0.01);
    ringGain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
    ring.connect(ringGain);
    ringGain.connect(this.ctx.destination);
    ring.start(now + 0.01);
    ring.stop(now + 0.12);
  }

  // 3. Theme Whoosh Sound (Aerodynamic Wind Sweep)
  playWhoosh() {
    this.triggerHaptic('medium');
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    const bufferSize = Math.floor(this.ctx.sampleRate * 0.32);
    const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
    const data = buffer.getChannelData(0);

    for (let i = 0; i < bufferSize; i++) {
      data[i] = (Math.random() * 2 - 1) * Math.sin(Math.PI * (i / bufferSize));
    }

    const noise = this.ctx.createBufferSource();
    noise.buffer = buffer;

    const filter = this.ctx.createBiquadFilter();
    filter.type = 'bandpass';
    filter.frequency.setValueAtTime(220, now);
    filter.frequency.exponentialRampToValueAtTime(3400, now + 0.14);
    filter.frequency.exponentialRampToValueAtTime(260, now + 0.32);
    filter.Q.setValueAtTime(2.6, now);

    const gain = this.ctx.createGain();
    gain.gain.setValueAtTime(0.65, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.32);

    noise.connect(filter);
    filter.connect(gain);
    gain.connect(this.ctx.destination);
    noise.start(now);
    noise.stop(now + 0.32);
  }

  // 4. Tactile Scrolling Haptic Tick (Digital Crown / Wheel Click)
  playScrollTick() {
    this.triggerHaptic('light');
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    if (now - this.lastScrollTick < 0.06) return;
    this.lastScrollTick = now;

    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(1600, now);
    osc.frequency.exponentialRampToValueAtTime(550, now + 0.015);
    gain.gain.setValueAtTime(0.22, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.015);

    osc.connect(gain);
    gain.connect(this.ctx.destination);
    osc.start(now);
    osc.stop(now + 0.015);
  }

  // 5. Crisp Two-Tone Notification Alert Bell Chime (for Leaked Questions & Urgent Notices)
  playAlertChime() {
    this.triggerHaptic('double');
    if (!this.enabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;

    // First tone (E5 ~ 659.25 Hz)
    const osc1 = this.ctx.createOscillator();
    const gain1 = this.ctx.createGain();
    osc1.type = 'sine';
    osc1.frequency.setValueAtTime(659.25, now);
    gain1.gain.setValueAtTime(0.28, now);
    gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.26);
    osc1.connect(gain1);
    gain1.connect(this.ctx.destination);
    osc1.start(now);
    osc1.stop(now + 0.26);

    // Second higher harmonic tone (A5 ~ 880 Hz)
    const osc2 = this.ctx.createOscillator();
    const gain2 = this.ctx.createGain();
    osc2.type = 'sine';
    osc2.frequency.setValueAtTime(880, now + 0.11);
    gain2.gain.setValueAtTime(0.35, now + 0.11);
    gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
    osc2.connect(gain2);
    gain2.connect(this.ctx.destination);
    osc2.start(now + 0.11);
    osc2.stop(now + 0.45);
  }
}

const sfx = new SoundFXEngine();

// Persistent UI State
let currentTheme = localStorage.getItem('arya_portal_theme') || 'light';
let timerViewMode = localStorage.getItem('arya_timer_view') || 'cards';
let downloadStats = {};
try {
  const storedDownloadStats = JSON.parse(localStorage.getItem('arya_download_stats') || '{}');
  if (storedDownloadStats && typeof storedDownloadStats === 'object' && !Array.isArray(storedDownloadStats)) {
    downloadStats = storedDownloadStats;
  }
} catch (error) {
  console.warn('Ignoring invalid saved download statistics.', error);
}
let zenActiveExamId = null;

// Initialize download stats
SUBJECTS_DATA.forEach(s => {
  if (!downloadStats[s.id]) {
    downloadStats[s.id] = s.baseDownloads;
  }
});
saveDownloadStats();

// DOM Initialization
document.addEventListener('DOMContentLoaded', () => {
  run5SecondAppLoader();
  applyTheme(currentTheme);
  setupWaveRippleEffect();
  initActiveUsersCounter();
  fetchUniqueVisitorsSummary();
  setInterval(fetchUniqueVisitorsSummary, 5000);
  renderSubjectSlots(SUBJECTS_DATA);
  fetchAndRenderReviews();
  setTimerView(timerViewMode);
  startLiveTimers();
  setupListeners();
});

// 5-Second Animated Loading Screen Engine
function run5SecondAppLoader() {
  const loader = document.getElementById('app-loader-screen');
  const bar = document.getElementById('loader-progress-bar');
  const percentText = document.getElementById('loader-percent-text');
  const statusText = document.getElementById('loader-status-text');
  const secondsText = document.getElementById('loader-seconds');

  if (!loader) return;

  const totalDuration = 5000; // Exactly 5 seconds
  const startTime = Date.now();

  const statusStages = [
    { at: 0, msg: "Initializing study protocol..." },
    { at: 1100, msg: "Calibrating 6 subject master solutions..." },
    { at: 2300, msg: "Synchronizing IOE BCT 2083 exam schedule..." },
    { at: 3600, msg: "Configuring iPhone Haptics & Audio..." },
    { at: 4600, msg: "Ready. Launching Arya's Notes Gallery..." }
  ];

  const updateLoader = () => {
    const elapsed = Date.now() - startTime;
    const progress = Math.min(elapsed / totalDuration, 1);
    const percent = Math.floor(progress * 100);
    const remainingSeconds = Math.max(0, Math.ceil((totalDuration - elapsed) / 1000));

    if (bar) bar.style.width = `${percent}%`;
    if (percentText) percentText.innerText = `${percent}%`;
    if (secondsText) secondsText.innerText = `${remainingSeconds}s`;

    // Find current status message
    for (let i = statusStages.length - 1; i >= 0; i--) {
      if (elapsed >= statusStages[i].at) {
        if (statusText && statusText.innerText !== statusStages[i].msg) {
          statusText.innerText = statusStages[i].msg;
        }
        break;
      }
    }

    if (progress < 1) {
      requestAnimationFrame(updateLoader);
    } else {
      // 5 seconds completed: smooth fade-out outro
      setTimeout(() => {
        loader.classList.add('loader-hidden');
        sfx.playHapticPop();
        setTimeout(() => {
          if (loader.parentNode) loader.parentNode.removeChild(loader);
        }, 550);
      }, 100);
    }
  };

  requestAnimationFrame(updateLoader);
}

// Active Users Live Counter (Random Range: 5 - 15, Never Below 5)
function initActiveUsersCounter() {
  const countEl = document.getElementById('active-users-count');
  if (!countEl) return;

  // Initialize random active count strictly between 5 and 15
  let currentActive = parseInt(sessionStorage.getItem('arya_online_range') || '', 10);
  if (isNaN(currentActive) || currentActive < 5 || currentActive > 15) {
    currentActive = Math.floor(Math.random() * 11) + 5; // 5 to 15
  }

  const updateDisplay = (count) => {
    // Strictly clamp between 5 and 15 (never 1, 2, 3, 4)
    const safeCount = Math.max(5, Math.min(15, count));
    countEl.innerText = `${safeCount} online`;
    try { sessionStorage.setItem('arya_online_range', safeCount.toString()); } catch (e) {}
  };

  updateDisplay(currentActive);

  // Subtle realistic fluctuation strictly within [5, 15] every 5 seconds
  setInterval(() => {
    const delta = (Math.random() > 0.48 ? 1 : -1) * (Math.random() > 0.75 ? 2 : 1);
    let next = currentActive + delta;
    if (next < 5) next = 5 + Math.floor(Math.random() * 2);
    if (next > 15) next = 15 - Math.floor(Math.random() * 2);
    currentActive = next;
    updateDisplay(currentActive);
  }, 5000);
}

// Unique Visitors Tracking & Modal Window Engine
let uniqueVisitorsData = { count: 1, list: [] };

async function fetchUniqueVisitorsSummary() {
  const pillText = document.getElementById('unique-visitors-pill-count');
  try {
    const res = await fetch('/api/requests', { cache: 'no-store' });
    if (!res.ok) return;
    const data = await res.json();
    uniqueVisitorsData.count = data.unique_visitors_count || 1;
    uniqueVisitorsData.list = data.unique_visitors_list || [];

    if (pillText) {
      pillText.innerText = `${uniqueVisitorsData.count} unique people`;
    }
  } catch (e) {
    if (pillText) pillText.innerText = `1 unique person`;
  }
}

function openVisitorsModal() {
  sfx.playHapticTap();
  const modal = document.getElementById('visitors-modal-backdrop');
  const totalTag = document.getElementById('visitors-modal-total');
  const summaryEl = document.getElementById('visitors-summary-text');
  const listEl = document.getElementById('visitors-modal-list');

  if (!modal) return;

  if (totalTag) totalTag.innerText = `${uniqueVisitorsData.count} PEOPLE`;
  if (summaryEl) {
    summaryEl.innerHTML = `<strong>Total Unique People Visited:</strong> ${uniqueVisitorsData.count} distinct clients registered across desktop and mobile devices.`;
  }

  if (listEl) {
    if (uniqueVisitorsData.list.length === 0) {
      listEl.innerHTML = `<div class="visitor-row-card"><span>Active unique visitor logging in progress...</span></div>`;
    } else {
      listEl.innerHTML = uniqueVisitorsData.list.map(v => `
        <div class="visitor-row-card mono">
          <div>
            <div><strong>👤 ${v.ip}</strong> · <span style="color:var(--text-muted);">${v.device}</span></div>
            <div style="font-size:0.68rem; color:var(--text-muted);">First seen: ${v.first_seen} · Last: ${v.last_seen}</div>
          </div>
          <div style="text-align:right;">
            <div><strong>${v.page_views} views</strong></div>
            <div style="font-size:0.68rem; color:var(--text-muted);">${v.downloads} dls</div>
          </div>
        </div>
      `).join('');
    }
  }

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeVisitorsModal() {
  sfx.playHapticTap();
  const modal = document.getElementById('visitors-modal-backdrop');
  if (modal) {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }
}

// Student Reviews & Feedback Engine
let currentFormRating = 5;
let currentVibeTag = "⚡ Life Saver";
let cachedReviews = [];

function setFormRating(stars) {
  currentFormRating = Math.max(1, Math.min(5, stars));
  sfx.playHapticTap();

  const starBtns = document.querySelectorAll('#star-rating-picker .star-btn');
  starBtns.forEach((btn, idx) => {
    btn.classList.toggle('active', idx < currentFormRating);
  });

  const scoreText = document.getElementById('star-rating-score');
  const ratingLabels = {
    5: "5.0 / 5.0 (Awesome!)",
    4: "4.0 / 5.0 (Great!)",
    3: "3.0 / 5.0 (Good)",
    2: "2.0 / 5.0 (Needs Improvement)",
    1: "1.0 / 5.0 (Poor)"
  };
  if (scoreText) scoreText.innerText = ratingLabels[currentFormRating] || `${currentFormRating}.0 / 5.0`;
}

function selectVibeTag(tag) {
  currentVibeTag = tag;
  sfx.playHapticTap();

  document.querySelectorAll('#vibe-tags-row .vibe-chip').forEach(btn => {
    btn.classList.toggle('active', btn.innerText.trim() === tag);
  });
}

function handleReviewCharCount() {
  const textarea = document.getElementById('review-comment-text');
  const countEl = document.getElementById('review-char-count');
  if (textarea && countEl) {
    const len = textarea.value.length;
    countEl.innerText = `${len} / 500`;
  }
}

function openLeaveReviewModal() {
  sfx.playHapticTap();
  const modal = document.getElementById('review-modal-backdrop');
  if (modal) {
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
      document.getElementById('review-author-name')?.focus();
    }, 150);
  }
}

function closeLeaveReviewModal() {
  sfx.playHapticTap();
  const modal = document.getElementById('review-modal-backdrop');
  if (modal) {
    modal.classList.remove('open');
    document.body.style.overflow = '';
  }
}

async function fetchAndRenderReviews() {
  try {
    const res = await fetch('/api/reviews', { cache: 'no-store' });
    if (!res.ok) return;
    const data = await res.json();

    cachedReviews = data.reviews || [];
    const total = data.total_reviews !== undefined ? data.total_reviews : cachedReviews.length;
    const avg = data.average_rating || 5.0;

    // Update Header button
    const headerBtnText = document.getElementById('header-reviews-text');
    if (headerBtnText) {
      headerBtnText.innerText = total > 0 ? `★ ${avg.toFixed(1)} (${total})` : `★ REVIEWS`;
    }

    // Update Section Summary
    const summaryLine = document.getElementById('reviews-summary-line');
    if (summaryLine) {
      summaryLine.innerText = total > 0 
        ? `⭐ ${avg.toFixed(1)} / 5.0 Average Rating · ${total} Student Testimonial${total === 1 ? '' : 's'}`
        : `⭐ Student Testimonials · Be the first to leave feedback!`;
    }

    // Render Review Cards Grid
    const grid = document.getElementById('reviews-grid');
    if (!grid) return;

    if (total === 0 || cachedReviews.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 2.5rem; color: var(--text-muted); border: 1px dashed var(--border-medium); border-radius: var(--radius-sm);" class="mono">
          No reviews yet. Be the first student to leave feedback!
        </div>
      `;
      return;
    }

    grid.innerHTML = cachedReviews.map(r => {
      const starsStr = '★'.repeat(r.rating) + '☆'.repeat(5 - r.rating);
      return `
        <div class="review-card" id="card-${r.id}">
          <div class="review-card-top">
            <div class="review-stars">${starsStr}</div>
            <span class="review-vibe-tag mono">${r.tag || '⚡ Life Saver'}</span>
          </div>

          <p class="review-comment">${escapeHtml(r.comment)}</p>

          <div class="review-card-footer mono">
            <div class="review-author-info">
              <span class="review-author-name">${escapeHtml(r.name)} ${r.roll ? `· Roll: ${escapeHtml(r.roll)}` : ''}</span>
              <span class="review-author-meta">${escapeHtml(r.subject)} · ${r.timestamp}</span>
            </div>
            <button class="review-like-btn" onclick="likeReview('${r.id}')" title="Mark as helpful">
              <span>👍</span>
              <span id="likes-${r.id}">${r.likes || 1}</span>
            </button>
          </div>
        </div>
      `;
    }).join('');

  } catch (err) {
    console.warn('Failed fetching reviews:', err);
  }
}

async function handleReviewSubmit(e) {
  e.preventDefault();
  const submitBtn = document.getElementById('submit-review-btn');
  const name = document.getElementById('review-author-name')?.value.trim() || 'Anonymous Student';
  const roll = document.getElementById('review-roll-no')?.value.trim() || '';
  const subject = document.getElementById('review-subject-select')?.value || 'General Gallery';
  const comment = document.getElementById('review-comment-text')?.value.trim();

  if (!comment) {
    showToast("Please write a short review before submitting!");
    return;
  }

  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerText = "SUBMITTING...";
  }

  try {
    const res = await fetch('/api/reviews', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        roll,
        subject,
        rating: currentFormRating,
        tag: currentVibeTag,
        comment
      })
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    sfx.playHapticPop();
    showToast("Thank you! Your review has been posted ⭐");
    closeLeaveReviewModal();
    document.getElementById('leave-review-form')?.reset();
    handleReviewCharCount();
    setFormRating(5);

    // Refresh reviews wall
    await fetchAndRenderReviews();

  } catch (err) {
    console.error('Failed submitting review:', err);
    showToast("Failed to submit review. Please try again!");
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerText = "SUBMIT REVIEW 🚀";
    }
  }
}

async function likeReview(revId) {
  sfx.playHapticTap();
  const likesEl = document.getElementById(`likes-${revId}`);

  try {
    const res = await fetch('/api/reviews/like', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: revId })
    });

    if (res.ok) {
      const data = await res.json();
      if (likesEl && data.likes) {
        likesEl.innerText = data.likes;
      }
    }
  } catch (e) {
    if (likesEl) {
      const cur = parseInt(likesEl.innerText, 10) || 1;
      likesEl.innerText = cur + 1;
    }
  }
}

function escapeHtml(str) {
  if (!str) return '';
  return str.replace(/[&<>"']/g, m => ({
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  }[m]));
}

// Render Subject Cards (Always in Grid Mode)
function renderSubjectSlots(subjects) {
  const container = document.getElementById('subject-grid');
  const countEl = document.getElementById('slots-count');
  if (!container) return;
  
  if (countEl) countEl.innerText = `${subjects.length} SUBJECTS`;
  
  if (subjects.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; padding: 3.5rem; text-align: center; color: var(--text-muted); font-family: var(--font-mono); border: 1px dashed var(--border-medium); border-radius: var(--radius-sm);">
        $ no matching subjects found. Try typing a different subject name.
      </div>
    `;
    return;
  }
  
  container.innerHTML = subjects.map(s => {
    const downloads = downloadStats[s.id] || s.baseDownloads;

    return `
      <div class="subject-card" id="card-${s.id}" style="--card-accent: ${s.accent};">
        <div class="card-header-area">
          <div class="card-top-row">
            <span class="subject-accent-tag">
              <span class="tag-dot"></span>
              <span>${s.tag}</span>
            </span>
          </div>

          <h2 class="subject-title">${s.title}</h2>
        </div>
        
        <div class="card-actions-wrapper">
          <!-- Primary Actions: Filled Download & Preview -->
          <div class="primary-download-row">
            <a href="${s.solutionsPdf}" class="btn-download-primary" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_Solutions_IOE.pdf" onclick="handleDownloadAction('${s.id}', '${s.title} Solutions')">
              <span>Download Solutions</span>
            </a>
            <button class="btn-preview-secondary" onclick="openPdfModal('${s.solutionsPdf}', '${s.title} — Master Solutions', '${s.pages} · ${s.fileSize}')" title="Preview Master Solutions">
              <span>Preview</span>
            </button>
          </div>
          
          <!-- Secondary Actions: Questions & Syllabus with instant preview -->
          <div class="secondary-download-row">
            <div class="sub-btn-group">
              <a href="${s.questionsPdf}" class="btn-sub-link" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_Questions_IOE.pdf" onclick="handleDownloadAction('${s.id}', '${s.title} Questions')">
                <span>Download Questions</span>
              </a>
              <button class="btn-sub-preview" onclick="openPdfModal('${s.questionsPdf}', '${s.title} — Questions PDF', 'Past Papers')" title="Preview Questions">
                <span>Preview</span>
              </button>
            </div>
            
            <div class="sub-btn-group">
              <a href="${s.syllabusPdf}" class="btn-sub-link" download="${s.title.replace(/[^a-zA-Z0-9]/g, '_')}_Syllabus_IOE.pdf" onclick="handleDownloadAction('${s.id}', '${s.title} Syllabus')">
                <span>Download Syllabus</span>
              </a>
              <button class="btn-sub-preview" onclick="openPdfModal('${s.syllabusPdf}', '${s.title} — Syllabus PDF', 'Official Blueprint')" title="Preview Syllabus">
                <span>Preview</span>
              </button>
            </div>
          </div>

          <!-- File Metadata Footer -->
          <div class="card-file-meta mono">
            <span>${s.pages} · ${s.fileSize}</span>
            <span class="downloads-badge" id="downloads-badge-${s.id}">
              <span class="badge-dot" style="width:5px;height:5px;background:var(--text-muted);border-radius:50%;display:inline-block;"></span>
              ${downloads} downloads
            </span>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

// Handle Download Tracking, Haptic Pop Sound & Toast
function handleDownloadAction(subjectId, docName) {
  sfx.playHapticPop();

  if (downloadStats[subjectId] !== undefined) {
    downloadStats[subjectId] += 1;
    saveDownloadStats();
    
    // Update badge on card
    const badge = document.getElementById(`downloads-badge-${subjectId}`);
    if (badge) {
      badge.innerHTML = `
        <span class="badge-dot" style="width:5px;height:5px;background:#10b981;border-radius:50%;display:inline-block;"></span>
        ${downloadStats[subjectId]} downloads
      `;
    }
  }

  showToast(`Downloaded: ${docName}`);
}

function saveDownloadStats() {
  try {
    localStorage.setItem('arya_download_stats', JSON.stringify(downloadStats));
  } catch (e) {}
}

// ==============================================================================
// BCT Exam Timer Engine
// ==============================================================================

function padZero(num) {
  return String(num).padStart(2, '0');
}

function getTimeBreakdown(targetMs, nowMs) {
  const diff = targetMs - nowMs;
  if (diff <= 0) {
    return { days: 0, hours: 0, minutes: 0, seconds: 0, isPassed: true };
  }

  const totalSeconds = Math.floor(diff / 1000);
  const days = Math.floor(totalSeconds / (3600 * 24));
  const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  return { days, hours, minutes, seconds, isPassed: false };
}

function getExamStatus(exam, nowMs) {
  const startMs = new Date(exam.targetDateStr).getTime();
  const endMs = new Date(exam.endDateStr).getTime();

  if (nowMs < startMs) {
    return { label: 'Upcoming', class: 'upcoming' };
  } else if (nowMs >= startMs && nowMs <= endMs) {
    return { label: 'Happening Now (1 PM - 4 PM)', class: 'today' };
  } else {
    return { label: 'Completed', class: 'passed' };
  }
}

function getNextUpcomingExam(nowMs) {
  for (const exam of EXAM_SCHEDULE) {
    const endMs = new Date(exam.endDateStr).getTime();
    if (nowMs < endMs) {
      return exam;
    }
  }
  return EXAM_SCHEDULE[0];
}

// Start Live Timers (Updates every second)
function startLiveTimers() {
  updateTimerUI();
  setInterval(updateTimerUI, 1000);
}

function updateTimerUI() {
  const now = new Date();
  const nowMs = now.getTime();

  // 1. Update Live Clock Badge
  const clockEl = document.getElementById('live-clock');
  if (clockEl) {
    try {
      const timeStr = now.toLocaleTimeString('en-US', {
        timeZone: 'Asia/Kathmandu',
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
      clockEl.innerText = `${timeStr} NPT (UTC+5:45)`;
    } catch (e) {
      clockEl.innerText = `${padZero(now.getHours())}:${padZero(now.getMinutes())}:${padZero(now.getSeconds())} NPT`;
    }
  }

  // 2. Update Hero Spotlight
  const nextExam = getNextUpcomingExam(nowMs);
  const targetMs = new Date(nextExam.targetDateStr).getTime();
  const heroT = getTimeBreakdown(targetMs, nowMs);

  const heroCodeEl = document.getElementById('hero-code');
  const heroTitleEl = document.getElementById('hero-title');
  const heroDateBsEl = document.getElementById('hero-date-bs');
  const heroDateAdEl = document.getElementById('hero-date-ad');
  const heroDaysEl = document.getElementById('hero-days');
  const heroHoursEl = document.getElementById('hero-hours');
  const heroMinsEl = document.getElementById('hero-mins');
  const heroSecsEl = document.getElementById('hero-secs');
  const heroCard = document.getElementById('hero-spotlight');

  if (heroCodeEl) heroCodeEl.innerText = nextExam.code;
  if (heroTitleEl) heroTitleEl.innerText = nextExam.name;
  if (heroDateBsEl) heroDateBsEl.innerText = `${nextExam.dateBS} B.S.`;
  if (heroDateAdEl) heroDateAdEl.innerText = `${nextExam.dateAD} · 1:00 PM NPT`;
  if (heroDaysEl) heroDaysEl.innerText = padZero(heroT.days);
  if (heroHoursEl) heroHoursEl.innerText = padZero(heroT.hours);
  if (heroMinsEl) heroMinsEl.innerText = padZero(heroT.minutes);
  if (heroSecsEl) heroSecsEl.innerText = padZero(heroT.seconds);
  if (heroCard) heroCard.style.borderTopColor = nextExam.accent;

  // 3. Update Schedule Views
  EXAM_SCHEDULE.forEach(exam => {
    const eTargetMs = new Date(exam.targetDateStr).getTime();
    const t = getTimeBreakdown(eTargetMs, nowMs);

    // Cards View Live Digits
    const dEl = document.getElementById(`timer-d-${exam.id}`);
    const hEl = document.getElementById(`timer-h-${exam.id}`);
    const mEl = document.getElementById(`timer-m-${exam.id}`);
    const sEl = document.getElementById(`timer-s-${exam.id}`);

    if (dEl) dEl.innerText = padZero(t.days);
    if (hEl) hEl.innerText = padZero(t.hours);
    if (mEl) mEl.innerText = padZero(t.minutes);
    if (sEl) sEl.innerText = padZero(t.seconds);

    // Table View Live Cell
    const tableRemainEl = document.getElementById(`table-remain-${exam.id}`);
    if (tableRemainEl) {
      if (t.isPassed) {
        tableRemainEl.innerText = 'Completed';
      } else {
        tableRemainEl.innerText = `${t.days}d ${padZero(t.hours)}h ${padZero(t.minutes)}m ${padZero(t.seconds)}s`;
      }
    }

    // Timeline View Live Cell
    const timelineRemainEl = document.getElementById(`timeline-remain-${exam.id}`);
    if (timelineRemainEl) {
      if (t.isPassed) {
        timelineRemainEl.innerText = 'Completed';
      } else {
        timelineRemainEl.innerText = `${t.days} Days ${padZero(t.hours)}h ${padZero(t.minutes)}m ${padZero(t.seconds)}s`;
      }
    }
  });

  // 4. Update Zen Mode if active
  if (zenActiveExamId) {
    const activeExam = EXAM_SCHEDULE.find(e => e.id === zenActiveExamId) || nextExam;
    const zenTargetMs = new Date(activeExam.targetDateStr).getTime();
    const zt = getTimeBreakdown(zenTargetMs, nowMs);

    const zd = document.getElementById('zen-days');
    const zh = document.getElementById('zen-hours');
    const zm = document.getElementById('zen-mins');
    const zs = document.getElementById('zen-secs');

    if (zd) zd.innerText = padZero(zt.days);
    if (zh) zh.innerText = padZero(zt.hours);
    if (zm) zm.innerText = padZero(zt.minutes);
    if (zs) zs.innerText = padZero(zt.seconds);
  }
}

// Switch Timer Views (Cards / Table / Timeline)
function setTimerView(view) {
  sfx.playHapticTap();
  timerViewMode = view;
  try {
    localStorage.setItem('arya_timer_view', view);
  } catch (e) {}

  // Update button active state
  ['cards', 'table', 'timeline'].forEach(v => {
    const btn = document.getElementById(`btn-view-${v}`);
    if (btn) btn.classList.toggle('active', v === view);
  });

  const container = document.getElementById('schedule-view-container');
  if (!container) return;

  const nowMs = Date.now();

  if (view === 'cards') {
    container.innerHTML = `
      <div class="schedule-cards-grid">
        ${EXAM_SCHEDULE.map(exam => {
          const t = getTimeBreakdown(new Date(exam.targetDateStr).getTime(), nowMs);
          const status = getExamStatus(exam, nowMs);

          return `
            <div class="schedule-card" id="sched-card-${exam.id}" style="--card-accent: ${exam.accent};">
              <div>
                <div class="schedule-card-header">
                  <span class="schedule-code mono">${exam.code}</span>
                  <span class="schedule-status mono">${status.label}</span>
                </div>
                <h4 class="schedule-title">${exam.name}</h4>
                <p class="schedule-dates mono">${exam.dateBS} B.S. · ${exam.dateAD}</p>
              </div>

              <div>
                <div class="schedule-timer-digits mono">
                  <div>
                    <span class="digit-unit-val" id="timer-d-${exam.id}">${padZero(t.days)}</span>
                    <span class="digit-unit-lbl">DAYS</span>
                  </div>
                  <div>
                    <span class="digit-unit-val" id="timer-h-${exam.id}">${padZero(t.hours)}</span>
                    <span class="digit-unit-lbl">HOURS</span>
                  </div>
                  <div>
                    <span class="digit-unit-val" id="timer-m-${exam.id}">${padZero(t.minutes)}</span>
                    <span class="digit-unit-lbl">MINS</span>
                  </div>
                  <div>
                    <span class="digit-unit-val" id="timer-s-${exam.id}">${padZero(t.seconds)}</span>
                    <span class="digit-unit-lbl">SECS</span>
                  </div>
                </div>

                <div class="schedule-card-footer">
                  <span class="mono" style="font-size: 0.72rem; color: var(--text-muted);">1:00 PM NPT</span>
                  <button class="btn-pill mono" onclick="openZenMode('${exam.id}')" title="Open Zen focus timer">
                    <span>ZEN MODE</span>
                  </button>
                </div>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  } else if (view === 'table') {
    container.innerHTML = `
      <div class="schedule-table-wrap">
        <table class="schedule-table mono">
          <thead>
            <tr>
              <th>Code</th>
              <th>Subject</th>
              <th>Nepali Date</th>
              <th>English Date</th>
              <th>Status</th>
              <th>Countdown</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            ${EXAM_SCHEDULE.map(exam => {
              const t = getTimeBreakdown(new Date(exam.targetDateStr).getTime(), nowMs);
              const status = getExamStatus(exam, nowMs);

              return `
                <tr>
                  <td><strong>${exam.code}</strong></td>
                  <td>${exam.name}</td>
                  <td>${exam.dateBS}</td>
                  <td>${exam.dateAD}</td>
                  <td>${status.label}</td>
                  <td id="table-remain-${exam.id}">
                    ${t.isPassed ? 'Completed' : `${t.days}d ${padZero(t.hours)}h ${padZero(t.minutes)}m ${padZero(t.seconds)}s`}
                  </td>
                  <td>
                    <button class="btn-pill" onclick="openZenMode('${exam.id}')">ZEN</button>
                  </td>
                </tr>
              `;
            }).join('')}
          </tbody>
        </table>
      </div>
    `;
  } else if (view === 'timeline') {
    container.innerHTML = `
      <div class="schedule-timeline">
        ${EXAM_SCHEDULE.map(exam => {
          const t = getTimeBreakdown(new Date(exam.targetDateStr).getTime(), nowMs);
          const status = getExamStatus(exam, nowMs);

          return `
            <div class="timeline-item" style="--card-accent: ${exam.accent};">
              <div>
                <span class="mono" style="font-size: 0.75rem; color: var(--text-muted); font-weight:700;">${exam.code} · ${exam.dateBS} B.S.</span>
                <h4 style="font-size: 1.15rem; font-weight: 800; margin: 0.2rem 0;">${exam.name}</h4>
                <p class="mono" style="font-size: 0.78rem; color: var(--text-muted);">${exam.dateAD} · 1:00 PM – 4:00 PM NPT</p>
              </div>
              <div style="text-align: right;">
                <span class="mono" id="timeline-remain-${exam.id}" style="font-size: 0.95rem; font-weight: 800; display: block; margin-bottom: 0.4rem;">
                  ${t.isPassed ? 'Completed' : `${t.days} Days ${padZero(t.hours)}h ${padZero(t.minutes)}m ${padZero(t.seconds)}s`}
                </span>
                <button class="btn-pill mono" onclick="openZenMode('${exam.id}')">FOCUS</button>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  }
}

// Zen Focus Mode
function openZenMode(examId) {
  sfx.playHapticTap();
  const nowMs = Date.now();
  const exam = examId ? EXAM_SCHEDULE.find(e => e.id === examId) : getNextUpcomingExam(nowMs);
  if (!exam) return;

  zenActiveExamId = exam.id;

  const overlay = document.getElementById('zen-overlay');
  const codeEl = document.getElementById('zen-code');
  const titleEl = document.getElementById('zen-title');
  const dateEl = document.getElementById('zen-date');

  if (codeEl) codeEl.innerText = exam.code;
  if (titleEl) titleEl.innerText = exam.name;
  if (dateEl) dateEl.innerText = `${exam.dateBS} B.S. · ${exam.dateAD} · 1:00 PM NPT`;

  if (overlay) {
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  showToast(`Entered Zen Mode: ${exam.name}`);
}

function closeZenMode() {
  sfx.playHapticTap();
  const overlay = document.getElementById('zen-overlay');
  zenActiveExamId = null;
  if (overlay) {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }
}

// Export Calendar Schedule (.ics)
function exportCalendarSchedule() {
  sfx.playHapticPop();

  let icsLines = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Aryas Notes Gallery//BCT Exam Schedule 2083//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'X-WR-CALNAME:IOE BCT Exam Schedule 2083',
    'X-WR-TIMEZONE:Asia/Kathmandu'
  ];

  EXAM_SCHEDULE.forEach(exam => {
    const startDt = new Date(exam.targetDateStr);
    const endDt = new Date(exam.endDateStr);

    const formatICSDate = (d) => {
      return d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
    };

    icsLines.push(
      'BEGIN:VEVENT',
      `UID:${exam.id}-2083-ioe@aryasnotes`,
      `DTSTAMP:${formatICSDate(new Date())}`,
      `DTSTART:${formatICSDate(startDt)}`,
      `DTEND:${formatICSDate(endDt)}`,
      `SUMMARY:IOE Exam: ${exam.code} - ${exam.name}`,
      `DESCRIPTION:Tribhuvan University IOE BCT Exam.\\nDate: ${exam.dateBS} B.S. (${exam.dateAD})\\nTime: 1:00 PM - 4:00 PM NPT`,
      'LOCATION:IOE Examination Hall',
      'STATUS:CONFIRMED',
      'BEGIN:VALARM',
      'TRIGGER:-P1D',
      'ACTION:DISPLAY',
      `DESCRIPTION:Reminder: Tomorrow is ${exam.code} - ${exam.name} Exam at 1:00 PM`,
      'END:VALARM',
      'END:VEVENT'
    );
  });

  icsLines.push('END:VCALENDAR');

  const icsBlob = new Blob([icsLines.join('\r\n')], { type: 'text/calendar;charset=utf-8' });
  const downloadUrl = URL.createObjectURL(icsBlob);
  const link = document.createElement('a');
  link.href = downloadUrl;
  link.setAttribute('download', 'IOE_BCT_Exam_Schedule_2083.ics');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(downloadUrl);

  showToast('Calendar schedule (.ics) exported!');
}

// "Surprise Me" Random Subject Pick
function pickRandomSubject() {
  sfx.playHapticTap();
  const randomIndex = Math.floor(Math.random() * SUBJECTS_DATA.length);
  const target = SUBJECTS_DATA[randomIndex];
  
  const card = document.getElementById(`card-${target.id}`);
  if (card) {
    card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    card.classList.remove('highlight-card');
    void card.offsetWidth;
    card.classList.add('highlight-card');
    showToast(`Surprise Pick: ${target.title}`);
  }
}

// Theme Switcher (Light <-> Dark) with Loud Whoosh Sound
function applyTheme(theme) {
  currentTheme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  try {
    localStorage.setItem('arya_portal_theme', theme);
  } catch (e) {}
  
  const btnText = document.getElementById('theme-toggle-text');
  if (btnText) {
    btnText.innerText = theme === 'light' ? 'DARK' : 'LIGHT';
  }
}

function toggleTheme() {
  sfx.playWhoosh();
  applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
  showToast(`Switched to ${currentTheme.toUpperCase()} mode`);
}

// Toast Notifications
function showToast(message) {
  const container = document.getElementById('toast-container');
  if (!container) return;
  
  const toast = document.createElement('div');
  toast.className = 'toast-message';
  toast.innerHTML = `
    <span class="toast-indicator"></span>
    <span>${message}</span>
  `;
  
  container.appendChild(toast);
  
  setTimeout(() => {
    toast.classList.add('toast-out');
    setTimeout(() => {
      if (toast.parentNode) toast.parentNode.removeChild(toast);
    }, 200);
  }, 2600);
}

// Quick Inline Search Filter
function handleQuickFilter(query) {
  const q = query.trim().toLowerCase();
  if (!q) {
    renderSubjectSlots(SUBJECTS_DATA);
    return;
  }
  
  const filtered = SUBJECTS_DATA.filter(s => {
    return s.title.toLowerCase().includes(q) ||
           s.tag.toLowerCase().includes(q) ||
           s.code.toLowerCase().includes(q) ||
           s.id.toLowerCase().includes(q);
  });
  
  renderSubjectSlots(filtered);
}

// PDF.js Continuous Multi-Page Document Reader Engine
let activePdfDoc = null;
let totalPdfPages = 0;
let pdfScale = 1.0;
let currentPdfUrl = '';
let renderedPagesMap = new Set();
let pageIntersectionObserver = null;

if (typeof window !== 'undefined' && window.pdfjsLib) {
  window.pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
}

// Modal for Ready PDF Preview
async function openPdfModal(url, title, meta) {
  if (!url || url === '#') return;

  sfx.playHapticTap();

  const modal = document.getElementById('pdf-modal-backdrop');
  const titleEl = document.getElementById('pdf-modal-title');
  const metaEl = document.getElementById('pdf-modal-meta');
  const downloadLink = document.getElementById('modal-download-btn');
  const fullscreenLink = document.getElementById('modal-fullscreen-btn');

  if (modal) {
    if (titleEl) titleEl.innerText = title;
    if (metaEl) metaEl.innerText = meta || "PDF DOCUMENT";

    if (downloadLink) {
      downloadLink.href = url;
      const downloadName = (title || 'document').replace(/[^a-zA-Z0-9]/g, '_') + '.pdf';
      downloadLink.setAttribute('download', downloadName);
      downloadLink.onclick = () => sfx.playHapticPop();
    }

    if (fullscreenLink) {
      fullscreenLink.href = url;
      fullscreenLink.onclick = () => sfx.playHapticTap();
    }

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';

    // Render continuous document
    await loadContinuousPdfDocument(url);
  }
}

async function loadContinuousPdfDocument(url) {
  currentPdfUrl = url;
  renderedPagesMap.clear();

  const feed = document.getElementById('pdf-pages-feed');
  const spinner = document.getElementById('pdf-loading-spinner');
  const indicator = document.getElementById('pdf-page-indicator');
  const iframe = document.getElementById('pdf-iframe');

  if (feed) feed.innerHTML = '';
  if (spinner) {
    spinner.style.display = 'flex';
    const textSpan = spinner.querySelector('span');
    if (textSpan) textSpan.innerText = 'Loading all pages into continuous reader...';
  }

  // Initial scale
  const isMobile = window.innerWidth <= 768;
  pdfScale = isMobile ? 1.0 : 1.25;

  if (window.pdfjsLib) {
    try {
      if (iframe) iframe.style.display = 'none';

      const loadingTask = window.pdfjsLib.getDocument({
        url: url,
        cMapUrl: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/cmaps/',
        cMapPacked: true
      });

      activePdfDoc = await loadingTask.promise;
      totalPdfPages = activePdfDoc.numPages;

      if (indicator) indicator.innerText = `Page 1 / ${totalPdfPages}`;
      if (spinner) spinner.style.display = 'none';

      // Setup page slots in the continuous feed
      setupContinuousPageSlots(totalPdfPages);

      // Render initial pages immediately (first 2 pages for instant viewing)
      const initialCount = Math.min(2, totalPdfPages);
      for (let p = 1; p <= initialCount; p++) {
        await renderSingleContinuousPage(p);
      }

      // Setup IntersectionObserver to lazy-render subsequent pages as user scrolls
      setupPageIntersectionObserver();
      return;
    } catch (err) {
      console.warn('PDF.js continuous reader error, falling back to direct iframe...', err);
    }
  }

  // Fallback to iframe if PDF.js unavailable
  if (iframe) {
    if (spinner) spinner.style.display = 'none';
    if (feed) feed.innerHTML = '';
    iframe.style.display = 'block';
    iframe.src = url;
  }
}

function setupContinuousPageSlots(numPages) {
  const feed = document.getElementById('pdf-pages-feed');
  if (!feed) return;

  feed.innerHTML = '';
  for (let i = 1; i <= numPages; i++) {
    const slot = document.createElement('div');
    slot.className = 'pdf-page-card';
    slot.id = `pdf-page-slot-${i}`;
    slot.setAttribute('data-page-number', i.toString());

    slot.innerHTML = `
      <div class="pdf-page-card-header mono">
        <span>PAGE ${i}</span>
        <span>OF ${numPages}</span>
      </div>
      <canvas id="pdf-canvas-p${i}" class="pdf-page-canvas"></canvas>
    `;

    feed.appendChild(slot);
  }
}

async function renderSingleContinuousPage(pageNum) {
  if (!activePdfDoc || pageNum < 1 || pageNum > totalPdfPages) return;
  if (renderedPagesMap.has(pageNum)) return;

  const canvas = document.getElementById(`pdf-canvas-p${pageNum}`);
  if (!canvas) return;

  try {
    const page = await activePdfDoc.getPage(pageNum);
    const ctx = canvas.getContext('2d');

    // Calculate container-aware scale
    const feed = document.getElementById('pdf-pages-feed');
    const containerWidth = feed ? Math.min(820, feed.clientWidth - 16) : 600;
    const unscaledViewport = page.getViewport({ scale: 1.0 });

    const computedScale = (containerWidth / unscaledViewport.width) * (pdfScale || 1.0);
    const dpr = Math.min(window.devicePixelRatio || 1, 2); // 2x for sharp retina rendering
    const viewport = page.getViewport({ scale: computedScale * dpr });

    canvas.width = viewport.width;
    canvas.height = viewport.height;
    canvas.style.width = `${viewport.width / dpr}px`;
    canvas.style.height = `${viewport.height / dpr}px`;

    const renderContext = {
      canvasContext: ctx,
      viewport: viewport
    };

    await page.render(renderContext).promise;
    renderedPagesMap.add(pageNum);
  } catch (e) {
    console.warn(`Failed rendering continuous page ${pageNum}:`, e);
  }
}

function setupPageIntersectionObserver() {
  if (pageIntersectionObserver) {
    pageIntersectionObserver.disconnect();
  }

  const indicator = document.getElementById('pdf-page-indicator');
  const scrollBody = document.getElementById('pdf-modal-body');

  pageIntersectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const pageNum = parseInt(entry.target.getAttribute('data-page-number'), 10);
      if (entry.isIntersecting) {
        renderSingleContinuousPage(pageNum);
        if (pageNum < totalPdfPages) renderSingleContinuousPage(pageNum + 1);

        if (indicator) {
          indicator.innerText = `Page ${pageNum} / ${totalPdfPages}`;
        }
      }
    });
  }, {
    root: scrollBody,
    rootMargin: '500px 0px 500px 0px', // Pre-render before page comes into view
    threshold: 0.1
  });

  document.querySelectorAll('.pdf-page-card').forEach(card => {
    pageIntersectionObserver.observe(card);
  });
}

function zoomPdf(delta) {
  pdfScale = Math.max(0.6, Math.min(2.2, pdfScale + delta));
  renderedPagesMap.clear();

  const slots = document.querySelectorAll('.pdf-page-card');
  slots.forEach(slot => {
    const p = parseInt(slot.getAttribute('data-page-number'), 10);
    renderSingleContinuousPage(p);
  });
}

function closePdfModal() {
  sfx.playHapticTap();
  const modal = document.getElementById('pdf-modal-backdrop');
  const frame = document.getElementById('pdf-iframe');
  const feed = document.getElementById('pdf-pages-feed');

  if (pageIntersectionObserver) {
    pageIntersectionObserver.disconnect();
    pageIntersectionObserver = null;
  }

  activePdfDoc = null;
  renderedPagesMap.clear();

  if (modal) {
    modal.classList.remove('open');
    if (frame) frame.src = '';
    if (feed) feed.innerHTML = '';
    document.body.style.overflow = '';
  }
}

// Listeners & Shortcuts Setup
function setupListeners() {
  // Sound FX Toggle
  document.getElementById('sound-toggle-btn')?.addEventListener('click', () => sfx.toggle());
  const soundBtnText = document.getElementById('sound-toggle-text');
  if (soundBtnText) soundBtnText.innerText = sfx.enabled ? 'SFX: ON' : 'SFX: OFF';

  // Quick Filter Input
  const quickFilter = document.getElementById('quick-filter-input');
  if (quickFilter) {
    quickFilter.addEventListener('input', (e) => handleQuickFilter(e.target.value));
  }

  // Header Controls
  document.getElementById('theme-toggle-btn')?.addEventListener('click', toggleTheme);
  document.getElementById('surprise-me-btn')?.addEventListener('click', pickRandomSubject);

  // Modal Closers
  document.getElementById('close-pdf-modal-btn')?.addEventListener('click', closePdfModal);

  // Close modals on backdrop click
  document.getElementById('pdf-modal-backdrop')?.addEventListener('click', (e) => {
    if (e.target.id === 'pdf-modal-backdrop') closePdfModal();
  });
  document.getElementById('leaked-notice-modal-backdrop')?.addEventListener('click', (e) => {
    if (e.target.id === 'leaked-notice-modal-backdrop') closeLeakedNoticeModal();
  });

  // Tactile Scroll Sound Listener (Responsive & Haptic)
  window.addEventListener('scroll', () => {
    const currentY = window.scrollY;
    if (Math.abs(currentY - sfx.lastScrollY) > 55) {
      sfx.playScrollTick();
      sfx.lastScrollY = currentY;
    }
  }, { passive: true });

  // Unlock AudioContext on first user interaction
  document.addEventListener('pointerdown', () => sfx.init(), { once: true });
  document.addEventListener('keydown', () => sfx.init(), { once: true });

  // Global Keyboard Shortcuts
  document.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') {
      if (e.key === 'Escape') {
        e.target.blur();
        closePdfModal();
        closeZenMode();
      }
      return;
    }
    
    if (e.key === '/' || ((e.metaKey || e.ctrlKey) && e.key === 'k')) {
      e.preventDefault();
      document.getElementById('quick-filter-input')?.focus();
    } else if (e.key === 't' || e.key === 'T') {
      toggleTheme();
    } else if (e.key === 'r' || e.key === 'R') {
      pickRandomSubject();
    } else if (e.key === 'l' || e.key === 'L') {
      openLeakedNoticeModal();
    } else if (e.key === 'z' || e.key === 'Z') {
      openZenMode();
    } else if (e.key === 'Escape') {
      closePdfModal();
      closeVisitorsModal();
      closeLeaveReviewModal();
      closeLeakedNoticeModal();
      closeZenMode();
    }
  });
}

// ==============================================================================
// 2083 Leaked Question Papers Meme Modal Engine (Suspicious Side-Eye Dog)
// ==============================================================================

function openLeakedNoticeModal() {
  const modal = document.getElementById('leaked-notice-modal-backdrop');
  if (!modal) return;

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';

  if (sfx) {
    sfx.playAlertChime();
  }

  showToast('🐶 Caught you looking for leaked question papers!');
}

function closeLeakedNoticeModal() {
  const modal = document.getElementById('leaked-notice-modal-backdrop');
  if (!modal) return;

  modal.classList.remove('open');
  document.body.style.overflow = '';
  if (sfx) sfx.playHapticTap();
}

function handleMemeGoStudy() {
  closeLeakedNoticeModal();
  if (sfx) sfx.playHapticPop();

  const grid = document.getElementById('subject-grid');
  if (grid) {
    grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
    document.querySelectorAll('.subject-slot').forEach(slot => {
      slot.classList.remove('leaked-target-highlight');
      void slot.offsetWidth;
      slot.classList.add('leaked-target-highlight');
    });
  }
  showToast('📚 Smart choice! Opening verified master solutions.');
}

function handleMemeGoTimers() {
  closeLeakedNoticeModal();
  if (sfx) sfx.playHapticTap();

  const timerSection = document.getElementById('exam-timer-section');
  if (timerSection) {
    timerSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
  showToast('⏱️ BCT 2083 Exam Countdown Timers');
}

// Temporal Wavy Time Motion Ripple on Tap / Click
function setupWaveRippleEffect() {
  let host = document.getElementById('wave-ripple-host');
  if (!host) {
    host = document.createElement('div');
    host.id = 'wave-ripple-host';
    host.className = 'wave-ripple-host';
    document.body.appendChild(host);
  }

  const triggerWave = (clientX, clientY) => {
    if (clientX === undefined || clientY === undefined) return;

    const ripple = document.createElement('div');
    ripple.className = 'temporal-wave-ripple';
    ripple.style.left = `${clientX}px`;
    ripple.style.top = `${clientY}px`;

    ripple.innerHTML = `
      <div class="wave-ring wave-ring-1"></div>
      <div class="wave-ring wave-ring-2"></div>
      <div class="wave-ring wave-ring-3"></div>
    `;

    host.appendChild(ripple);

    setTimeout(() => {
      if (ripple.parentNode) ripple.parentNode.removeChild(ripple);
    }, 1100);
  };

  // Listen globally to all taps and clicks
  window.addEventListener('pointerdown', (e) => {
    triggerWave(e.clientX, e.clientY);
  }, { passive: true });
}
