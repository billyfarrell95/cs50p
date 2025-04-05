import sys, requests

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        qty = float(sys.argv[1])
        print(f"${get_bitcoin(qty)}")
    except ValueError:
        sys.exit(1)

def get_bitcoin(n):
    try:
        url = "https://api.coincap.io/v2/assets/bitcoin"
        r = requests.get(url)
        r_json = r.json()
        price = r_json["data"]["priceUsd"]
        f_price = float(price)
        o_price = round(f_price * n, 4)
        return f"{o_price:,.4f}"

    except requests.RequestException:
        print("Error fetching")

    except KeyError:
        print("Key error, data not returned or has changed naming/structure")

if __name__ == "__main__":
    main()

# PASS
# check50 --local cs50/problems/2022/python/bitcoin