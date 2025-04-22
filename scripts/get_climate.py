# log
log_file = open(snakemake.log[0],"w")
sys.stderr = sys.stdout = log_file

# variables
in_file = snakemake.input[0]
out_file = snakemake.output[0]

# test
# in_file = "data/derived_data/site/Paracou.tsv"
# out_file = "data/derived_data/climate/Paracou_climate.tsv"

# libs
import pandas as pd
import ee
import xarray as xr

site = pd.read_table(in_file)
ee.Initialize(project="ee-sylvainmschmitt", opt_url='https://earthengine-highvolume.googleapis.com')
ic = ee.ImageCollection("IDAHO_EPSCOR/TERRACLIMATE")
leg = ee.Geometry.Rectangle(site["longitude"].values[0], site["latitude"].values[0], site["longitude"].values[0], site["latitude"].values[0])
ds = xr.open_mfdataset([ic], engine='ee', projection=ic.first().select(0).projection(), geometry=leg)
tab = ds[['aet', 'def', 'pdsi', 'pet', 'pr', 'soil', 'tmmn', 'tmmx', 'vpd']].to_dataframe()
tab.insert(0, "site", site["site"].values[0])
tab.to_csv(out_file, sep="\t", index=True)
