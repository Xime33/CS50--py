import sys
import requests

def main():
    if len(sys.argv)== 2:
        try:
            num = float(sys.argv[1])
        except:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #convert into a dictionary
        r = url.json()
        rate = r['bpi']['USD']['rate_float']
    except requests.RequestException:
        sys.exit(1)

    x = float(sys.argv[1])* rate
    print(f"${x:,.4f}")





main()
