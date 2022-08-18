"""
change the WMO of argo_floats , see all the cyclies easily on different figures that makes it more understandable


"""
import numpy as np
import xarray as xr
import netCDF4
xr.set_options(display_style="html", display_expand_attrs=False);
from matplotlib import pyplot as plt
from argopy import DataFetcher as ArgoDataFetcher

def cycle_number():
    argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
    apDS = argo_loader.float(3902004).load().data
    data = apDS.argo.point2profile()
    cycle = []
    cycle = data.CYCLE_NUMBER
    c = int(cycle[len(cycle) - 1])  # c miz artık cycle sayısı
    return c

argo_float=3902004
#number=cycle_number()
number=40
print(number)

check_point=0
j=1
if number%4==0:
    while(True):
        print(check_point,int(number/4))


        if check_point==number/4:
            break

        argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
        fig, ax = plt.subplots(nrows=2, ncols=4)
        z = 4  # 4 cycle on one figure
        k = 0  # temperature
        l = 1  # salinity
        m = 0  # buffer of temperature and salinity

        while(z>0):
            argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
            argo_loader = argo_loader.profile(argo_float,j).load()
            apDS2 = argo_loader.data
            data = apDS2.argo.point2profile()

            # Temperature
            ax[k,m].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
            ax[k,m].set_title("SEA TEMPERATURE IN SITU\nITS-90 SCALE\n{}. cycle".format(j))
            ax[k,m].set_ylabel(data.PRES.long_name)
            ax[k,m].grid()
            ax[k,m].legend()

            # Salinity
            ax[l,m].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
            ax[l,m].set_title(data.PSAL.long_name)
            ax[l,m].grid()
            z=z-1
            j=j+1
            m=m+1

        check_point=check_point+1
elif number%4!=0:
    buffer=number
    while(True):

        argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
        if buffer>4:
            fig, ax = plt.subplots(nrows=2, ncols=4)
            z = 4  # 4 cycle on one figure
            k = 0  # temperature
            l = 1  # salinity
            m = 0  # buffer of temperature and salinity

            while(z>0):
                argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
                argo_loader = argo_loader.profile(argo_float,j).load()
                apDS2 = argo_loader.data
                data = apDS2.argo.point2profile()

                # Temperature
                ax[k,m].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[k,m].set_title("SEA TEMPERATURE IN SITU\nITS-90 SCALE\n{}. cycle".format(j))
                ax[k,m].set_ylabel(data.PRES.long_name)
                ax[k,m].grid()
                ax[k,m].legend()

                # Salinity
                ax[l,m].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[l,m].set_title(data.PSAL.long_name)
                ax[l,m].grid()
                z=z-1
                j=j+1
                m=m+1
            buffer = buffer - 4
        elif 0<buffer<4:
            fig, ax = plt.subplots(nrows=2, ncols=buffer)
            z = buffer   # 4 cycle on one figure
            k = 0  # temperature
            l = 1  # salinity
            m = 0  # buffer of temperature and salinity

            while (z > 0):

                argo_loader = ArgoDataFetcher(src='erddap', cache=True, cachedir='tmp')
                argo_loader = argo_loader.profile(argo_float, j).load()
                apDS2 = argo_loader.data
                data = apDS2.argo.point2profile()

                # Temperature
                ax[k, m].plot(data.TEMP[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[k, m].set_title("SEA TEMPERATURE IN SITU\nITS-90 SCALE\n{}. cycle".format(j))
                ax[k, m].set_ylabel(data.PRES.long_name)
                ax[k, m].grid()
                ax[k, m].legend()

                # Salinity
                ax[l, m].plot(data.PSAL[0], -data.PRES[0], 'b-', label='N_PROF=0')
                ax[l, m].set_title(data.PSAL.long_name)
                ax[l, m].grid()
                z = z - 1
                j = j + 1
                m = m + 1
            buffer = buffer - 4

        else:
            break
        check_point=check_point+1
plt.show()
