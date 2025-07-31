#!/usr/bin/env python3
"""
Physics Wallah Lectures Downloader
----------------------------------

This script automates downloading lecture PDFs from Physics Wallah.
"""

import argparse
import sys
import os
import downloader  # Our core module

def main():
    parser = argparse.ArgumentParser(description='Download Physics Wallah lectures')
    parser.add_argument('course_id', help='Target course identifier')
    parser.add_argument('--workers', type=int, default=3,
                        help='Max concurrent downloads (default: 3)')
    parser.add_argument('--cookie', help='Login session cookie')
    parser.add_argument('--outdir', help='Output directory')
    
    args = parser.parse_args()
    
    # Set working directory
    if args.outdir:
        os.makedirs(args.outdir, exist_ok=True)
        os.chdir(args.outdir)
    
    # Execute download task
    try:
        downloader.download_lectures(
            args.course_id, 
            args.cookie, 
            max_workers=args.workers
        )
    except KeyboardInterrupt:
        print("\nDownload interrupted.")

if __name__ == '__main__':
    main()