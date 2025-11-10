# Technical Best Practices for FHIR R4 Crawler

**Version**: 1.0
**Date**: November 8, 2025
**Purpose**: Document technical best practices and lessons learned from the FHIR R4 crawler implementation

---

## Table of Contents

1. [Web Crawling Best Practices](#web-crawling-best-practices)
2. [Anti-Detection Strategies](#anti-detection-strategies)
3. [Data Quality Assurance](#data-quality-assurance)
4. [Performance Optimization](#performance-optimization)
5. [Error Handling & Recovery](#error-handling--recovery)
6. [Documentation Standards](#documentation-standards)
7. [Security Considerations](#security-considerations)
8. [Future Improvements](#future-improvements)

---

## Web Crawling Best Practices

### 1. Respect Robots.txt

```python
# Always check robots.txt before crawling
import urllib.robotparser

def can_fetch(url: str, user_agent: str) -> bool:
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(url, '/robots.txt'))
    rp.read()
    return rp.can_fetch(user_agent, url)
```

### 2. Implement Rate Limiting

```python
import time
import random
from typing import Optional

class RateLimiter:
    def __init__(self, min_delay: int = 5, max_delay: int = 10):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.last_request = 0

    def wait(self):
        """Implement exponential backoff with jitter"""
        delay = random.uniform(self.min_delay, self.max_delay)
        time.sleep(delay)
        self.last_request = time.time()
```

### 3. Use Session Management

```python
import aiohttp
from typing import Dict, Any

class CrawlerSession:
    def __init__(self):
        self.session: Optional[aiohttp.ClientSession] = None
        self.cookies: Dict[str, str] = {}

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            headers=self._get_headers(),
            cookie_jar=aiohttp.CookieJar()
        )
        return self

    def _get_headers(self) -> Dict[str, str]:
        return {
            'User-Agent': self._get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
```

### 4. Handle Dynamic Content

```python
from playwright.async_api import async_playwright

async def extract_dynamic_content(url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Wait for dynamic content to load
        await page.goto(url)
        await page.wait_for_load_state('networkidle')

        # Wait for specific elements if needed
        await page.wait_for_selector('.content-loaded', timeout=30000)

        content = await page.content()
        await browser.close()

    return content
```

---

## Anti-Detection Strategies

### 1. Browser Fingerprint Randomization

```python
import random
from typing import Dict, Any

class FingerprintRandomizer:
    def __init__(self):
        self.user_agents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        self.viewport_sizes = [
            (1920, 1080), (1366, 768), (1536, 864), (1440, 900)
        ]

    def get_random_config(self) -> Dict[str, Any]:
        return {
            'user_agent': random.choice(self.user_agents),
            'viewport': random.choice(self.viewport_sizes),
            'locale': random.choice(['en-US', 'en-GB', 'en-CA']),
            'timezone': random.choice(['America/New_York', 'America/Chicago', 'America/Los_Angeles'])
        }
```

### 2. Human Behavior Simulation

```python
async def simulate_human_behavior(page):
    """Simulate human-like interactions with the page"""

    # Random mouse movements
    for _ in range(random.randint(2, 5)):
        x = random.randint(100, 800)
        y = random.randint(100, 600)
        await page.mouse.move(x, y)
        await asyncio.sleep(random.uniform(0.1, 0.3))

    # Random scrolling
    scroll_distance = random.randint(100, 300)
    await page.evaluate(f"window.scrollBy(0, {scroll_distance})")
    await asyncio.sleep(random.uniform(1, 2))

    # Occasional hover over elements
    elements = await page.query_selector_all('a, button')
    if elements:
        element = random.choice(elements[:5])  # Limit to first 5
        await element.hover()
        await asyncio.sleep(random.uniform(0.5, 1))
```

### 3. Detection Evasion Techniques

```javascript
// JavaScript injection to override detection properties
const overrideScript = """
    // Override navigator.webdriver
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    });

    // Override chrome automation properties
    Object.defineProperty(window, 'chrome', {
        get: () => ({
            runtime: {}
        })
    });

    // Override permissions query
    const originalQuery = window.navigator.permissions.query;
    window.navigator.permissions.query = (parameters) => (
        parameters.name === 'notifications' ?
            Promise.resolve({state: Notification.permission}) :
            originalQuery(parameters)
    );

    // Add realistic plugins
    Object.defineProperty(navigator, 'plugins', {
        get: () => [1, 2, 3, 4, 5]
    });
"""
```

---

## Data Quality Assurance

### 1. Content Validation Pipeline

```python
from typing import Dict, List, Tuple
import hashlib

class ContentValidator:
    def __init__(self):
        self.min_content_length = 10240  # 10KB minimum
        self.captcha_patterns = [
            "Let's confirm you are human",
            "Complete the security check",
            "Please verify you're not a robot"
        ]

    def validate(self, content: str, url: str) -> Tuple[bool, List[str]]:
        """Validate extracted content quality"""
        issues = []

        # Check content length
        if len(content) < self.min_content_length:
            issues.append(f"Content too short: {len(content)} bytes")

        # Check for CAPTCHA
        for pattern in self.captcha_patterns:
            if pattern in content:
                issues.append(f"CAPTCHA detected: '{pattern}'")

        # Check for actual FHIR content
        fhir_indicators = ['FHIR', 'HL7', 'resource', 'element']
        if not any(indicator in content for indicator in fhir_indicators):
            issues.append("No FHIR-specific content found")

        # Check encoding
        try:
            content.encode('utf-8')
        except UnicodeEncodeError:
            issues.append("Encoding issues detected")

        return len(issues) == 0, issues
```

### 2. Duplicate Detection

```python
class DuplicateDetector:
    def __init__(self):
        self.content_hashes = {}

    def is_duplicate(self, content: str, url: str) -> bool:
        """Detect duplicate content using content hashing"""
        # Normalize content
        normalized = self._normalize_content(content)
        content_hash = hashlib.sha256(normalized.encode()).hexdigest()

        if content_hash in self.content_hashes:
            original_url = self.content_hashes[content_hash]
            print(f"Duplicate content: {url} matches {original_url}")
            return True

        self.content_hashes[content_hash] = url
        return False

    def _normalize_content(self, content: str) -> str:
        """Remove whitespace and formatting for comparison"""
        import re
        # Remove extra whitespace
        content = re.sub(r'\s+', ' ', content)
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        return content.strip()
```

### 3. Metadata Preservation

```python
from datetime import datetime
import yaml

class MetadataManager:
    @staticmethod
    def create_frontmatter(url: str, title: str, metadata: Dict) -> str:
        """Create YAML frontmatter for markdown files"""
        frontmatter = {
            'url': url,
            'title': title,
            'extracted': datetime.now().isoformat(),
            'source': metadata.get('source', 'web_crawl'),
            'version': 'R4',
            'content_hash': hashlib.md5(url.encode()).hexdigest()[:8]
        }

        return f"---\n{yaml.dump(frontmatter, default_flow_style=False)}---\n\n"
```

---

## Performance Optimization

### 1. Concurrent Processing

```python
import asyncio
from typing import List, Callable
from asyncio import Semaphore

class ConcurrentProcessor:
    def __init__(self, max_workers: int = 5):
        self.semaphore = Semaphore(max_workers)

    async def process_batch(
        self,
        items: List[str],
        processor: Callable
    ) -> List[Any]:
        """Process items concurrently with rate limiting"""
        tasks = [
            self._process_with_semaphore(item, processor)
            for item in items
        ]
        return await asyncio.gather(*tasks, return_exceptions=True)

    async def _process_with_semaphore(self, item: str, processor: Callable):
        async with self.semaphore:
            return await processor(item)
```

### 2. Caching Strategy

```python
import pickle
import hashlib
from pathlib import Path
from typing import Optional, Any

class CacheManager:
    def __init__(self, cache_dir: str = ".cache"):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

    def get(self, key: str) -> Optional[Any]:
        """Retrieve cached content"""
        cache_file = self._get_cache_path(key)
        if cache_file.exists():
            with open(cache_file, 'rb') as f:
                data = pickle.load(f)
                # Check if cache is still valid (24 hours)
                if time.time() - data['timestamp'] < 86400:
                    return data['content']
        return None

    def set(self, key: str, value: Any):
        """Store content in cache"""
        cache_file = self._get_cache_path(key)
        with open(cache_file, 'wb') as f:
            pickle.dump({
                'content': value,
                'timestamp': time.time()
            }, f)

    def _get_cache_path(self, key: str) -> Path:
        """Generate cache file path from key"""
        hash_key = hashlib.md5(key.encode()).hexdigest()
        return self.cache_dir / f"{hash_key}.pkl"
```

### 3. Memory Management

```python
import gc
import psutil
import logging

class MemoryManager:
    def __init__(self, threshold_mb: int = 1024):
        self.threshold_bytes = threshold_mb * 1024 * 1024
        self.logger = logging.getLogger(__name__)

    def check_memory(self):
        """Check and manage memory usage"""
        process = psutil.Process()
        memory_info = process.memory_info()

        if memory_info.rss > self.threshold_bytes:
            self.logger.warning(f"High memory usage: {memory_info.rss / 1024 / 1024:.2f} MB")
            # Force garbage collection
            gc.collect()

            # Clear caches if needed
            self._clear_caches()

    def _clear_caches(self):
        """Clear internal caches to free memory"""
        # Clear BeautifulSoup parse tree cache
        from bs4 import BeautifulSoup
        BeautifulSoup.clear()

        # Clear other caches as needed
        import functools
        functools.lru_cache().cache_clear()
```

---

## Error Handling & Recovery

### 1. Retry Logic with Exponential Backoff

```python
import asyncio
from typing import Callable, Any, Optional
import logging

class RetryManager:
    def __init__(
        self,
        max_retries: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0
    ):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.logger = logging.getLogger(__name__)

    async def execute_with_retry(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> Optional[Any]:
        """Execute function with retry logic"""
        last_exception = None

        for attempt in range(self.max_retries):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                last_exception = e
                delay = min(
                    self.base_delay * (2 ** attempt),
                    self.max_delay
                )

                self.logger.warning(
                    f"Attempt {attempt + 1} failed: {str(e)}. "
                    f"Retrying in {delay:.1f} seconds..."
                )

                await asyncio.sleep(delay)

        self.logger.error(f"All retries failed: {str(last_exception)}")
        raise last_exception
```

### 2. Graceful Degradation

```python
class GracefulDegrader:
    def __init__(self):
        self.fallback_strategies = [
            self._try_direct_request,
            self._try_cached_version,
            self._try_wayback_machine,
            self._try_local_mirror
        ]

    async def fetch_with_fallback(self, url: str) -> Optional[str]:
        """Try multiple strategies to fetch content"""
        for strategy in self.fallback_strategies:
            try:
                content = await strategy(url)
                if content:
                    return content
            except Exception as e:
                logging.warning(f"Strategy {strategy.__name__} failed: {e}")
                continue

        return None

    async def _try_direct_request(self, url: str) -> str:
        """Direct HTTP request"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    async def _try_cached_version(self, url: str) -> Optional[str]:
        """Try local cache"""
        cache = CacheManager()
        return cache.get(url)

    async def _try_wayback_machine(self, url: str) -> Optional[str]:
        """Try Internet Archive"""
        wayback_url = f"https://web.archive.org/web/*/{url}"
        # Implementation details...
        return None

    async def _try_local_mirror(self, url: str) -> Optional[str]:
        """Try local mirror if available"""
        # Implementation details...
        return None
```

---

## Documentation Standards

### 1. Code Documentation

```python
def extract_markdown(
    html_content: str,
    base_url: str,
    preserve_links: bool = True
) -> str:
    """
    Extract and convert HTML content to Markdown format.

    This function processes raw HTML content and converts it to clean,
    structured Markdown suitable for documentation purposes.

    Args:
        html_content (str): Raw HTML content to process
        base_url (str): Base URL for resolving relative links
        preserve_links (bool): Whether to preserve hyperlinks in output

    Returns:
        str: Processed Markdown content

    Raises:
        ValueError: If html_content is empty or invalid
        ConversionError: If conversion process fails

    Example:
        >>> html = "<h1>Title</h1><p>Content</p>"
        >>> markdown = extract_markdown(html, "https://example.com")
        >>> print(markdown)
        # Title\n\nContent

    Note:
        - Tables are converted to ASCII format
        - Images are preserved with alt text
        - Code blocks maintain syntax highlighting hints
    """
    # Implementation...
```

### 2. Configuration Documentation

```yaml
# crawler_config.yml
# Configuration for FHIR R4 documentation crawler
# Last updated: 2025-11-08

# Browser Configuration
browser:
  headless: true  # Run in headless mode for production
  user_agent: "Mozilla/5.0..."  # Spoofed user agent string
  viewport:
    width: 1920  # Standard desktop viewport
    height: 1080

  # Anti-detection measures
  anti_detection:
    simulate_user: true  # Simulate human-like behavior
    override_navigator: true  # Override navigator.webdriver
    randomize_fingerprint: true  # Randomize browser fingerprint

  # Network settings
  network:
    timeout: 45000  # 45 seconds timeout
    retry_count: 3  # Number of retries on failure

# Extraction Configuration
extraction:
  # Content validation
  validation:
    min_size: 10240  # Minimum 10KB for valid content
    check_captcha: true  # Detect CAPTCHA challenges
    verify_encoding: true  # Ensure UTF-8 encoding

  # Performance settings
  performance:
    max_workers: 5  # Concurrent extraction workers
    cache_enabled: true  # Enable content caching
    cache_ttl: 86400  # Cache for 24 hours
```

### 3. Operational Runbooks

```markdown
## Runbook: CAPTCHA Detection and Recovery

### Symptoms
- Extracted files contain "Let's confirm you are human"
- Multiple pages have identical content
- File sizes < 10KB for pages that should be larger

### Diagnosis
1. Check recent extraction logs:
   ```bash
   grep -i "captcha\|human" logs/extraction_*.log
   ```

2. Validate affected files:
   ```bash
   for file in 03_OUTPUTS_COMPLETE/markdown/*.md; do
     if grep -q "confirm you are human" "$file"; then
       echo "$file is affected"
     fi
   done
   ```

### Recovery Steps
1. **Immediate Action**
   - Stop current extraction process
   - Switch to local mirror mode

2. **Execute Recovery**
   ```bash
   # Download official specification
   wget https://hl7.org/fhir/R4/fhir-spec.zip

   # Extract and rebuild
   python scripts/10_rebuild_markdown_from_local.py
   ```

3. **Verify Recovery**
   ```bash
   python scripts/validate_outputs.py
   ```

### Prevention
- Implement longer delays between requests
- Rotate user agents more frequently
- Consider using proxy rotation
```

---

## Security Considerations

### 1. Input Validation

```python
import re
from urllib.parse import urlparse
from typing import Optional

class SecurityValidator:
    def __init__(self):
        self.allowed_domains = ['hl7.org', 'www.hl7.org']
        self.blocked_patterns = [
            r'javascript:',
            r'data:',
            r'vbscript:',
            r'file://'
        ]

    def validate_url(self, url: str) -> bool:
        """Validate URL for security concerns"""
        # Parse URL
        try:
            parsed = urlparse(url)
        except Exception:
            return False

        # Check domain whitelist
        if parsed.netloc not in self.allowed_domains:
            return False

        # Check for blocked patterns
        for pattern in self.blocked_patterns:
            if re.search(pattern, url, re.IGNORECASE):
                return False

        # Ensure HTTPS
        if parsed.scheme != 'https':
            return False

        return True
```

### 2. Secrets Management

```python
import os
from pathlib import Path
from cryptography.fernet import Fernet

class SecretsManager:
    def __init__(self, key_file: str = ".secrets.key"):
        self.key_file = Path(key_file)
        self.cipher = self._get_cipher()

    def _get_cipher(self) -> Fernet:
        """Get or create encryption cipher"""
        if self.key_file.exists():
            key = self.key_file.read_bytes()
        else:
            key = Fernet.generate_key()
            self.key_file.write_bytes(key)
            self.key_file.chmod(0o600)  # Restrict permissions

        return Fernet(key)

    def encrypt_secret(self, secret: str) -> str:
        """Encrypt sensitive data"""
        return self.cipher.encrypt(secret.encode()).decode()

    def decrypt_secret(self, encrypted: str) -> str:
        """Decrypt sensitive data"""
        return self.cipher.decrypt(encrypted.encode()).decode()
```

---

## Future Improvements

### 1. Machine Learning Integration

```python
# Potential ML-based CAPTCHA detection
from sklearn.ensemble import RandomForestClassifier
import numpy as np

class CaptchaDetector:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.features = []

    def extract_features(self, content: str) -> np.ndarray:
        """Extract features for ML classification"""
        features = [
            len(content),
            content.count('human'),
            content.count('robot'),
            content.count('verify'),
            # Add more features
        ]
        return np.array(features)

    def predict(self, content: str) -> bool:
        """Predict if content is CAPTCHA"""
        features = self.extract_features(content)
        return self.model.predict([features])[0] == 1
```

### 2. Distributed Crawling

```python
# Potential distributed architecture using Celery
from celery import Celery

app = Celery('fhir_crawler', broker='redis://localhost:6379')

@app.task(bind=True, max_retries=3)
def extract_page_task(self, url: str):
    """Distributed page extraction task"""
    try:
        return extract_page(url)
    except Exception as exc:
        # Exponential backoff
        raise self.retry(exc=exc, countdown=2 ** self.request.retries)

# Orchestration
def distribute_extraction(urls: List[str]):
    """Distribute extraction across workers"""
    job = group(extract_page_task.s(url) for url in urls)
    result = job.apply_async()
    return result.get(timeout=300)
```

### 3. Real-time Monitoring

```python
# Potential monitoring with Prometheus
from prometheus_client import Counter, Histogram, start_http_server

# Metrics
extraction_counter = Counter(
    'page_extractions_total',
    'Total number of page extractions',
    ['status']
)

extraction_duration = Histogram(
    'extraction_duration_seconds',
    'Page extraction duration'
)

@extraction_duration.time()
async def monitored_extraction(url: str):
    """Extract with monitoring"""
    try:
        result = await extract_page(url)
        extraction_counter.labels(status='success').inc()
        return result
    except Exception as e:
        extraction_counter.labels(status='failure').inc()
        raise
```

---

## Conclusion

This technical best practices document represents the accumulated knowledge from building and operating the FHIR R4 crawler. Key takeaways:

1. **Adaptability is crucial** - When web crawling fails, have alternative approaches ready
2. **Quality over quantity** - Better to extract fewer high-quality pages than many corrupted ones
3. **Documentation is code** - Treat documentation with the same rigor as production code
4. **Monitor everything** - You can't improve what you don't measure
5. **Security first** - Always validate inputs and protect sensitive data

These practices should be continuously refined as the project evolves and new challenges emerge.

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Next Review**: February 8, 2026

---

*For questions or improvements, please submit a pull request to the repository.*