import sys
import antigravity

# Usage example:
# python3 geohashing.py 37.421542 -122.085589 "2024-07-29-06:15:00"

def geohashing():
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py <latitude> <longitude> <date>")
        sys.exit(1)
    
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date = sys.argv[3]
    except ValueError:
        print("Error: Latitude and Longitude must be valid numbers.")
        sys.exit(1)
    
    # The antigravity module's geohashing function expects the date in a specific format
    try:
        antigravity.geohash(latitude, longitude, date.encode('utf-8'))
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    geohashing()