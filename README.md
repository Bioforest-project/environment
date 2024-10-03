# Environment
Oct 3, 2024

[![](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)
[![lint](https://github.com/Bioforest-project/environment/workflows/lint/badge.svg)](https://github.com/Bioforest-project/environment/actions?query=workflow%3Alint)

**environment** is a sub-project of the
[**BioForest**](https://github.com/Bioforest-project) project aimed at
gathering environmental variables of climate
([TerraClimate](https://www.climatologylab.org/terraclimate.html)), soil
([SoilGrids](https://www.isric.org/explore/soilgrids)) and landscape
([TMF](https://forobs.jrc.ec.europa.eu/TMF)) for data preparation within
the project.

## Usage

**environment** takes advantage of
[snakemake](https://snakemake.readthedocs.io/en/stable/) and
[conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
for data retrieval defined by the sites list. First check the sites list
in `config/sites.tsv` and you can run the whole workflow with
`snakemake -j #cores –use-conda –keep-going` . Further details on usage
can be found in
<https://bioforest-project.github.io/environment/10_methods.html> . Then
all analyses rely on the quarto documents (`files.qmd`) that can be run
with R and associated environment defined with
[renv](https://rstudio.github.io/renv/articles/renv.html).

## Project

**environment** includes:

- [snakemake](https://snakemake.readthedocs.io/en/stable/) and
  [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
  workflow for automatic data retrieval:
  - Workflow definition in `Snakefile`
  - Worflow scripts in `scripts/`
  - Workflow configuration in `config/`
  - conda environments in `envs/`
- Analyse of the data with associated [documentation and
  figures](https://bioforest-project.github.io/environment/):
  - Reproductive analyses in `files.qmd`
  - Resulting pages in `docs/`
  - Document structure definition in `_quarto.yml`
- Data in `data/`
- Intermediary files in `outputs/`
- R environment definition with
  [renv](https://rstudio.github.io/renv/articles/renv.html) in `renv/`
  and `renv/lock`
- R files (`.Rbuildignore` , `.Rdata` , `.Rprofile` , `.Rhistory`)
- Git and GitHub files (`.gitignore` , `.github/`)
- Project documentation (`README.qmd` , `README.md` , `NEWS.md` )

> Should we add a license?

## Contribution

You can contribute to the project by forking the repository on github
and cloning the fork to your machine using several options, including
GitHub desktop GUI. Further informations on contribution are detailed in
the online document:
<https://bioforest-project.github.io/environment/98_contributing.html>.

## Help

Please preferentially create an issue on GitHub for any questions, bugs
or help needed regarding **environment**:
<https://github.com/Bioforest-project/environment/issues> . You may
however reach us by mail with people from the core group (see below).

## Core group

- Sylvain Schmitt (sylvain.schmitt@cirad.fr)
- Camille Piponiot-Laroche (camille.piponiot-laroche@cirad.fr)
- Géraldine Derroire (geraldine.derroire@cirad.fr)
- Mithila Unkule (mithila.unkule@fondationbiodiversite.fr)
- Irié Cazimir Zo-Bi (iczobi@gmail.com)
- Anand Roopsind (aroopsind@gmail.com)

The whole group consist of participants to the [Bioforest
project](https://www.fondationbiodiversite.fr/la-frb-en-action/programmes-et-projets/le-cesab/bioforest/).

![](https://www.fondationbiodiversite.fr/wp-content/uploads/2023/10/bioforest-ws1_web.jpeg)
