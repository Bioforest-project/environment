configfile: "config/config.yml"

import pandas as pd
sites = pd.read_table(config["sites"])
sites['site_plot'] = sites['site'] + "_" + sites['plot']

rule all:
   input:
      expand("data/climate/{site}_climate.tsv",
              site=sites.site_plot)
    #   expand("soil/{site}_soil.tsv",
    #           site=sites.site_plot),
    #   expand("landscape/{site}_landscape.tsv",
    #           site=sites.site_plot)

rule get_climate:
    input:
        config["sites"]
    output:
        "data/climate/{site}_climate.tsv"
    log:
        "data/logs/{site}_climate.log"
    benchmark:
        "data/benchmarks/{site}_climate.benchmark.txt"
    threads: 1
    resources:
        mem_mb=1000
    conda:
        "envs/bioforest-env.yml"
    params:
        site="{site}"
    script:
      "scripts/get_climate.py"
      
rule get_soil:
    input:
        config["sites"]
    output:
        "data/soil/{site}_soil.tsv"
    log:
        "data/logs/{site}_soil.log"
    benchmark:
        "data/benchmarks/{site}_soil.benchmark.txt"
    threads: 1
    resources:
        mem_mb=1000
    conda:
        "envs/bioforest-env.yml"
    params:
        site="{site}"
    script:
      "scripts/get_climate.py"
      
rule get_landscape:
    input:
        config["sites"]
    output:
        "data/landscape/{site}_landscape.tsv"
    log:
        "data/logs/{site}_landscape.log"
    benchmark:
        "data/benchmarks/{site}_landscape.benchmark.txt"
    threads: 1
    resources:
        mem_mb=1000
    conda:
        "envs/bioforest-env.yml"
    params:
        site="{site}",
        radius=config["landscape_radius"]
    script:
      "scripts/get_landscape.py"
      
