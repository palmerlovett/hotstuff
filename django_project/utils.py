
import os
import time
import asyncio
from playwright.async_api import async_playwright

async def _take_screenshot_async(url, output_file):
    """
    Take a screenshot of a webpage using Playwright (async implementation).
    """
    try:
        async with async_playwright() as playwright:
            browser = await playwright.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                ]
            )
            
            page = await browser.new_page(viewport={"width": 1200, "height": 800})
            await page.goto(url, wait_until='networkidle')
            
            # Wait a bit more to ensure full page rendering
            await asyncio.sleep(2)
            
            # Make sure all content is visible
            await page.evaluate("document.body.style.overflow = 'hidden';")
            
            # Take screenshot
            await page.screenshot(path=output_file, full_page=True)
            print(f"Screenshot saved to {output_file}")
            
            await browser.close()
            return True
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        return False

def take_screenshot(url, output_file):
    """
    Synchronous wrapper for the async screenshot function.
    """
    return asyncio.run(_take_screenshot_async(url, output_file))
