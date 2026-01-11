#!/usr/bin/env python3
# coding: utf-8
#
# Simple NMEA Serial Parser for Beidou/GPS
#
import serial
import time


def parse_lat(lat, ns):
    if not lat:
        return None
    deg = int(float(lat) / 100)
    minute = float(lat) - deg * 100
    val = deg + minute / 60
    if ns == 'S':
        val = -val
    return val


def parse_lon(lon, ew):
    if not lon:
        return None
    deg = int(float(lon) / 100)
    minute = float(lon) - deg * 100
    val = deg + minute / 60
    if ew == 'W':
        val = -val
    return val


def parse_nmea(line):
    """Return dict with parsed data or None."""
    if not line.startswith("$"):
        return None

    parts = line.split(',')
    head = parts[0][3:]   # e.g. BDGGA -> GGA
    data = {}

    try:
        if head.endswith("ZDA"):
            # $BDZDA,121852.00,22,11,2025,00,00*7F
            data["type"] = "ZDA"
            data["utc"] = parts[1]
            data["day"] = parts[2]
            data["month"] = parts[3]
            data["year"] = parts[4]

        elif head.endswith("RMC"):
            # $BDRMC,121853.00,A,3951.66,N,11629.76,E,0.30,,221125,,,A,V*28
            data["type"] = "RMC"
            data["utc"] = parts[1]
            data["valid"] = parts[2]
            data["lat"] = parse_lat(parts[3], parts[4])
            data["lon"] = parse_lon(parts[5], parts[6])
            data["speed_knots"] = parts[7]

        elif head.endswith("GGA"):
            # $BDGGA,121853.00,3951...,N,116...,E,1,12,1.8,62.54,M,-8.63,M,,*55
            data["type"] = "GGA"
            data["utc"] = parts[1]
            data["lat"] = parse_lat(parts[2], parts[3])
            data["lon"] = parse_lon(parts[4], parts[5])
            data["fix"] = parts[6]
            data["sat"] = parts[7]
            data["hdop"] = parts[8]
            data["alt"] = parts[9]

        elif head.endswith("GSA"):
            data["type"] = "GSA"
            data["mode"] = parts[1]
            data["fix_type"] = parts[2]
            data["pdop"] = parts[-3]
            data["hdop"] = parts[-2]
            data["vdop"] = parts[-1].split('*')[0]

        elif head.endswith("TXT"):
            data["type"] = "TXT"
            data["msg"] = parts[4].split('*')[0]

        else:
            # Not supported yet
            return None

        return data

    except Exception:
        return None


def main():
    port = input("Enter COM port (e.g., COM3): ").strip()
    baud = input("Baudrate (e.g., 115200): ").strip()

    ser = serial.Serial(port, int(baud), timeout=0.2)
    print("\n--- Listening NMEA on %s ---\n" % port)

    last_pos = None

    while True:
        try:
            line = ser.readline().decode(errors='ignore').strip()
            if not line:
                continue

            parsed = parse_nmea(line)
            if not parsed:
                continue

            t = parsed["type"]

            if t == "TXT":
                print("[TXT] %s" % parsed["msg"])

            elif t == "ZDA":
                print("[TIME] %s-%s-%s  %s UTC" %
                      (parsed["year"], parsed["month"], parsed["day"], parsed["utc"]))

            elif t == "RMC":
                if parsed["lat"] and parsed["lon"]:
                    print("[RMC] Lat: %.6f  Lon: %.6f  Speed(knots): %s" %
                          (parsed["lat"], parsed["lon"], parsed["speed_knots"]))

            elif t == "GGA":
                print("[GGA] Fix:%s  Sat:%s  HDOP:%s  Alt:%s m" %
                      (parsed["fix"], parsed["sat"], parsed["hdop"], parsed["alt"]))

            elif t == "GSA":
                print("[GSA] PDOP:%s  HDOP:%s  VDOP:%s" %
                      (parsed["pdop"], parsed["hdop"], parsed["vdop"]))

        except KeyboardInterrupt:
            break

    ser.close()


if __name__ == "__main__":
    main()
