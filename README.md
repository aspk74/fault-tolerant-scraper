# Fault-Tolerant Web Scraper

Production-grade scraper with:
- Auto-retry for failed requests
- Proxy rotation
- Prometheus monitoring

## 🚀 Deployment
```bash
# Local run
scrapy crawl robust -o output.json

# Docker (with monitoring)
docker-compose up --build