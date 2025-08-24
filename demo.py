#!/usr/bin/env python3
"""
Vibetest Demo - Automated QA Testing with Browser-Use Agents
This demo showcases the vibetest functionality for testing websites.
"""

import asyncio
import os
import sys
from vibetest.agents import run_pool, summarize_bug_reports
import json
from datetime import datetime

# ASCII art for the demo
VIBETEST_ASCII = """
██╗   ██╗██╗██████╗ ███████╗████████╗███████╗███████╗████████╗
██║   ██║██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
██║   ██║██║██████╔╝█████╗     ██║   █████╗  ███████╗   ██║   
╚██╗ ██╔╝██║██╔══██╗██╔══╝     ██║   ██╔══╝  ╚════██║   ██║   
 ╚████╔╝ ██║██████╔╝███████╗   ██║   ███████╗███████║   ██║   
  ╚═══╝  ╚═╝╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝   
          Automated QA Testing with Browser-Use Agents
"""

async def run_test(url: str, num_agents: int = 3, headless: bool = True):
    """Run a vibetest on the specified URL"""
    print(f"\n🚀 Starting test on: {url}")
    print(f"   Agents: {num_agents}")
    print(f"   Mode: {'Headless' if headless else 'Visual'}")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n" + "="*60 + "\n")
    
    try:
        # Run the test
        print("🤖 Launching browser agents...\n")
        test_id = await run_pool(url, num_agents, headless=headless)
        
        print(f"✅ Test started with ID: {test_id}")
        print("⏳ Agents are now testing the website...\n")
        
        # Wait a bit for agents to complete
        await asyncio.sleep(5)
        
        # Get results
        print("📊 Analyzing results...\n")
        results = await summarize_bug_reports(test_id)
        
        # Display results
        print("📋 TEST RESULTS")
        print("="*60)
        
        if "error" in results:
            print(f"❌ Error: {results['error']}")
            return
        
        print(f"Status: {results.get('status_emoji', '?')} {results.get('overall_status', 'Unknown')}")
        print(f"Description: {results.get('status_description', 'No description available')}")
        
        if 'duration_formatted' in results:
            print(f"Duration: {results['duration_formatted']}")
        
        print(f"\nAgents Summary:")
        print(f"  • Total agents: {results.get('total_agents', 0)}")
        print(f"  • Successful: {results.get('successful_agents', 0)}")
        print(f"  • Failed: {results.get('failed_agents', 0)}")
        
        # Display issues by severity
        severity_breakdown = results.get('severity_breakdown', {})
        total_issues = results.get('total_issues', 0)
        
        print(f"\nIssues Found: {total_issues}")
        
        if severity_breakdown.get('high_severity'):
            print("\n🔴 HIGH SEVERITY ISSUES:")
            for issue in severity_breakdown['high_severity']:
                print(f"  • [{issue['category']}] {issue['description']}")
        
        if severity_breakdown.get('medium_severity'):
            print("\n🟠 MEDIUM SEVERITY ISSUES:")
            for issue in severity_breakdown['medium_severity']:
                print(f"  • [{issue['category']}] {issue['description']}")
        
        if severity_breakdown.get('low_severity'):
            print("\n🟡 LOW SEVERITY ISSUES:")
            for issue in severity_breakdown['low_severity']:
                print(f"  • [{issue['category']}] {issue['description']}")
        
        if total_issues == 0:
            print("\n✅ No issues detected! The website appears to be working well.")
        
        print("\n" + "="*60)
        
        # Save detailed results
        results_file = f"vibetest_results_{test_id}.json"
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n💾 Detailed results saved to: {results_file}")
        
    except Exception as e:
        print(f"\n❌ Error during test: {str(e)}")
        print("   Make sure you have set the GOOGLE_API_KEY environment variable.")

async def main():
    """Main demo function"""
    print(VIBETEST_ASCII)
    
    # Check for API key
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️  WARNING: GOOGLE_API_KEY environment variable not set!")
        print("   You need a Google API key to use Gemini 2.0 Flash.")
        print("   Get one at: https://developers.google.com/maps/api-security-best-practices")
        print("\n   Set it with: export GOOGLE_API_KEY='your_api_key_here'")
        return
    
    print("\n🎯 VIBETEST DEMO - Choose a test scenario:\n")
    print("1. Test a popular website (browser-use.com)")
    print("2. Test a local development server (localhost:3000)")
    print("3. Test a custom URL")
    print("4. Run multiple tests")
    print("5. Exit")
    
    choice = input("\nSelect option (1-5): ").strip()
    
    if choice == "1":
        await run_test("https://browser-use.com", num_agents=3, headless=True)
    
    elif choice == "2":
        print("\n⚠️  Make sure your local server is running on localhost:3000")
        input("Press Enter to continue...")
        await run_test("http://localhost:3000", num_agents=3, headless=True)
    
    elif choice == "3":
        url = input("\nEnter URL to test: ").strip()
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        
        num_agents = input("Number of agents (default 3): ").strip()
        num_agents = int(num_agents) if num_agents.isdigit() else 3
        
        headless = input("Run headless? (y/n, default y): ").strip().lower()
        headless = headless != 'n'
        
        await run_test(url, num_agents=num_agents, headless=headless)
    
    elif choice == "4":
        print("\n🔄 Running multiple test scenarios...")
        test_sites = [
            "https://example.com",
            "https://httpstat.us/404",  # Test 404 handling
            "https://www.google.com"
        ]
        
        for site in test_sites:
            await run_test(site, num_agents=2, headless=True)
            print("\n" + "-"*60 + "\n")
    
    elif choice == "5":
        print("\n👋 Thanks for using Vibetest!")
        return
    
    else:
        print("\n❌ Invalid option. Please try again.")
        await main()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Test interrupted. Goodbye!")
        sys.exit(0)