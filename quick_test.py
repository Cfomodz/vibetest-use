#!/usr/bin/env python3
"""Quick test to verify vibetest is working"""

import asyncio
import os
import sys

# Add the workspace to Python path
sys.path.insert(0, '/workspace')

from vibetest.agents import run_pool, summarize_bug_reports

async def quick_test():
    """Run a quick test on example.com"""
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not set")
        print("Set it with: export GOOGLE_API_KEY='your-key-here'")
        return
    
    print("🧪 Running quick vibetest on example.com...")
    print("This will launch 2 headless browser agents to test the site.\n")
    
    try:
        # Run test with 2 agents in headless mode
        test_id = await run_pool("https://example.com", num_agents=2, headless=True)
        print(f"✅ Test started successfully! Test ID: {test_id}")
        
        # Wait a bit for results
        print("⏳ Waiting for agents to complete testing...")
        await asyncio.sleep(10)
        
        # Get results
        results = await summarize_bug_reports(test_id)
        
        print("\n📊 Quick Test Results:")
        print(f"Status: {results.get('status_emoji', '?')} {results.get('overall_status', 'Unknown')}")
        print(f"Total issues found: {results.get('total_issues', 0)}")
        
        if results.get('total_issues', 0) == 0:
            print("\n✅ Success! Vibetest is working correctly.")
            print("   Example.com appears to have no major issues.")
        else:
            print("\n✅ Success! Vibetest is working and found some issues.")
        
        print("\n💡 Try running ./demo.py for an interactive demo!")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nMake sure:")
        print("1. You've activated the virtual environment: source venv/bin/activate")
        print("2. You've set GOOGLE_API_KEY environment variable")
        print("3. You've installed all dependencies: pip install -e .")

if __name__ == "__main__":
    asyncio.run(quick_test())