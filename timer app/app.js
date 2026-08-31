/**
 * Minimalist BCT Exam Countdown Timer Engine
 * Computes live countdowns, handles views, theme switching, zen mode, and calendar exports.
 * All exams start at 1:00 PM Nepal Time (Asia/Kathmandu, UTC+5:45).
 * Revised Schedule as of 2083-05-15 (IOE Notice).
 */

// Schedule Data Definition (6 Theory Subjects - Revised 2083 Bhadra Schedule)
const EXAM_SCHEDULE = [
  {
    id: 'ensh151',
    code: 'ENSH 151',
    name: 'Engineering Mathematics II',
    dateBS: '2083-05-23',
    dateAD: 'September 8, 2026',
    targetDateStr: '2026-09-08T13:00:00+05:45',
    endDateStr: '2026-09-08T16:00:00+05:45',
    durationHours: 3,
    description: 'Calculus, Ordinary Differential Equations, Linear Algebra & Vectors'
  },
  {
    id: 'enex151',
    code: 'ENEX 151',
    name: 'Electronic Device & Circuit',
    dateBS: '2083-05-27',
    dateAD: 'September 12, 2026',
    targetDateStr: '2026-09-12T13:00:00+05:45',
    endDateStr: '2026-09-12T16:00:00+05:45',
    durationHours: 3,
    description: 'Semiconductor Diodes, BJT, FET, Op-Amps & Amplifier Circuits'
  },
  {
    id: 'ensh153',
    code: 'ENSH 153',
    name: 'Engineering Chemistry',
    dateBS: '2083-05-31',
    dateAD: 'September 16, 2026',
    targetDateStr: '2026-09-16T13:00:00+05:45',
    endDateStr: '2026-09-16T16:00:00+05:45',
    durationHours: 3,
    description: 'Electrochemistry, Polymers, Water Technology & Engineering Materials'
  },
  {
    id: 'enct151',
    code: 'ENCT 151',
    name: 'Object Oriented Programming',
    dateBS: '2083-06-04',
    dateAD: 'September 20, 2026',
    targetDateStr: '2026-09-20T13:00:00+05:45',
    endDateStr: '2026-09-20T16:00:00+05:45',
    durationHours: 3,
    description: 'C++ Concepts, Classes & Objects, Inheritance, Polymorphism & Templates'
  },
  {
    id: 'enex152',
    code: 'ENEX 152',
    name: 'Digital Logics',
    dateBS: '2083-06-08',
    dateAD: 'September 24, 2026',
    targetDateStr: '2026-09-24T13:00:00+05:45',
    endDateStr: '2026-09-24T16:00:00+05:45',
    durationHours: 3,
    description: 'Boolean Algebra, Combinational Logic, Sequential Circuits, Counters & Registers'
  },
  {
    id: 'enee154',
    code: 'ENEE 154',
    name: 'Electrical Circuit & Machines',
    dateBS: '2083-06-12',
    dateAD: 'September 28, 2026',
    targetDateStr: '2026-09-28T13:00:00+05:45',
    endDateStr: '2026-09-28T16:00:00+05:45',
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

// Get next upcoming exam
function getNextUpcomingExam(nowMs) {
  for (const exam of EXAM_SCHEDULE) {
    const endMs = new Date(exam.endDateStr).getTime();
    if (nowMs < endMs) {
      return exam;
    }
  }
  return EXAM_SCHEDULE[0];
}

// Format date into human-readable format
function formatDateTimeNPT(dateObj) {
  return dateObj.toLocaleTimeString('en-US', {
    timeZone: 'Asia/Kathmandu',
    hour12: false,
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  });
}

// Update Live Clock Header
function updateLiveClock(now) {
  const clockEl = document.getElementById('live-clock');
  if (clockEl) {
    try {
      const timeStr = formatDateTimeNPT(now);
      clockEl.textContent = `${timeStr} NPT (UTC+5:45)`;
    } catch (e) {
      clockEl.textContent = `${padZero(now.getHours())}:${padZero(now.getMinutes())}:${padZero(now.getSeconds())} NPT`;
    }
  }
}

// Update Hero Spotlight (Next Target)
function updateHeroSpotlight(nowMs) {
  const nextExam = getNextUpcomingExam(nowMs);
  const targetMs = new Date(nextExam.targetDateStr).getTime();
  const breakdown = getTimeBreakdown(targetMs, nowMs);

  const heroCode = document.getElementById('hero-code');
  const heroTitle = document.getElementById('hero-title');
  const heroDateBs = document.getElementById('hero-date-bs');
  const heroDateAd = document.getElementById('hero-date-ad');
  const heroDays = document.getElementById('hero-days');
  const heroHours = document.getElementById('hero-hours');
  const heroMins = document.getElementById('hero-mins');
  const heroSecs = document.getElementById('hero-secs');
  const heroPercent = document.getElementById('hero-progress-percent');
  const heroFill = document.getElementById('hero-progress-fill');

  if (heroCode) heroCode.textContent = nextExam.code;
  if (heroTitle) heroTitle.textContent = nextExam.name;
  if (heroDateBs) heroDateBs.textContent = `${nextExam.dateBS} B.S.`;
  if (heroDateAd) heroDateAd.textContent = `${nextExam.dateAD} • 1:00 PM NPT`;

  if (heroDays) heroDays.textContent = padZero(breakdown.days);
  if (heroHours) heroHours.textContent = padZero(breakdown.hours);
  if (heroMins) heroMins.textContent = padZero(breakdown.minutes);
  if (heroSecs) heroSecs.textContent = padZero(breakdown.seconds);

  // Progress relative to preparation window
  const totalWindowMs = 30 * 24 * 60 * 60 * 1000;
  const remainingMs = Math.max(0, targetMs - nowMs);
  const percentPassed = Math.min(100, Math.max(0, Math.round(((totalWindowMs - remainingMs) / totalWindowMs) * 100)));

  if (heroPercent) heroPercent.textContent = `${percentPassed}%`;
  if (heroFill) heroFill.style.width = `${percentPassed}%`;
}

// Render Subject Cards Grid
function renderCardsGrid(nowMs) {
  const container = document.getElementById('cards-grid-container');
  if (!container) return;

  container.innerHTML = EXAM_SCHEDULE.map(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);

    let statusTag = '';
    if (breakdown.isPassed) {
      statusTag = '<span class="status-pill completed">Completed</span>';
    } else if (breakdown.days === 0 && breakdown.hours < 3) {
      statusTag = '<span class="status-pill live">Happening Today</span>';
    } else {
      statusTag = '<span class="status-pill upcoming">Upcoming</span>';
    }

    return `
      <div class="card" id="card-${exam.id}">
        <div class="card-header">
          <div>
            <div class="card-code">${exam.code}</div>
            <h3 class="card-title">${exam.name}</h3>
          </div>
          ${statusTag}
        </div>

        <div class="card-meta">
          <div class="meta-row">
            <span class="meta-label">Date (B.S.):</span>
            <span class="meta-value">${exam.dateBS}</span>
          </div>
          <div class="meta-row">
            <span class="meta-label">Date (A.D.):</span>
            <span class="meta-value">${exam.dateAD}</span>
          </div>
          <div class="meta-row">
            <span class="meta-label">Exam Time:</span>
            <span class="meta-value">1:00 PM – 4:00 PM NPT</span>
          </div>
        </div>

        <div class="card-timer-grid">
          <div class="timer-box">
            <span class="timer-num" id="d-${exam.id}">${padZero(breakdown.days)}</span>
            <span class="timer-label">Days</span>
          </div>
          <div class="timer-box">
            <span class="timer-num" id="h-${exam.id}">${padZero(breakdown.hours)}</span>
            <span class="timer-label">Hours</span>
          </div>
          <div class="timer-box">
            <span class="timer-num" id="m-${exam.id}">${padZero(breakdown.minutes)}</span>
            <span class="timer-label">Mins</span>
          </div>
          <div class="timer-box">
            <span class="timer-num" id="s-${exam.id}">${padZero(breakdown.seconds)}</span>
            <span class="timer-label">Secs</span>
          </div>
        </div>

        <div class="card-actions">
          <button class="action-btn" onclick="openZenMode('${exam.id}')">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 14 14"></polyline></svg>
            Zen Focus
          </button>
        </div>
      </div>
    `;
  }).join('');
}

// Update Digits in Cards View
function updateCardNumbers(nowMs) {
  EXAM_SCHEDULE.forEach(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);

    const dEl = document.getElementById(`d-${exam.id}`);
    const hEl = document.getElementById(`h-${exam.id}`);
    const mEl = document.getElementById(`m-${exam.id}`);
    const sEl = document.getElementById(`s-${exam.id}`);

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

  container.innerHTML = `
    <table class="schedule-table">
      <thead>
        <tr>
          <th>Code</th>
          <th>Subject Name</th>
          <th>B.S. Date</th>
          <th>A.D. Date</th>
          <th>Time (NPT)</th>
          <th>Countdown</th>
          <th>Action</th>
        </tr>
      </thead>
      <tbody>
        ${EXAM_SCHEDULE.map(exam => {
          const startMs = new Date(exam.targetDateStr).getTime();
          const breakdown = getTimeBreakdown(startMs, nowMs);
          const timeText = breakdown.isPassed 
            ? 'Completed' 
            : `${breakdown.days}d ${padZero(breakdown.hours)}h ${padZero(breakdown.minutes)}m ${padZero(breakdown.seconds)}s`;

          return `
            <tr>
              <td><strong>${exam.code}</strong></td>
              <td>${exam.name}</td>
              <td>${exam.dateBS}</td>
              <td>${exam.dateAD}</td>
              <td>1:00 PM</td>
              <td id="table-timer-${exam.id}">${timeText}</td>
              <td>
                <button class="table-zen-btn" onclick="openZenMode('${exam.id}')">Focus</button>
              </td>
            </tr>
          `;
        }).join('')}
      </tbody>
    </table>
  `;
}

// Update Table Countdown Cells
function updateTableNumbers(nowMs) {
  EXAM_SCHEDULE.forEach(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const cell = document.getElementById(`table-timer-${exam.id}`);
    if (cell) {
      cell.textContent = breakdown.isPassed 
        ? 'Completed' 
        : `${breakdown.days}d ${padZero(breakdown.hours)}h ${padZero(breakdown.minutes)}m ${padZero(breakdown.seconds)}s`;
    }
  });
}

// Render Timeline View
function renderTimelineView(nowMs) {
  const container = document.getElementById('timeline-view-container');
  if (!container) return;

  container.innerHTML = `
    <div class="timeline-wrapper">
      ${EXAM_SCHEDULE.map((exam, index) => {
        const startMs = new Date(exam.targetDateStr).getTime();
        const breakdown = getTimeBreakdown(startMs, nowMs);

        return `
          <div class="timeline-node ${breakdown.isPassed ? 'passed' : ''}">
            <div class="timeline-marker">${index + 1}</div>
            <div class="timeline-card">
              <div class="timeline-header">
                <div>
                  <span class="timeline-code">${exam.code}</span>
                  <h4 class="timeline-title">${exam.name}</h4>
                </div>
                <span class="timeline-timer" id="timeline-timer-${exam.id}">
                  ${breakdown.isPassed ? 'Done' : `${breakdown.days}d ${padZero(breakdown.hours)}h left`}
                </span>
              </div>
              <p class="timeline-date">${exam.dateBS} B.S. (${exam.dateAD}) • 1:00 PM NPT</p>
              <p class="timeline-desc">${exam.description}</p>
            </div>
          </div>
        `;
      }).join('')}
    </div>
  `;
}

// Update Timeline Cells
function updateTimelineNumbers(nowMs) {
  EXAM_SCHEDULE.forEach(exam => {
    const startMs = new Date(exam.targetDateStr).getTime();
    const breakdown = getTimeBreakdown(startMs, nowMs);
    const cell = document.getElementById(`timeline-timer-${exam.id}`);
    if (cell) {
      cell.textContent = breakdown.isPassed ? 'Done' : `${breakdown.days}d ${padZero(breakdown.hours)}h left`;
    }
  });
}

// Zen / Focus Mode Logic
window.openZenMode = function(subjectId) {
  const exam = EXAM_SCHEDULE.find(e => e.id === subjectId) || getNextUpcomingExam(Date.now());
  if (!exam) return;

  state.zenSubjectId = exam.id;

  const zenCode = document.getElementById('zen-code');
  const zenTitle = document.getElementById('zen-title');
  const zenDates = document.getElementById('zen-dates');
  const zenModal = document.getElementById('zen-modal');

  if (zenCode) zenCode.textContent = exam.code;
  if (zenTitle) zenTitle.textContent = exam.name;
  if (zenDates) zenDates.textContent = `${exam.dateBS} B.S. • ${exam.dateAD} (1:00 PM NPT)`;

  if (zenModal) zenModal.classList.add('active');
  updateZenNumbers(Date.now());
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
