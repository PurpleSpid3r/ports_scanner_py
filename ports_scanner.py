#!/usr/bin/env python3
"""*********************************************************"""
"""**************************** ****************************"""
"""***************  HECHO POR PURPL3SP1D3r  ****************"""
"""**************************** ****************************"""
"""*********************************************************"""

"""Escáner de puertos TCP simple en Python 3.

Realiza un "connect scan" (TCP) sobre uno o varios objetivos y un rango de
puertos configurable. Pensado para aprendizaje y laboratorios de pentesting
autorizados. Úsalo solo contra sistemas para los que tengas permiso explícito.
"""
import argparse
import socket
import sys


def scan_port(host, port, timeout):
    """Devuelve True si el puerto TCP está abierto en `host`."""
    # connect_ex devuelve 0 si la conexión tuvo éxito, en lugar de lanzar una
    # excepción: es más limpio para comprobar puertos uno a uno.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            return sock.connect_ex((host, port)) == 0
        except (socket.gaierror, OSError):
            # Host no resoluble o error de red: lo tratamos como cerrado.
            return False


def scan(host, ports, timeout):
    """Escanea una lista de puertos en `host` y devuelve los abiertos."""
    print(f"\n[*] Escaneando {host} ({ports[0]}-{ports[-1]}, {len(ports)} puertos)")
    abiertos = []
    for port in ports:
        if scan_port(host, port, timeout):
            print(f"[+] Puerto abierto: {port}")
            abiertos.append(port)
    if not abiertos:
        print("[-] No se encontraron puertos abiertos en el rango indicado.")
    return abiertos


def parse_ports(spec):
    """Convierte '1-1024', '80' o '22,80,443' en una lista ordenada de puertos."""
    ports = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            ports.update(range(int(start), int(end) + 1))  # rango inclusivo
        else:
            ports.add(int(part))
    return sorted(p for p in ports if 0 < p <= 65535)


def main():
    parser = argparse.ArgumentParser(description="Escáner de puertos TCP.")
    parser.add_argument("targets", nargs="?",
                        help="IP(s) u host(s) a escanear, separados por coma")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Puertos: '1-1024', '80' o '22,80,443' (por defecto 1-1024)")
    parser.add_argument("-t", "--timeout", type=float, default=1.0,
                        help="Timeout por conexión en segundos (por defecto 1.0)")
    args = parser.parse_args()

    targets = args.targets or input(
        "[*] Ingresa objetivo(s) separados por coma: ")

    try:
        ports = parse_ports(args.ports)
    except ValueError:
        parser.error("Formato de puertos inválido. Ej: '1-1024', '80', '22,80,443'.")
    if not ports:
        parser.error("El rango de puertos quedó vacío.")

    for target in (t.strip() for t in targets.split(",") if t.strip()):
        scan(target, ports, args.timeout)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Escaneo interrumpido por el usuario.")
        sys.exit(130)
