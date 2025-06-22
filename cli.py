import argparse

def cel_to_fah(c):
    return (c * 9/5) + 32

def fah_to_cel(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description='Convert temperature between Celsius(°C) and Fahrenheit(°F).'
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--c2f', type=float, help='Convert Celsius to Fahrenheit')
    group.add_argument('--f2c', type=float, help='Convert Fahrenheit to Celsius')

    args = parser.parse_args()

    if args.c2f is not None:
        fahrenheit = cel_to_fah(args.c2f)
        print(f"{args.c2f}°C = {fahrenheit:.2f}°F")
    elif args.f2c is not None:
        celsius = fah_to_cel(args.f2c)
        print(f"{args.f2c}°F = {celsius:.2f}°C")

if __name__ == "__main__":
    main()
