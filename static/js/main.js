document.addEventListener('DOMContentLoaded', () => {
    // Parallax mouse effect on Mascot HUD
    const mascotContainer = document.getElementById('mascot-parallax');
    if (mascotContainer) {
        document.addEventListener('mousemove', (e) => {
            const x = (window.innerWidth / 2 - e.clientX) / 40;
            const y = (window.innerHeight / 2 - e.clientY) / 40;
            mascotContainer.style.transform = `translate3d(${x}px, ${y}px, 0)`;
        });
    }

    // Terminal Widget Handler
    const terminalInput = document.getElementById('terminal-input');
    const terminalOutput = document.getElementById('terminal-output');

    if (terminalInput) {
        terminalInput.addEventListener('keydown', async (e) => {
            if (e.key === 'Enter') {
                const query = terminalInput.value.trim();
                if (!query) return;

                // Render query
                appendOutput(`$ ask_agent '${query}'`, 'prompt-line');
                terminalInput.value = '';

                try {
                    // Call Python FastAPI Backend Service
                    const response = await fetch('http://127.0.0.1:8000/api/agent', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ query: query })
                    });
                    
                    const data = await response.json();
                    typewriterStream(data.response);
                } catch (err) {
                    // Local fallback response
                    typewriterStream(getLocalFallback(query));
                }
            }
        });
    }

    function appendOutput(text, className = '') {
        const line = document.createElement('div');
        line.className = `term-line ${className}`;
        line.textContent = text;
        terminalOutput.appendChild(line);
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }

    function typewriterStream(text) {
        const line = document.createElement('div');
        line.className = 'term-line resp-line';
        line.style.color = '#22d3ee';
        terminalOutput.appendChild(line);

        let idx = 0;
        const interval = setInterval(() => {
            if (idx < text.length) {
                line.textContent += text.charAt(idx);
                idx++;
                terminalOutput.scrollTop = terminalOutput.scrollHeight;
            } else {
                clearInterval(interval);
            }
        }, 15);
    }

    function getLocalFallback(cmd) {
        const lower = cmd.toLowerCase();
        if (lower.includes('hasnain') || lower.includes('do')) {
            return "Hafiz Muhammad Hasnain Tariq is an Aspiring AI Agentic Engineer specializing in Python, FastAPI, and C++ static analysis tools.";
        } else if (lower.includes('stack') || lower.includes('skills')) {
            return "Primary Stack: Python, C++, FastAPI, PyTorch, LangChain, Streamlit, Groq AI, Supabase.";
        } else if (lower.includes('contact')) {
            return "Email: hafizhasnaintariq@gmail.com | GitHub: @artificialai26-hash";
        }
        return `Executing agent query: '${cmd}'... Agent processed input successfully.`;
    }
});