# ports_scanner_py

Escáner de puertos TCP en Python 3. Escanea una o varias IPs/hosts sobre un
rango de puertos configurable mediante un *connect scan*.

> ⚠️ **Uso autorizado únicamente.** Escanea solo sistemas de tu propiedad o
> para los que tengas permiso explícito. El escaneo de puertos no autorizado
> puede ser ilegal en tu jurisdicción.

## Requisitos

- Python 3.6 o superior (solo usa la librería estándar, sin dependencias).

## Uso

Modo con argumentos (recomendado):

```bash
# Escanear los puertos 1-1024 (por defecto) de un host
python3 ports_scanner.py 10.0.0.1

# Rango o lista de puertos concretos
python3 ports_scanner.py 10.0.0.1 -p 1-65535
python3 ports_scanner.py 10.0.0.1 -p 22,80,443

# Varios objetivos y timeout más agresivo
python3 ports_scanner.py 10.0.0.1,10.0.0.2 -p 1-1024 -t 0.5
```

Modo interactivo (si no pasas objetivo, lo pregunta):

```bash
python3 ports_scanner.py
```

## Opciones

| Opción            | Descripción                                             |
|-------------------|---------------------------------------------------------|
| `targets`         | IP(s) u host(s) separados por coma                      |
| `-p`, `--ports`   | Puertos: `1-1024`, `80` o `22,80,443` (def. `1-1024`)   |
| `-t`, `--timeout` | Timeout por conexión en segundos (def. `1.0`)           |

Probado en Kali Linux y Parrot OS.
