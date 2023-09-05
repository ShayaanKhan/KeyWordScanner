from utils.intelx import intelx
from rich import print
import os

if (x:=os.getenv('INTELX_API_KEY')):
    itx = intelx(x)
else:
    itx = intelx()

while True:
    email = input('Search email/domain: ')

    records = itx.search(email, maxresults=9999)['records']
    print(f"[bold red]Found {len(records)} records[/bold red]")

    for result in records:
        content = itx.FILE_VIEW(
            result['type'],
            result['media'],
            result['storageid'],
            result['bucket']
        )
        for line in content.split('\n'):
            if email in line:
                print(':+1: ', line.strip(), '[bold]{from: [red]%s[/red]}[/bold]\n' % result['name'])