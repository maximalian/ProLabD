import psycopg2
import requests
from bs4 import BeautifulSoup
import json
import math

def fetch_price(url):
    try:
        # Check if URL is valid (not NaN or None)
        if url is None or url == 'NaN' or isinstance(url, float) and math.isnan(url):
            print(f"Invalid URL: {url}")
            return None

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        price = None
        
        if "barbora" in url:
            # Look for the price within the Barbora page's structure
            product_info_div = soup.find("div", class_="b-product-info")
            if product_info_div and 'data-b-units' in product_info_div.attrs:
                # Extract the JSON data from data-b-units attribute
                data_units = json.loads(product_info_div['data-b-units'])
                price = data_units['units'][0]['price']  # Extract price

        elif "rimi" in url:
            price_element = soup.select_one('.price-per')
            if price_element:
                price_text = price_element.text.replace('€', '').replace(',', '.').strip()
                price_text = price_text.split()[0]
                price = float(price_text)
        
        return price
    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 404:
            print(f"Page not found (404) for URL: {url}")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as e:
        print(f"Error fetching price from {url}: {e}")
        return None

def update_product_prices():
    conn = psycopg2.connect(
        host="13.61.89.142",
        port="5432",
        database="prolab24",
        user="postgres",
        password="prolab24",
        options="-c client_encoding=UTF8"
    )
    cursor = conn.cursor()

    # Step 1: Reset prices in the database
    cursor.execute("UPDATE Produkts SET cena_maxima = NULL, cena_rimi = NULL")
    conn.commit()
    print("Previous prices cleared.")

    # Step 2: Fetch products with links and units of measurement
    cursor.execute("SELECT id, saite_maxima, saite_rimi, meris_vieniba FROM Produkts")
    products = cursor.fetchall()

    for product in products:
        product_id, saite_maxima, saite_rimi, meris_vieniba = product
        cena_maxima, cena_rimi = None, None

        # Check if Barbora (Maxima) link exists and fetch price if available
        if saite_maxima and saite_maxima != 'NaN':
            price = fetch_price(saite_maxima)
            if price is not None:
                cena_maxima = price if meris_vieniba == 'gab' else price / 10  # Adjust for unit if needed

        # Check if Rimi link exists and fetch price if available
        if saite_rimi and saite_rimi != 'NaN':
            price = fetch_price(saite_rimi)
            if price is not None:
                cena_rimi = price if meris_vieniba == 'gab' else price / 10

        # Update the product's prices in the database
        update_query = """
        UPDATE Produkts
        SET cena_maxima = %s, cena_rimi = %s
        WHERE id = %s
        """
        cursor.execute(update_query, (cena_maxima, cena_rimi, product_id))

    conn.commit()
    cursor.close()
    conn.close()
    print("Product prices updated.")

# Run the function
update_product_prices()
