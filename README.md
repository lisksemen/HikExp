# HikExp
Simple script to test hikvision cameras (CVE-2021-36260)

### Installation
#### Requirements:
* Python
* Routerscan (http://stascorp.com/load/1-1-0-56)
* Git
Run to install:
```
apt install git python3 && git clone https://github.com/lisksemen/HikExp
```

After scanning ips with routerscan export scan table to the application directory.
Enter your filename on 18 line in main.py
Run main.py with:
```
python3 main.py
```

Vulnerable ips and ports will appear in results.txt
