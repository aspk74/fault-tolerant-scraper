from datetime import datetime

class ValidationPipeline:
    def process_item(self, item, spider):
        if not item.get('url'):
            raise scrapy.exceptions.DropItem("Missing URL")
        item['timestamp'] = datetime.utcnow()
        return item