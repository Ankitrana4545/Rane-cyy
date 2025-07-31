#!/usr/bin/env python3
"""
Physics Wallah Lectures Core Downloader
Handles main download orchestration logic
"""

import requests
import time
import utils

def download_lecture(session, url, cookies=None):
    """Download single lecture with proper error handling"""
    try:
        # Apply anti-detection measures
        headers = {
            'Accept-Language': 'en-US,en;q=0.9',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Fetch content with timeout
        response = session.get(
            url, 
            headers=headers,
            cookies=cookies,
            timeout=(5, 30),
            stream=True
        )
        response.raise_for_status()
        
        # Calculate expected file size
        content_length = int(response.headers.get('content-length', 0))
        size_str = utils.human_readable_size(content_length) if content_length else '?'
        
        # Save to disk
        output_path = utils.sanitize_filename(url.split('/')[-1].rsplit('.', 1)[0])
        
        with open(output_path, 'wb') as f:
            chunk_size = 8192
            total_chunks = 0
            
            # Show progress
            if content_length > 0:
                chunks_expected = content_length // chunk_size + \
                                 (1 if content_length % chunk_size else 0)
            
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                total_chunks += 1
                
                # Periodic status updates
                if content_length > 0 and total_chunks % 50 == 0:
                    progress = (total_chunks * chunk_size) / content_length
                    elapsed = time.time() - start_time
                    
                    print(f"[{progress:.1%}] ~{elapsed:.1f}s | {size_str} | Speed: {(chunk_size * 50)/elapsed:.0f} B/s")
            
            return output_path
            
    except Exception as e:
        raise RuntimeError(f"Failed to download '{output_path}': {e}")