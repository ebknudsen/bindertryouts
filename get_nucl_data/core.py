#!/usr/bin/python3
import pathlib as pl
import requests
import subprocess as sp
import sys

nucl_data_urls={
        'endfb_VII':"https://anl.box.com/shared/static/d359skd2w6wrm86om2997a1bxgigc8pu.xz",
        'endfb_VIII':"https://anl.box.com/shared/static/nd7p4jherolkx4b1rfaw5uqp58nxtstr.xz",
        'jeff':"https://anl.box.com/shared/static/ddetxzp0gv1buk1ev67b8ynik7f268hw.xz"
        }

class GetData():
    def __init__(self,libname='endfb_VII', dirname='nuclear_data'):
        self.libname=libname
        self.dirname=dirname
        self.url=nucl_data_urls[libname]
        self.localname=self.url.split('/')[-1]
        self.path=self.dirname / pl.Path(self.localname)

    def get_nucl_data(self):
        if self.path.exists():
            return str(self.path)
        if not pl.Path(self.dirname).exists():
            pl.Path(self.dirname).mkdir(parents=True)
        with requests.get(self.url, stream=True) as r:
            print(f'retreiving {self.libname} nuclear cross section data from {self.url} to {self.dirname}')
            r.raise_for_status()
            tot_len=int(r.headers.get('content-length'))
            with open(self.path, 'wb') as f:
                dl=0
                for chunk in r.iter_content(chunk_size=8192):
                    dl += len(chunk)
                    f.write(chunk)
                    done=float(dl) / tot_len*100.0
                    sys.stdout.write(f"\r{done:4.1f} % done")
                    sys.stdout.flush()
        return str(self.path)

    def extract_nucl_data(self):
        if self.path.exists():
            print(f'Info: extracting nuclear cross sections into {self.dirname}')
            results.sp.run(['tar','-xf','--verbose',self.path],capture_output=True,text=True)
            s=results.split()
            print(f'info: extracted {len(s)} .h5-files from {s[0]} to {s[-1]}')
        #store the base extracted path - for instance to set the OPENMC_CROSS_SECTIONS env. var.
        self.extract_path=pl.Path(s[0]).parent()
        return str(self.extract_path)

    def cleanup(self):
        self.path.unlink(missing_ok=True)
    
    def purge(self):
        p = pl.Path(self.dirname)
        for pp in p.glob('*'):
            print('unlink ' / (self.dirname / pp) )
