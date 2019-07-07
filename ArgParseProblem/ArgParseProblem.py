import argparse

def print_details(n, metric, device, provider=False):
    print(n)
    print(metric)
    print(device)
    print(provider)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", help="Please provide the no of days", type=int)
    parser.add_argument("metric", help="Please provide the metric", type=str)
    parser.add_argument("device", help="Please provide the device id", type=str)
    parser.add_argument("-o", '--p', help="Please provide the provider", type=str, default="...")
    
    args = parser.parse_args()
    print_details(args.n, args.metric, args.device, args.p)


if __name__ == "__main__":
    main()