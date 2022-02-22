#!/usr/bin/python3
import pathlib as pl
import requests
import subprocess as sp

data_locations={
        'endfb_VII':"https://anl.box.com/shared/static/d359skd2w6wrm86om2997a1bxgigc8pu.xz",
        'endfb_VIII':"https://anl.box.com/shared/static/nd7p4jherolkx4b1rfaw5uqp58nxtstr.xz",
        'jeff':"https://anl.box.com/shared/static/ddetxzp0gv1buk1ev67b8ynik7f268hw.xz"
        }

def get_nucl_data(libname='endfb_VIII', dirname=''):
    url=data_locations[libname]
    localname=url.split('/')[-1]
    p=pl.Path(localname)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dirname / p, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return (dirname / p).str

def extract_nucl_data(libname='endfb_VIII',dirname=''):
    url=data_locations[libname]
    localname=url.split('/')[-1]
    p=pl.Path(localname)
    if p.exists():
        results.sp.run(['tar','-xf','--verbose',p],capture_output=True,text=True)
        s=results.split()
        print(f'info: extracted {len(s)} .h5-files from {s[0]} to {s[-1]}')

def cleanup(libname='endfb_VIII',dirname=''):
    url=data_locations[libname]
    localname=url.split('/')[-1]
    p=pl.Path(localname)
    p.unlink(missing_ok=True)
