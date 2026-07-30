// Premium Responsive Ambient Cursor Tracking Mesh Core
const glowRing = document.getElementById('mouse-glow');
if (glowRing) {
    window.addEventListener('mousemove', (e) => {
        glowRing.style.left = e.clientX + 'px';
        glowRing.style.top = e.clientY + 'px';
    });
}

const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('active'); });
}, { threshold: 0.05 });

async function executeFolioSync() {
    const fullName = document.getElementById('fullname_input').value.trim();
    const techTitle = document.getElementById('title_input').value.trim();
    const githubUser = document.getElementById('github_user_input').value.trim();
    const linkedinUrl = document.getElementById('linkedin_url_input').value.trim();
    
    const syncBtn = document.getElementById('sync-action-btn');
    const loader = document.getElementById('loader');
    const outputCanvas = document.getElementById('portfolio-output-view');
    const inputDock = document.getElementById('generator-dock');

    if (!fullName || !githubUser) {
        alert("Please fulfill both Name and GitHub username configuration fields.");
        return;
    }

    syncBtn.disabled = true;
    loader.classList.remove('hidden');

    const formData = new FormData();
    formData.append("fullname", fullName);
    formData.append("title", techTitle);
    formData.append("github_user", githubUser);
    formData.append("linkedin_url", linkedinUrl);

    try {
        const response = await fetch('/api/sync-profile', { method: 'POST', body: formData });
        if (!response.ok) {
            const errData = await response.json();
            throw new Error(errData.detail || "AI engine failed to synchronize asset context framework.");
        }
        const data = await response.json();

        // Populate Main DOM Canvas
        if(document.getElementById('out-name')) document.getElementById('out-name').textContent = data.full_name || fullName;
        if(document.getElementById('out-title')) document.getElementById('out-title').textContent = data.headline || techTitle;
        if(document.getElementById('out-bio')) document.getElementById('out-bio').textContent = data.bio || "";

        // Render Skill Chips
        const skillsGrid = document.getElementById('out-skills');
        if (skillsGrid) {
            skillsGrid.innerHTML = '';
            if (data.skills) {
                data.skills.forEach(s => {
                    const chip = document.createElement('span');
                    chip.className = 'skill-chip';
                    chip.textContent = s;
                    skillsGrid.appendChild(chip);
                });
            }
        }

        // Render Career Chronology Cards
        const historyContainer = document.getElementById('out-history');
        if (historyContainer) {
            historyContainer.innerHTML = '';
            if (data.career_history) {
                data.career_history.forEach(job => {
                    const item = document.createElement('div');
                    item.className = 'project-card';
                    item.innerHTML = `
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <span style="font-weight:700; color:#fff; font-size:0.92rem;">💼 ${job.role}</span>
                            <span style="color:var(--accent-cyan); font-size:0.75rem; font-family:'JetBrains Mono', monospace;">${job.duration}</span>
                        </div>
                        <div style="color:var(--text-muted); font-size:0.75rem; font-family:'JetBrains Mono', monospace; margin-bottom:8px; text-transform:uppercase;">${job.company}</div>
                        <p style="color:var(--text-muted); font-size:0.88rem; line-height:1.6;">${job.details}</p>
                    `;
                    historyContainer.appendChild(item);
                });
            }
        }

        // Render Repositories Cards + Media Preview Frame Engine
        const reposContainer = document.getElementById('out-repos');
        if (reposContainer) {
            reposContainer.innerHTML = '';
            if (data.inferred_projects) {
                data.inferred_projects.forEach(repo => {
                    const card = document.createElement('div');
                    card.className = 'project-card';
                    let markup = `
                        <h4 style="margin:0 0 8px 0; color:#fff; font-size:0.95rem; font-weight:700;">📁 ${repo.title}</h4>
                        <p style="color:var(--text-muted); font-size:0.88rem; margin:0 0 14px 0; line-height:1.6;">${repo.description}</p>
                        <div style="color:var(--accent-cyan); font-family:'JetBrains Mono', monospace; font-size:0.75rem; font-weight:500;">Stack // ${repo.tech_used ? repo.tech_used.join(', ') : ''}</div>
                    `;
                    
                    if (repo.has_preview && repo.preview_url) {
                        const urlLower = repo.preview_url.toLowerCase();
                        let mediaElement = '';

                        if (urlLower.includes('youtube.com/embed')) {
                            mediaElement = `<iframe style="width:100%; height:200px; border:none;" src="${repo.preview_url}" allowfullscreen></iframe>`;
                        } else if (urlLower.endsWith('.gif') || urlLower.includes('.gif?')) {
                            mediaElement = `<img src="${repo.preview_url}" style="width:100%; height:auto; max-height:240px; object-fit:contain;" alt="Demo Asset"/>`;
                        } else {
                            mediaElement = `<video controls autoplay loop muted playsinline style="width:100%; height:auto; max-height:240px; background:#000;"><source src="${repo.preview_url}" type="video/mp4"></video>`;
                        }

                        markup += `
                            <div class="app-preview-container">
                                <div class="simulator-header">
                                    <span class="simulator-dot"></span>
                                    <span class="simulator-dot"></span>
                                    <div class="simulator-path">git://repository/${repo.title.toLowerCase()}/preview</div>
                                </div>
                                <div style="background:#000; display:flex; align-items:center; justify-content:center; padding:4px;">
                                    ${mediaElement}
                                </div>
                            </div>`;
                    }
                    card.innerHTML = markup;
                    reposContainer.appendChild(card);
                });
            }
        }

        // Transitions Canvas view state
        if (inputDock) inputDock.classList.add('hidden');
        if (outputCanvas) outputCanvas.classList.remove('hidden');

    } catch (e) {
        console.error("Folio Runtime Exception Grid Trace: ", e);
        alert(`Synchronization Fault: ${e.message}`);
    } finally {
        syncBtn.disabled = false;
        if (loader) loader.classList.add('hidden');
    }
}