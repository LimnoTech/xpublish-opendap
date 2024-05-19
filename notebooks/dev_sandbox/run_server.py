import xarray as xr
import xpublish
from xpublish_opendap import OpenDapPlugin
from pathlib import Path
import uvicorn
import nest_asyncio
nest_asyncio.apply()

HOST = '127.0.0.1'
PORT = 8000
PATH = Path(__file__).parent / "data/PRISM_v2_slice.nc"

def main():
    ds = xr.open_dataset(
        PATH,
        engine='netcdf4'
    )

    rest = xpublish.Rest(
        {'ds': ds},
        plugins={'opendap': OpenDapPlugin()}
    )

    rest.serve(host=HOST, port=PORT)

if __name__ == '__main__':
    print(PATH)
    main()

