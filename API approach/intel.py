import os
from rich import print

from utils.intelx import intelx

# Verify the correct location of the intelx module and update the import statement if necessary

x = os.getenv('intelToken')

if x:
    itx = intelx(x)
else:
    itx = intelx()

while True:
    email = input('Search email/domain: ')

    records = itx.search(email, max_results=9999)['records']
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
