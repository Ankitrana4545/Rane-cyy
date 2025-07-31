#!/usr/bin/env python3
"""
Utilities Module for Physics Wallah Downloader
Contains shared functions reused across application layers
"""

import os
import re
import time
import random
import string

def sanitize_filename(name, extension=".pdf"):
    """Clean file names for safe filesystem interaction"""
    # Remove special characters and limit length
    clean_name = re.sub(r'[<>:"/\\|?*\[\]]', '_', name[:75]) + extension
    
    # Replace leading/trailing whitespace and dots
    return clean_name.strip('._')

def random_string(length=8):
    """Generate random string for temp files"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def human_readable_size(bytes_in):
    """Convert bytes to KB, MB, GB representation"""
    units = ['B', 'KB', 'MB', 'GB']
    index = 0
    
    while bytes_in >= 1024 and index < len(units) - 1:
        bytes_in /= 1024
        index += 1
    
    return f"{bytes_in:.2f} {units[index]}"

def retry_operation(operation, attempts=3, delay=5):
    """Execute operation with retry mechanism"""
    last_exception = None
    
    for attempt in range(attempts):
        try:
            return operation()
        except Exception as e:
            last_exception = e
            if attempt < attempts - 1:
                print(f"Retry #{attempt + 1}: {e}")
                time.sleep(delay * (attempt + 1))  # Exponential backoff
    
    raise last_exception