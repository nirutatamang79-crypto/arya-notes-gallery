/**
 * Minimalist BCT Exam Countdown Timer Engine
 * Computes live countdowns, handles views, theme switching, zen mode, and calendar exports.
 * All exams start at 1:00 PM Nepal Time (Asia/Kathmandu, UTC+5:45).
 */

// Schedule Data Definition (6 Theory Subjects)
const EXAM_SCHEDULE = [
  {
    id: 'ensh151',
    code: 'ENSH 151',
    name: 'Engineering Mathematics II',
    dateBS: '2083-05-16',
    dateAD: 'September 1, 2026',
    targetDateStr: '2026-09-01T13:00:00+05:45',
    endDateStr: '2026-09-01T16:00:00+05:45',
    durationHours: 3,
    description: 'Calculus, Ordinary Differential Equations, Linear Algebra & Vectors'
  },
  {
    id: 'enex151',
    code: 'ENEX 151',
    name: 'Electronic Device & Circuit',
    dateBS: '2083-05-20',
    dateAD: 'September 5, 2026',
    targetDateStr: '2026-09-05T13:00:00+05:45',
    endDateStr: '2026-09-05T16:00:00+05:45',
    durationHours: 3,
    description: 'Semiconductor Diodes, BJT, FET, Op-Amps & Amplifier Circuits'
  },
  {
    id: 'ensh153',
    code: 'ENSH 153',
    name: 'Engineering Chemistry',
    dateBS: '2083-05-24',
    dateAD: 'September 9, 2026',
    targetDateStr: '2026-09-09T13:00:00+05:45',
    endDateStr: '2026-09-09T16:00:00+05:45',
    durationHours: 3,
    description: 'Electrochemistry, Polymers, Water Technology & Engineering Materials'
  },
  {
    id: 'enct151',
    code: 'ENCT 151',
    name: 'Object Oriented Programming',
    dateBS: '2083-05-28',
    dateAD: 'September 13, 2026',
    targetDateStr: '2026-09-13T13:00:00+05:45',
    endDateStr: '2026-09-13T16:00:00+05:45',
    durationHours: 3,
    description: 'C++ Concepts, Classes & Objects, Inheritance, Polymorphism & Templates'
  },
  {
    id: 'enex152',
    code: 'ENEX 152',
    name: 'Digital Logics',
    dateBS: '2083-06-01',
    dateAD: 'September 17, 2026',
    targetDateStr: '2026-09-17T13:00:00+05:45',
    endDateStr: '2026-09-17T16:00:00+05:45',
    durationHours: 3,
    description: 'Boolean Algebra, Combinational Logic, Sequential Circuits, Counters & Registers'
  },
  {
    id: 'enee154',
    code: 'ENEE 154',
    name: 'Electrical Circuit & Machines',
    dateBS: '2083-06-05',
    dateAD: 'September 21, 2026',
    targetDateStr: '2026-09-21T13:00:00+05:45',
    endDateStr: '2026-09-21T16:00:00+05:45',
    durationHours: 3,
    description: 'Network Theorems, AC Circuits, Transformers, DC & AC Machines'
  }
];

// App State
const state = {
  currentView: 'grid', // 'grid' | 'table' | 'timeline'
  theme: localStorage.getItem('theme') || 'dark',
  zenSubjectId: null,
  activeFilter: 'all'
};

// Zero-padding helper
function padZero(num) {
  return String(num).padStart(2, '0');
}

// Calculate remaining time object
function getTimeBreakdown(targetMs, nowMs) {
  const diff = targetMs - nowMs;
  if (diff <= 0) {
    return {
      days: 0,
      hours: 0,
      minutes: 0,
      seconds: 0,
      totalHours: 0,
      totalMinutes: 0,
      totalSeconds: 0,
      isPassed: true
    };
  }

  const totalSeconds = Math.floor(diff / 1000);
  const totalMinutes = Math.floor(diff / (1000 * 60));
  const totalHours = Math.floor(diff / (1000 * 60 * 60));
  const days = Math.floor(totalSeconds / (3600 * 24));
  const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  return {
    days,
    hours,
    minutes,
    seconds,
    totalHours,
    totalMinutes,
    totalSeconds,
    isPassed: false
  };
}

// Determine status of an exam
function getExamStatus(exam, nowMs) {
  const startMs = new Date(exam.targetDateStr).getTime();
  const endMs = new Date(exam.endDateStr).getTime();

  if (nowMs < startMs) {
    return { type: 'upcoming', label: 'Upcoming', class: 'upcoming' };
  } else if (nowMs >= startMs && nowMs <= endMs) {
    return { type: 'in-progress', label: 'Happening Now (1 PM - 4 PM)', class: 'today' };
  } else {
    return { type: 'completed', label: 'Completed', class: 'passed' };
  }
}

// Web Audio API Gentle Chime
function playGentleChime() {
  try {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (!AudioContext) return;
    const ctx = new AudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(587.33, ctx.currentTime); // D5
    osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.1); // A5

    gain.gain.setValueAtTime(0.01, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.2, ctx.currentTime + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.8);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + 0.85);
  } catch (e) {
    console.log('Audio chime not available');
  }
}

// Render Hero Spotlight (Next Pending Exam)
function updateHeroSpotlight(nowMs) {
  // Find closest upcoming or in-progress exam
  let nextExam = EXAM_SCHEDULE.find(item => {
    const endMs = new Date(item.endDateStr).getTime();
    return nowMs < endMs;
  });

  if (!nextExam) {
    nextExam = EXAM_SCHEDULE[EXAM_SCHEDULE.length - 1];
  }

  const startMs = new Date(nextExam.targetDateStr).getTime();
  const endMs = new Date(nextExam.endDateStr).getTime();
  const status = getExamStatus(nextExam, nowMs);

  const heroCodeEl = document.getElementById('hero-code');
  const heroTitleEl = document.getElementById('hero-title');
  const heroDateBSEl = document.getElementById('hero-date-bs');
  const heroDateADEl = document.getElementById('hero-date-ad');
  const heroStatusPillEl = document.getElementById('hero-status-pill');

  const heroDaysEl = document.getElementById('hero-days');
  const heroHoursEl = document.getElementById('hero-hours');
  const heroMinsEl = document.getElementById('hero-mins');
  const heroSecsEl = document.getElementById('hero-secs');
  const heroProgressBar = document.getElementById('hero-progress-fill');
  const heroProgressPercent = document.getElementById('hero-progress-percent');

  if (heroCodeEl) heroCodeEl.textContent = nextExam.code;
  if (heroTitleEl) heroTitleEl.textContent = nextExam.name;
  if (heroDateBSEl) heroDateBSEl.textContent = `${nextExam.dateBS} B.S.`;
  if (heroDateADEl) heroDateADEl.textContent = `${nextExam.dateAD} • 1:00 PM NPT`;
  
  if (heroStatusPillEl) {
    heroStatusPillEl.innerHTML = `<span class="live-dot"></span> Next Target`;
    if (status.type === 'in-progress') {
      heroStatusPillEl.innerHTML = `<span class="live-dot" style="background:#fbbf24;box-shadow:0 0 8px #fbbf24"></span> In Progress (1 PM - 4 PM)`;
    } else if (status.type === 'completed') {
      heroStatusPillEl.innerHTML = `✓ Completed`;
    }
  }

  const breakdown = getTimeBreakdown(startMs, nowMs);

  if (heroDaysEl) heroDaysEl.textContent = padZero(breakdown.days);
  if (heroHoursEl) heroHoursEl.textContent = padZero(breakdown.hours);
  if (heroMinsEl) heroMinsEl.textContent = padZero(breakdown.minutes);
  if (heroSecsEl) heroSecsEl.textContent = padZero(breakdown.seconds);

  // Approximate preparation progress
  // Anchor date: August 20, 2026
  const prepStartMs = new Date('2026-08-20T00:00:00+05:45').getTime();
  const totalWindow = startMs - prepStartMs;
  const elapsed = nowMs - prepStartMs;
  let progressPct = Math.min(100, Math.max(0, (elapsed / totalWindow) * 100));

  if (status.type === 'in-progress' || status.type === 'completed') {
    progressPct = 100;
  }

  if (heroProgressBar) heroProgressBar.style.width = `${progressPct.toFixed(1)}%`;
  if (heroProgressPercent) heroProgressPercent.textContent = `${progressPct.toFixed(0)}% Time Elapsed`;

  // Attach quick focus button target
  const heroFocusBtn = document.getElementById('hero-focus-btn');
  if (heroFocusBtn) {
    heroFocusBtn.onclick = () => openZenMode(nextExam.id);
  }
}

// Render Card Grid View
function renderCardsGrid(nowMs) {
  const container = document.getElementById('cards-grid-container');
  if (!container) return;

  const cardsHtml = EXAM_SCHEDULE.map((exam, idx) => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const status = getExamStatus(exam, nowMs);

    return `
      <div class="exam-card ${status.type === 'upcoming' && idx === 0 ? 'next-up' : ''} ${status.type === 'completed' ? 'completed' : ''}" data-id="${exam.id}">
        <div class="card-top">
          <span class="card-code">${exam.code}</span>
          <span class="card-order-tag">#0${idx + 1}</span>
        </div>
        
        <h3 class="card-subject-name">${exam.name}</h3>
        
        <div class="card-dates">
          <div class="date-row">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <span class="date-tag-bs">${exam.dateBS} B.S.</span>
          </div>
          <div class="date-row">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            <span class="date-tag-ad">${exam.dateAD} • <strong>1:00 PM NPT</strong></span>
          </div>
        </div>

        <div class="card-timer-row">
          <div class="mini-unit">
            <span class="mini-val" id="card-${exam.id}-d">${padZero(breakdown.days)}</span>
            <span class="mini-lbl">Days</span>
          </div>
          <div class="mini-unit">
            <span class="mini-val" id="card-${exam.id}-h">${padZero(breakdown.hours)}</span>
            <span class="mini-lbl">Hours</span>
          </div>
          <div class="mini-unit">
            <span class="mini-val" id="card-${exam.id}-m">${padZero(breakdown.minutes)}</span>
            <span class="mini-lbl">Mins</span>
          </div>
          <div class="mini-unit">
            <span class="mini-val" id="card-${exam.id}-s">${padZero(breakdown.seconds)}</span>
            <span class="mini-lbl">Secs</span>
          </div>
        </div>

        <div class="card-status-banner">
          <span class="status-badge ${status.class}">
            ${status.type === 'in-progress' ? '● ' : '○ '}${status.label}
          </span>
          <button class="control-btn" style="padding:0.25rem 0.6rem; font-size:0.75rem;" onclick="openZenMode('${exam.id}')">
            Focus Mode
          </button>
        </div>
      </div>
    `;
  }).join('');

  container.innerHTML = cardsHtml;
}

// Update existing Card numbers smoothly without full re-render
function updateCardNumbers(nowMs) {
  EXAM_SCHEDULE.forEach(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);

    const dEl = document.getElementById(`card-${exam.id}-d`);
    const hEl = document.getElementById(`card-${exam.id}-h`);
    const mEl = document.getElementById(`card-${exam.id}-m`);
    const sEl = document.getElementById(`card-${exam.id}-s`);

    if (dEl) dEl.textContent = padZero(breakdown.days);
    if (hEl) hEl.textContent = padZero(breakdown.hours);
    if (mEl) mEl.textContent = padZero(breakdown.minutes);
    if (sEl) sEl.textContent = padZero(breakdown.seconds);
  });
}

// Render Table View
function renderTableView(nowMs) {
  const container = document.getElementById('table-view-container');
  if (!container) return;

  const rowsHtml = EXAM_SCHEDULE.map((exam, idx) => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const status = getExamStatus(exam, nowMs);

    return `
      <tr class="${status.type === 'upcoming' && idx === 0 ? 'highlight-row' : ''}">
        <td><span class="card-code">${exam.code}</span></td>
        <td><strong>${exam.name}</strong><br><small style="color:var(--text-muted)">${exam.description}</small></td>
        <td><span class="date-tag-bs">${exam.dateBS} B.S.</span></td>
        <td>${exam.dateAD}</td>
        <td><strong>1:00 PM NPT</strong></td>
        <td>
          <span class="table-timer-inline" id="table-${exam.id}-timer">
            ${padZero(breakdown.days)}d : ${padZero(breakdown.hours)}h : ${padZero(breakdown.minutes)}m : ${padZero(breakdown.seconds)}s
          </span>
        </td>
        <td>
          <span class="status-badge ${status.class}">${status.label}</span>
        </td>
      </tr>
    `;
  }).join('');

  container.innerHTML = `
    <table class="exam-table">
      <thead>
        <tr>
          <th>Code</th>
          <th>Subject Name</th>
          <th>Date (B.S.)</th>
          <th>Date (A.D.)</th>
          <th>Time (Kathmandu)</th>
          <th>Time Left</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        ${rowsHtml}
      </tbody>
    </table>
  `;
}

function updateTableNumbers(nowMs) {
  EXAM_SCHEDULE.forEach(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const timerEl = document.getElementById(`table-${exam.id}-timer`);
    if (timerEl) {
      timerEl.textContent = `${padZero(breakdown.days)}d : ${padZero(breakdown.hours)}h : ${padZero(breakdown.minutes)}m : ${padZero(breakdown.seconds)}s`;
    }
  });
}

// Render Timeline View
function renderTimelineView(nowMs) {
  const container = document.getElementById('timeline-view-container');
  if (!container) return;

  const itemsHtml = EXAM_SCHEDULE.map((exam) => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const status = getExamStatus(exam, nowMs);

    return `
      <div class="timeline-item ${status.type === 'upcoming' ? 'active' : ''}">
        <div class="timeline-dot"></div>
        <div class="timeline-card">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
            <span class="card-code">${exam.code}</span>
            <span style="font-family:var(--font-mono); font-size:0.85rem; color:var(--accent-cyan);" id="tl-${exam.id}-timer">
              ${padZero(breakdown.days)}d ${padZero(breakdown.hours)}h ${padZero(breakdown.minutes)}m ${padZero(breakdown.seconds)}s
            </span>
          </div>
          <h4 style="font-size:1.05rem; font-weight:700; margin-bottom:0.25rem;">${exam.name}</h4>
          <p style="font-size:0.82rem; color:var(--text-secondary); margin-bottom:0.5rem;">
            <strong>${exam.dateBS} B.S.</strong> • ${exam.dateAD} • <strong>1:00 PM NPT</strong>
          </p>
          <p style="font-size:0.8rem; color:var(--text-muted);">${exam.description}</p>
        </div>
      </div>
    `;
  }).join('');

  container.innerHTML = `
    <div class="timeline-line"></div>
    ${itemsHtml}
  `;
}

function updateTimelineNumbers(nowMs) {
  EXAM_SCHEDULE.forEach(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const timerEl = document.getElementById(`tl-${exam.id}-timer`);
    if (timerEl) {
      timerEl.textContent = `${padZero(breakdown.days)}d ${padZero(breakdown.hours)}h ${padZero(breakdown.minutes)}m ${padZero(breakdown.seconds)}s`;
    }
  });
}

// Live Clock in Header (Formatted for Nepal Time / Asia/Kathmandu)
function updateLiveClock(nowDate) {
  const clockEl = document.getElementById('live-clock');
  if (!clockEl) return;

  try {
    const nptTime = nowDate.toLocaleTimeString('en-US', {
      timeZone: 'Asia/Kathmandu',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
      hour12: true
    });
    const nptDate = nowDate.toLocaleDateString('en-US', {
      timeZone: 'Asia/Kathmandu',
      weekday: 'short',
      month: 'short',
      day: 'numeric'
    });
    clockEl.textContent = `${nptDate} • ${nptTime} NPT`;
  } catch (e) {
    clockEl.textContent = nowDate.toLocaleString('en-US', { hour12: true });
  }
}

// Zen / Focus Mode
window.openZenMode = function(subjectId) {
  let targetExam = EXAM_SCHEDULE.find(e => e.id === subjectId);
  if (!targetExam) targetExam = EXAM_SCHEDULE[0];

  state.zenSubjectId = targetExam.id;

  const zenModal = document.getElementById('zen-modal');
  const zenCode = document.getElementById('zen-code');
  const zenTitle = document.getElementById('zen-title');
  const zenDates = document.getElementById('zen-dates');

  if (zenCode) zenCode.textContent = targetExam.code;
  if (zenTitle) zenTitle.textContent = targetExam.name;
  if (zenDates) zenDates.textContent = `${targetExam.dateBS} B.S. • ${targetExam.dateAD} (1:00 PM NPT)`;

  if (zenModal) zenModal.classList.add('active');
  playGentleChime();
};

window.closeZenMode = function() {
  const zenModal = document.getElementById('zen-modal');
  if (zenModal) zenModal.classList.remove('active');
  state.zenSubjectId = null;
};

function updateZenNumbers(nowMs) {
  if (!state.zenSubjectId) return;
  const exam = EXAM_SCHEDULE.find(e => e.id === state.zenSubjectId);
  if (!exam) return;

  const startMs = new Date(exam.targetDateStr).getTime();
  const breakdown = getTimeBreakdown(startMs, nowMs);

  const zDays = document.getElementById('zen-days');
  const zHours = document.getElementById('zen-hours');
  const zMins = document.getElementById('zen-mins');
  const zSecs = document.getElementById('zen-secs');

  if (zDays) zDays.textContent = padZero(breakdown.days);
  if (zHours) zHours.textContent = padZero(breakdown.hours);
  if (zMins) zMins.textContent = padZero(breakdown.minutes);
  if (zSecs) zSecs.textContent = padZero(breakdown.seconds);

  // Cumulative Totals
  const zTotalHours = document.getElementById('zen-total-hours');
  const zTotalMinutes = document.getElementById('zen-total-minutes');
  const zTotalSeconds = document.getElementById('zen-total-seconds');

  if (zTotalHours) zTotalHours.textContent = breakdown.totalHours.toLocaleString('en-US');
  if (zTotalMinutes) zTotalMinutes.textContent = breakdown.totalMinutes.toLocaleString('en-US');
  if (zTotalSeconds) zTotalSeconds.textContent = breakdown.totalSeconds.toLocaleString('en-US');
}

// Generate .ics Calendar Download File
function downloadCalendarFile() {
  let icsLines = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//BCT Exam Schedule Kathmandu//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH'
  ];

  EXAM_SCHEDULE.forEach(exam => {
    const startDate = new Date(exam.targetDateStr);
    const endDate = new Date(exam.endDateStr);

    const formatIcsDate = (d) => {
      return d.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';
    };

    icsLines.push('BEGIN:VEVENT');
    icsLines.push(`UID:${exam.id}-bct-2083@exam-timer`);
    icsLines.push(`DTSTAMP:${formatIcsDate(new Date())}`);
    icsLines.push(`DTSTART:${formatIcsDate(startDate)}`);
    icsLines.push(`DTEND:${formatIcsDate(endDate)}`);
    icsLines.push(`SUMMARY:BCT Exam: ${exam.code} - ${exam.name}`);
    icsLines.push(`DESCRIPTION:${exam.name} (${exam.code})\\nNepali Date: ${exam.dateBS} B.S.\\nEnglish Date: ${exam.dateAD}\\nTime: 1:00 PM - 4:00 PM (Nepal Standard Time UTC+5:45)\\n${exam.description}`);
    icsLines.push('BEGIN:VALARM');
    icsLines.push('TRIGGER:-PT24H');
    icsLines.push('ACTION:DISPLAY');
    icsLines.push(`DESCRIPTION:Reminder: ${exam.name} (${exam.code}) exam tomorrow at 1:00 PM NPT`);
    icsLines.push('END:VALARM');
    icsLines.push('END:VEVENT');
  });

  icsLines.push('END:VCALENDAR');

  const blob = new Blob([icsLines.join('\r\n')], { type: 'text/calendar;charset=utf-8' });
  const link = document.createElement('a');
  link.href = window.URL.createObjectURL(blob);
  link.setAttribute('download', 'BCT_Exam_Schedule_2083_NPT.ics');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

// Notification Request
function requestNotificationAccess() {
  if (!('Notification' in window)) {
    alert('Browser notifications are not supported on this device.');
    return;
  }
  Notification.requestPermission().then(perm => {
    if (perm === 'granted') {
      new Notification('BCT Exam Timer (Kathmandu Time)', {
        body: 'Notifications enabled! You will be reminded for upcoming 1:00 PM NPT exams.',
        icon: 'favicon.svg'
      });
    }
  });
}

// Switch View Mode
function switchView(viewName) {
  state.currentView = viewName;
  const gridWrapper = document.getElementById('cards-grid-container');
  const tableWrapper = document.getElementById('table-view-container');
  const timelineWrapper = document.getElementById('timeline-view-container');

  const btnGrid = document.getElementById('view-grid-btn');
  const btnTable = document.getElementById('view-table-btn');
  const btnTimeline = document.getElementById('view-timeline-btn');

  [btnGrid, btnTable, btnTimeline].forEach(b => b && b.classList.remove('active'));

  if (viewName === 'grid') {
    if (gridWrapper) gridWrapper.style.display = 'grid';
    if (tableWrapper) tableWrapper.style.display = 'none';
    if (timelineWrapper) timelineWrapper.style.display = 'none';
    if (btnGrid) btnGrid.classList.add('active');
  } else if (viewName === 'table') {
    if (gridWrapper) gridWrapper.style.display = 'none';
    if (tableWrapper) tableWrapper.style.display = 'block';
    if (timelineWrapper) timelineWrapper.style.display = 'none';
    if (btnTable) btnTable.classList.add('active');
  } else if (viewName === 'timeline') {
    if (gridWrapper) gridWrapper.style.display = 'none';
    if (tableWrapper) tableWrapper.style.display = 'none';
    if (timelineWrapper) timelineWrapper.style.display = 'block';
    if (btnTimeline) btnTimeline.classList.add('active');
  }
}

// Theme Toggle
function toggleTheme() {
  state.theme = state.theme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', state.theme);
  localStorage.setItem('theme', state.theme);

  const themeBtn = document.getElementById('theme-toggle-btn');
  if (themeBtn) {
    themeBtn.innerHTML = state.theme === 'dark' 
      ? `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg> Light Mode`
      : `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg> Dark Mode`;
  }
}

// Core Tick Loop
function tick() {
  const now = new Date();
  const nowMs = now.getTime();

  updateLiveClock(now);
  updateHeroSpotlight(nowMs);

  if (state.currentView === 'grid') {
    updateCardNumbers(nowMs);
  } else if (state.currentView === 'table') {
    updateTableNumbers(nowMs);
  } else if (state.currentView === 'timeline') {
    updateTimelineNumbers(nowMs);
  }

  if (state.zenSubjectId) {
    updateZenNumbers(nowMs);
  }
}

// Initialization on DOM Ready
document.addEventListener('DOMContentLoaded', () => {
  // Set saved theme
  document.documentElement.setAttribute('data-theme', state.theme);

  // Initial Full Render
  const nowMs = Date.now();
  renderCardsGrid(nowMs);
  renderTableView(nowMs);
  renderTimelineView(nowMs);
  switchView('grid');

  // Event Listeners
  const themeBtn = document.getElementById('theme-toggle-btn');
  if (themeBtn) {
    themeBtn.addEventListener('click', toggleTheme);
    if (state.theme === 'light') {
      themeBtn.innerHTML = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg> Dark Mode`;
    }
  }

  document.getElementById('view-grid-btn')?.addEventListener('click', () => switchView('grid'));
  document.getElementById('view-table-btn')?.addEventListener('click', () => switchView('table'));
  document.getElementById('view-timeline-btn')?.addEventListener('click', () => switchView('timeline'));

  document.getElementById('export-cal-btn')?.addEventListener('click', downloadCalendarFile);
  document.getElementById('export-cal-btn-2')?.addEventListener('click', downloadCalendarFile);
  document.getElementById('notify-btn')?.addEventListener('click', requestNotificationAccess);
  document.getElementById('zen-close-btn')?.addEventListener('click', closeZenMode);

  // Keyboard shortcut: ESC to close Zen modal
  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeZenMode();
    }
  });

  // Run first tick immediately and start precise interval
  tick();
  setInterval(tick, 1000);
});
