import sys, requests

def main():
    if len(sys.argv) == 2:
        try:
            qty = float(sys.argv[1])
            get_bitcoin(qty)
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit()
    else:
        print("Missing command-line argument")
        sys.exit()

def get_bitcoin(n):
    try:
        url = "https://api.coincap.io/v2/assets/bitcoin"
        print(f"Fetching price of {n} Bitcoin(s)...\n")
        r = requests.get(url)
        r_json = r.json()
        price = r_json["data"]["priceUsd"]
        f_price = float(price)
        o_price = round(f_price * n, 4)
        print(f"Price for {n} Bitcoin: ${o_price:,.2f}")

    except requests.RequestException:
        print("Error fetching")

    except KeyError:
        print("Key error, data not returned or has changed naming/structure")

if __name__ == "__main__":
    main()