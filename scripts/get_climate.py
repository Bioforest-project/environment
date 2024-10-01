# log
log_file = open(snakemake.log[0],"w")
sys.stderr = sys.stdout = log_file

# variables
sites_tab = snakemake.input[0]
site = snakemake.params.site
out_file = snakemake.output[0]

# test
# sites_tab = "config/sites.tsv"
# site = "Uppangala_LP2"
# out_file = "data/climate/Uppangala_LP2_climate.tsv"

# libs
import pandas as pd
import ee
import xarray as xr

sites = pd.read_table(sites_tab)
sites['site_plot'] = sites['site'] + "_" + sites['plot']
sites = sites[sites["site_plot"]==site]
ee.Initialize(opt_url='https://earthengine-highvolume.googleapis.com')

ic = ee.ImageCollection("IDAHO_EPSCOR/TERRACLIMATE")
leg = ee.Geometry.Rectangle(sites["longitude"].values[0], sites["latitude"].values[0], sites["longitude"].values[0], sites["latitude"].values[0])
ds = xr.open_mfdataset([ic], engine='ee', projection=ic.first().select(0).projection(), geometry=leg)
ds_month = ds.groupby("time.month").mean()
tab_month = ds_month[['aet', 'def', 'pdsi', 'pet', 'pr', 'tmmn', 'tmmx', 'vpd']].to_dataframe()
tab_month.insert(0, "site", sites["site"].values[0])
tab_month.insert(0, "plot", sites["plot"].values[0])
tab_month.to_csv(out_file, sep="\t", index=True)
