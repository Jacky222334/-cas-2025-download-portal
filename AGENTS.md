# AGENTS.md

## Cursor Cloud specific instructions

This is a simple Python Streamlit web application — a document download portal for a "CAS 2025" educational course.

### Running the app

```bash
streamlit run app.py --server.headless true --server.port 8501 --browser.gatherUsageStats false
```

The `--server.headless true` flag is required in the cloud environment (no browser auto-open). The app serves on `http://localhost:8501`.

### Notes

- The `streamlit` binary installs to `~/.local/bin`. If not on PATH, prefix commands: `~/.local/bin/streamlit run app.py ...`
- No external services, databases, or secrets are required.
- No automated tests exist in the repository. Validation is done by starting the app and verifying the health endpoint: `curl http://localhost:8501/_stcore/health` (should return `ok`).
- No linter or build step is configured. The project is a single `app.py` file with `requirements.txt`.
- See `README.md` for standard run instructions.
