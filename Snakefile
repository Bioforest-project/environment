configfile: "config/config.yml"

rule all:
   input:
      expand("data/derived_data/climate/{site}_climate.tsv",
              site=config["sites"]),
      expand("data/derived_data/soil/{site}_soil.tsv",
              site=config["sites"])

rule get_climate:
    input:
        "data/derived_data/site/{site}.tsv"
    output:
        "data/derived_data/climate/{site}_climate.tsv"
    log:
        "data/derived_data/logs/{site}_climate.log"
    benchmark:
        "data/derived_data/benchmarks/{site}_climate.benchmark.txt"
    threads: 1
    resources:
        mem_mb=1000
    conda:
        "envs/bioforest-env.yml"
    script:
      "scripts/get_climate.py"
      
rule get_soil:
    input:
        "data/derived_data/site/{site}.tsv"
    output:
        "data/derived_data/soil/{site}_soil.tsv"
    log:
        "data/derived_data/logs/{site}_soil.log"
    benchmark:
        "data/derived_data/benchmarks/{site}_soil.benchmark.txt"
    threads: 1
    resources:
        mem_mb=1000
    conda:
        "envs/bioforest-env.yml"
    script:
      "scripts/get_soil.py"
