import pycurl
from io import BytesIO


def ping_url():
    url = input("Enter your URL: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    buf = BytesIO()
    c = pycurl.Curl()
    try:
        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buf)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.TIMEOUT, 15)
        c.perform()
        print({
            "status": c.getinfo(c.RESPONSE_CODE),
            "dns": c.getinfo(c.NAMELOOKUP_TIME),
            "connect": c.getinfo(c.CONNECT_TIME),
            "tls": c.getinfo(c.APPCONNECT_TIME),
            "ttfb": c.getinfo(c.STARTTRANSFER_TIME),
            "total": c.getinfo(c.TOTAL_TIME),
            "bytes": c.getinfo(c.SIZE_DOWNLOAD_T),
            "ip": c.getinfo(c.PRIMARY_IP),
        })
    except pycurl.error as e:
        print(f"Request failed: {e}")
    finally:
        c.close()


if __name__ == "__main__":
    ping_url()