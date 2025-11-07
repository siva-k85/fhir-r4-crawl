"""
Shared utility functions for FHIR R4 crawler
"""

import os
import re
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def ensure_directory(path: str) -> Path:
    """
    Ensure directory exists, create if it doesn't

    Args:
        path: Directory path to create

    Returns:
        Path object for the directory
    """
    dir_path = Path(path)
    dir_path.mkdir(parents=True, exist_ok=True)
    return dir_path


def sanitize_filename(url: str, max_length: int = 200) -> str:
    """
    Convert URL to safe filename

    Args:
        url: URL to sanitize
        max_length: Maximum filename length

    Returns:
        Safe filename string
    """
    # Remove protocol
    filename = re.sub(r'^https?://', '', url)
    # Replace non-alphanumeric with underscore
    filename = re.sub(r'[^a-zA-Z0-9_-]+', '_', filename)
    # Remove trailing/leading underscores
    filename = filename.strip('_')
    # Truncate to max length
    filename = filename[:max_length]
    return filename


def is_r4_url(url: str) -> bool:
    """
    Check if URL is a valid FHIR R4 URL

    Args:
        url: URL to check

    Returns:
        True if valid R4 URL, False otherwise
    """
    # Must contain /R4/
    if '/R4/' not in url:
        return False

    # Must not contain other versions
    blocked_patterns = ['/R5/', '/R4B/', '/R3/', '/R2/', '/ballot/']
    if any(pattern in url for pattern in blocked_patterns):
        return False

    # Must not be binary file
    blocked_extensions = ['.zip', '.tgz', '.tar', '.gz', '.pdf', '.xml', '.json']
    if any(url.lower().endswith(ext) for ext in blocked_extensions):
        return False

    return True


def load_json(file_path: str) -> Dict[str, Any]:
    """
    Load JSON file

    Args:
        file_path: Path to JSON file

    Returns:
        Parsed JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading JSON from {file_path}: {e}")
        return {}


def save_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to JSON file

    Args:
        data: Data to save
        file_path: Path to save JSON file
    """
    try:
        ensure_directory(os.path.dirname(file_path))
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved JSON to {file_path}")
    except Exception as e:
        logger.error(f"Error saving JSON to {file_path}: {e}")


def get_timestamp() -> str:
    """
    Get current timestamp in ISO format

    Returns:
        ISO formatted timestamp string
    """
    return datetime.utcnow().isoformat() + 'Z'


def get_datestamp() -> str:
    """
    Get current date in YYYY-MM-DD format

    Returns:
        Date string
    """
    return datetime.now().strftime('%Y-%m-%d')


def count_files_in_directory(directory: str, pattern: str = '*') -> int:
    """
    Count files matching pattern in directory

    Args:
        directory: Directory path
        pattern: Glob pattern (default: all files)

    Returns:
        Number of matching files
    """
    try:
        path = Path(directory)
        return len(list(path.glob(pattern)))
    except Exception as e:
        logger.error(f"Error counting files in {directory}: {e}")
        return 0


def read_file_lines(file_path: str) -> List[str]:
    """
    Read file and return non-empty lines

    Args:
        file_path: Path to file

    Returns:
        List of non-empty lines
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return []


def write_file_lines(file_path: str, lines: List[str]) -> None:
    """
    Write lines to file

    Args:
        file_path: Path to file
        lines: List of lines to write
    """
    try:
        ensure_directory(os.path.dirname(file_path))
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
        logger.info(f"Wrote {len(lines)} lines to {file_path}")
    except Exception as e:
        logger.error(f"Error writing to {file_path}: {e}")
