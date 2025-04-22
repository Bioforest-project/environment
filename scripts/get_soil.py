# log
log_file = open(snakemake.log[0],"w")
sys.stderr = sys.stdout = log_file

# variables
in_file = snakemake.input[0]
out_file = snakemake.output[0]

# test
# in_file = "data/derived_data/site/Paracou.tsv"
# out_file = "data/derived_data/soil/Paracou_climate.tsv"


# libs
import pandas as pd
import ee
import xarray as xr

site = pd.read_table(in_file)
ee.Initialize(project="ee-sylvainmschmitt", opt_url='https://earthengine-highvolume.googleapis.com')
radius = 0.001
leg = ee.Geometry.Rectangle(site["longitude"].values[0]-radius, site["latitude"].values[0]-radius, 
                            site["longitude"].values[0]+radius, site["latitude"].values[0]+radius)
def get_var(var):
    im = ee.Image("projects/soilgrids-isric/" + var)
    ic = ee.ImageCollection.fromImages([im])                       
    ds = xr.open_mfdataset([ic], engine='ee',  projection=ic.first().select(0).projection(), geometry=leg)
    return ds.to_dataframe()
all_tabs = [get_var("bdod_mean"),
            get_var("cec_mean"),
            get_var("cfvo_mean"),
            get_var("clay_mean"),
            get_var("sand_mean"),
            get_var("silt_mean"),
            get_var("nitrogen_mean"),
            get_var("phh2o_mean"),
            get_var("soc_mean"),
            get_var("ocd_mean"),
            get_var("ocs_mean")]
tab = pd.concat(all_tabs, axis=1)
tab.insert(0, "site", site["site"].values[0])
tab.to_csv(out_file, sep="\t", index=True)
