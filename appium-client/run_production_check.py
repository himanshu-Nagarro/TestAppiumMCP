#!/usr/bin/env python3
"""
Runner script for the Production Check validation test.
"""

import os
import sys
import logging
import argparse
import subprocess
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("inditex_automation.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description="Run INDITEX Production Check validation test")
    parser.add_argument("--audit", "-a", help="Specify audit ID to test")
    parser.add_argument("--device", "-d", help="Specify device name")
    args = parser.parse_args()
    
    # Get the directory where this script is located
    script_dir = Path(__file__).resolve().parent
    
    # Construct the path to the test script
    test_script_path = script_dir / "tests" / "test_production_check.py"
    
    if not test_script_path.exists():
        logger.error(f"Test script not found: {test_script_path}")
        sys.exit(1)
    
    logger.info("Starting Production Check test...")
    
    # Check if Appium server is running
    try:
        # TODO: Add Appium server check here
        pass
    except Exception as e:
        logger.warning(f"Error checking Appium server status: {e}")
        logger.warning("Make sure Appium server is running before continuing!")
    
    # Run the test script
    try:
        logger.info(f"Running test script: {test_script_path}")
        result = subprocess.run([sys.executable, str(test_script_path)], 
                                capture_output=True, 
                                text=True, 
                                check=False)
        
        if result.returncode != 0:
            logger.error(f"Test script failed with exit code {result.returncode}")
            logger.error(f"Error output: {result.stderr}")
            return 1
            
        logger.info(f"Test output: {result.stdout}")
        logger.info("Test completed successfully")
        return 0
        
    except Exception as e:
        logger.error(f"Error running test script: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())