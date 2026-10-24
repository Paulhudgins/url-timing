# url-timing

A small Python tool that requests a URL and reports connection timing broken down by phase (DNS, TCP connect, TLS, time to first byte, total), using libcurl via `pycurl`.

This is the first piece of a larger personal project: a custom performance testing and monitoring tool built in Python.

## Requirements

- Python 3.x
- pycurl

```
python -m pip install -r requirements.txt
```

## Usage

```
python url_timing.py
```

Enter a URL when prompted. If no scheme is given, `https://` is assumed.

## Sample output

```
{'status': 200, 'dns': 0.031348, 'connect': 0.061915, 'tls': 0.164104, 'ttfb': 0.203806, 'total': 0.22403, 'bytes': 87445, 'ip': '142.251.154.119'}
```

Timings are in seconds and **cumulative** from the start of the request (libcurl behavior). Per-phase