# Vibetest Demo Guide

This demo showcases the Vibetest automated QA testing tool that uses Browser-Use agents to find UI bugs, broken links, accessibility issues, and other technical problems on websites.

## ✅ What's Been Updated

1. **Updated to Latest Versions** - All dependencies are now pinned to their latest stable versions:
   - `browser-use==0.6.1` (latest)
   - `mcp==1.13.1` (latest)
   - `playwright==1.54.0` (latest)
   - `langchain_google_genai==2.1.9` (latest)
   - All other dependencies pinned to prevent breaking changes

2. **MCP Server Works** - The `vibetest-mcp` command is installed and functional as an MCP server

3. **CLI Works** - The CLI entry point is properly configured in pyproject.toml

## 🚀 Quick Start Demo

### Prerequisites

1. **Google API Key** - You need a Gemini API key:
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   ```
   Get one at: https://ai.google.dev/

2. **Activate Virtual Environment**:
   ```bash
   source venv/bin/activate
   ```

### Run the Interactive Demo

```bash
./demo.py
```

This will present you with several options:
1. Test a popular website (browser-use.com)
2. Test a local development server
3. Test a custom URL
4. Run multiple tests
5. Exit

### Test the Demo Website

We've included a test website with intentional issues for demonstration:

1. **Start the test server** (in a separate terminal):
   ```bash
   source venv/bin/activate
   ./serve_test_site.py
   ```

2. **Run vibetest on it**:
   ```bash
   source venv/bin/activate
   export GOOGLE_API_KEY="your-api-key"
   ./demo.py
   # Choose option 2 for localhost:3000
   ```

## 📊 What Vibetest Detects

The test website (`test_website.html`) includes various intentional issues:

- **Broken Links** - 404 pages and missing resources
- **JavaScript Errors** - Buttons that throw errors
- **Accessibility Issues** - Low contrast text, missing alt attributes
- **Form Errors** - Server errors on submission
- **Navigation Issues** - Non-functional menu items

## 🎯 Example Output

When you run the demo, you'll see:

```
🚀 Starting test on: http://localhost:3000/test_website.html
   Agents: 3
   Mode: Headless
   Time: 2024-01-15 10:30:00

============================================================

🤖 Launching browser agents...

✅ Test started with ID: 123e4567-e89b-12d3-a456-426614174000
⏳ Agents are now testing the website...

📊 Analyzing results...

📋 TEST RESULTS
============================================================
Status: 🔴 high-severity
Description: Critical issues found that need immediate attention
Duration: 45s

Agents Summary:
  • Total agents: 3
  • Successful: 3
  • Failed: 0

Issues Found: 5

🔴 HIGH SEVERITY ISSUES:
  • [broken_functionality] Upon clicking the 'Documentation' link in the header navigation, the page redirected to a 404 error
  • [javascript_error] When clicking the 'Error Button' in the Broken Feature section, JavaScript threw an uncaught error

🟠 MEDIUM SEVERITY ISSUES:
  • [form_error] When submitting the newsletter signup form with a valid email, the form displayed 'Server Error 500' instead of confirmation

🟡 LOW SEVERITY ISSUES:
  • [accessibility] The text "This text has very low contrast and is hard to read" has insufficient color contrast ratio
  • [accessibility] Image missing alt attribute for screen reader accessibility

============================================================

💾 Detailed results saved to: vibetest_results_123e4567-e89b-12d3-a456-426614174000.json
```

## 🔧 Using with MCP (Model Context Protocol)

### Claude Desktop Configuration

Add to your Claude config:
```json
{
  "mcpServers": {
    "vibetest": {
      "command": "/full/path/to/vibetest-use/venv/bin/vibetest-mcp",
      "env": {
        "GOOGLE_API_KEY": "your_api_key"
      }
    }
  }
}
```

### Cursor Configuration

In Cursor's MCP settings, add:
```json
{
  "mcpServers": {
    "vibetest": {
      "command": "/full/path/to/vibetest-use/venv/bin/vibetest-mcp",
      "env": {
        "GOOGLE_API_KEY": "your_api_key"
      }
    }
  }
}
```

Then in Claude/Cursor:
```
> Vibetest my website with 5 agents: https://example.com
> Run vibetest on localhost:3000
> Run a headless vibetest on localhost:8080 with 10 agents
```

## 📝 Key Features Demonstrated

1. **Multi-Agent Testing** - Multiple browser agents test different parts of the site simultaneously
2. **Smart Issue Detection** - AI-powered analysis to identify real issues vs. design choices
3. **Severity Classification** - Issues are categorized as high/medium/low severity
4. **Detailed Reporting** - Specific descriptions of what was tested and what failed
5. **JSON Output** - Machine-readable results for integration with other tools

## 🎥 Visual Mode

For debugging or demonstrations, you can run in non-headless mode to see the browsers:

```python
await run_test(url, num_agents=3, headless=False)
```

This will open visible browser windows showing the agents in action.

## 🔍 Troubleshooting

1. **"GOOGLE_API_KEY not set"** - Make sure to export your API key
2. **"playwright not installed"** - Run `playwright install chromium --with-deps`
3. **Import errors** - Make sure you're in the virtual environment
4. **Connection refused** - Make sure the test server is running on port 3000

## 🚀 Next Steps

1. Try testing your own websites
2. Adjust the number of agents for more thorough testing
3. Integrate vibetest into your CI/CD pipeline
4. Customize the issue detection logic in `agents.py`

Happy testing with Vibetest! 🎉