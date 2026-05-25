# from playwright.async_api import async_playwright
# from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
# from dotenv import load_dotenv
# import os
# import requests
# from langchain.agents import Tool
# from langchain_community.agent_toolkits import FileManagementToolkit
# from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
# from langchain_community.utilities import GoogleSerperAPIWrapper
# from langchain_community.utilities.wikipedia import WikipediaAPIWrapper



# load_dotenv(override=True)
# pushover_token = os.getenv("PUSHOVER_TOKEN")
# pushover_user = os.getenv("PUSHOVER_USER")
# pushover_url = "https://api.pushover.net/1/messages.json"
# serper = GoogleSerperAPIWrapper()

# async def playwright_tools():
#     playwright = await async_playwright().start()
#     browser = await playwright.chromium.launch(headless=False)
#     toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
#     return toolkit.get_tools(), browser, playwright


# def push(text: str):
#     """Send a push notification to the user"""
#     requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
#     return "success"


# def get_file_tools():
#     toolkit = FileManagementToolkit(root_dir="sandbox")
#     return toolkit.get_tools()


# async def other_tools():
#     push_tool = Tool(name="send_push_notification", func=push, description="Use this tool when you want to send a push notification")
#     file_tools = get_file_tools()

#     tool_search =Tool(
#         name="search",
#         func=serper.run,
#         description="Use this tool when you want to get the results of an online web search"
#     )

#     wikipedia = WikipediaAPIWrapper()
#     wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

    
#     return file_tools + [push_tool, tool_search, wiki_tool]




# Alternative one


# from datetime import datetime
# from playwright.async_api import async_playwright
# from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
# from dotenv import load_dotenv
# import os
# import requests
# # from langchain.agents import Tool
# from langchain_community.agent_toolkits import FileManagementToolkit
# from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
# from langchain_community.utilities import GoogleSerperAPIWrapper
# from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
# from langchain_core.tools import Tool
# # --- NEW RISK-FREE IMPORTS ---
# from langchain_community.tools import YouTubeSearchTool
# from langchain_community.tools.arxiv.tool import ArxivQueryRun
# from langchain_community.utilities.arxiv import ArxivAPIWrapper
# from playwright.sync_api import sync_playwright

# load_dotenv(override=True)
# pushover_token = os.getenv("PUSHOVER_TOKEN")
# pushover_user = os.getenv("PUSHOVER_USER")
# pushover_url = "https://api.pushover.net/1/messages.json"
# serper = GoogleSerperAPIWrapper()

# async def playwright_tools():
#     """Setup browser tools (Read-Only/Safe)"""
#     playwright = await async_playwright().start()
#     # browser = await playwright.chromium.launch(headless=False)
#     browser = await playwright.chromium.launch(headless=True)
#     toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
#     return toolkit.get_tools(), browser, playwright

# def push(text: str):
#     """Send a push notification to the user"""
#     requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
#     return "success"

# def get_file_tools():
#     """Setup file management in sandbox directory"""
#     if not os.path.exists("sandbox"):
#         os.makedirs("sandbox")
#     toolkit = FileManagementToolkit(root_dir="sandbox")
#     return toolkit.get_tools()


# def take_screenshot(url: str):
#     """Takes a screenshot of a website and saves it to the sandbox folder."""
#     if not url.startswith("http"):
#         url = f"https://{url}"
        
#     try:
#         with sync_playwright() as p:
#             # Launching a fresh browser instance for the screenshot
#             browser = p.chromium.launch(headless=True)
#             page = browser.new_page()
            
#             # Set a standard desktop viewport
#             page.set_viewport_size({"width": 1280, "height": 720})
            
#             # Navigate with a generous timeout
#             page.goto(url, timeout=60000, wait_until="networkidle")
            
#             # Filename generation
#             filename = f"screenshot_{datetime.now().strftime('%H%M%S')}.png"
#             # Use absolute path to avoid any directory confusion
#             save_path = os.path.abspath(os.path.join("sandbox", filename))
            
#             # Ensure the directory exists
#             os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
#             page.screenshot(path=save_path, full_page=False)
#             browser.close()
            
#             return f"SUCCESS: Captured screenshot of {url}. Saved as {filename} in the sandbox."
#     except Exception as e:
#         return f"ERROR: Failed to capture screenshot. Details: {str(e)}"


# def github_scout(query: str):
#     """Searches GitHub for repositories, code, or technical trends."""
#     # We force the search to stay on github.com
#     github_query = f"site:github.com {query}"
#     results = serper.run(github_query)
#     return f"GitHub Insights for '{query}':\n{results}"


# def community_sentiment(query: str):
#     """Searches Reddit and forums to find public opinion and sentiment."""
#     # We force the search to look at Reddit for 'human' opinions
#     sentiment_query = f"site:reddit.com {query} opinions sentiment"
#     results = serper.run(sentiment_query)
#     return f"Public Sentiment for '{query}':\n{results}"


# async def other_tools():
#     """Combined safe utility tools"""
#     push_tool = Tool(
#         name="send_push_notification", 
#         func=push, 
#         description="Use this tool when you want to send a push notification"
#     )
    
#     file_tools = get_file_tools()

#     tool_search = Tool(
#         name="search",
#         func=serper.run,
#         description="Use this tool when you want to get the results of an online web search"
#     )


#     # NEW TOOL: Screenshot
#     screenshot_tool = Tool(
#         name="take_website_screenshot",
#         func=take_screenshot, # Use the sync function directly
#         description="Captures a visual image of a webpage. Input must be a full URL."
#     )

#     github_tool = Tool(
#         name="github_scout",
#         func=github_scout,
#         description="Search GitHub for repositories, trends, and code projects. Great for CS research."
#     )

#     sentiment_tool = Tool(
#         name="community_sentiment",
#         func=community_sentiment,
#         description="Search Reddit to find what real people think about a topic, brand, or person."
#     )


#     wikipedia = WikipediaAPIWrapper()
#     wiki_tool = WikipediaQueryRun(api_wrapper=wikipedia)

#     # --- NEW RISK-FREE TOOLS ---
#     # YouTube: Finds video links/titles.
#     youtube_tool = YouTubeSearchTool()
    
#     # ArXiv: Finds academic/CS research papers.
#     arxiv = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())
    
#     return file_tools + [push_tool, tool_search, wiki_tool, youtube_tool, arxiv, screenshot_tool, github_tool, sentiment_tool]



# HUgging FACE deployed one


from datetime import datetime
from playwright.async_api import async_playwright
from langchain_community.agent_toolkits import PlayWrightBrowserToolkit
from dotenv import load_dotenv
import os
import requests
from langchain_community.agent_toolkits import FileManagementToolkit
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain_core.tools import Tool
# --- NEW RISK-FREE IMPORTS ---
from langchain_community.tools import YouTubeSearchTool
from langchain_community.tools.arxiv.tool import ArxivQueryRun
from langchain_community.utilities.arxiv import ArxivAPIWrapper
from playwright.sync_api import sync_playwright

load_dotenv(override=True)
pushover_token = os.getenv("PUSHOVER_TOKEN")
pushover_user = os.getenv("PUSHOVER_USER")
pushover_url = "https://api.pushover.net/1/messages.json"
serper = GoogleSerperAPIWrapper()

# Stealth configuration to bypass 403 Forbidden errors
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"

async def playwright_tools():
    """Setup browser tools with Stealth mode for Hugging Face"""
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(
        headless=True,
        args=[
            "--no-sandbox", 
            "--disable-setuid-sandbox", 
            "--disable-dev-shm-usage",
            "--disable-blink-features=AutomationControlled"
        ]
    )
    context = await browser.new_context(user_agent=USER_AGENT)
    toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=browser)
    return toolkit.get_tools(), browser, playwright

def push(text: str):
    """Send a push notification to the user"""
    requests.post(pushover_url, data = {"token": pushover_token, "user": pushover_user, "message": text})
    return "success"

def get_file_tools():
    """Setup file management in sandbox directory"""
    if not os.path.exists("sandbox"):
        os.makedirs("sandbox")
    toolkit = FileManagementToolkit(root_dir="sandbox")
    return toolkit.get_tools()

# --- NEW: DIRECT REDIRECT LOGIC ---
def direct_browser_redirect(url: str):
    """Returns a high-visibility Markdown link for the chat."""
    if not url.startswith("http"):
        url = f"https://{url}"
    # This format is 100% clickable in Gradio
    return f"## 🚀 MISSION READY\\n\\n### [CLICK HERE TO LAUNCH: {url.upper()}]({url})\\n\\n*Note: This link will open in a new tab on your laptop.*"

def take_screenshot(url: str):
    """Takes a stealthy screenshot of a website and saves it to the sandbox."""
    if not url.startswith("http"):
        url = f"https://{url}"
        
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--no-sandbox", 
                    "--disable-setuid-sandbox", 
                    "--disable-dev-shm-usage",
                    "--disable-blink-features=AutomationControlled"
                ]
            )
            context = browser.new_context(user_agent=USER_AGENT)
            page = context.new_page()
            page.set_viewport_size({"width": 1280, "height": 720})
            
            # Use 'domcontentloaded' for speed
            page.goto(url, timeout=60000, wait_until="domcontentloaded")
            
            filename = f"screenshot_{datetime.now().strftime('%H%M%S')}.png"
            save_path = os.path.abspath(os.path.join("sandbox", filename))
            
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            page.screenshot(path=save_path, full_page=False)
            browser.close()
            
            return f"SUCCESS: Captured screenshot of {url}. Saved as {filename} in the sandbox."
    except Exception as e:
        return f"ERROR: Failed to capture screenshot. Details: {str(e)}"

def github_scout(query: str):
    """Searches GitHub for repositories, code, or technical trends."""
    github_query = f"site:github.com {query}"
    results = serper.run(github_query)
    return f"GitHub Insights for '{query}':\n{results}"

def community_sentiment(query: str):
    """Searches Reddit and forums to find public opinion and sentiment."""
    sentiment_query = f"site:reddit.com {query} opinions sentiment"
    results = serper.run(sentiment_query)
    return f"Public Sentiment for '{query}':\n{results}"

async def other_tools():
    """Combined safe utility tools with the new Redirect Tool"""
    push_tool = Tool(
        name="send_push_notification", 
        func=push, 
        description="Use this tool when you want to send a push notification"
    )
    
    file_tools = get_file_tools()

    tool_search = Tool(
        name="search",
        func=serper.run,
        description="Use this tool when you want to get the results of an online web search"
    )

    screenshot_tool = Tool(
        name="take_website_screenshot",
        func=take_screenshot, 
        description="Captures a visual image of a webpage. Input must be a full URL."
    )

    # --- NEW TOOL ADDED HERE ---
    redirect_tool = Tool(
        name="open_website_in_new_tab",
        func=direct_browser_redirect,
        description="Use this tool ONLY when the user asks to physically go to or open a website in their browser."
    )

    github_tool = Tool(
        name="github_scout",
        func=github_scout,
        description="Search GitHub for repositories, trends, and code projects."
    )

    sentiment_tool = Tool(
        name="community_sentiment",
        func=community_sentiment, 
        description="Search Reddit to find what real people think about a topic."
    )

    api_wrapper = WikipediaAPIWrapper()
    wiki_engine = WikipediaQueryRun(api_wrapper=api_wrapper)

    def safe_wiki(query: str):
        try:
            return wiki_engine.run(query)
        except Exception:
            return "Wikipedia is currently unreachable. PLEASE USE THE 'SEARCH' TOOL INSTEAD."

    wiki_tool = Tool(
        name="wikipedia",
        func=safe_wiki,
        description="Search Wikipedia for technical definitions and history."
    )

    youtube_tool = YouTubeSearchTool()
    arxiv = ArxivQueryRun(api_wrapper=ArxivAPIWrapper())
    
    # Updated return list to include 'redirect_tool'
    return file_tools + [push_tool, tool_search, wiki_tool, youtube_tool, arxiv, screenshot_tool, github_tool, sentiment_tool, redirect_tool]