<div align="center">

```
 ██████╗ ██╗  ██╗     ██████╗ ██████╗ ██████╗ ███████╗    ██████╗ ██████╗ ██╗ ██████╗ ██████╗ 
██╔════╝ ██║  ██║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔══██╗██╔══██╗██║██╔═══██╗██╔══██╗
██║  ███╗███████║    ██║     ██║   ██║██║  ██║█████╗      ██████╔╝██████╔╝██║██║   ██║██████╔╝
██║   ██║██╔══██║    ██║     ██║   ██║██║  ██║██╔══╝      ██╔══██╗██╔══██╗██║██║   ██║██╔══██╗
╚██████╔╝██║  ██║    ╚██████╗╚██████╔╝██████╔╝███████╗    ██████╔╝██║  ██║██║╚██████╔╝██║  ██║
 ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝
```

<br/>

![Typing SVG](https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=28&duration=3000&pause=1000&color=00FFFF&vCenter=true&multiline=true&repeatType=mirror&width=600&height=100&lines=FULL+STACK+DEVELOPER;GAMER+%2F+CODER+%2F+CREATOR)

</div>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&display=swap');

  :root {
    --neon-cyan: #00ffff;
    --neon-magenta: #ff00ff;
    --neon-green: #39ff14;
    --neon-red: #ff073a;
    --neon-yellow: #ffe600;
    --dark-bg: #0a0a1a;
    --card-bg: #0d0d2b;
    --card-border: #1a1a3e;
  }

  * { box-sizing: border-box; }

  .hud-container {
    font-family: 'Orbitron', 'Share Tech Mono', monospace;
    background: linear-gradient(180deg, #050510 0%, #0a0a1a 30%, #0d0d2b 100%);
    border: 1px solid var(--neon-cyan);
    border-radius: 16px;
    padding: 30px 25px;
    margin: 20px 0;
    position: relative;
    overflow: hidden;
    box-shadow:
      0 0 15px rgba(0, 255, 255, 0.3),
      0 0 60px rgba(0, 255, 255, 0.1),
      inset 0 0 60px rgba(0, 255, 255, 0.03);
  }

  .hud-container::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: repeating-linear-gradient(
      0deg,
      transparent,
      transparent 2px,
      rgba(0, 255, 255, 0.015) 2px,
      rgba(0, 255, 255, 0.015) 4px
    );
    pointer-events: none;
    z-index: 1;
  }

  .hud-container::after {
    content: '';
    position: absolute;
    top: -100%;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      180deg,
      transparent 0%,
      rgba(0, 255, 255, 0.04) 50%,
      transparent 100%
    );
    animation: scanline 4s linear infinite;
    pointer-events: none;
    z-index: 1;
  }

  @keyframes scanline {
    0% { top: -100%; }
    100% { top: 200%; }
  }

  @keyframes glitch {
    0%, 100% { transform: translate(0); text-shadow: 0 0 10px var(--neon-cyan); }
    10% { transform: translate(-2px, 1px); }
    20% { transform: translate(2px, -1px); }
    30% { transform: translate(-1px, 2px); text-shadow: -2px 0 var(--neon-magenta), 2px 0 var(--neon-cyan); }
    40% { transform: translate(1px, -2px); }
    50% { transform: translate(-2px, -1px); text-shadow: 0 0 20px var(--neon-cyan); }
    60% { transform: translate(2px, 1px); }
    70% { transform: translate(-1px, -2px); text-shadow: 2px 0 var(--neon-magenta), -2px 0 var(--neon-cyan); }
    80% { transform: translate(1px, 2px); }
    90% { transform: translate(-2px, -1px); }
  }

  @keyframes neonPulse {
    0%, 100% { opacity: 1; filter: brightness(1); }
    50% { opacity: 0.85; filter: brightness(1.3); }
  }

  @keyframes borderGlow {
    0%, 100% { border-color: var(--neon-cyan); box-shadow: 0 0 15px rgba(0,255,255,0.4); }
    33% { border-color: var(--neon-magenta); box-shadow: 0 0 15px rgba(255,0,255,0.4); }
    66% { border-color: var(--neon-green); box-shadow: 0 0 15px rgba(57,255,20,0.4); }
  }

  @keyframes floatUp {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
  }

  @keyframes xpFill {
    0% { width: 0%; }
    100% { width: 78%; }
  }

  @keyframes levelUp {
    0% { transform: scale(1); }
    50% { transform: scale(1.15); text-shadow: 0 0 30px var(--neon-green); }
    100% { transform: scale(1); }
  }

  .section-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 30px 0 15px 0;
    position: relative;
    z-index: 2;
  }

  .section-header::before {
    content: '▸';
    color: var(--neon-cyan);
    font-size: 1.2rem;
    text-shadow: 0 0 10px var(--neon-cyan);
    animation: neonPulse 2s ease-in-out infinite;
  }

  .section-header h2 {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 4px;
    color: var(--neon-cyan);
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.6);
    margin: 0;
    text-transform: uppercase;
  }

  .player-name {
    font-family: 'Orbitron', sans-serif;
    font-size: 2.8rem;
    font-weight: 900;
    color: #fff;
    text-shadow:
      0 0 10px var(--neon-cyan),
      0 0 40px var(--neon-cyan),
      0 0 80px rgba(0, 255, 255, 0.4);
    animation: glitch 4s ease-in-out infinite;
    margin: 10px 0 5px 0;
    letter-spacing: 6px;
  }

  .player-tag {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.95rem;
    color: var(--neon-magenta);
    letter-spacing: 3px;
    text-shadow: 0 0 8px rgba(255, 0, 255, 0.5);
    margin: 0;
  }

  .status-bar {
    display: flex;
    justify-content: center;
    gap: 30px;
    margin: 20px 0;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
  }

  .status-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 4px;
  }

  .status-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: #555;
    letter-spacing: 3px;
    text-transform: uppercase;
  }

  .status-value {
    font-family: 'Orbitron', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 2px;
  }

  .online-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: var(--neon-green);
    border-radius: 50%;
    box-shadow: 0 0 6px var(--neon-green), 0 0 12px var(--neon-green);
    animation: neonPulse 1.5s ease-in-out infinite;
    margin-right: 6px;
    vertical-align: middle;
  }

  .xp-bar-container {
    width: 100%;
    max-width: 500px;
    margin: 25px auto 10px auto;
    position: relative;
    z-index: 2;
  }

  .xp-bar-label {
    display: flex;
    justify-content: space-between;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.7rem;
    color: #666;
    letter-spacing: 2px;
    margin-bottom: 6px;
  }

  .xp-bar {
    width: 100%;
    height: 14px;
    background: #111;
    border: 1px solid #333;
    border-radius: 7px;
    overflow: hidden;
    position: relative;
  }

  .xp-fill {
    height: 100%;
    width: 0%;
    background: linear-gradient(90deg, var(--neon-cyan), var(--neon-magenta));
    border-radius: 7px;
    animation: xpFill 2s ease-out forwards;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.6), 0 0 20px rgba(255, 0, 255, 0.3);
    position: relative;
  }

  .xp-fill::after {
    content: '';
    position: absolute;
    top: 0; right: 0;
    width: 20px; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4));
    border-radius: 0 7px 7px 0;
  }

  .card {
    background: linear-gradient(135deg, rgba(13, 13, 43, 0.9), rgba(10, 10, 26, 0.95));
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 20px;
    margin: 15px 0;
    position: relative;
    z-index: 2;
    transition: all 0.3s ease;
  }

  .card:hover {
    border-color: var(--neon-cyan);
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.15), inset 0 0 30px rgba(0, 255, 255, 0.03);
  }

  .card-cyan { border-left: 3px solid var(--neon-cyan); }
  .card-magenta { border-left: 3px solid var(--neon-magenta); }
  .card-green { border-left: 3px solid var(--neon-green); }
  .card-yellow { border-left: 3px solid var(--neon-yellow); }

  .tech-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(80px, 1fr));
    gap: 15px;
    padding: 10px 0;
  }

  .tech-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    padding: 12px 8px;
    background: rgba(0, 255, 255, 0.03);
    border: 1px solid rgba(0, 255, 255, 0.1);
    border-radius: 10px;
    transition: all 0.3s ease;
    animation: floatUp 3s ease-in-out infinite;
  }

  .tech-item:nth-child(2) { animation-delay: 0.3s; }
  .tech-item:nth-child(3) { animation-delay: 0.6s; }
  .tech-item:nth-child(4) { animation-delay: 0.9s; }
  .tech-item:nth-child(5) { animation-delay: 1.2s; }
  .tech-item:nth-child(6) { animation-delay: 1.5s; }

  .tech-item:hover {
    border-color: var(--neon-cyan);
    background: rgba(0, 255, 255, 0.08);
    transform: translateY(-4px);
    box-shadow: 0 4px 15px rgba(0, 255, 255, 0.2);
  }

  .tech-item img {
    width: 36px;
    height: 36px;
    filter: drop-shadow(0 0 4px rgba(0, 255, 255, 0.3));
    transition: filter 0.3s;
  }

  .tech-item:hover img {
    filter: drop-shadow(0 0 8px rgba(0, 255, 255, 0.6));
  }

  .tech-item span {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    color: #666;
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  .achievements-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 12px;
  }

  .achievement {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 14px;
    background: rgba(255, 230, 0, 0.03);
    border: 1px solid rgba(255, 230, 0, 0.15);
    border-radius: 10px;
    transition: all 0.3s ease;
  }

  .achievement:hover {
    border-color: var(--neon-yellow);
    background: rgba(255, 230, 0, 0.06);
    box-shadow: 0 0 15px rgba(255, 230, 0, 0.1);
  }

  .achievement-icon {
    font-size: 1.6rem;
    flex-shrink: 0;
    filter: drop-shadow(0 0 4px rgba(255, 230, 0, 0.4));
  }

  .achievement-text {
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .achievement-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    color: var(--neon-yellow);
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  .achievement-desc {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: #666;
    letter-spacing: 1px;
  }

  .social-bar {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin: 10px 0;
    position: relative;
    z-index: 2;
  }

  .social-bar img {
    transition: all 0.3s ease;
    border-radius: 6px;
  }

  .social-bar img:hover {
    transform: translateY(-3px) scale(1.05);
    filter: brightness(1.2) drop-shadow(0 0 8px rgba(0, 255, 255, 0.4));
  }

  .stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 15px;
    margin: 10px 0;
  }

  .footer-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 30px;
    padding-top: 15px;
    border-top: 1px solid #1a1a3e;
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: #333;
    letter-spacing: 2px;
    position: relative;
    z-index: 2;
  }

  .footer-bar span {
    animation: neonPulse 3s ease-in-out infinite;
  }

  .corner-decor {
    position: absolute;
    width: 20px;
    height: 20px;
    z-index: 2;
  }

  .corner-decor.tl { top: 8px; left: 8px; border-top: 2px solid var(--neon-cyan); border-left: 2px solid var(--neon-cyan); }
  .corner-decor.tr { top: 8px; right: 8px; border-top: 2px solid var(--neon-cyan); border-right: 2px solid var(--neon-cyan); }
  .corner-decor.bl { bottom: 8px; left: 8px; border-bottom: 2px solid var(--neon-cyan); border-left: 2px solid var(--neon-cyan); }
  .corner-decor.br { bottom: 8px; right: 8px; border-bottom: 2px solid var(--neon-cyan); border-right: 2px solid var(--neon-cyan); }
</style>

<div class="hud-container">
  <!-- Corner Decorations -->
  <div class="corner-decor tl"></div>
  <div class="corner-decor tr"></div>
  <div class="corner-decor bl"></div>
  <div class="corner-decor br"></div>

  <!-- PLAYER IDENTITY -->
  <div align="center">
    <div style="font-family:'Share Tech Mono',monospace;font-size:0.7rem;color:#333;letter-spacing:6px;margin-bottom:5px;position:relative;z-index:2;">// PLAYER IDENTIFICATION //</div>
    <div class="player-name">GK503</div>
    <div class="player-tag">&gt; FULL STACK DEV _ GAMER _ CREATOR_</div>

    <!-- STATUS BAR -->
    <div class="status-bar">
      <div class="status-item">
        <span class="status-label">CLASS</span>
        <span class="status-value" style="color:var(--neon-cyan);">DEVELOPER</span>
      </div>
      <div class="status-item">
        <span class="status-label">LEVEL</span>
        <span class="status-value" style="color:var(--neon-magenta);">99</span>
      </div>
      <div class="status-item">
        <span class="status-label">RANK</span>
        <span class="status-value" style="color:var(--neon-yellow);">ELITE</span>
      </div>
      <div class="status-item">
        <span class="status-label">STATUS</span>
        <span class="status-value" style="color:var(--neon-green);"><span class="online-dot"></span>ONLINE</span>
      </div>
    </div>

    <!-- XP BAR -->
    <div class="xp-bar-container">
      <div class="xp-bar-label">
        <span>XP PROGRESS</span>
        <span style="color:var(--neon-cyan);">78,420 / 100,000</span>
      </div>
      <div class="xp-bar">
        <div class="xp-fill"></div>
      </div>
    </div>
  </div>

  <!-- SECTION: STATS -->
  <div class="section-header">
    <h2>Player Stats</h2>
  </div>

  <div class="stats-container">
    <div class="card card-cyan" align="center">
      <img src="https://raw.githubusercontent.com/GK503/GK503/stats-output/stats.svg?hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=dracula&locale=en&hide_border=false" height="165" alt="GitHub Stats" style="border-radius:8px;" />
    </div>
    <div class="card card-magenta" align="center">
      <img src="https://raw.githubusercontent.com/GK503/GK503/languages-output/languages.svg?locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=dracula&hide_border=false" height="165" alt="Languages" style="border-radius:8px;" />
    </div>
  </div>

  <!-- SECTION: LOADOUT -->
  <div class="section-header">
    <h2>Equipped Loadout</h2>
  </div>

  <div class="card card-cyan">
    <div class="tech-grid">
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JavaScript" />
        <span>JavaScript</span>
      </div>
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" alt="TypeScript" />
        <span>TypeScript</span>
      </div>
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React" />
        <span>React</span>
      </div>
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5" />
        <span>HTML5</span>
      </div>
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3" />
        <span>CSS3</span>
      </div>
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" />
        <span>Python</span>
      </div>
      <div class="tech-item">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" alt="C#" />
        <span>C-Sharp</span>
      </div>
    </div>
  </div>

  <!-- SECTION: ACHIEVEMENTS -->
  <div class="section-header">
    <h2>Achievements Unlocked</h2>
  </div>

  <div class="card card-yellow">
    <div class="achievements-grid">
      <div class="achievement">
        <div class="achievement-icon">&#x1F680;</div>
        <div class="achievement-text">
          <div class="achievement-title">First Commit</div>
          <div class="achievement-desc">Pushed to production</div>
        </div>
      </div>
      <div class="achievement">
        <div class="achievement-icon">&#x26A1;</div>
        <div class="achievement-text">
          <div class="achievement-title">Speed Coder</div>
          <div class="achievement-desc">100+ commits this year</div>
        </div>
      </div>
      <div class="achievement">
        <div class="achievement-icon">&#x1F3AE;</div>
        <div class="achievement-text">
          <div class="achievement-title">Gamer Mode</div>
          <div class="achievement-desc">Code by day, game by night</div>
        </div>
      </div>
      <div class="achievement">
        <div class="achievement-icon">&#x1F4BB;</div>
        <div class="achievement-text">
          <div class="achievement-title">Full Stack</div>
          <div class="achievement-desc">Frontend + Backend mastery</div>
        </div>
      </div>
    </div>
  </div>

  <!-- SECTION: SOCIALS -->
  <div class="section-header">
    <h2>Connect</h2>
  </div>

  <div class="social-bar">
    <a href="https://youtube.com/@GK503" target="_blank"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="YouTube" /></a>
    <a href="https://instagram.com/gk503" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" /></a>
    <a href="https://twitch.tv/gk503" target="_blank"><img src="https://img.shields.io/badge/Twitch-9146FF?style=for-the-badge&logo=twitch&logoColor=white" alt="Twitch" /></a>
    <a href="https://discord.gg/gk503" target="_blank"><img src="https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>
    <a href="mailto:gk503@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" /></a>
    <a href="https://linkedin.com/in/gk503" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  </div>

  <!-- SECTION: SNAKE -->
  <div style="margin-top:20px; position:relative; z-index:2;">
    <img src="https://raw.githubusercontent.com/GK503/GK503/snake-output/snake.svg" alt="Snake animation" style="width:100%;border-radius:8px;border:1px solid #1a1a3e;" />
  </div>

  <!-- SECTION: DETAILED STATS -->
  <div style="margin-top:20px; position:relative; z-index:2;">
    <div class="stats-container">
      <div align="center">
        <a href="https://github-stats-extended.vercel.app/api?username=GK503&show=reviews%2Cdiscussions_started%2Cdiscussions_answered%2Cprs_merged%2Cprs_merged_percentage%2Cprs_commented%2Cprs_reviewed%2Cissues_commented%2Ccontributions%2Call_time_contribs&include_all_commits=true&theme=shadow_blue">
          <img src="https://github-stats-extended.vercel.app/api?username=GK503&show=reviews%2Cdiscussions_started%2Cdiscussions_answered%2Cprs_merged%2Cprs_merged_percentage%2Cprs_commented%2Cprs_reviewed%2Cissues_commented%2Ccontributions%2Call_time_contribs&include_all_commits=true&theme=shadow_blue" alt="Extended Stats" style="border-radius:8px;" />
        </a>
      </div>
      <div align="center">
        <a href="https://github-stats-extended.vercel.app/api/top-langs?username=GK503&layout=compact&langs_count=200&theme=dracula">
          <img src="https://github-stats-extended.vercel.app/api/top-langs?username=GK503&layout=compact&langs_count=200&theme=dracula" alt="Top Languages" style="border-radius:8px;" />
        </a>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer-bar">
    <span>SYS::ONLINE</span>
    <span>GK503 // FULL STACK DEV</span>
    <span>SESSION::ACTIVE</span>
  </div>
</div>
