from apscheduler.schedulers.background import BackgroundScheduler
from scrape_script import scrape_product_prices

scheduler = BackgroundScheduler()

def scheduled_scraping():
    url = 'https://example.com/products'
    prices = scrape_product_prices(url)
    print(f"Scraped prices: {prices}")

# Programar la tarea para ejecutarse cada 30 minutos
scheduler.add_job(scheduled_scraping, 'interval', minutes=30)
scheduler.start()

if __name__ == "__main__":
    try:
        while True:
            pass  # Mantener el scheduler corriendo
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
