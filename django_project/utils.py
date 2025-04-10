import os
import time
import shutil
import subprocess
from html2image import Html2Image
from PIL import Image
import tempfile
from django.conf import settings

def find_chrome_executable():
    """
    Find a valid Chrome executable on the system.
    """
    # Check multiple possible Chrome paths in Replit environment
    chrome_paths = [
        "/nix/store/x205pbkd5xh5g4iv0n6hm9rdqr559vqa-chromium-112.0.5615.49/bin/chromium",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
        "/usr/bin/google-chrome",
        "/nix/store/f1yq455j9c3dj4idqwq2ac0q7wj0s2w9-chromium-125.0.6422.141/bin/chromium"
    ]

    # Try alternative paths from the system
    try:
        # Check if chromium is available in PATH
        chromium_path = subprocess.check_output(["which", "chromium"], 
                                             stderr=subprocess.STDOUT, 
                                             text=True).strip()
        if chromium_path:
            chrome_paths.insert(0, chromium_path)
    except subprocess.CalledProcessError:
        pass

    # Check if these paths exist and are executable
    for path in chrome_paths:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            print(f"Found Chrome executable at: {path}")
            return path

    return None

def take_screenshot(url, output_file):
    """
    Take a screenshot of a webpage using HTML2Image library with improved configuration.
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Get the actual URL
        if not url.startswith(('http://', 'https://')):
            # Use the Replit domain as the base for relative URLs
            replit_domain = os.environ.get('REPL_SLUG', 'your-repl')
            replit_owner = os.environ.get('REPL_OWNER', 'user')
            base_url = f"https://{replit_domain}.{replit_owner}.repl.co"

            # Remove leading slash if present in the relative URL
            if url.startswith('/'):
                url = url[1:]

            full_url = f"{base_url}/{url}"
        else:
            full_url = url

        # Create a temporary directory for html2image outputs
        with tempfile.TemporaryDirectory() as temp_dir:
            # Find a valid Chrome executable
            chrome_path = find_chrome_executable()

            # Initialize Html2Image with more configuration options
            if chrome_path:
                hti = Html2Image(
                    output_path=temp_dir,
                    size=(800, 1100),
                    browser_executable=chrome_path,
                    custom_flags=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--headless'],
                )
                print(f"Using Chrome at: {chrome_path}")
            else:
                print("No Chrome executable found, using default configuration")
                hti = Html2Image(
                    output_path=temp_dir,
                    size=(800, 1100),
                    custom_flags=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage', '--headless'],
                )


            print(f"Attempting to capture: {full_url}")

            # Wait for page to fully render (including CSS, fonts, images)
            # Sleep before taking screenshot to allow page to render
            time.sleep(1)  # Wait 1 second for page to render
            img_files = hti.screenshot(
                url=full_url, 
                save_as=os.path.basename(output_file)
            )

            # Check if the screenshot was created
            if img_files and os.path.exists(os.path.join(temp_dir, img_files[0])):
                # Copy from temp dir to output location
                shutil.copy(
                    os.path.join(temp_dir, img_files[0]),
                    output_file
                )
                print(f"Screenshot saved to {output_file}")
                return True
            else:
                raise Exception("Screenshot capture failed")

    except Exception as e:
        print(f"Error taking screenshot: {e}")
        # Create a fallback image with error message
        try:
            # Create a simple image with error text
            img = Image.new('RGB', (800, 600), color=(255, 255, 255))
            from PIL import ImageDraw, ImageFont
            draw = ImageDraw.Draw(img)
            draw.text((20, 20), f"Error capturing screenshot: {str(e)}", fill=(0, 0, 0))
            draw.text((20, 60), f"URL: {url}", fill=(0, 0, 0))
            img.save(output_file)
            print(f"Created error image at {output_file}")
            return True
        except Exception as fallback_error:
            print(f"Failed to create error image: {fallback_error}")
            return False