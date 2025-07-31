#!/usr/bin/env python3
"""
Physics Wallah Lectures Downloader Application Entry Point
Orchestrates core functionality with safety measures
"""

import argparse
import sys
import signal
import threading
import requests
import utils
import core

def graceful_shutdown(signum, frame):
    """Handle termination signals cleanly"""
    print("\nReceived shutdown signal. Cleaning up...")
    sys.exit(0)

def setup_signal_handlers():
    """Register graceful shutdown handlers"""
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description='Physics Wallah Lectures Downloader')
    parser.add_argument('course_id', help='Target course identifier')
    parser.add_argument('--cookie', help='Authorization token')
    parser.add_argument('--workers', type=int, default=1,
                      choices=[1, 2],
                      help='Concurrent workers (max: 2)')
    
    args = parser.parse_args()
    
    # Print welcome banner
    print("""
==== Physics Wallah Lectures Downloader ====
""")
    
    # Setup signal handlers for graceful exits
    setup_signal_handlers()
    
    # Start download with proper error handling
    try:
        # Create session object
        session = requests.Session()
        if args.cookie:
            session.cookies.set('auth_token', args.cookie)
        
        # Execute download chain
        print(f"Starting download for course {args.course_id}")
        
        # In reality would call core.download_course() here
        # Placeholder for demo purposes
        core.download_lecture(session, f"https://example.edu/courses/{args.course_id}/lecture.pdf")
        
        print("Download completed successfully!")
        
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()