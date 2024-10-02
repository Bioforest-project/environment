# log
log_file = open(snakemake.log[0],"w")
sys.stderr = sys.stdout = log_file

# variables
sites_tab = snakemake.input[0]
site = snakemake.params.site
radius = snakemake.params.radius
out_file = snakemake.output[0]

# test
# sites_tab = "config/sites.tsv"
# site = "Uppangala_LP2"
# radius = 0.009
# out_file = "data/landscape/Uppangala_LP2_landscape.tsv"

# libs
import pandas as pd
import ee
import xarray as xr
import numpy as np

sites = pd.read_table(sites_tab)
sites['site_plot'] = sites['site'] + "_" + sites['plot']
sites = sites[sites["site_plot"]==site]
ee.Initialize(opt_url='https://earthengine-highvolume.googleapis.com')
leg = ee.Geometry.Rectangle(sites["longitude"].values[0]-radius, sites["latitude"].values[0]-radius, 
                            sites["longitude"].values[0]+radius, sites["latitude"].values[0]+radius)

ic = ee.ImageCollection("projects/JRC/TMF/v1_2022/AnnualChanges")
ds = xr.open_mfdataset(
        [ic],
        engine='ee',
        projection=ic.first().select(0).projection(),
        geometry=leg
).sel(time=2).drop('time')
ds2 = ds.to_array("year", name="tmf").to_dataset().assign_coords(
    year=np.arange(1990,2023)
)
forest = ds2[["lon", "lat", "year"]]
forest["forest"] = (ds2.tmf.isin([1,2,4])).astype(int)
tab = forest.to_dataframe()
tab.insert(0, "site", sites["site"].values[0])
tab.insert(0, "plot", sites["plot"].values[0])
tab.to_csv(out_file, sep="\t", index=True)

# plot
# from matplotlib import pyplot as plt
# forest.sel(year=1990)["forest"].plot()
# plt.show()
