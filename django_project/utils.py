
import os
import time
from html2image import Html2Image
from PIL import Image

def take_screenshot(url, output_file):
    """
    Take a screenshot of a webpage using HTML2Image library.
    This approach creates a static HTML file and converts it to an image.
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Initialize the HTML2Image converter
        hti = Html2Image(output_path=os.path.dirname(output_file))
        
        # If the URL is a relative URL or a local file path
        if not url.startswith(('http://', 'https://')):
            # Assume it's a local file or path
            if os.path.isfile(url):
                # It's a local HTML file
                with open(url, 'r') as f:
                    html_content = f.read()
            else:
                # Use the Replit domain as the base
                replit_domain = os.environ.get('REPL_SLUG', 'your-repl')
                replit_owner = os.environ.get('REPL_OWNER', 'user')
                base_url = f"https://{replit_domain}.{replit_owner}.repl.co"
                
                # Remove leading slash if present in the relative URL
                if url.startswith('/'):
                    url = url[1:]
                    
                full_url = f"{base_url}/{url}"
                print(f"Converting URL: {full_url}")
                
                # Use the HTML2Image to screenshot a URL
                img_path = hti.screenshot(url=full_url, save_as=os.path.basename(output_file))
                
                # Verify the file was created
                if img_path and os.path.exists(img_path[0]):
                    print(f"Screenshot saved to {output_file}")
                    return True
                else:
                    print("Failed to capture screenshot")
                    return False
        else:
            # It's a full URL
            print(f"Converting URL: {url}")
            img_path = hti.screenshot(url=url, save_as=os.path.basename(output_file))
            
            # Verify the file was created
            if img_path and os.path.exists(img_path[0]):
                print(f"Screenshot saved to {output_file}")
                return True
            else:
                print("Failed to capture screenshot")
                return False
                
        return True
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        # Create a fallback image with error message
        try:
            # Create a simple image with error text
            img = Image.new('RGB', (800, 400), color=(255, 255, 255))
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
