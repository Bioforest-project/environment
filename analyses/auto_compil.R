sites <- "Misiones"
sites <- unique(readr::read_tsv("data/derived_data/sites.tsv")$site)
for (site in sites) {
  print(site)
  file_name <- paste0(site, "_environment.pdf")
  quarto::quarto_render(
    input = "analyses/site_summary.qmd",
    output_file = file_name,
    execute_params = list(site = site)
  )
  file.rename(
    from = file_name,
    to = file.path(
      "outputs",
      "site_summary",
      file_name
    )
  )
}
