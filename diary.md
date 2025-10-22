# Diary for project

## Setup

1. Set up environment

   ```bash
   uv init ai-agent
   cd ai-agent
   uv venv
   source .venv/bin/activate
   ```

2. Add dependencies

   ```bash
   uv add google-genai==1.12.1
   uv add python-dotenv==1.1.0
   ```

3. Check the output of your CLI command to see a results breakdown.

    uv pip list

4. To run the project ...

    uv run main.py

