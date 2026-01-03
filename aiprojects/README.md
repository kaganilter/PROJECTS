# AI project workspace quickstart

1) Create a virtual environment so VS Code can find `${workspaceFolder}/.venv/bin/python`:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   ```
2) Install base tooling and common AI stacks when you are ready:
   ```bash
   pip install black ruff pytest jupyter ipykernel
   # Choose frameworks as needed
   pip install "torch==2.*" torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
   pip install "transformers==4.*" "datasets==2.*" "accelerate==0.*"
   ```
3) In VS Code, accept the recommended extensions. They enable Python linting/formatting, Jupyter notebooks, and Docker integration.
4) Hit `⌘⇧P` → `Python: Select Interpreter` and pick `.venv`. Format on save, Ruff lint, and Pytest discovery will now work automatically.
5) Run tests from the Testing panel or with `pytest`. Notebooks will use the selected interpreter once you create a kernel (`Python: Create Python Environment`).

Notes
- Settings assume tests live under `tests/`. Adjust `.vscode/settings.json` if you use a different layout.
- If you add GPU or other native deps, prefer a `requirements.txt` or `pyproject.toml` so teammates pick up the same environment.
- For full laptop bootstrap (Homebrew, pyenv, VS Code, CLI tools), see `SYSTEM_SETUP.md`.
- Quick venv creation: run `scripts/bootstrap_venv.sh` (uses `python3`, installs black/ruff/pytest/ipykernel). For uv, run `uv venv .venv && source .venv/bin/activate`.
- Coding standards for AI agents and humans: see `CODE_GUIDELINES.md` (PEP 8, typing, docstrings, testing).
- Privacy-first: VS Code telemetry disabled in `.vscode/settings.json`; keep secrets/PII out of logs and repos. Avoid pushing code to public remotes unless explicitly intended.

## OpenAI Agents SDK sample

1) Create/activate a venv (see quickstart above).
2) Install the sample dependency: `pip install -r requirements.txt`.
3) Export your API key: `export OPENAI_API_KEY=<key>`.
4) Run the agent demo: `python sample_agent.py "Plan a short onboarding for a new teammate" --session demo`.
5) The agent uses stubbed tools (`search_local_docs`, `get_weather`); replace them with real implementations to hook into your systems. Explore the full SDK docs at https://github.com/openai/openai-agents-python for handoffs, guardrails, and tracing.
