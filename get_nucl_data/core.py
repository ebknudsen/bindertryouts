#!/usr/bin/python3
import pathlib as pl
import requests
import subprocess as sp

nucl_data_urls={
        'endfb_VII':"https://anl.box.com/shared/static/d359skd2w6wrm86om2997a1bxgigc8pu.xz",
        'endfb_VIII':"https://anl.box.com/shared/static/nd7p4jherolkx4b1rfaw5uqp58nxtstr.xz",
        'jeff':"https://anl.box.com/shared/static/ddetxzp0gv1buk1ev67b8ynik7f268hw.xz"
        }

class GetData():
    def __init__(self,libname='endfb_VIII', dirname='nuclear_data'):
        self.libname=libname
        self.dirname=dirname
        self.url=nucl_data_urls[libname]
        self.localname=self.url.split('/')[-1]
        self.path=self.dirname / pl.Path(self.localname)

    def get_nucl_data(self):
        if not pl.Path(self.dirname).exists():
            pl.Path.mkdir(parents=True)
        with requests.get(self.url, stream=True) as r:
            r.raise_for_status()
            with open(self.path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return str(dirname / p)

    def extract_nucl_data(self):
        if self.path.exists():
            results.sp.run(['tar','-xf','--verbose',self.path],capture_output=True,text=True)
            s=results.split()
            print(f'info: extracted {len(s)} .h5-files from {s[0]} to {s[-1]}')

    def cleanup(self):
        self.path.unlink(missing_ok=True)
    
    def purge(self):
        p = pl.Path(self.dirname)
        for pp in p.glob('*'):
            print('unlink ' / (self.dirname / pp) )
