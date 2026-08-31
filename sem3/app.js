/**
 * IOE Tribhuvan University — BE Computer Engineering (BCT)
 * 3rd Semester (II/I New Course Regular) Exam Countdown Timer Engine
 * Exams occur exactly 24 hours after each 2nd Semester Exam.
 * Timezone: Asia/Kathmandu (NPT, UTC+5:45) · Start Time: 1:00 PM NPT
 */

// BCT 3rd Semester (II/I) Master Exam Schedule (24 Hours after 2nd Semester)
const SEM3_EXAM_SCHEDULE = [
  {
    id: 'ensh201',
    code: 'ENSH 201',
    name: 'Engineering Mathematics III',
    dateBS: '2083-05-24',
    dateAD: 'September 9, 2026',
    targetDateStr: '2026-09-09T13:00:00+05:45',
    endDateStr: '2026-09-09T16:00:00+05:45',
    accent: '#8b5cf6',
    desc: 'Complex Variables, Numerical Methods, Fourier & Z-Transforms, Linear Programming'
  },
  {
    id: 'enex201',
    code: 'ENEX 201',
    name: 'Electronic Devices & Circuits II',
    dateBS: '2083-05-28',
    dateAD: 'September 13, 2026',
    targetDateStr: '2026-09-13T13:00:00+05:45',
    endDateStr: '2026-09-13T16:00:00+05:45',
    accent: '#0284c7',
    desc: 'High-Frequency Models, Differential Amplifiers, Feedback, Oscillators & Waveguides'
  },
  {
    id: 'enct201',
    code: 'ENCT 201',
    name: 'Data Structures & Algorithms (DSA)',
    dateBS: '2083-06-01',
    dateAD: 'September 17, 2026',
    targetDateStr: '2026-09-17T13:00:00+05:45',
    endDateStr: '2026-09-17T16:00:00+05:45',
    accent: '#10b981',
    desc: 'Stacks, Queues, Trees, AVL, Graphs, Hashing, Sorting & Algorithm Complexity'
  },
  {
    id: 'enct202',
    code: 'ENCT 202',
    name: 'Discrete Structure',
    dateBS: '2083-06-05',
    dateAD: 'September 21, 2026',
    targetDateStr: '2026-09-21T13:00:00+05:45',
    endDateStr: '2026-09-21T16:00:00+05:45',
    accent: '#ec4899',
    desc: 'Propositional Logic, Proof Methods, Relations, Graph Theory, Combinatorics & Trees'
  },
  {
    id: 'enex202',
    code: 'ENEX 202',
    name: 'Microprocessors & Assembly Language',
    dateBS: '2083-06-09',
    dateAD: 'September 25, 2026',
    targetDateStr: '2026-09-25T13:00:00+05:45',
    endDateStr: '2026-09-25T16:00:00+05:45',
    accent: '#f59e0b',
    desc: '8085/8086 Architecture, Assembly Programming, Interrupts, 8255 PPI & Memory Interfacing'
  },
  {
    id: 'enee201',
    code: 'ENEE 201',
    name: 'Electrical Engineering Technology',
    dateBS: '2083-06-13',
    dateAD: 'September 29, 2026',
    targetDateStr: '2026-09-29T13:00:00+05:45',
    endDateStr: '2026-09-29T16:00:00+05:45',
    accent: '#06b6d4',
    desc: 'Sensors, Transducers, Signal Conditioning, Analog & Digital Instrumentation Systems'
  }
];

let timerViewMode = localStorage.getItem('sem3_timer_view') || 'cards';
let currentTheme = localStorage.getItem('theme') || 'light';
let zenActiveExamId = null;

function padZero(num) {
  return String(num).padStart(2, '0');
}

function getTimeBreakdown(targetMs, nowMs) {
  const diff = targetMs - nowMs;
  if (diff <= 0) {
    return { days: 0, hours: 0, minutes: 0, seconds: 0, isPassed: true };
  }
  const totalSecs = Math.floor(diff / 1000);
  const days = Math.floor(totalSecs / 86400);
  const hours = Math.floor((totalSecs % 86400) / 3600);
  const minutes = Math.floor((totalSecs % 3600) / 60);
  const seconds = totalSecs % 60;
  return { days, hours, minutes, seconds, isPassed: false };
}

function getExamStatus(exam, nowMs) {
  const startMs = new Date(exam.targetDateStr).getTime();
  const endMs = new Date(exam.endDateStr).getTime();
  if (nowMs < startMs) {
    return { label: 'Upcoming', class: 'upcoming' };
  } else if (nowMs >= startMs && nowMs <= endMs) {
    return { label: 'Exam in Progress (1-4 PM)', class: 'today' };
  } else {
    return { label: 'Completed', class: 'passed' };
  }
}

function getNextUpcomingExam(nowMs) {
  for (const exam of SEM3_EXAM_SCHEDULE) {
    const endMs = new Date(exam.endDateStr).getTime();
    if (nowMs < endMs) {
      return exam;
    }
  }
  return SEM3_EXAM_SCHEDULE[0];
}

function updateLiveClock(now) {
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
}

function updateTimerUI() {
  const now = new Date();
  const nowMs = now.getTime();

  updateLiveClock(now);

  // Update Hero Spotlight
  const nextExam = getNextUpcomingExam(nowMs);
  const targetMs = new Date(nextExam.targetDateStr).getTime();
  const heroT = getTimeBreakdown(targetMs, nowMs);

  const heroCode = document.getElementById('hero-code');
  const heroTitle = document.getElementById('hero-title');
  const heroDates = document.getElementById('hero-dates');
  const heroDays = document.getElementById('hero-days');
  const heroHours = document.getElementById('hero-hours');
  const heroMins = document.getElementById('hero-mins');
  const heroSecs = document.getElementById('hero-secs');
  const heroSpotlight = document.getElementById('hero-spotlight');

  if (heroCode) heroCode.innerText = nextExam.code;
  if (heroTitle) heroTitle.innerText = nextExam.name;
  if (heroDates) heroDates.innerText = `${nextExam.dateBS} B.S. · ${nextExam.dateAD} · 1:00 PM NPT (24h after Sem 2)`;
  if (heroDays) heroDays.innerText = padZero(heroT.days);
  if (heroHours) heroHours.innerText = padZero(heroT.hours);
  if (heroMins) heroMins.innerText = padZero(heroT.minutes);
  if (heroSecs) heroSecs.innerText = padZero(heroT.seconds);
  if (heroSpotlight) heroSpotlight.style.borderTopColor = nextExam.accent;

  // Update View Units
  SEM3_EXAM_SCHEDULE.forEach(exam => {
    const eTargetMs = new Date(exam.targetDateStr).getTime();
    const t = getTimeBreakdown(eTargetMs, nowMs);

    const dEl = document.getElementById(`timer-d-${exam.id}`);
    const hEl = document.getElementById(`timer-h-${exam.id}`);
    const mEl = document.getElementById(`timer-m-${exam.id}`);
    const sEl = document.getElementById(`timer-s-${exam.id}`);

    if (dEl) dEl.innerText = padZero(t.days);
    if (hEl) hEl.innerText = padZero(t.hours);
    if (mEl) mEl.innerText = padZero(t.minutes);
    if (sEl) sEl.innerText = padZero(t.seconds);

    const tableRemain = document.getElementById(`table-remain-${exam.id}`);
    if (tableRemain) {
      tableRemain.innerText = t.isPassed ? 'Completed' : `${t.days}d ${padZero(t.hours)}h ${padZero(t.minutes)}m ${padZero(t.seconds)}s`;
    }

    const timelineRemain = document.getElementById(`timeline-remain-${exam.id}`);
    if (timelineRemain) {
      timelineRemain.innerText = t.isPassed ? 'Completed' : `${t.days} Days ${padZero(t.hours)}h ${padZero(t.minutes)}m ${padZero(t.seconds)}s`;
    }
  });

  // Zen Mode
  if (zenActiveExamId) {
    const activeExam = SEM3_EXAM_SCHEDULE.find(e => e.id === zenActiveExamId) || nextExam;
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

function setTimerView(view) {
  timerViewMode = view;
  try {
    localStorage.setItem('sem3_timer_view', view);
  } catch (e) {}

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
        ${SEM3_EXAM_SCHEDULE.map(exam => {
          const t = getTimeBreakdown(new Date(exam.targetDateStr).getTime(), nowMs);
          const status = getExamStatus(exam, nowMs);

          return `
            <div class="sched-card" style="--card-accent: ${exam.accent};">
              <div>
                <div class="sched-card-top">
                  <span class="sched-code mono">${exam.code}</span>
                  <span class="sched-status mono">${status.label}</span>
                </div>
                <h3 class="sched-title">${exam.name}</h3>
                <p class="sched-desc">${exam.desc}</p>
                <p class="sched-dates mono">${exam.dateBS} B.S. · ${exam.dateAD}</p>
              </div>

              <div>
                <div class="sched-digits-row mono">
                  <div>
                    <span class="digit-val" id="timer-d-${exam.id}">${padZero(t.days)}</span>
                    <span class="digit-lbl">DAYS</span>
                  </div>
                  <div>
                    <span class="digit-val" id="timer-h-${exam.id}">${padZero(t.hours)}</span>
                    <span class="digit-lbl">HOURS</span>
                  </div>
                  <div>
                    <span class="digit-val" id="timer-m-${exam.id}">${padZero(t.minutes)}</span>
                    <span class="digit-lbl">MINS</span>
                  </div>
                  <div>
                    <span class="digit-val" id="timer-s-${exam.id}">${padZero(t.seconds)}</span>
                    <span class="digit-lbl">SECS</span>
                  </div>
                </div>

                <div class="sched-card-footer">
                  <span class="mono" style="font-size:0.72rem; color:var(--text-muted);">1:00 PM NPT (+24h)</span>
                  <button class="btn-pill mono" onclick="openZenMode('${exam.id}')">ZEN FOCUS</button>
                </div>
              </div>
            </div>
          `;
        }).join('')}
      </div>
    `;
  } else if (view === 'table') {
    container.innerHTML = `
      <div class="table-wrapper">
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
            ${SEM3_EXAM_SCHEDULE.map(exam => {
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
      <div class="timeline-wrapper">
        ${SEM3_EXAM_SCHEDULE.map(exam => {
          const t = getTimeBreakdown(new Date(exam.targetDateStr).getTime(), nowMs);

          return `
            <div class="timeline-item" style="--card-accent: ${exam.accent};">
              <div>
                <span class="mono" style="font-size:0.75rem; color:var(--text-muted); font-weight:700;">${exam.code} · ${exam.dateBS} B.S.</span>
                <h4 style="font-size:1.15rem; font-weight:800; margin:0.2rem 0;">${exam.name}</h4>
                <p style="font-size:0.8rem; color:var(--text-secondary); margin-bottom:0.25rem;">${exam.desc}</p>
                <p class="mono" style="font-size:0.78rem; color:var(--text-muted);">${exam.dateAD} · 1:00 PM – 4:00 PM NPT</p>
              </div>
              <div style="text-align: right;">
                <span class="mono" id="timeline-remain-${exam.id}" style="font-size:0.95rem; font-weight:800; display:block; margin-bottom:0.4rem;">
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

function openZenMode(examId) {
  const nowMs = Date.now();
  const exam = examId ? SEM3_EXAM_SCHEDULE.find(e => e.id === examId) : getNextUpcomingExam(nowMs);
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
  showToast(`Zen Focus: ${exam.name}`);
}

function closeZenMode() {
  const overlay = document.getElementById('zen-overlay');
  zenActiveExamId = null;
  if (overlay) {
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }
}

function toggleTheme() {
  currentTheme = currentTheme === 'light' ? 'dark' : 'light';
  document.documentElement.setAttribute('data-theme', currentTheme);
  localStorage.setItem('theme', currentTheme);
  const btnText = document.getElementById('theme-toggle-text');
  if (btnText) btnText.innerText = currentTheme === 'light' ? 'DARK' : 'LIGHT';
}

function showToast(message) {
  const container = document.getElementById('toast-container');
  if (!container) return;
  const toast = document.createElement('div');
  toast.className = 'toast mono';
  toast.innerText = message;
  container.appendChild(toast);
  setTimeout(() => {
    toast.style.opacity = '0';
    setTimeout(() => toast.remove(), 300);
  }, 2400);
}

function exportCalendarICS() {
  let icsLines = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Aryas Notes Gallery//BCT 3rd Sem Exam Schedule 2083//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'X-WR-CALNAME:IOE BCT 3rd Semester Exam Schedule 2083',
    'X-WR-TIMEZONE:Asia/Kathmandu'
  ];

  SEM3_EXAM_SCHEDULE.forEach(exam => {
    const startDt = new Date(exam.targetDateStr);
    const endDt = new Date(exam.endDateStr);
    const formatICSDate = (d) => d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');

    icsLines.push(
      'BEGIN:VEVENT',
      `UID:${exam.id}-sem3-2083@aryasnotes`,
      `DTSTAMP:${formatICSDate(new Date())}`,
      `DTSTART:${formatICSDate(startDt)}`,
      `DTEND:${formatICSDate(endDt)}`,
      `SUMMARY:IOE 3rd Sem Exam: ${exam.code} - ${exam.name}`,
      `DESCRIPTION:Tribhuvan University IOE BCT 3rd Sem Exam.\\nDate: ${exam.dateBS} B.S. (${exam.dateAD})\\nTime: 1:00 PM - 4:00 PM NPT`,
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

  const blob = new Blob([icsLines.join('\r\n')], { type: 'text/calendar;charset=utf-8' });
  const downloadUrl = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = downloadUrl;
  link.setAttribute('download', 'IOE_BCT_3rd_Semester_Exam_Schedule_2083.ics');
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(downloadUrl);
  showToast('Calendar schedule (.ics) exported!');
}

document.addEventListener('DOMContentLoaded', () => {
  document.documentElement.setAttribute('data-theme', currentTheme);
  const btnText = document.getElementById('theme-toggle-text');
  if (btnText) btnText.innerText = currentTheme === 'light' ? 'DARK' : 'LIGHT';

  setTimerView(timerViewMode);
  updateTimerUI();
  setInterval(updateTimerUI, 1000);

  window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeZenMode();
    if (e.key.toLowerCase() === 't' && !['input', 'textarea'].includes(document.activeElement.tagName.toLowerCase())) {
      toggleTheme();
    }
  });
});
