# Debian-Preseed-Options

```bash
apt install -y debconf-utils
debconf-get-selections --installer > preseed-raw.cfg
debconf-get-selections >> preseed-raw.cfg
python3 sort-options.py
# view `preseed.cfg`
```
