import cv2
import numpy as np
import os
from datetime import datetime
from mss import mss
import time
import keyboard
from mss.exception import ScreenShotError
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

# ASCII Art Logo
LOGO = """

██████╗  ██████╗  ██████╗     ███████╗ ██████╗ ███╗   ███╗██████╗ ██╗███████╗███████╗                  
██╔══██╗██╔═══██╗██╔════╝     ╚══███╔╝██╔═══██╗████╗ ████║██╔══██╗██║██╔════╝██╔════╝                  
██████╔╝██║   ██║███████╗       ███╔╝ ██║   ██║██╔████╔██║██████╔╝██║█████╗  ███████╗                  
██╔══██╗██║   ██║██╔═══██╗     ███╔╝  ██║   ██║██║╚██╔╝██║██╔══██╗██║██╔══╝  ╚════██║                  
██████╔╝╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝██║███████╗███████║                  
╚═════╝  ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝╚══════╝╚══════╝          
        
██╗     ██╗███████╗███████╗     ██╗███╗   ██╗███████╗██╗   ██╗██████╗  █████╗ ███╗   ██╗ ██████╗███████╗
██║     ██║██╔════╝██╔════╝     ██║████╗  ██║██╔════╝██║   ██║██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝
██║     ██║█████╗  █████╗       ██║██╔██╗ ██║███████╗██║   ██║██████╔╝███████║██╔██╗ ██║██║     █████╗  
██║     ██║██╔══╝  ██╔══╝       ██║██║╚██╗██║╚════██║██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║     ██╔══╝  
███████╗██║██║     ███████╗     ██║██║ ╚████║███████║╚██████╔╝██║  ██║██║  ██║██║ ╚████║╚██████╗███████╗
╚══════╝╚═╝╚═╝     ╚══════╝     ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝
                                                                                                       

https://github.com/ethan-haas/zombies-life-insurance
"""

def print_logo():
    print(Fore.GREEN + LOGO + Style.RESET_ALL)

def screen_capture_and_detect(template_path, output_folder, monitor_number=1):
    with mss() as sct:  # Create new instance each time
        try:
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
        
            template = cv2.imread(template_path, 0)
            if template is None:
                print(Fore.RED + "Error: Could not load template image" + Style.RESET_ALL)
                return False

            monitor = sct.monitors[monitor_number]
            screenshot = sct.grab(monitor)
            
            screen = np.array(screenshot)
            screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            
            result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.8
            
            locations = np.where(result >= threshold)
            matches = list(zip(*locations[::-1]))
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            
            if matches:
                print(Fore.YELLOW + f"🧟 Object detected!" + Style.RESET_ALL)
                keyboard.press_and_release('alt+f4')
                print(Fore.CYAN + "🎮 Sent Alt+F4" + Style.RESET_ALL)
                
                output = screen.copy()
                for pt in matches:
                    cv2.rectangle(output, pt, 
                                 (pt[0] + template.shape[1], pt[1] + template.shape[0]),
                                 (0, 255, 0), 2)
                
                output_path = os.path.join(output_folder, f'detected_symbols_{timestamp}.png')
                cv2.imwrite(output_path, output)
                print(Fore.GREEN + f"📸 Detection image saved to: {output_path}" + Style.RESET_ALL)
                time.sleep(2)
                
            return len(matches) > 0
            
        except ScreenShotError as e:
            print(Fore.RED + f"Screenshot error: {e}" + Style.RESET_ALL)
            return False
        except Exception as e:
            print(Fore.RED + f"An error occurred: {e}" + Style.RESET_ALL)
            return False

def continuous_monitor(template_path, output_folder, interval=1):
    print(Fore.CYAN + "Starting continuous monitoring. Press Ctrl+C to stop." + Style.RESET_ALL)
    detection_count = 0
    
    try:
        while True:
            if screen_capture_and_detect(template_path, output_folder):
                detection_count += 1
                print(Fore.MAGENTA + f"🧟 Total detections: {detection_count}" + Style.RESET_ALL)
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print(Fore.YELLOW + f"\nMonitoring stopped by user. Total detections: {detection_count}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Monitoring error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    print_logo()
    output_folder = "detection_results"
    template_path = "icon.png"
    
    # Print available monitors
    with mss() as sct:
        print(Fore.CYAN + "Available monitors:" + Style.RESET_ALL)
        print(Fore.WHITE + str(sct.monitors) + Style.RESET_ALL)
    
    continuous_monitor(template_path, output_folder, interval=1)
