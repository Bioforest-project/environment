# Results of the snakemake workflow
Sylvain Schmitt -
Oct 3, 2024

This folder will contains the results of the snakemake workflow used by
analyses in the quarto document. In particular:

- `benchmarks/` contains every task benchmarking
- `climate/` contains all climatic data for every plot
- `landscape/` contains all landscape data for every plot
- `logs/` contains every task logs
- `soil/` contains all soil data for every plot

``` r
fs::dir_tree()
```

    .
    ├── README.md
    ├── README.qmd
    ├── README.rmarkdown
    ├── benchmarks
    │   ├── BAFOG_III_climate.benchmark.txt
    │   ├── BAFOG_III_landscape.benchmark.txt
    │   ├── BAFOG_III_soil.benchmark.txt
    │   ├── BAFOG_II_climate.benchmark.txt
    │   ├── BAFOG_II_landscape.benchmark.txt
    │   ├── BAFOG_II_soil.benchmark.txt
    │   ├── BAFOG_IV_climate.benchmark.txt
    │   ├── BAFOG_IV_landscape.benchmark.txt
    │   ├── BAFOG_IV_soil.benchmark.txt
    │   ├── BAFOG_I_climate.benchmark.txt
    │   ├── BAFOG_I_landscape.benchmark.txt
    │   ├── BAFOG_I_soil.benchmark.txt
    │   ├── BAFOG_VII_climate.benchmark.txt
    │   ├── BAFOG_VII_landscape.benchmark.txt
    │   ├── BAFOG_VII_soil.benchmark.txt
    │   ├── BAFOG_VI_climate.benchmark.txt
    │   ├── BAFOG_VI_landscape.benchmark.txt
    │   ├── BAFOG_VI_soil.benchmark.txt
    │   ├── BAFOG_V_climate.benchmark.txt
    │   ├── BAFOG_V_landscape.benchmark.txt
    │   ├── BAFOG_V_soil.benchmark.txt
    │   ├── Ecosilva_10_climate.benchmark.txt
    │   ├── Ecosilva_10_landscape.benchmark.txt
    │   ├── Ecosilva_10_soil.benchmark.txt
    │   ├── Ecosilva_11_climate.benchmark.txt
    │   ├── Ecosilva_11_landscape.benchmark.txt
    │   ├── Ecosilva_11_soil.benchmark.txt
    │   ├── Ecosilva_12_climate.benchmark.txt
    │   ├── Ecosilva_12_landscape.benchmark.txt
    │   ├── Ecosilva_12_soil.benchmark.txt
    │   ├── Ecosilva_13_climate.benchmark.txt
    │   ├── Ecosilva_13_landscape.benchmark.txt
    │   ├── Ecosilva_13_soil.benchmark.txt
    │   ├── Ecosilva_14_climate.benchmark.txt
    │   ├── Ecosilva_14_landscape.benchmark.txt
    │   ├── Ecosilva_14_soil.benchmark.txt
    │   ├── Ecosilva_15_climate.benchmark.txt
    │   ├── Ecosilva_15_landscape.benchmark.txt
    │   ├── Ecosilva_15_soil.benchmark.txt
    │   ├── Ecosilva_16_climate.benchmark.txt
    │   ├── Ecosilva_16_landscape.benchmark.txt
    │   ├── Ecosilva_16_soil.benchmark.txt
    │   ├── Ecosilva_17_climate.benchmark.txt
    │   ├── Ecosilva_17_landscape.benchmark.txt
    │   ├── Ecosilva_17_soil.benchmark.txt
    │   ├── Ecosilva_18_climate.benchmark.txt
    │   ├── Ecosilva_18_landscape.benchmark.txt
    │   ├── Ecosilva_18_soil.benchmark.txt
    │   ├── Ecosilva_1_climate.benchmark.txt
    │   ├── Ecosilva_1_landscape.benchmark.txt
    │   ├── Ecosilva_1_soil.benchmark.txt
    │   ├── Ecosilva_2_climate.benchmark.txt
    │   ├── Ecosilva_2_landscape.benchmark.txt
    │   ├── Ecosilva_2_soil.benchmark.txt
    │   ├── Ecosilva_3_climate.benchmark.txt
    │   ├── Ecosilva_3_landscape.benchmark.txt
    │   ├── Ecosilva_3_soil.benchmark.txt
    │   ├── Ecosilva_4_climate.benchmark.txt
    │   ├── Ecosilva_4_landscape.benchmark.txt
    │   ├── Ecosilva_4_soil.benchmark.txt
    │   ├── Ecosilva_5_climate.benchmark.txt
    │   ├── Ecosilva_5_landscape.benchmark.txt
    │   ├── Ecosilva_5_soil.benchmark.txt
    │   ├── Ecosilva_6_climate.benchmark.txt
    │   ├── Ecosilva_6_landscape.benchmark.txt
    │   ├── Ecosilva_6_soil.benchmark.txt
    │   ├── Ecosilva_7_climate.benchmark.txt
    │   ├── Ecosilva_7_landscape.benchmark.txt
    │   ├── Ecosilva_7_soil.benchmark.txt
    │   ├── Ecosilva_8_climate.benchmark.txt
    │   ├── Ecosilva_8_landscape.benchmark.txt
    │   ├── Ecosilva_8_soil.benchmark.txt
    │   ├── Ecosilva_9_climate.benchmark.txt
    │   ├── Ecosilva_9_landscape.benchmark.txt
    │   ├── Ecosilva_9_soil.benchmark.txt
    │   ├── Iwokrama_IWO-01_climate.benchmark.txt
    │   ├── Iwokrama_IWO-01_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-01_soil.benchmark.txt
    │   ├── Iwokrama_IWO-02_climate.benchmark.txt
    │   ├── Iwokrama_IWO-02_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-02_soil.benchmark.txt
    │   ├── Iwokrama_IWO-03_climate.benchmark.txt
    │   ├── Iwokrama_IWO-03_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-03_soil.benchmark.txt
    │   ├── Iwokrama_IWO-04_climate.benchmark.txt
    │   ├── Iwokrama_IWO-04_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-04_soil.benchmark.txt
    │   ├── Iwokrama_IWO-05_climate.benchmark.txt
    │   ├── Iwokrama_IWO-05_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-05_soil.benchmark.txt
    │   ├── Iwokrama_IWO-06_climate.benchmark.txt
    │   ├── Iwokrama_IWO-06_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-06_soil.benchmark.txt
    │   ├── Iwokrama_IWO-07_climate.benchmark.txt
    │   ├── Iwokrama_IWO-07_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-07_soil.benchmark.txt
    │   ├── Iwokrama_IWO-08_climate.benchmark.txt
    │   ├── Iwokrama_IWO-08_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-08_soil.benchmark.txt
    │   ├── Iwokrama_IWO-09_climate.benchmark.txt
    │   ├── Iwokrama_IWO-09_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-09_soil.benchmark.txt
    │   ├── Iwokrama_IWO-10_climate.benchmark.txt
    │   ├── Iwokrama_IWO-10_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-10_soil.benchmark.txt
    │   ├── Iwokrama_IWO-11_climate.benchmark.txt
    │   ├── Iwokrama_IWO-11_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-11_soil.benchmark.txt
    │   ├── Iwokrama_IWO-12_climate.benchmark.txt
    │   ├── Iwokrama_IWO-12_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-12_soil.benchmark.txt
    │   ├── Iwokrama_IWO-13_climate.benchmark.txt
    │   ├── Iwokrama_IWO-13_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-13_soil.benchmark.txt
    │   ├── Iwokrama_IWO-14_climate.benchmark.txt
    │   ├── Iwokrama_IWO-14_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-14_soil.benchmark.txt
    │   ├── Iwokrama_IWO-15_climate.benchmark.txt
    │   ├── Iwokrama_IWO-15_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-15_soil.benchmark.txt
    │   ├── Iwokrama_IWO-16_climate.benchmark.txt
    │   ├── Iwokrama_IWO-16_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-16_soil.benchmark.txt
    │   ├── Iwokrama_IWO-17_climate.benchmark.txt
    │   ├── Iwokrama_IWO-17_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-17_soil.benchmark.txt
    │   ├── Iwokrama_IWO-21_climate.benchmark.txt
    │   ├── Iwokrama_IWO-21_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-21_soil.benchmark.txt
    │   ├── Iwokrama_IWO-22_climate.benchmark.txt
    │   ├── Iwokrama_IWO-22_landscape.benchmark.txt
    │   ├── Iwokrama_IWO-22_soil.benchmark.txt
    │   ├── Jari_101_climate.benchmark.txt
    │   ├── Jari_101_landscape.benchmark.txt
    │   ├── Jari_101_soil.benchmark.txt
    │   ├── Jari_102_climate.benchmark.txt
    │   ├── Jari_102_landscape.benchmark.txt
    │   ├── Jari_102_soil.benchmark.txt
    │   ├── Jari_103_climate.benchmark.txt
    │   ├── Jari_103_landscape.benchmark.txt
    │   ├── Jari_103_soil.benchmark.txt
    │   ├── Jari_104_climate.benchmark.txt
    │   ├── Jari_104_landscape.benchmark.txt
    │   ├── Jari_104_soil.benchmark.txt
    │   ├── Jari_105_climate.benchmark.txt
    │   ├── Jari_105_landscape.benchmark.txt
    │   ├── Jari_105_soil.benchmark.txt
    │   ├── Jari_106_climate.benchmark.txt
    │   ├── Jari_106_landscape.benchmark.txt
    │   ├── Jari_106_soil.benchmark.txt
    │   ├── Jari_107_climate.benchmark.txt
    │   ├── Jari_107_landscape.benchmark.txt
    │   ├── Jari_107_soil.benchmark.txt
    │   ├── Jari_108_climate.benchmark.txt
    │   ├── Jari_108_landscape.benchmark.txt
    │   ├── Jari_108_soil.benchmark.txt
    │   ├── Jari_109_climate.benchmark.txt
    │   ├── Jari_109_landscape.benchmark.txt
    │   ├── Jari_109_soil.benchmark.txt
    │   ├── Jari_110_climate.benchmark.txt
    │   ├── Jari_110_landscape.benchmark.txt
    │   ├── Jari_110_soil.benchmark.txt
    │   ├── Jari_111_climate.benchmark.txt
    │   ├── Jari_111_landscape.benchmark.txt
    │   ├── Jari_111_soil.benchmark.txt
    │   ├── Jari_112_climate.benchmark.txt
    │   ├── Jari_112_landscape.benchmark.txt
    │   ├── Jari_112_soil.benchmark.txt
    │   ├── Jari_1_climate.benchmark.txt
    │   ├── Jari_1_landscape.benchmark.txt
    │   ├── Jari_1_soil.benchmark.txt
    │   ├── Jari_201_climate.benchmark.txt
    │   ├── Jari_201_landscape.benchmark.txt
    │   ├── Jari_201_soil.benchmark.txt
    │   ├── Jari_202_climate.benchmark.txt
    │   ├── Jari_202_landscape.benchmark.txt
    │   ├── Jari_202_soil.benchmark.txt
    │   ├── Jari_203_climate.benchmark.txt
    │   ├── Jari_203_landscape.benchmark.txt
    │   ├── Jari_203_soil.benchmark.txt
    │   ├── Jari_204_climate.benchmark.txt
    │   ├── Jari_204_landscape.benchmark.txt
    │   ├── Jari_204_soil.benchmark.txt
    │   ├── Jari_205_climate.benchmark.txt
    │   ├── Jari_205_landscape.benchmark.txt
    │   ├── Jari_205_soil.benchmark.txt
    │   ├── Jari_206_climate.benchmark.txt
    │   ├── Jari_206_landscape.benchmark.txt
    │   ├── Jari_206_soil.benchmark.txt
    │   ├── Jari_207_climate.benchmark.txt
    │   ├── Jari_207_landscape.benchmark.txt
    │   ├── Jari_207_soil.benchmark.txt
    │   ├── Jari_208_climate.benchmark.txt
    │   ├── Jari_208_landscape.benchmark.txt
    │   ├── Jari_208_soil.benchmark.txt
    │   ├── Jari_209_climate.benchmark.txt
    │   ├── Jari_209_landscape.benchmark.txt
    │   ├── Jari_209_soil.benchmark.txt
    │   ├── Jari_210_climate.benchmark.txt
    │   ├── Jari_210_landscape.benchmark.txt
    │   ├── Jari_210_soil.benchmark.txt
    │   ├── Jari_211_climate.benchmark.txt
    │   ├── Jari_211_landscape.benchmark.txt
    │   ├── Jari_211_soil.benchmark.txt
    │   ├── Jari_212_climate.benchmark.txt
    │   ├── Jari_212_landscape.benchmark.txt
    │   ├── Jari_212_soil.benchmark.txt
    │   ├── Jari_2_climate.benchmark.txt
    │   ├── Jari_2_landscape.benchmark.txt
    │   ├── Jari_2_soil.benchmark.txt
    │   ├── Jari_301_climate.benchmark.txt
    │   ├── Jari_301_landscape.benchmark.txt
    │   ├── Jari_301_soil.benchmark.txt
    │   ├── Jari_302_climate.benchmark.txt
    │   ├── Jari_302_landscape.benchmark.txt
    │   ├── Jari_302_soil.benchmark.txt
    │   ├── Jari_303_climate.benchmark.txt
    │   ├── Jari_303_landscape.benchmark.txt
    │   ├── Jari_303_soil.benchmark.txt
    │   ├── Jari_304_climate.benchmark.txt
    │   ├── Jari_304_landscape.benchmark.txt
    │   ├── Jari_304_soil.benchmark.txt
    │   ├── Jari_305_climate.benchmark.txt
    │   ├── Jari_305_landscape.benchmark.txt
    │   ├── Jari_305_soil.benchmark.txt
    │   ├── Jari_306_climate.benchmark.txt
    │   ├── Jari_306_landscape.benchmark.txt
    │   ├── Jari_306_soil.benchmark.txt
    │   ├── Jari_307_climate.benchmark.txt
    │   ├── Jari_307_landscape.benchmark.txt
    │   ├── Jari_307_soil.benchmark.txt
    │   ├── Jari_308_climate.benchmark.txt
    │   ├── Jari_308_landscape.benchmark.txt
    │   ├── Jari_308_soil.benchmark.txt
    │   ├── Jari_309_climate.benchmark.txt
    │   ├── Jari_309_landscape.benchmark.txt
    │   ├── Jari_309_soil.benchmark.txt
    │   ├── Jari_310_climate.benchmark.txt
    │   ├── Jari_310_landscape.benchmark.txt
    │   ├── Jari_310_soil.benchmark.txt
    │   ├── Jari_311_climate.benchmark.txt
    │   ├── Jari_311_landscape.benchmark.txt
    │   ├── Jari_311_soil.benchmark.txt
    │   ├── Jari_312_climate.benchmark.txt
    │   ├── Jari_312_landscape.benchmark.txt
    │   ├── Jari_312_soil.benchmark.txt
    │   ├── Jari_3_climate.benchmark.txt
    │   ├── Jari_3_landscape.benchmark.txt
    │   ├── Jari_3_soil.benchmark.txt
    │   ├── Jari_4_climate.benchmark.txt
    │   ├── Jari_4_landscape.benchmark.txt
    │   ├── Jari_4_soil.benchmark.txt
    │   ├── Kabo_KAB-12_climate.benchmark.txt
    │   ├── Kabo_KAB-12_landscape.benchmark.txt
    │   ├── Kabo_KAB-12_soil.benchmark.txt
    │   ├── Kabo_KAB-14_climate.benchmark.txt
    │   ├── Kabo_KAB-14_landscape.benchmark.txt
    │   ├── Kabo_KAB-14_soil.benchmark.txt
    │   ├── Kabo_KAB-19_climate.benchmark.txt
    │   ├── Kabo_KAB-19_landscape.benchmark.txt
    │   ├── Kabo_KAB-19_soil.benchmark.txt
    │   ├── Kabo_KAB-22_climate.benchmark.txt
    │   ├── Kabo_KAB-22_landscape.benchmark.txt
    │   ├── Kabo_KAB-22_soil.benchmark.txt
    │   ├── Kabo_KAB-26_climate.benchmark.txt
    │   ├── Kabo_KAB-26_landscape.benchmark.txt
    │   ├── Kabo_KAB-26_soil.benchmark.txt
    │   ├── Kabo_KAB-28_climate.benchmark.txt
    │   ├── Kabo_KAB-28_landscape.benchmark.txt
    │   ├── Kabo_KAB-28_soil.benchmark.txt
    │   ├── Kabo_KAB-32_climate.benchmark.txt
    │   ├── Kabo_KAB-32_landscape.benchmark.txt
    │   ├── Kabo_KAB-32_soil.benchmark.txt
    │   ├── Kabo_KAB-34_climate.benchmark.txt
    │   ├── Kabo_KAB-34_landscape.benchmark.txt
    │   ├── Kabo_KAB-34_soil.benchmark.txt
    │   ├── Kabo_KAB-38_climate.benchmark.txt
    │   ├── Kabo_KAB-38_landscape.benchmark.txt
    │   ├── Kabo_KAB-38_soil.benchmark.txt
    │   ├── Kabo_KAB-41_climate.benchmark.txt
    │   ├── Kabo_KAB-41_landscape.benchmark.txt
    │   ├── Kabo_KAB-41_soil.benchmark.txt
    │   ├── Kabo_KAB-42_climate.benchmark.txt
    │   ├── Kabo_KAB-42_landscape.benchmark.txt
    │   ├── Kabo_KAB-42_soil.benchmark.txt
    │   ├── Kabo_KAB-43_climate.benchmark.txt
    │   ├── Kabo_KAB-43_landscape.benchmark.txt
    │   ├── Kabo_KAB-43_soil.benchmark.txt
    │   ├── Lesong_10_climate.benchmark.txt
    │   ├── Lesong_10_landscape.benchmark.txt
    │   ├── Lesong_10_soil.benchmark.txt
    │   ├── Lesong_11_climate.benchmark.txt
    │   ├── Lesong_11_landscape.benchmark.txt
    │   ├── Lesong_11_soil.benchmark.txt
    │   ├── Lesong_12_climate.benchmark.txt
    │   ├── Lesong_12_landscape.benchmark.txt
    │   ├── Lesong_12_soil.benchmark.txt
    │   ├── Lesong_1_climate.benchmark.txt
    │   ├── Lesong_1_landscape.benchmark.txt
    │   ├── Lesong_1_soil.benchmark.txt
    │   ├── Lesong_2_climate.benchmark.txt
    │   ├── Lesong_2_landscape.benchmark.txt
    │   ├── Lesong_2_soil.benchmark.txt
    │   ├── Lesong_3_climate.benchmark.txt
    │   ├── Lesong_3_landscape.benchmark.txt
    │   ├── Lesong_3_soil.benchmark.txt
    │   ├── Lesong_4_climate.benchmark.txt
    │   ├── Lesong_4_landscape.benchmark.txt
    │   ├── Lesong_4_soil.benchmark.txt
    │   ├── Lesong_5_climate.benchmark.txt
    │   ├── Lesong_5_landscape.benchmark.txt
    │   ├── Lesong_5_soil.benchmark.txt
    │   ├── Lesong_6_climate.benchmark.txt
    │   ├── Lesong_6_landscape.benchmark.txt
    │   ├── Lesong_6_soil.benchmark.txt
    │   ├── Lesong_7_climate.benchmark.txt
    │   ├── Lesong_7_landscape.benchmark.txt
    │   ├── Lesong_7_soil.benchmark.txt
    │   ├── Lesong_8_climate.benchmark.txt
    │   ├── Lesong_8_landscape.benchmark.txt
    │   ├── Lesong_8_soil.benchmark.txt
    │   ├── Lesong_9_climate.benchmark.txt
    │   ├── Lesong_9_landscape.benchmark.txt
    │   ├── Lesong_9_soil.benchmark.txt
    │   ├── Malinau_CNV01_climate.benchmark.txt
    │   ├── Malinau_CNV01_landscape.benchmark.txt
    │   ├── Malinau_CNV01_soil.benchmark.txt
    │   ├── Malinau_CNV02_climate.benchmark.txt
    │   ├── Malinau_CNV02_landscape.benchmark.txt
    │   ├── Malinau_CNV02_soil.benchmark.txt
    │   ├── Malinau_CNV03_climate.benchmark.txt
    │   ├── Malinau_CNV03_landscape.benchmark.txt
    │   ├── Malinau_CNV03_soil.benchmark.txt
    │   ├── Malinau_CNV04_climate.benchmark.txt
    │   ├── Malinau_CNV04_landscape.benchmark.txt
    │   ├── Malinau_CNV04_soil.benchmark.txt
    │   ├── Malinau_CNV05_climate.benchmark.txt
    │   ├── Malinau_CNV05_landscape.benchmark.txt
    │   ├── Malinau_CNV05_soil.benchmark.txt
    │   ├── Malinau_CNV06_climate.benchmark.txt
    │   ├── Malinau_CNV06_landscape.benchmark.txt
    │   ├── Malinau_CNV06_soil.benchmark.txt
    │   ├── Malinau_CNV07_climate.benchmark.txt
    │   ├── Malinau_CNV07_landscape.benchmark.txt
    │   ├── Malinau_CNV07_soil.benchmark.txt
    │   ├── Malinau_CNV08_climate.benchmark.txt
    │   ├── Malinau_CNV08_landscape.benchmark.txt
    │   ├── Malinau_CNV08_soil.benchmark.txt
    │   ├── Malinau_CNV09_climate.benchmark.txt
    │   ├── Malinau_CNV09_landscape.benchmark.txt
    │   ├── Malinau_CNV09_soil.benchmark.txt
    │   ├── Malinau_CNV10_climate.benchmark.txt
    │   ├── Malinau_CNV10_landscape.benchmark.txt
    │   ├── Malinau_CNV10_soil.benchmark.txt
    │   ├── Malinau_CNV11_climate.benchmark.txt
    │   ├── Malinau_CNV11_landscape.benchmark.txt
    │   ├── Malinau_CNV11_soil.benchmark.txt
    │   ├── Malinau_CNV12_climate.benchmark.txt
    │   ├── Malinau_CNV12_landscape.benchmark.txt
    │   ├── Malinau_CNV12_soil.benchmark.txt
    │   ├── Malinau_RIL01_climate.benchmark.txt
    │   ├── Malinau_RIL01_landscape.benchmark.txt
    │   ├── Malinau_RIL01_soil.benchmark.txt
    │   ├── Malinau_RIL02_climate.benchmark.txt
    │   ├── Malinau_RIL02_landscape.benchmark.txt
    │   ├── Malinau_RIL02_soil.benchmark.txt
    │   ├── Malinau_RIL03_climate.benchmark.txt
    │   ├── Malinau_RIL03_landscape.benchmark.txt
    │   ├── Malinau_RIL03_soil.benchmark.txt
    │   ├── Malinau_RIL04_climate.benchmark.txt
    │   ├── Malinau_RIL04_landscape.benchmark.txt
    │   ├── Malinau_RIL04_soil.benchmark.txt
    │   ├── Malinau_RIL05_climate.benchmark.txt
    │   ├── Malinau_RIL05_landscape.benchmark.txt
    │   ├── Malinau_RIL05_soil.benchmark.txt
    │   ├── Malinau_RIL06_climate.benchmark.txt
    │   ├── Malinau_RIL06_landscape.benchmark.txt
    │   ├── Malinau_RIL06_soil.benchmark.txt
    │   ├── Malinau_RIL07_climate.benchmark.txt
    │   ├── Malinau_RIL07_landscape.benchmark.txt
    │   ├── Malinau_RIL07_soil.benchmark.txt
    │   ├── Malinau_RIL08_climate.benchmark.txt
    │   ├── Malinau_RIL08_landscape.benchmark.txt
    │   ├── Malinau_RIL08_soil.benchmark.txt
    │   ├── Malinau_RIL09_climate.benchmark.txt
    │   ├── Malinau_RIL09_landscape.benchmark.txt
    │   ├── Malinau_RIL09_soil.benchmark.txt
    │   ├── Malinau_RIL10_climate.benchmark.txt
    │   ├── Malinau_RIL10_landscape.benchmark.txt
    │   ├── Malinau_RIL10_soil.benchmark.txt
    │   ├── Malinau_RIL11_climate.benchmark.txt
    │   ├── Malinau_RIL11_landscape.benchmark.txt
    │   ├── Malinau_RIL11_soil.benchmark.txt
    │   ├── Malinau_RIL12_climate.benchmark.txt
    │   ├── Malinau_RIL12_landscape.benchmark.txt
    │   ├── Malinau_RIL12_soil.benchmark.txt
    │   ├── Manare_Manare_II_climate.benchmark.txt
    │   ├── Manare_Manare_II_landscape.benchmark.txt
    │   ├── Manare_Manare_II_soil.benchmark.txt
    │   ├── Manare_Manare_I_climate.benchmark.txt
    │   ├── Manare_Manare_I_landscape.benchmark.txt
    │   ├── Manare_Manare_I_soil.benchmark.txt
    │   ├── Manare_Saut_Lavilette_climate.benchmark.txt
    │   ├── Manare_Saut_Lavilette_landscape.benchmark.txt
    │   ├── Manare_Saut_Lavilette_soil.benchmark.txt
    │   ├── Misiones_10_climate.benchmark.txt
    │   ├── Misiones_10_landscape.benchmark.txt
    │   ├── Misiones_10_soil.benchmark.txt
    │   ├── Misiones_11_climate.benchmark.txt
    │   ├── Misiones_11_landscape.benchmark.txt
    │   ├── Misiones_11_soil.benchmark.txt
    │   ├── Misiones_12_climate.benchmark.txt
    │   ├── Misiones_12_landscape.benchmark.txt
    │   ├── Misiones_12_soil.benchmark.txt
    │   ├── Misiones_13_climate.benchmark.txt
    │   ├── Misiones_13_landscape.benchmark.txt
    │   ├── Misiones_13_soil.benchmark.txt
    │   ├── Misiones_14_climate.benchmark.txt
    │   ├── Misiones_14_landscape.benchmark.txt
    │   ├── Misiones_14_soil.benchmark.txt
    │   ├── Misiones_16_climate.benchmark.txt
    │   ├── Misiones_16_landscape.benchmark.txt
    │   ├── Misiones_16_soil.benchmark.txt
    │   ├── Misiones_19_climate.benchmark.txt
    │   ├── Misiones_19_landscape.benchmark.txt
    │   ├── Misiones_19_soil.benchmark.txt
    │   ├── Misiones_1_climate.benchmark.txt
    │   ├── Misiones_1_landscape.benchmark.txt
    │   ├── Misiones_1_soil.benchmark.txt
    │   ├── Misiones_20_climate.benchmark.txt
    │   ├── Misiones_20_landscape.benchmark.txt
    │   ├── Misiones_20_soil.benchmark.txt
    │   ├── Misiones_21_climate.benchmark.txt
    │   ├── Misiones_21_landscape.benchmark.txt
    │   ├── Misiones_21_soil.benchmark.txt
    │   ├── Misiones_2_climate.benchmark.txt
    │   ├── Misiones_2_landscape.benchmark.txt
    │   ├── Misiones_2_soil.benchmark.txt
    │   ├── Misiones_3_climate.benchmark.txt
    │   ├── Misiones_3_landscape.benchmark.txt
    │   ├── Misiones_3_soil.benchmark.txt
    │   ├── Misiones_4_climate.benchmark.txt
    │   ├── Misiones_4_landscape.benchmark.txt
    │   ├── Misiones_4_soil.benchmark.txt
    │   ├── Misiones_5_climate.benchmark.txt
    │   ├── Misiones_5_landscape.benchmark.txt
    │   ├── Misiones_5_soil.benchmark.txt
    │   ├── Misiones_6_climate.benchmark.txt
    │   ├── Misiones_6_landscape.benchmark.txt
    │   ├── Misiones_6_soil.benchmark.txt
    │   ├── Misiones_7_climate.benchmark.txt
    │   ├── Misiones_7_landscape.benchmark.txt
    │   ├── Misiones_7_soil.benchmark.txt
    │   ├── Misiones_8_climate.benchmark.txt
    │   ├── Misiones_8_landscape.benchmark.txt
    │   ├── Misiones_8_soil.benchmark.txt
    │   ├── Misiones_9_climate.benchmark.txt
    │   ├── Misiones_9_landscape.benchmark.txt
    │   ├── Misiones_9_soil.benchmark.txt
    │   ├── Moju_10_climate.benchmark.txt
    │   ├── Moju_10_landscape.benchmark.txt
    │   ├── Moju_10_soil.benchmark.txt
    │   ├── Moju_11_climate.benchmark.txt
    │   ├── Moju_11_landscape.benchmark.txt
    │   ├── Moju_11_soil.benchmark.txt
    │   ├── Moju_12_climate.benchmark.txt
    │   ├── Moju_12_landscape.benchmark.txt
    │   ├── Moju_12_soil.benchmark.txt
    │   ├── Moju_13_climate.benchmark.txt
    │   ├── Moju_13_landscape.benchmark.txt
    │   ├── Moju_13_soil.benchmark.txt
    │   ├── Moju_14_climate.benchmark.txt
    │   ├── Moju_14_landscape.benchmark.txt
    │   ├── Moju_14_soil.benchmark.txt
    │   ├── Moju_15_climate.benchmark.txt
    │   ├── Moju_15_landscape.benchmark.txt
    │   ├── Moju_15_soil.benchmark.txt
    │   ├── Moju_16_climate.benchmark.txt
    │   ├── Moju_16_landscape.benchmark.txt
    │   ├── Moju_16_soil.benchmark.txt
    │   ├── Moju_17_climate.benchmark.txt
    │   ├── Moju_17_landscape.benchmark.txt
    │   ├── Moju_17_soil.benchmark.txt
    │   ├── Moju_18_climate.benchmark.txt
    │   ├── Moju_18_landscape.benchmark.txt
    │   ├── Moju_18_soil.benchmark.txt
    │   ├── Moju_19_climate.benchmark.txt
    │   ├── Moju_19_landscape.benchmark.txt
    │   ├── Moju_19_soil.benchmark.txt
    │   ├── Moju_1_climate.benchmark.txt
    │   ├── Moju_1_landscape.benchmark.txt
    │   ├── Moju_1_soil.benchmark.txt
    │   ├── Moju_20_climate.benchmark.txt
    │   ├── Moju_20_landscape.benchmark.txt
    │   ├── Moju_20_soil.benchmark.txt
    │   ├── Moju_21_climate.benchmark.txt
    │   ├── Moju_21_landscape.benchmark.txt
    │   ├── Moju_21_soil.benchmark.txt
    │   ├── Moju_22_climate.benchmark.txt
    │   ├── Moju_22_landscape.benchmark.txt
    │   ├── Moju_22_soil.benchmark.txt
    │   ├── Moju_2_climate.benchmark.txt
    │   ├── Moju_2_landscape.benchmark.txt
    │   ├── Moju_2_soil.benchmark.txt
    │   ├── Moju_3_climate.benchmark.txt
    │   ├── Moju_3_landscape.benchmark.txt
    │   ├── Moju_3_soil.benchmark.txt
    │   ├── Moju_4_climate.benchmark.txt
    │   ├── Moju_4_landscape.benchmark.txt
    │   ├── Moju_4_soil.benchmark.txt
    │   ├── Moju_5_climate.benchmark.txt
    │   ├── Moju_5_landscape.benchmark.txt
    │   ├── Moju_5_soil.benchmark.txt
    │   ├── Moju_6_climate.benchmark.txt
    │   ├── Moju_6_landscape.benchmark.txt
    │   ├── Moju_6_soil.benchmark.txt
    │   ├── Moju_7_climate.benchmark.txt
    │   ├── Moju_7_landscape.benchmark.txt
    │   ├── Moju_7_soil.benchmark.txt
    │   ├── Moju_8_climate.benchmark.txt
    │   ├── Moju_8_landscape.benchmark.txt
    │   ├── Moju_8_soil.benchmark.txt
    │   ├── Moju_9_climate.benchmark.txt
    │   ├── Moju_9_landscape.benchmark.txt
    │   ├── Moju_9_soil.benchmark.txt
    │   ├── Montagne_tortue_P17_exploitee_1_climate.benchmark.txt
    │   ├── Montagne_tortue_P17_exploitee_1_landscape.benchmark.txt
    │   ├── Montagne_tortue_P17_exploitee_1_soil.benchmark.txt
    │   ├── Montagne_tortue_P17_exploitee_2_climate.benchmark.txt
    │   ├── Montagne_tortue_P17_exploitee_2_landscape.benchmark.txt
    │   ├── Montagne_tortue_P17_exploitee_2_soil.benchmark.txt
    │   ├── Montagne_tortue_P17_temoin_climate.benchmark.txt
    │   ├── Montagne_tortue_P17_temoin_landscape.benchmark.txt
    │   ├── Montagne_tortue_P17_temoin_soil.benchmark.txt
    │   ├── Paracou_10_climate.benchmark.txt
    │   ├── Paracou_10_landscape.benchmark.txt
    │   ├── Paracou_10_soil.benchmark.txt
    │   ├── Paracou_11_climate.benchmark.txt
    │   ├── Paracou_11_landscape.benchmark.txt
    │   ├── Paracou_11_soil.benchmark.txt
    │   ├── Paracou_12_climate.benchmark.txt
    │   ├── Paracou_12_landscape.benchmark.txt
    │   ├── Paracou_12_soil.benchmark.txt
    │   ├── Paracou_13_climate.benchmark.txt
    │   ├── Paracou_13_landscape.benchmark.txt
    │   ├── Paracou_13_soil.benchmark.txt
    │   ├── Paracou_14_climate.benchmark.txt
    │   ├── Paracou_14_landscape.benchmark.txt
    │   ├── Paracou_14_soil.benchmark.txt
    │   ├── Paracou_15_climate.benchmark.txt
    │   ├── Paracou_15_landscape.benchmark.txt
    │   ├── Paracou_15_soil.benchmark.txt
    │   ├── Paracou_1_climate.benchmark.txt
    │   ├── Paracou_1_landscape.benchmark.txt
    │   ├── Paracou_1_soil.benchmark.txt
    │   ├── Paracou_2_climate.benchmark.txt
    │   ├── Paracou_2_landscape.benchmark.txt
    │   ├── Paracou_2_soil.benchmark.txt
    │   ├── Paracou_3_climate.benchmark.txt
    │   ├── Paracou_3_landscape.benchmark.txt
    │   ├── Paracou_3_soil.benchmark.txt
    │   ├── Paracou_4_climate.benchmark.txt
    │   ├── Paracou_4_landscape.benchmark.txt
    │   ├── Paracou_4_soil.benchmark.txt
    │   ├── Paracou_5_climate.benchmark.txt
    │   ├── Paracou_5_landscape.benchmark.txt
    │   ├── Paracou_5_soil.benchmark.txt
    │   ├── Paracou_6_climate.benchmark.txt
    │   ├── Paracou_6_landscape.benchmark.txt
    │   ├── Paracou_6_soil.benchmark.txt
    │   ├── Paracou_7_climate.benchmark.txt
    │   ├── Paracou_7_landscape.benchmark.txt
    │   ├── Paracou_7_soil.benchmark.txt
    │   ├── Paracou_8_climate.benchmark.txt
    │   ├── Paracou_8_landscape.benchmark.txt
    │   ├── Paracou_8_soil.benchmark.txt
    │   ├── Paracou_9_climate.benchmark.txt
    │   ├── Paracou_9_landscape.benchmark.txt
    │   ├── Paracou_9_soil.benchmark.txt
    │   ├── Peteco_10_climate.benchmark.txt
    │   ├── Peteco_10_landscape.benchmark.txt
    │   ├── Peteco_10_soil.benchmark.txt
    │   ├── Peteco_11_climate.benchmark.txt
    │   ├── Peteco_11_landscape.benchmark.txt
    │   ├── Peteco_11_soil.benchmark.txt
    │   ├── Peteco_12_climate.benchmark.txt
    │   ├── Peteco_12_landscape.benchmark.txt
    │   ├── Peteco_12_soil.benchmark.txt
    │   ├── Peteco_13_climate.benchmark.txt
    │   ├── Peteco_13_landscape.benchmark.txt
    │   ├── Peteco_13_soil.benchmark.txt
    │   ├── Peteco_14_climate.benchmark.txt
    │   ├── Peteco_14_landscape.benchmark.txt
    │   ├── Peteco_14_soil.benchmark.txt
    │   ├── Peteco_15_climate.benchmark.txt
    │   ├── Peteco_15_landscape.benchmark.txt
    │   ├── Peteco_15_soil.benchmark.txt
    │   ├── Peteco_16_climate.benchmark.txt
    │   ├── Peteco_16_landscape.benchmark.txt
    │   ├── Peteco_16_soil.benchmark.txt
    │   ├── Peteco_17_climate.benchmark.txt
    │   ├── Peteco_17_landscape.benchmark.txt
    │   ├── Peteco_17_soil.benchmark.txt
    │   ├── Peteco_18_climate.benchmark.txt
    │   ├── Peteco_18_landscape.benchmark.txt
    │   ├── Peteco_18_soil.benchmark.txt
    │   ├── Peteco_1_climate.benchmark.txt
    │   ├── Peteco_1_landscape.benchmark.txt
    │   ├── Peteco_1_soil.benchmark.txt
    │   ├── Peteco_20_climate.benchmark.txt
    │   ├── Peteco_20_landscape.benchmark.txt
    │   ├── Peteco_20_soil.benchmark.txt
    │   ├── Peteco_21_climate.benchmark.txt
    │   ├── Peteco_21_landscape.benchmark.txt
    │   ├── Peteco_21_soil.benchmark.txt
    │   ├── Peteco_22_climate.benchmark.txt
    │   ├── Peteco_22_landscape.benchmark.txt
    │   ├── Peteco_22_soil.benchmark.txt
    │   ├── Peteco_23_climate.benchmark.txt
    │   ├── Peteco_23_landscape.benchmark.txt
    │   ├── Peteco_23_soil.benchmark.txt
    │   ├── Peteco_24_climate.benchmark.txt
    │   ├── Peteco_24_landscape.benchmark.txt
    │   ├── Peteco_24_soil.benchmark.txt
    │   ├── Peteco_25_climate.benchmark.txt
    │   ├── Peteco_25_landscape.benchmark.txt
    │   ├── Peteco_25_soil.benchmark.txt
    │   ├── Peteco_26_climate.benchmark.txt
    │   ├── Peteco_26_landscape.benchmark.txt
    │   ├── Peteco_26_soil.benchmark.txt
    │   ├── Peteco_27_climate.benchmark.txt
    │   ├── Peteco_27_landscape.benchmark.txt
    │   ├── Peteco_27_soil.benchmark.txt
    │   ├── Peteco_28_climate.benchmark.txt
    │   ├── Peteco_28_landscape.benchmark.txt
    │   ├── Peteco_28_soil.benchmark.txt
    │   ├── Peteco_29_climate.benchmark.txt
    │   ├── Peteco_29_landscape.benchmark.txt
    │   ├── Peteco_29_soil.benchmark.txt
    │   ├── Peteco_2_climate.benchmark.txt
    │   ├── Peteco_2_landscape.benchmark.txt
    │   ├── Peteco_2_soil.benchmark.txt
    │   ├── Peteco_30_climate.benchmark.txt
    │   ├── Peteco_30_landscape.benchmark.txt
    │   ├── Peteco_30_soil.benchmark.txt
    │   ├── Peteco_31_climate.benchmark.txt
    │   ├── Peteco_31_landscape.benchmark.txt
    │   ├── Peteco_31_soil.benchmark.txt
    │   ├── Peteco_32_climate.benchmark.txt
    │   ├── Peteco_32_landscape.benchmark.txt
    │   ├── Peteco_32_soil.benchmark.txt
    │   ├── Peteco_33_climate.benchmark.txt
    │   ├── Peteco_33_landscape.benchmark.txt
    │   ├── Peteco_33_soil.benchmark.txt
    │   ├── Peteco_34_climate.benchmark.txt
    │   ├── Peteco_34_landscape.benchmark.txt
    │   ├── Peteco_34_soil.benchmark.txt
    │   ├── Peteco_35_climate.benchmark.txt
    │   ├── Peteco_35_landscape.benchmark.txt
    │   ├── Peteco_35_soil.benchmark.txt
    │   ├── Peteco_36_climate.benchmark.txt
    │   ├── Peteco_36_landscape.benchmark.txt
    │   ├── Peteco_36_soil.benchmark.txt
    │   ├── Peteco_3_climate.benchmark.txt
    │   ├── Peteco_3_landscape.benchmark.txt
    │   ├── Peteco_3_soil.benchmark.txt
    │   ├── Peteco_4_climate.benchmark.txt
    │   ├── Peteco_4_landscape.benchmark.txt
    │   ├── Peteco_4_soil.benchmark.txt
    │   ├── Peteco_5_climate.benchmark.txt
    │   ├── Peteco_5_landscape.benchmark.txt
    │   ├── Peteco_5_soil.benchmark.txt
    │   ├── Peteco_6_climate.benchmark.txt
    │   ├── Peteco_6_landscape.benchmark.txt
    │   ├── Peteco_6_soil.benchmark.txt
    │   ├── Peteco_7_climate.benchmark.txt
    │   ├── Peteco_7_landscape.benchmark.txt
    │   ├── Peteco_7_soil.benchmark.txt
    │   ├── Peteco_8_climate.benchmark.txt
    │   ├── Peteco_8_landscape.benchmark.txt
    │   ├── Peteco_8_soil.benchmark.txt
    │   ├── Peteco_9_climate.benchmark.txt
    │   ├── Peteco_9_landscape.benchmark.txt
    │   ├── Peteco_9_soil.benchmark.txt
    │   ├── Sungai Lalang_13_climate.benchmark.txt
    │   ├── Sungai Lalang_13_landscape.benchmark.txt
    │   ├── Sungai Lalang_13_soil.benchmark.txt
    │   ├── Sungai Lalang_14_climate.benchmark.txt
    │   ├── Sungai Lalang_14_landscape.benchmark.txt
    │   ├── Sungai Lalang_14_soil.benchmark.txt
    │   ├── Sungai Lalang_15_climate.benchmark.txt
    │   ├── Sungai Lalang_15_landscape.benchmark.txt
    │   ├── Sungai Lalang_15_soil.benchmark.txt
    │   ├── Sungai Lalang_16_climate.benchmark.txt
    │   ├── Sungai Lalang_16_landscape.benchmark.txt
    │   ├── Sungai Lalang_16_soil.benchmark.txt
    │   ├── Sungai Lalang_17_climate.benchmark.txt
    │   ├── Sungai Lalang_17_landscape.benchmark.txt
    │   ├── Sungai Lalang_17_soil.benchmark.txt
    │   ├── Sungai Lalang_18_climate.benchmark.txt
    │   ├── Sungai Lalang_18_landscape.benchmark.txt
    │   ├── Sungai Lalang_18_soil.benchmark.txt
    │   ├── Sungai Lalang_19_climate.benchmark.txt
    │   ├── Sungai Lalang_19_landscape.benchmark.txt
    │   ├── Sungai Lalang_19_soil.benchmark.txt
    │   ├── Sungai Lalang_20_climate.benchmark.txt
    │   ├── Sungai Lalang_20_landscape.benchmark.txt
    │   ├── Sungai Lalang_20_soil.benchmark.txt
    │   ├── Sungai Lalang_21_climate.benchmark.txt
    │   ├── Sungai Lalang_21_landscape.benchmark.txt
    │   ├── Sungai Lalang_21_soil.benchmark.txt
    │   ├── Tapajos km 114_101_climate.benchmark.txt
    │   ├── Tapajos km 114_101_landscape.benchmark.txt
    │   ├── Tapajos km 114_101_soil.benchmark.txt
    │   ├── Tapajos km 114_102_climate.benchmark.txt
    │   ├── Tapajos km 114_102_landscape.benchmark.txt
    │   ├── Tapajos km 114_102_soil.benchmark.txt
    │   ├── Tapajos km 114_103_climate.benchmark.txt
    │   ├── Tapajos km 114_103_landscape.benchmark.txt
    │   ├── Tapajos km 114_103_soil.benchmark.txt
    │   ├── Tapajos km 114_104_climate.benchmark.txt
    │   ├── Tapajos km 114_104_landscape.benchmark.txt
    │   ├── Tapajos km 114_104_soil.benchmark.txt
    │   ├── Tapajos km 114_105_climate.benchmark.txt
    │   ├── Tapajos km 114_105_landscape.benchmark.txt
    │   ├── Tapajos km 114_105_soil.benchmark.txt
    │   ├── Tapajos km 114_106_climate.benchmark.txt
    │   ├── Tapajos km 114_106_landscape.benchmark.txt
    │   ├── Tapajos km 114_106_soil.benchmark.txt
    │   ├── Tapajos km 114_107_climate.benchmark.txt
    │   ├── Tapajos km 114_107_landscape.benchmark.txt
    │   ├── Tapajos km 114_107_soil.benchmark.txt
    │   ├── Tapajos km 114_108_climate.benchmark.txt
    │   ├── Tapajos km 114_108_landscape.benchmark.txt
    │   ├── Tapajos km 114_108_soil.benchmark.txt
    │   ├── Tapajos km 114_109_climate.benchmark.txt
    │   ├── Tapajos km 114_109_landscape.benchmark.txt
    │   ├── Tapajos km 114_109_soil.benchmark.txt
    │   ├── Tapajos km 114_110_climate.benchmark.txt
    │   ├── Tapajos km 114_110_landscape.benchmark.txt
    │   ├── Tapajos km 114_110_soil.benchmark.txt
    │   ├── Tapajos km 114_111_climate.benchmark.txt
    │   ├── Tapajos km 114_111_landscape.benchmark.txt
    │   ├── Tapajos km 114_111_soil.benchmark.txt
    │   ├── Tapajos km 114_112_climate.benchmark.txt
    │   ├── Tapajos km 114_112_landscape.benchmark.txt
    │   ├── Tapajos km 114_112_soil.benchmark.txt
    │   ├── Tapajos km 114_201_climate.benchmark.txt
    │   ├── Tapajos km 114_201_landscape.benchmark.txt
    │   ├── Tapajos km 114_201_soil.benchmark.txt
    │   ├── Tapajos km 114_202_climate.benchmark.txt
    │   ├── Tapajos km 114_202_landscape.benchmark.txt
    │   ├── Tapajos km 114_202_soil.benchmark.txt
    │   ├── Tapajos km 114_203_climate.benchmark.txt
    │   ├── Tapajos km 114_203_landscape.benchmark.txt
    │   ├── Tapajos km 114_203_soil.benchmark.txt
    │   ├── Tapajos km 114_204_climate.benchmark.txt
    │   ├── Tapajos km 114_204_landscape.benchmark.txt
    │   ├── Tapajos km 114_204_soil.benchmark.txt
    │   ├── Tapajos km 114_205_climate.benchmark.txt
    │   ├── Tapajos km 114_205_landscape.benchmark.txt
    │   ├── Tapajos km 114_205_soil.benchmark.txt
    │   ├── Tapajos km 114_206_climate.benchmark.txt
    │   ├── Tapajos km 114_206_landscape.benchmark.txt
    │   ├── Tapajos km 114_206_soil.benchmark.txt
    │   ├── Tapajos km 114_207_climate.benchmark.txt
    │   ├── Tapajos km 114_207_landscape.benchmark.txt
    │   ├── Tapajos km 114_207_soil.benchmark.txt
    │   ├── Tapajos km 114_208_climate.benchmark.txt
    │   ├── Tapajos km 114_208_landscape.benchmark.txt
    │   ├── Tapajos km 114_208_soil.benchmark.txt
    │   ├── Tapajos km 114_209_climate.benchmark.txt
    │   ├── Tapajos km 114_209_landscape.benchmark.txt
    │   ├── Tapajos km 114_209_soil.benchmark.txt
    │   ├── Tapajos km 114_210_climate.benchmark.txt
    │   ├── Tapajos km 114_210_landscape.benchmark.txt
    │   ├── Tapajos km 114_210_soil.benchmark.txt
    │   ├── Tapajos km 114_211_climate.benchmark.txt
    │   ├── Tapajos km 114_211_landscape.benchmark.txt
    │   ├── Tapajos km 114_211_soil.benchmark.txt
    │   ├── Tapajos km 114_212_climate.benchmark.txt
    │   ├── Tapajos km 114_212_landscape.benchmark.txt
    │   ├── Tapajos km 114_212_soil.benchmark.txt
    │   ├── Tapajos km 114_301_climate.benchmark.txt
    │   ├── Tapajos km 114_301_landscape.benchmark.txt
    │   ├── Tapajos km 114_301_soil.benchmark.txt
    │   ├── Tapajos km 114_302_climate.benchmark.txt
    │   ├── Tapajos km 114_302_landscape.benchmark.txt
    │   ├── Tapajos km 114_302_soil.benchmark.txt
    │   ├── Tapajos km 114_303_climate.benchmark.txt
    │   ├── Tapajos km 114_303_landscape.benchmark.txt
    │   ├── Tapajos km 114_303_soil.benchmark.txt
    │   ├── Tapajos km 114_304_climate.benchmark.txt
    │   ├── Tapajos km 114_304_landscape.benchmark.txt
    │   ├── Tapajos km 114_304_soil.benchmark.txt
    │   ├── Tapajos km 114_305_climate.benchmark.txt
    │   ├── Tapajos km 114_305_landscape.benchmark.txt
    │   ├── Tapajos km 114_305_soil.benchmark.txt
    │   ├── Tapajos km 114_306_climate.benchmark.txt
    │   ├── Tapajos km 114_306_landscape.benchmark.txt
    │   ├── Tapajos km 114_306_soil.benchmark.txt
    │   ├── Tapajos km 114_307_climate.benchmark.txt
    │   ├── Tapajos km 114_307_landscape.benchmark.txt
    │   ├── Tapajos km 114_307_soil.benchmark.txt
    │   ├── Tapajos km 114_308_climate.benchmark.txt
    │   ├── Tapajos km 114_308_landscape.benchmark.txt
    │   ├── Tapajos km 114_308_soil.benchmark.txt
    │   ├── Tapajos km 114_309_climate.benchmark.txt
    │   ├── Tapajos km 114_309_landscape.benchmark.txt
    │   ├── Tapajos km 114_309_soil.benchmark.txt
    │   ├── Tapajos km 114_310_climate.benchmark.txt
    │   ├── Tapajos km 114_310_landscape.benchmark.txt
    │   ├── Tapajos km 114_310_soil.benchmark.txt
    │   ├── Tapajos km 114_311_climate.benchmark.txt
    │   ├── Tapajos km 114_311_landscape.benchmark.txt
    │   ├── Tapajos km 114_311_soil.benchmark.txt
    │   ├── Tapajos km 114_312_climate.benchmark.txt
    │   ├── Tapajos km 114_312_landscape.benchmark.txt
    │   ├── Tapajos km 114_312_soil.benchmark.txt
    │   ├── Tapajos km 114_401_climate.benchmark.txt
    │   ├── Tapajos km 114_401_landscape.benchmark.txt
    │   ├── Tapajos km 114_401_soil.benchmark.txt
    │   ├── Tapajos km 114_402_climate.benchmark.txt
    │   ├── Tapajos km 114_402_landscape.benchmark.txt
    │   ├── Tapajos km 114_402_soil.benchmark.txt
    │   ├── Tapajos km 114_403_climate.benchmark.txt
    │   ├── Tapajos km 114_403_landscape.benchmark.txt
    │   ├── Tapajos km 114_403_soil.benchmark.txt
    │   ├── Tapajos km 114_404_climate.benchmark.txt
    │   ├── Tapajos km 114_404_landscape.benchmark.txt
    │   ├── Tapajos km 114_404_soil.benchmark.txt
    │   ├── Tapajos km 114_405_climate.benchmark.txt
    │   ├── Tapajos km 114_405_landscape.benchmark.txt
    │   ├── Tapajos km 114_405_soil.benchmark.txt
    │   ├── Tapajos km 114_406_climate.benchmark.txt
    │   ├── Tapajos km 114_406_landscape.benchmark.txt
    │   ├── Tapajos km 114_406_soil.benchmark.txt
    │   ├── Tapajos km 114_407_climate.benchmark.txt
    │   ├── Tapajos km 114_407_landscape.benchmark.txt
    │   ├── Tapajos km 114_407_soil.benchmark.txt
    │   ├── Tapajos km 114_408_climate.benchmark.txt
    │   ├── Tapajos km 114_408_landscape.benchmark.txt
    │   ├── Tapajos km 114_408_soil.benchmark.txt
    │   ├── Tapajos km 114_409_climate.benchmark.txt
    │   ├── Tapajos km 114_409_landscape.benchmark.txt
    │   ├── Tapajos km 114_409_soil.benchmark.txt
    │   ├── Tapajos km 114_410_climate.benchmark.txt
    │   ├── Tapajos km 114_410_landscape.benchmark.txt
    │   ├── Tapajos km 114_410_soil.benchmark.txt
    │   ├── Tapajos km 114_411_climate.benchmark.txt
    │   ├── Tapajos km 114_411_landscape.benchmark.txt
    │   ├── Tapajos km 114_411_soil.benchmark.txt
    │   ├── Tapajos km 114_412_climate.benchmark.txt
    │   ├── Tapajos km 114_412_landscape.benchmark.txt
    │   ├── Tapajos km 114_412_soil.benchmark.txt
    │   ├── Tapajos km 114_501_climate.benchmark.txt
    │   ├── Tapajos km 114_501_landscape.benchmark.txt
    │   ├── Tapajos km 114_501_soil.benchmark.txt
    │   ├── Tapajos km 114_502_climate.benchmark.txt
    │   ├── Tapajos km 114_502_landscape.benchmark.txt
    │   ├── Tapajos km 114_502_soil.benchmark.txt
    │   ├── Tapajos km 114_503_climate.benchmark.txt
    │   ├── Tapajos km 114_503_landscape.benchmark.txt
    │   ├── Tapajos km 114_503_soil.benchmark.txt
    │   ├── Tapajos km 114_504_climate.benchmark.txt
    │   ├── Tapajos km 114_504_landscape.benchmark.txt
    │   ├── Tapajos km 114_504_soil.benchmark.txt
    │   ├── Tapajos km 114_505_climate.benchmark.txt
    │   ├── Tapajos km 114_505_landscape.benchmark.txt
    │   ├── Tapajos km 114_505_soil.benchmark.txt
    │   ├── Tapajos km 114_506_climate.benchmark.txt
    │   ├── Tapajos km 114_506_landscape.benchmark.txt
    │   ├── Tapajos km 114_506_soil.benchmark.txt
    │   ├── Tapajos km 114_507_climate.benchmark.txt
    │   ├── Tapajos km 114_507_landscape.benchmark.txt
    │   ├── Tapajos km 114_507_soil.benchmark.txt
    │   ├── Tapajos km 114_508_climate.benchmark.txt
    │   ├── Tapajos km 114_508_landscape.benchmark.txt
    │   ├── Tapajos km 114_508_soil.benchmark.txt
    │   ├── Tapajos km 114_509_climate.benchmark.txt
    │   ├── Tapajos km 114_509_landscape.benchmark.txt
    │   ├── Tapajos km 114_509_soil.benchmark.txt
    │   ├── Tapajos km 114_510_climate.benchmark.txt
    │   ├── Tapajos km 114_510_landscape.benchmark.txt
    │   ├── Tapajos km 114_510_soil.benchmark.txt
    │   ├── Tapajos km 114_511_climate.benchmark.txt
    │   ├── Tapajos km 114_511_landscape.benchmark.txt
    │   ├── Tapajos km 114_511_soil.benchmark.txt
    │   ├── Tapajos km 114_512_climate.benchmark.txt
    │   ├── Tapajos km 114_512_landscape.benchmark.txt
    │   ├── Tapajos km 114_512_soil.benchmark.txt
    │   ├── Tapajós km 67_01E_climate.benchmark.txt
    │   ├── Tapajós km 67_01E_landscape.benchmark.txt
    │   ├── Tapajós km 67_01E_soil.benchmark.txt
    │   ├── Tapajós km 67_01T_climate.benchmark.txt
    │   ├── Tapajós km 67_01T_landscape.benchmark.txt
    │   ├── Tapajós km 67_01T_soil.benchmark.txt
    │   ├── Tapajós km 67_02E_climate.benchmark.txt
    │   ├── Tapajós km 67_02E_landscape.benchmark.txt
    │   ├── Tapajós km 67_02E_soil.benchmark.txt
    │   ├── Tapajós km 67_02T_climate.benchmark.txt
    │   ├── Tapajós km 67_02T_landscape.benchmark.txt
    │   ├── Tapajós km 67_02T_soil.benchmark.txt
    │   ├── Tapajós km 67_03E_climate.benchmark.txt
    │   ├── Tapajós km 67_03E_landscape.benchmark.txt
    │   ├── Tapajós km 67_03E_soil.benchmark.txt
    │   ├── Tapajós km 67_03T_climate.benchmark.txt
    │   ├── Tapajós km 67_03T_landscape.benchmark.txt
    │   ├── Tapajós km 67_03T_soil.benchmark.txt
    │   ├── Tapajós km 67_04E_climate.benchmark.txt
    │   ├── Tapajós km 67_04E_landscape.benchmark.txt
    │   ├── Tapajós km 67_04E_soil.benchmark.txt
    │   ├── Tapajós km 67_04T_climate.benchmark.txt
    │   ├── Tapajós km 67_04T_landscape.benchmark.txt
    │   ├── Tapajós km 67_04T_soil.benchmark.txt
    │   ├── Tapajós km 67_05E_climate.benchmark.txt
    │   ├── Tapajós km 67_05E_landscape.benchmark.txt
    │   ├── Tapajós km 67_05E_soil.benchmark.txt
    │   ├── Tapajós km 67_05T_climate.benchmark.txt
    │   ├── Tapajós km 67_05T_landscape.benchmark.txt
    │   ├── Tapajós km 67_05T_soil.benchmark.txt
    │   ├── Tapajós km 67_06E_climate.benchmark.txt
    │   ├── Tapajós km 67_06E_landscape.benchmark.txt
    │   ├── Tapajós km 67_06E_soil.benchmark.txt
    │   ├── Tapajós km 67_06T_climate.benchmark.txt
    │   ├── Tapajós km 67_06T_landscape.benchmark.txt
    │   ├── Tapajós km 67_06T_soil.benchmark.txt
    │   ├── Tapajós km 67_07E_climate.benchmark.txt
    │   ├── Tapajós km 67_07E_landscape.benchmark.txt
    │   ├── Tapajós km 67_07E_soil.benchmark.txt
    │   ├── Tapajós km 67_07T_climate.benchmark.txt
    │   ├── Tapajós km 67_07T_landscape.benchmark.txt
    │   ├── Tapajós km 67_07T_soil.benchmark.txt
    │   ├── Tapajós km 67_08E_climate.benchmark.txt
    │   ├── Tapajós km 67_08E_landscape.benchmark.txt
    │   ├── Tapajós km 67_08E_soil.benchmark.txt
    │   ├── Tapajós km 67_08T_climate.benchmark.txt
    │   ├── Tapajós km 67_08T_landscape.benchmark.txt
    │   ├── Tapajós km 67_08T_soil.benchmark.txt
    │   ├── Tapajós km 67_09E_climate.benchmark.txt
    │   ├── Tapajós km 67_09E_landscape.benchmark.txt
    │   ├── Tapajós km 67_09E_soil.benchmark.txt
    │   ├── Tapajós km 67_09T_climate.benchmark.txt
    │   ├── Tapajós km 67_09T_landscape.benchmark.txt
    │   ├── Tapajós km 67_09T_soil.benchmark.txt
    │   ├── Tapajós km 67_10E_climate.benchmark.txt
    │   ├── Tapajós km 67_10E_landscape.benchmark.txt
    │   ├── Tapajós km 67_10E_soil.benchmark.txt
    │   ├── Tapajós km 67_10T_climate.benchmark.txt
    │   ├── Tapajós km 67_10T_landscape.benchmark.txt
    │   ├── Tapajós km 67_10T_soil.benchmark.txt
    │   ├── Tapajós km 67_11E_climate.benchmark.txt
    │   ├── Tapajós km 67_11E_landscape.benchmark.txt
    │   ├── Tapajós km 67_11E_soil.benchmark.txt
    │   ├── Tapajós km 67_11T_climate.benchmark.txt
    │   ├── Tapajós km 67_11T_landscape.benchmark.txt
    │   ├── Tapajós km 67_11T_soil.benchmark.txt
    │   ├── Tapajós km 67_12E_climate.benchmark.txt
    │   ├── Tapajós km 67_12E_landscape.benchmark.txt
    │   ├── Tapajós km 67_12E_soil.benchmark.txt
    │   ├── Tapajós km 67_12T_climate.benchmark.txt
    │   ├── Tapajós km 67_12T_landscape.benchmark.txt
    │   ├── Tapajós km 67_12T_soil.benchmark.txt
    │   ├── Tapajós km 67_13E_climate.benchmark.txt
    │   ├── Tapajós km 67_13E_landscape.benchmark.txt
    │   ├── Tapajós km 67_13E_soil.benchmark.txt
    │   ├── Tapajós km 67_13T_climate.benchmark.txt
    │   ├── Tapajós km 67_13T_landscape.benchmark.txt
    │   ├── Tapajós km 67_13T_soil.benchmark.txt
    │   ├── Tapajós km 67_14E_climate.benchmark.txt
    │   ├── Tapajós km 67_14E_landscape.benchmark.txt
    │   ├── Tapajós km 67_14E_soil.benchmark.txt
    │   ├── Tapajós km 67_14T_climate.benchmark.txt
    │   ├── Tapajós km 67_14T_landscape.benchmark.txt
    │   ├── Tapajós km 67_14T_soil.benchmark.txt
    │   ├── Tapajós km 67_15E_climate.benchmark.txt
    │   ├── Tapajós km 67_15E_landscape.benchmark.txt
    │   ├── Tapajós km 67_15E_soil.benchmark.txt
    │   ├── Tapajós km 67_15T_climate.benchmark.txt
    │   ├── Tapajós km 67_15T_landscape.benchmark.txt
    │   ├── Tapajós km 67_15T_soil.benchmark.txt
    │   ├── Tapajós km 67_16E_climate.benchmark.txt
    │   ├── Tapajós km 67_16E_landscape.benchmark.txt
    │   ├── Tapajós km 67_16E_soil.benchmark.txt
    │   ├── Tapajós km 67_16T_climate.benchmark.txt
    │   ├── Tapajós km 67_16T_landscape.benchmark.txt
    │   ├── Tapajós km 67_16T_soil.benchmark.txt
    │   ├── Tapajós km 67_17E_climate.benchmark.txt
    │   ├── Tapajós km 67_17E_landscape.benchmark.txt
    │   ├── Tapajós km 67_17E_soil.benchmark.txt
    │   ├── Tapajós km 67_17T_climate.benchmark.txt
    │   ├── Tapajós km 67_17T_landscape.benchmark.txt
    │   ├── Tapajós km 67_17T_soil.benchmark.txt
    │   ├── Tapajós km 67_18E_climate.benchmark.txt
    │   ├── Tapajós km 67_18E_landscape.benchmark.txt
    │   ├── Tapajós km 67_18E_soil.benchmark.txt
    │   ├── Tapajós km 67_18T_climate.benchmark.txt
    │   ├── Tapajós km 67_18T_landscape.benchmark.txt
    │   ├── Tapajós km 67_18T_soil.benchmark.txt
    │   ├── Tapajós km 67_19E_climate.benchmark.txt
    │   ├── Tapajós km 67_19E_landscape.benchmark.txt
    │   ├── Tapajós km 67_19E_soil.benchmark.txt
    │   ├── Tapajós km 67_20E_climate.benchmark.txt
    │   ├── Tapajós km 67_20E_landscape.benchmark.txt
    │   ├── Tapajós km 67_20E_soil.benchmark.txt
    │   ├── Tapajós km 67_21E_climate.benchmark.txt
    │   ├── Tapajós km 67_21E_landscape.benchmark.txt
    │   ├── Tapajós km 67_21E_soil.benchmark.txt
    │   ├── Tapajós km 67_22E_climate.benchmark.txt
    │   ├── Tapajós km 67_22E_landscape.benchmark.txt
    │   ├── Tapajós km 67_22E_soil.benchmark.txt
    │   ├── Tapajós km 67_23E_climate.benchmark.txt
    │   ├── Tapajós km 67_23E_landscape.benchmark.txt
    │   ├── Tapajós km 67_23E_soil.benchmark.txt
    │   ├── Tapajós km 67_24E_climate.benchmark.txt
    │   ├── Tapajós km 67_24E_landscape.benchmark.txt
    │   ├── Tapajós km 67_24E_soil.benchmark.txt
    │   ├── Tapajós km 67_25E_climate.benchmark.txt
    │   ├── Tapajós km 67_25E_landscape.benchmark.txt
    │   ├── Tapajós km 67_25E_soil.benchmark.txt
    │   ├── Tapajós km 67_26E_climate.benchmark.txt
    │   ├── Tapajós km 67_26E_landscape.benchmark.txt
    │   ├── Tapajós km 67_26E_soil.benchmark.txt
    │   ├── Tapajós km 67_27E_climate.benchmark.txt
    │   ├── Tapajós km 67_27E_landscape.benchmark.txt
    │   ├── Tapajós km 67_27E_soil.benchmark.txt
    │   ├── Tapajós km 67_28E_climate.benchmark.txt
    │   ├── Tapajós km 67_28E_landscape.benchmark.txt
    │   ├── Tapajós km 67_28E_soil.benchmark.txt
    │   ├── Tapajós km 67_29E_climate.benchmark.txt
    │   ├── Tapajós km 67_29E_landscape.benchmark.txt
    │   ├── Tapajós km 67_29E_soil.benchmark.txt
    │   ├── Tapajós km 67_30E_climate.benchmark.txt
    │   ├── Tapajós km 67_30E_landscape.benchmark.txt
    │   ├── Tapajós km 67_30E_soil.benchmark.txt
    │   ├── Tapajós km 67_31E_climate.benchmark.txt
    │   ├── Tapajós km 67_31E_landscape.benchmark.txt
    │   ├── Tapajós km 67_31E_soil.benchmark.txt
    │   ├── Tapajós km 67_32E_climate.benchmark.txt
    │   ├── Tapajós km 67_32E_landscape.benchmark.txt
    │   ├── Tapajós km 67_32E_soil.benchmark.txt
    │   ├── Tapajós km 67_33E_climate.benchmark.txt
    │   ├── Tapajós km 67_33E_landscape.benchmark.txt
    │   ├── Tapajós km 67_33E_soil.benchmark.txt
    │   ├── Tapajós km 67_34E_climate.benchmark.txt
    │   ├── Tapajós km 67_34E_landscape.benchmark.txt
    │   ├── Tapajós km 67_34E_soil.benchmark.txt
    │   ├── Tapajós km 67_35E_climate.benchmark.txt
    │   ├── Tapajós km 67_35E_landscape.benchmark.txt
    │   ├── Tapajós km 67_35E_soil.benchmark.txt
    │   ├── Tapajós km 67_36E_climate.benchmark.txt
    │   ├── Tapajós km 67_36E_landscape.benchmark.txt
    │   ├── Tapajós km 67_36E_soil.benchmark.txt
    │   ├── Tene_Subplot_10_climate.benchmark.txt
    │   ├── Tene_Subplot_10_landscape.benchmark.txt
    │   ├── Tene_Subplot_10_soil.benchmark.txt
    │   ├── Tene_Subplot_11_climate.benchmark.txt
    │   ├── Tene_Subplot_11_landscape.benchmark.txt
    │   ├── Tene_Subplot_11_soil.benchmark.txt
    │   ├── Tene_Subplot_12_climate.benchmark.txt
    │   ├── Tene_Subplot_12_landscape.benchmark.txt
    │   ├── Tene_Subplot_12_soil.benchmark.txt
    │   ├── Tene_Subplot_13_climate.benchmark.txt
    │   ├── Tene_Subplot_13_landscape.benchmark.txt
    │   ├── Tene_Subplot_13_soil.benchmark.txt
    │   ├── Tene_Subplot_14_climate.benchmark.txt
    │   ├── Tene_Subplot_14_landscape.benchmark.txt
    │   ├── Tene_Subplot_14_soil.benchmark.txt
    │   ├── Tene_Subplot_15_climate.benchmark.txt
    │   ├── Tene_Subplot_15_landscape.benchmark.txt
    │   ├── Tene_Subplot_15_soil.benchmark.txt
    │   ├── Tene_Subplot_16_climate.benchmark.txt
    │   ├── Tene_Subplot_16_landscape.benchmark.txt
    │   ├── Tene_Subplot_16_soil.benchmark.txt
    │   ├── Tene_Subplot_17_climate.benchmark.txt
    │   ├── Tene_Subplot_17_landscape.benchmark.txt
    │   ├── Tene_Subplot_17_soil.benchmark.txt
    │   ├── Tene_Subplot_18_climate.benchmark.txt
    │   ├── Tene_Subplot_18_landscape.benchmark.txt
    │   ├── Tene_Subplot_18_soil.benchmark.txt
    │   ├── Tene_Subplot_19_climate.benchmark.txt
    │   ├── Tene_Subplot_19_landscape.benchmark.txt
    │   ├── Tene_Subplot_19_soil.benchmark.txt
    │   ├── Tene_Subplot_1_climate.benchmark.txt
    │   ├── Tene_Subplot_1_landscape.benchmark.txt
    │   ├── Tene_Subplot_1_soil.benchmark.txt
    │   ├── Tene_Subplot_20_climate.benchmark.txt
    │   ├── Tene_Subplot_20_landscape.benchmark.txt
    │   ├── Tene_Subplot_20_soil.benchmark.txt
    │   ├── Tene_Subplot_21_climate.benchmark.txt
    │   ├── Tene_Subplot_21_landscape.benchmark.txt
    │   ├── Tene_Subplot_21_soil.benchmark.txt
    │   ├── Tene_Subplot_22_climate.benchmark.txt
    │   ├── Tene_Subplot_22_landscape.benchmark.txt
    │   ├── Tene_Subplot_22_soil.benchmark.txt
    │   ├── Tene_Subplot_23_climate.benchmark.txt
    │   ├── Tene_Subplot_23_landscape.benchmark.txt
    │   ├── Tene_Subplot_23_soil.benchmark.txt
    │   ├── Tene_Subplot_24_climate.benchmark.txt
    │   ├── Tene_Subplot_24_landscape.benchmark.txt
    │   ├── Tene_Subplot_24_soil.benchmark.txt
    │   ├── Tene_Subplot_25_climate.benchmark.txt
    │   ├── Tene_Subplot_25_landscape.benchmark.txt
    │   ├── Tene_Subplot_25_soil.benchmark.txt
    │   ├── Tene_Subplot_2_climate.benchmark.txt
    │   ├── Tene_Subplot_2_landscape.benchmark.txt
    │   ├── Tene_Subplot_2_soil.benchmark.txt
    │   ├── Tene_Subplot_3_climate.benchmark.txt
    │   ├── Tene_Subplot_3_landscape.benchmark.txt
    │   ├── Tene_Subplot_3_soil.benchmark.txt
    │   ├── Tene_Subplot_4_climate.benchmark.txt
    │   ├── Tene_Subplot_4_landscape.benchmark.txt
    │   ├── Tene_Subplot_4_soil.benchmark.txt
    │   ├── Tene_Subplot_5_climate.benchmark.txt
    │   ├── Tene_Subplot_5_landscape.benchmark.txt
    │   ├── Tene_Subplot_5_soil.benchmark.txt
    │   ├── Tene_Subplot_6_climate.benchmark.txt
    │   ├── Tene_Subplot_6_landscape.benchmark.txt
    │   ├── Tene_Subplot_6_soil.benchmark.txt
    │   ├── Tene_Subplot_7_climate.benchmark.txt
    │   ├── Tene_Subplot_7_landscape.benchmark.txt
    │   ├── Tene_Subplot_7_soil.benchmark.txt
    │   ├── Tene_Subplot_8_climate.benchmark.txt
    │   ├── Tene_Subplot_8_landscape.benchmark.txt
    │   ├── Tene_Subplot_8_soil.benchmark.txt
    │   ├── Tene_Subplot_9_climate.benchmark.txt
    │   ├── Tene_Subplot_9_landscape.benchmark.txt
    │   ├── Tene_Subplot_9_soil.benchmark.txt
    │   ├── Ulu Muda_22_climate.benchmark.txt
    │   ├── Ulu Muda_22_landscape.benchmark.txt
    │   ├── Ulu Muda_22_soil.benchmark.txt
    │   ├── Ulu Muda_23_climate.benchmark.txt
    │   ├── Ulu Muda_23_landscape.benchmark.txt
    │   ├── Ulu Muda_23_soil.benchmark.txt
    │   ├── Ulu Muda_24_climate.benchmark.txt
    │   ├── Ulu Muda_24_landscape.benchmark.txt
    │   ├── Ulu Muda_24_soil.benchmark.txt
    │   ├── Ulu Muda_25_climate.benchmark.txt
    │   ├── Ulu Muda_25_landscape.benchmark.txt
    │   ├── Ulu Muda_25_soil.benchmark.txt
    │   ├── Ulu Muda_26_climate.benchmark.txt
    │   ├── Ulu Muda_26_landscape.benchmark.txt
    │   ├── Ulu Muda_26_soil.benchmark.txt
    │   ├── Ulu Muda_27_climate.benchmark.txt
    │   ├── Ulu Muda_27_landscape.benchmark.txt
    │   ├── Ulu Muda_27_soil.benchmark.txt
    │   ├── Ulu Muda_28_climate.benchmark.txt
    │   ├── Ulu Muda_28_landscape.benchmark.txt
    │   ├── Ulu Muda_28_soil.benchmark.txt
    │   ├── Ulu Muda_29_climate.benchmark.txt
    │   ├── Ulu Muda_29_landscape.benchmark.txt
    │   ├── Ulu Muda_29_soil.benchmark.txt
    │   ├── Ulu Muda_30_climate.benchmark.txt
    │   ├── Ulu Muda_30_landscape.benchmark.txt
    │   ├── Ulu Muda_30_soil.benchmark.txt
    │   ├── Uppangala_LP1_climate.benchmark.txt
    │   ├── Uppangala_LP1_landscape.benchmark.txt
    │   ├── Uppangala_LP1_soil.benchmark.txt
    │   ├── Uppangala_LP2_climate.benchmark.txt
    │   ├── Uppangala_LP2_landscape.benchmark.txt
    │   ├── Uppangala_LP2_soil.benchmark.txt
    │   ├── Uppangala_LP3_climate.benchmark.txt
    │   ├── Uppangala_LP3_landscape.benchmark.txt
    │   ├── Uppangala_LP3_soil.benchmark.txt
    │   ├── Uppangala_LP4_climate.benchmark.txt
    │   ├── Uppangala_LP4_landscape.benchmark.txt
    │   ├── Uppangala_LP4_soil.benchmark.txt
    │   ├── Uppangala_UP1_climate.benchmark.txt
    │   ├── Uppangala_UP1_landscape.benchmark.txt
    │   ├── Uppangala_UP1_soil.benchmark.txt
    │   ├── Uppangala_UP2_climate.benchmark.txt
    │   ├── Uppangala_UP2_landscape.benchmark.txt
    │   ├── Uppangala_UP2_soil.benchmark.txt
    │   ├── sao_nicolau_1_climate.benchmark.txt
    │   ├── sao_nicolau_1_landscape.benchmark.txt
    │   ├── sao_nicolau_1_soil.benchmark.txt
    │   ├── sao_nicolau_2_climate.benchmark.txt
    │   ├── sao_nicolau_2_landscape.benchmark.txt
    │   ├── sao_nicolau_2_soil.benchmark.txt
    │   ├── sao_nicolau_3_climate.benchmark.txt
    │   ├── sao_nicolau_3_landscape.benchmark.txt
    │   ├── sao_nicolau_3_soil.benchmark.txt
    │   ├── sao_nicolau_4_climate.benchmark.txt
    │   ├── sao_nicolau_4_landscape.benchmark.txt
    │   ├── sao_nicolau_4_soil.benchmark.txt
    │   ├── sao_nicolau_5_climate.benchmark.txt
    │   ├── sao_nicolau_5_landscape.benchmark.txt
    │   ├── sao_nicolau_5_soil.benchmark.txt
    │   ├── sao_nicolau_6_climate.benchmark.txt
    │   ├── sao_nicolau_6_landscape.benchmark.txt
    │   └── sao_nicolau_6_soil.benchmark.txt
    ├── climate
    │   ├── BAFOG_III_climate.tsv
    │   ├── BAFOG_II_climate.tsv
    │   ├── BAFOG_IV_climate.tsv
    │   ├── BAFOG_I_climate.tsv
    │   ├── BAFOG_VII_climate.tsv
    │   ├── BAFOG_VI_climate.tsv
    │   ├── BAFOG_V_climate.tsv
    │   ├── Ecosilva_10_climate.tsv
    │   ├── Ecosilva_11_climate.tsv
    │   ├── Ecosilva_12_climate.tsv
    │   ├── Ecosilva_13_climate.tsv
    │   ├── Ecosilva_14_climate.tsv
    │   ├── Ecosilva_15_climate.tsv
    │   ├── Ecosilva_16_climate.tsv
    │   ├── Ecosilva_17_climate.tsv
    │   ├── Ecosilva_18_climate.tsv
    │   ├── Ecosilva_1_climate.tsv
    │   ├── Ecosilva_2_climate.tsv
    │   ├── Ecosilva_3_climate.tsv
    │   ├── Ecosilva_4_climate.tsv
    │   ├── Ecosilva_5_climate.tsv
    │   ├── Ecosilva_6_climate.tsv
    │   ├── Ecosilva_7_climate.tsv
    │   ├── Ecosilva_8_climate.tsv
    │   ├── Ecosilva_9_climate.tsv
    │   ├── Iwokrama_IWO-01_climate.tsv
    │   ├── Iwokrama_IWO-02_climate.tsv
    │   ├── Iwokrama_IWO-03_climate.tsv
    │   ├── Iwokrama_IWO-04_climate.tsv
    │   ├── Iwokrama_IWO-05_climate.tsv
    │   ├── Iwokrama_IWO-06_climate.tsv
    │   ├── Iwokrama_IWO-07_climate.tsv
    │   ├── Iwokrama_IWO-08_climate.tsv
    │   ├── Iwokrama_IWO-09_climate.tsv
    │   ├── Iwokrama_IWO-10_climate.tsv
    │   ├── Iwokrama_IWO-11_climate.tsv
    │   ├── Iwokrama_IWO-12_climate.tsv
    │   ├── Iwokrama_IWO-13_climate.tsv
    │   ├── Iwokrama_IWO-14_climate.tsv
    │   ├── Iwokrama_IWO-15_climate.tsv
    │   ├── Iwokrama_IWO-16_climate.tsv
    │   ├── Iwokrama_IWO-17_climate.tsv
    │   ├── Iwokrama_IWO-21_climate.tsv
    │   ├── Iwokrama_IWO-22_climate.tsv
    │   ├── Jari_101_climate.tsv
    │   ├── Jari_102_climate.tsv
    │   ├── Jari_103_climate.tsv
    │   ├── Jari_104_climate.tsv
    │   ├── Jari_105_climate.tsv
    │   ├── Jari_106_climate.tsv
    │   ├── Jari_107_climate.tsv
    │   ├── Jari_108_climate.tsv
    │   ├── Jari_109_climate.tsv
    │   ├── Jari_110_climate.tsv
    │   ├── Jari_111_climate.tsv
    │   ├── Jari_112_climate.tsv
    │   ├── Jari_1_climate.tsv
    │   ├── Jari_201_climate.tsv
    │   ├── Jari_202_climate.tsv
    │   ├── Jari_203_climate.tsv
    │   ├── Jari_204_climate.tsv
    │   ├── Jari_205_climate.tsv
    │   ├── Jari_206_climate.tsv
    │   ├── Jari_207_climate.tsv
    │   ├── Jari_208_climate.tsv
    │   ├── Jari_209_climate.tsv
    │   ├── Jari_210_climate.tsv
    │   ├── Jari_211_climate.tsv
    │   ├── Jari_212_climate.tsv
    │   ├── Jari_2_climate.tsv
    │   ├── Jari_301_climate.tsv
    │   ├── Jari_302_climate.tsv
    │   ├── Jari_303_climate.tsv
    │   ├── Jari_304_climate.tsv
    │   ├── Jari_305_climate.tsv
    │   ├── Jari_306_climate.tsv
    │   ├── Jari_307_climate.tsv
    │   ├── Jari_308_climate.tsv
    │   ├── Jari_309_climate.tsv
    │   ├── Jari_310_climate.tsv
    │   ├── Jari_311_climate.tsv
    │   ├── Jari_312_climate.tsv
    │   ├── Jari_3_climate.tsv
    │   ├── Jari_4_climate.tsv
    │   ├── Kabo_KAB-12_climate.tsv
    │   ├── Kabo_KAB-14_climate.tsv
    │   ├── Kabo_KAB-19_climate.tsv
    │   ├── Kabo_KAB-22_climate.tsv
    │   ├── Kabo_KAB-26_climate.tsv
    │   ├── Kabo_KAB-28_climate.tsv
    │   ├── Kabo_KAB-32_climate.tsv
    │   ├── Kabo_KAB-34_climate.tsv
    │   ├── Kabo_KAB-38_climate.tsv
    │   ├── Kabo_KAB-41_climate.tsv
    │   ├── Kabo_KAB-42_climate.tsv
    │   ├── Kabo_KAB-43_climate.tsv
    │   ├── Lesong_10_climate.tsv
    │   ├── Lesong_11_climate.tsv
    │   ├── Lesong_12_climate.tsv
    │   ├── Lesong_1_climate.tsv
    │   ├── Lesong_2_climate.tsv
    │   ├── Lesong_3_climate.tsv
    │   ├── Lesong_4_climate.tsv
    │   ├── Lesong_5_climate.tsv
    │   ├── Lesong_6_climate.tsv
    │   ├── Lesong_7_climate.tsv
    │   ├── Lesong_8_climate.tsv
    │   ├── Lesong_9_climate.tsv
    │   ├── Malinau_CNV01_climate.tsv
    │   ├── Malinau_CNV02_climate.tsv
    │   ├── Malinau_CNV03_climate.tsv
    │   ├── Malinau_CNV04_climate.tsv
    │   ├── Malinau_CNV05_climate.tsv
    │   ├── Malinau_CNV06_climate.tsv
    │   ├── Malinau_CNV07_climate.tsv
    │   ├── Malinau_CNV08_climate.tsv
    │   ├── Malinau_CNV09_climate.tsv
    │   ├── Malinau_CNV10_climate.tsv
    │   ├── Malinau_CNV11_climate.tsv
    │   ├── Malinau_CNV12_climate.tsv
    │   ├── Malinau_RIL01_climate.tsv
    │   ├── Malinau_RIL02_climate.tsv
    │   ├── Malinau_RIL03_climate.tsv
    │   ├── Malinau_RIL04_climate.tsv
    │   ├── Malinau_RIL05_climate.tsv
    │   ├── Malinau_RIL06_climate.tsv
    │   ├── Malinau_RIL07_climate.tsv
    │   ├── Malinau_RIL08_climate.tsv
    │   ├── Malinau_RIL09_climate.tsv
    │   ├── Malinau_RIL10_climate.tsv
    │   ├── Malinau_RIL11_climate.tsv
    │   ├── Malinau_RIL12_climate.tsv
    │   ├── Manare_Manare_II_climate.tsv
    │   ├── Manare_Manare_I_climate.tsv
    │   ├── Manare_Saut_Lavilette_climate.tsv
    │   ├── Misiones_10_climate.tsv
    │   ├── Misiones_11_climate.tsv
    │   ├── Misiones_12_climate.tsv
    │   ├── Misiones_13_climate.tsv
    │   ├── Misiones_14_climate.tsv
    │   ├── Misiones_16_climate.tsv
    │   ├── Misiones_19_climate.tsv
    │   ├── Misiones_1_climate.tsv
    │   ├── Misiones_20_climate.tsv
    │   ├── Misiones_21_climate.tsv
    │   ├── Misiones_2_climate.tsv
    │   ├── Misiones_3_climate.tsv
    │   ├── Misiones_4_climate.tsv
    │   ├── Misiones_5_climate.tsv
    │   ├── Misiones_6_climate.tsv
    │   ├── Misiones_7_climate.tsv
    │   ├── Misiones_8_climate.tsv
    │   ├── Misiones_9_climate.tsv
    │   ├── Moju_10_climate.tsv
    │   ├── Moju_11_climate.tsv
    │   ├── Moju_12_climate.tsv
    │   ├── Moju_13_climate.tsv
    │   ├── Moju_14_climate.tsv
    │   ├── Moju_15_climate.tsv
    │   ├── Moju_16_climate.tsv
    │   ├── Moju_17_climate.tsv
    │   ├── Moju_18_climate.tsv
    │   ├── Moju_19_climate.tsv
    │   ├── Moju_1_climate.tsv
    │   ├── Moju_20_climate.tsv
    │   ├── Moju_21_climate.tsv
    │   ├── Moju_22_climate.tsv
    │   ├── Moju_2_climate.tsv
    │   ├── Moju_3_climate.tsv
    │   ├── Moju_4_climate.tsv
    │   ├── Moju_5_climate.tsv
    │   ├── Moju_6_climate.tsv
    │   ├── Moju_7_climate.tsv
    │   ├── Moju_8_climate.tsv
    │   ├── Moju_9_climate.tsv
    │   ├── Montagne_tortue_P17_exploitee_1_climate.tsv
    │   ├── Montagne_tortue_P17_exploitee_2_climate.tsv
    │   ├── Montagne_tortue_P17_temoin_climate.tsv
    │   ├── Paracou_10_climate.tsv
    │   ├── Paracou_11_climate.tsv
    │   ├── Paracou_12_climate.tsv
    │   ├── Paracou_13_climate.tsv
    │   ├── Paracou_14_climate.tsv
    │   ├── Paracou_15_climate.tsv
    │   ├── Paracou_1_climate.tsv
    │   ├── Paracou_2_climate.tsv
    │   ├── Paracou_3_climate.tsv
    │   ├── Paracou_4_climate.tsv
    │   ├── Paracou_5_climate.tsv
    │   ├── Paracou_6_climate.tsv
    │   ├── Paracou_7_climate.tsv
    │   ├── Paracou_8_climate.tsv
    │   ├── Paracou_9_climate.tsv
    │   ├── Peteco_10_climate.tsv
    │   ├── Peteco_11_climate.tsv
    │   ├── Peteco_12_climate.tsv
    │   ├── Peteco_13_climate.tsv
    │   ├── Peteco_14_climate.tsv
    │   ├── Peteco_15_climate.tsv
    │   ├── Peteco_16_climate.tsv
    │   ├── Peteco_17_climate.tsv
    │   ├── Peteco_18_climate.tsv
    │   ├── Peteco_1_climate.tsv
    │   ├── Peteco_20_climate.tsv
    │   ├── Peteco_21_climate.tsv
    │   ├── Peteco_22_climate.tsv
    │   ├── Peteco_23_climate.tsv
    │   ├── Peteco_24_climate.tsv
    │   ├── Peteco_25_climate.tsv
    │   ├── Peteco_26_climate.tsv
    │   ├── Peteco_27_climate.tsv
    │   ├── Peteco_28_climate.tsv
    │   ├── Peteco_29_climate.tsv
    │   ├── Peteco_2_climate.tsv
    │   ├── Peteco_30_climate.tsv
    │   ├── Peteco_31_climate.tsv
    │   ├── Peteco_32_climate.tsv
    │   ├── Peteco_33_climate.tsv
    │   ├── Peteco_34_climate.tsv
    │   ├── Peteco_35_climate.tsv
    │   ├── Peteco_36_climate.tsv
    │   ├── Peteco_3_climate.tsv
    │   ├── Peteco_4_climate.tsv
    │   ├── Peteco_5_climate.tsv
    │   ├── Peteco_6_climate.tsv
    │   ├── Peteco_7_climate.tsv
    │   ├── Peteco_8_climate.tsv
    │   ├── Peteco_9_climate.tsv
    │   ├── Sungai Lalang_13_climate.tsv
    │   ├── Sungai Lalang_14_climate.tsv
    │   ├── Sungai Lalang_15_climate.tsv
    │   ├── Sungai Lalang_16_climate.tsv
    │   ├── Sungai Lalang_17_climate.tsv
    │   ├── Sungai Lalang_18_climate.tsv
    │   ├── Sungai Lalang_19_climate.tsv
    │   ├── Sungai Lalang_20_climate.tsv
    │   ├── Sungai Lalang_21_climate.tsv
    │   ├── Tapajos km 114_101_climate.tsv
    │   ├── Tapajos km 114_102_climate.tsv
    │   ├── Tapajos km 114_103_climate.tsv
    │   ├── Tapajos km 114_104_climate.tsv
    │   ├── Tapajos km 114_105_climate.tsv
    │   ├── Tapajos km 114_106_climate.tsv
    │   ├── Tapajos km 114_107_climate.tsv
    │   ├── Tapajos km 114_108_climate.tsv
    │   ├── Tapajos km 114_109_climate.tsv
    │   ├── Tapajos km 114_110_climate.tsv
    │   ├── Tapajos km 114_111_climate.tsv
    │   ├── Tapajos km 114_112_climate.tsv
    │   ├── Tapajos km 114_201_climate.tsv
    │   ├── Tapajos km 114_202_climate.tsv
    │   ├── Tapajos km 114_203_climate.tsv
    │   ├── Tapajos km 114_204_climate.tsv
    │   ├── Tapajos km 114_205_climate.tsv
    │   ├── Tapajos km 114_206_climate.tsv
    │   ├── Tapajos km 114_207_climate.tsv
    │   ├── Tapajos km 114_208_climate.tsv
    │   ├── Tapajos km 114_209_climate.tsv
    │   ├── Tapajos km 114_210_climate.tsv
    │   ├── Tapajos km 114_211_climate.tsv
    │   ├── Tapajos km 114_212_climate.tsv
    │   ├── Tapajos km 114_301_climate.tsv
    │   ├── Tapajos km 114_302_climate.tsv
    │   ├── Tapajos km 114_303_climate.tsv
    │   ├── Tapajos km 114_304_climate.tsv
    │   ├── Tapajos km 114_305_climate.tsv
    │   ├── Tapajos km 114_306_climate.tsv
    │   ├── Tapajos km 114_307_climate.tsv
    │   ├── Tapajos km 114_308_climate.tsv
    │   ├── Tapajos km 114_309_climate.tsv
    │   ├── Tapajos km 114_310_climate.tsv
    │   ├── Tapajos km 114_311_climate.tsv
    │   ├── Tapajos km 114_312_climate.tsv
    │   ├── Tapajos km 114_401_climate.tsv
    │   ├── Tapajos km 114_402_climate.tsv
    │   ├── Tapajos km 114_403_climate.tsv
    │   ├── Tapajos km 114_404_climate.tsv
    │   ├── Tapajos km 114_405_climate.tsv
    │   ├── Tapajos km 114_406_climate.tsv
    │   ├── Tapajos km 114_407_climate.tsv
    │   ├── Tapajos km 114_408_climate.tsv
    │   ├── Tapajos km 114_409_climate.tsv
    │   ├── Tapajos km 114_410_climate.tsv
    │   ├── Tapajos km 114_411_climate.tsv
    │   ├── Tapajos km 114_412_climate.tsv
    │   ├── Tapajos km 114_501_climate.tsv
    │   ├── Tapajos km 114_502_climate.tsv
    │   ├── Tapajos km 114_503_climate.tsv
    │   ├── Tapajos km 114_504_climate.tsv
    │   ├── Tapajos km 114_505_climate.tsv
    │   ├── Tapajos km 114_506_climate.tsv
    │   ├── Tapajos km 114_507_climate.tsv
    │   ├── Tapajos km 114_508_climate.tsv
    │   ├── Tapajos km 114_509_climate.tsv
    │   ├── Tapajos km 114_510_climate.tsv
    │   ├── Tapajos km 114_511_climate.tsv
    │   ├── Tapajos km 114_512_climate.tsv
    │   ├── Tapajós km 67_01E_climate.tsv
    │   ├── Tapajós km 67_01T_climate.tsv
    │   ├── Tapajós km 67_02E_climate.tsv
    │   ├── Tapajós km 67_02T_climate.tsv
    │   ├── Tapajós km 67_03E_climate.tsv
    │   ├── Tapajós km 67_03T_climate.tsv
    │   ├── Tapajós km 67_04E_climate.tsv
    │   ├── Tapajós km 67_04T_climate.tsv
    │   ├── Tapajós km 67_05E_climate.tsv
    │   ├── Tapajós km 67_05T_climate.tsv
    │   ├── Tapajós km 67_06E_climate.tsv
    │   ├── Tapajós km 67_06T_climate.tsv
    │   ├── Tapajós km 67_07E_climate.tsv
    │   ├── Tapajós km 67_07T_climate.tsv
    │   ├── Tapajós km 67_08E_climate.tsv
    │   ├── Tapajós km 67_08T_climate.tsv
    │   ├── Tapajós km 67_09E_climate.tsv
    │   ├── Tapajós km 67_09T_climate.tsv
    │   ├── Tapajós km 67_10E_climate.tsv
    │   ├── Tapajós km 67_10T_climate.tsv
    │   ├── Tapajós km 67_11E_climate.tsv
    │   ├── Tapajós km 67_11T_climate.tsv
    │   ├── Tapajós km 67_12E_climate.tsv
    │   ├── Tapajós km 67_12T_climate.tsv
    │   ├── Tapajós km 67_13E_climate.tsv
    │   ├── Tapajós km 67_13T_climate.tsv
    │   ├── Tapajós km 67_14E_climate.tsv
    │   ├── Tapajós km 67_14T_climate.tsv
    │   ├── Tapajós km 67_15E_climate.tsv
    │   ├── Tapajós km 67_15T_climate.tsv
    │   ├── Tapajós km 67_16E_climate.tsv
    │   ├── Tapajós km 67_16T_climate.tsv
    │   ├── Tapajós km 67_17E_climate.tsv
    │   ├── Tapajós km 67_17T_climate.tsv
    │   ├── Tapajós km 67_18E_climate.tsv
    │   ├── Tapajós km 67_18T_climate.tsv
    │   ├── Tapajós km 67_19E_climate.tsv
    │   ├── Tapajós km 67_20E_climate.tsv
    │   ├── Tapajós km 67_21E_climate.tsv
    │   ├── Tapajós km 67_22E_climate.tsv
    │   ├── Tapajós km 67_23E_climate.tsv
    │   ├── Tapajós km 67_24E_climate.tsv
    │   ├── Tapajós km 67_25E_climate.tsv
    │   ├── Tapajós km 67_26E_climate.tsv
    │   ├── Tapajós km 67_27E_climate.tsv
    │   ├── Tapajós km 67_28E_climate.tsv
    │   ├── Tapajós km 67_29E_climate.tsv
    │   ├── Tapajós km 67_30E_climate.tsv
    │   ├── Tapajós km 67_31E_climate.tsv
    │   ├── Tapajós km 67_32E_climate.tsv
    │   ├── Tapajós km 67_33E_climate.tsv
    │   ├── Tapajós km 67_34E_climate.tsv
    │   ├── Tapajós km 67_35E_climate.tsv
    │   ├── Tapajós km 67_36E_climate.tsv
    │   ├── Tene_Subplot_10_climate.tsv
    │   ├── Tene_Subplot_11_climate.tsv
    │   ├── Tene_Subplot_12_climate.tsv
    │   ├── Tene_Subplot_13_climate.tsv
    │   ├── Tene_Subplot_14_climate.tsv
    │   ├── Tene_Subplot_15_climate.tsv
    │   ├── Tene_Subplot_16_climate.tsv
    │   ├── Tene_Subplot_17_climate.tsv
    │   ├── Tene_Subplot_18_climate.tsv
    │   ├── Tene_Subplot_19_climate.tsv
    │   ├── Tene_Subplot_1_climate.tsv
    │   ├── Tene_Subplot_20_climate.tsv
    │   ├── Tene_Subplot_21_climate.tsv
    │   ├── Tene_Subplot_22_climate.tsv
    │   ├── Tene_Subplot_23_climate.tsv
    │   ├── Tene_Subplot_24_climate.tsv
    │   ├── Tene_Subplot_25_climate.tsv
    │   ├── Tene_Subplot_2_climate.tsv
    │   ├── Tene_Subplot_3_climate.tsv
    │   ├── Tene_Subplot_4_climate.tsv
    │   ├── Tene_Subplot_5_climate.tsv
    │   ├── Tene_Subplot_6_climate.tsv
    │   ├── Tene_Subplot_7_climate.tsv
    │   ├── Tene_Subplot_8_climate.tsv
    │   ├── Tene_Subplot_9_climate.tsv
    │   ├── Ulu Muda_22_climate.tsv
    │   ├── Ulu Muda_23_climate.tsv
    │   ├── Ulu Muda_24_climate.tsv
    │   ├── Ulu Muda_25_climate.tsv
    │   ├── Ulu Muda_26_climate.tsv
    │   ├── Ulu Muda_27_climate.tsv
    │   ├── Ulu Muda_28_climate.tsv
    │   ├── Ulu Muda_29_climate.tsv
    │   ├── Ulu Muda_30_climate.tsv
    │   ├── Uppangala_LP1_climate.tsv
    │   ├── Uppangala_LP2_climate.tsv
    │   ├── Uppangala_LP3_climate.tsv
    │   ├── Uppangala_LP4_climate.tsv
    │   ├── Uppangala_UP1_climate.tsv
    │   ├── Uppangala_UP2_climate.tsv
    │   ├── sao_nicolau_1_climate.tsv
    │   ├── sao_nicolau_2_climate.tsv
    │   ├── sao_nicolau_3_climate.tsv
    │   ├── sao_nicolau_4_climate.tsv
    │   ├── sao_nicolau_5_climate.tsv
    │   └── sao_nicolau_6_climate.tsv
    ├── landscape
    │   ├── BAFOG_III_landscape.tsv
    │   ├── BAFOG_II_landscape.tsv
    │   ├── BAFOG_IV_landscape.tsv
    │   ├── BAFOG_I_landscape.tsv
    │   ├── BAFOG_VII_landscape.tsv
    │   ├── BAFOG_VI_landscape.tsv
    │   ├── BAFOG_V_landscape.tsv
    │   ├── Ecosilva_10_landscape.tsv
    │   ├── Ecosilva_11_landscape.tsv
    │   ├── Ecosilva_12_landscape.tsv
    │   ├── Ecosilva_13_landscape.tsv
    │   ├── Ecosilva_14_landscape.tsv
    │   ├── Ecosilva_15_landscape.tsv
    │   ├── Ecosilva_16_landscape.tsv
    │   ├── Ecosilva_17_landscape.tsv
    │   ├── Ecosilva_18_landscape.tsv
    │   ├── Ecosilva_1_landscape.tsv
    │   ├── Ecosilva_2_landscape.tsv
    │   ├── Ecosilva_3_landscape.tsv
    │   ├── Ecosilva_4_landscape.tsv
    │   ├── Ecosilva_5_landscape.tsv
    │   ├── Ecosilva_6_landscape.tsv
    │   ├── Ecosilva_7_landscape.tsv
    │   ├── Ecosilva_8_landscape.tsv
    │   ├── Ecosilva_9_landscape.tsv
    │   ├── Iwokrama_IWO-01_landscape.tsv
    │   ├── Iwokrama_IWO-02_landscape.tsv
    │   ├── Iwokrama_IWO-03_landscape.tsv
    │   ├── Iwokrama_IWO-04_landscape.tsv
    │   ├── Iwokrama_IWO-05_landscape.tsv
    │   ├── Iwokrama_IWO-06_landscape.tsv
    │   ├── Iwokrama_IWO-07_landscape.tsv
    │   ├── Iwokrama_IWO-08_landscape.tsv
    │   ├── Iwokrama_IWO-09_landscape.tsv
    │   ├── Iwokrama_IWO-10_landscape.tsv
    │   ├── Iwokrama_IWO-11_landscape.tsv
    │   ├── Iwokrama_IWO-12_landscape.tsv
    │   ├── Iwokrama_IWO-13_landscape.tsv
    │   ├── Iwokrama_IWO-14_landscape.tsv
    │   ├── Iwokrama_IWO-15_landscape.tsv
    │   ├── Iwokrama_IWO-16_landscape.tsv
    │   ├── Iwokrama_IWO-17_landscape.tsv
    │   ├── Iwokrama_IWO-21_landscape.tsv
    │   ├── Iwokrama_IWO-22_landscape.tsv
    │   ├── Jari_101_landscape.tsv
    │   ├── Jari_102_landscape.tsv
    │   ├── Jari_103_landscape.tsv
    │   ├── Jari_104_landscape.tsv
    │   ├── Jari_105_landscape.tsv
    │   ├── Jari_106_landscape.tsv
    │   ├── Jari_107_landscape.tsv
    │   ├── Jari_108_landscape.tsv
    │   ├── Jari_109_landscape.tsv
    │   ├── Jari_110_landscape.tsv
    │   ├── Jari_111_landscape.tsv
    │   ├── Jari_112_landscape.tsv
    │   ├── Jari_1_landscape.tsv
    │   ├── Jari_201_landscape.tsv
    │   ├── Jari_202_landscape.tsv
    │   ├── Jari_203_landscape.tsv
    │   ├── Jari_204_landscape.tsv
    │   ├── Jari_205_landscape.tsv
    │   ├── Jari_206_landscape.tsv
    │   ├── Jari_207_landscape.tsv
    │   ├── Jari_208_landscape.tsv
    │   ├── Jari_209_landscape.tsv
    │   ├── Jari_210_landscape.tsv
    │   ├── Jari_211_landscape.tsv
    │   ├── Jari_212_landscape.tsv
    │   ├── Jari_2_landscape.tsv
    │   ├── Jari_301_landscape.tsv
    │   ├── Jari_302_landscape.tsv
    │   ├── Jari_303_landscape.tsv
    │   ├── Jari_304_landscape.tsv
    │   ├── Jari_305_landscape.tsv
    │   ├── Jari_306_landscape.tsv
    │   ├── Jari_307_landscape.tsv
    │   ├── Jari_308_landscape.tsv
    │   ├── Jari_309_landscape.tsv
    │   ├── Jari_310_landscape.tsv
    │   ├── Jari_311_landscape.tsv
    │   ├── Jari_312_landscape.tsv
    │   ├── Jari_3_landscape.tsv
    │   ├── Jari_4_landscape.tsv
    │   ├── Kabo_KAB-12_landscape.tsv
    │   ├── Kabo_KAB-14_landscape.tsv
    │   ├── Kabo_KAB-19_landscape.tsv
    │   ├── Kabo_KAB-22_landscape.tsv
    │   ├── Kabo_KAB-26_landscape.tsv
    │   ├── Kabo_KAB-28_landscape.tsv
    │   ├── Kabo_KAB-32_landscape.tsv
    │   ├── Kabo_KAB-34_landscape.tsv
    │   ├── Kabo_KAB-38_landscape.tsv
    │   ├── Kabo_KAB-41_landscape.tsv
    │   ├── Kabo_KAB-42_landscape.tsv
    │   ├── Kabo_KAB-43_landscape.tsv
    │   ├── Lesong_10_landscape.tsv
    │   ├── Lesong_11_landscape.tsv
    │   ├── Lesong_12_landscape.tsv
    │   ├── Lesong_1_landscape.tsv
    │   ├── Lesong_2_landscape.tsv
    │   ├── Lesong_3_landscape.tsv
    │   ├── Lesong_4_landscape.tsv
    │   ├── Lesong_5_landscape.tsv
    │   ├── Lesong_6_landscape.tsv
    │   ├── Lesong_7_landscape.tsv
    │   ├── Lesong_8_landscape.tsv
    │   ├── Lesong_9_landscape.tsv
    │   ├── Malinau_CNV01_landscape.tsv
    │   ├── Malinau_CNV02_landscape.tsv
    │   ├── Malinau_CNV03_landscape.tsv
    │   ├── Malinau_CNV04_landscape.tsv
    │   ├── Malinau_CNV05_landscape.tsv
    │   ├── Malinau_CNV06_landscape.tsv
    │   ├── Malinau_CNV07_landscape.tsv
    │   ├── Malinau_CNV08_landscape.tsv
    │   ├── Malinau_CNV09_landscape.tsv
    │   ├── Malinau_CNV10_landscape.tsv
    │   ├── Malinau_CNV11_landscape.tsv
    │   ├── Malinau_CNV12_landscape.tsv
    │   ├── Malinau_RIL01_landscape.tsv
    │   ├── Malinau_RIL02_landscape.tsv
    │   ├── Malinau_RIL03_landscape.tsv
    │   ├── Malinau_RIL04_landscape.tsv
    │   ├── Malinau_RIL05_landscape.tsv
    │   ├── Malinau_RIL06_landscape.tsv
    │   ├── Malinau_RIL07_landscape.tsv
    │   ├── Malinau_RIL08_landscape.tsv
    │   ├── Malinau_RIL09_landscape.tsv
    │   ├── Malinau_RIL10_landscape.tsv
    │   ├── Malinau_RIL11_landscape.tsv
    │   ├── Malinau_RIL12_landscape.tsv
    │   ├── Manare_Manare_II_landscape.tsv
    │   ├── Manare_Manare_I_landscape.tsv
    │   ├── Manare_Saut_Lavilette_landscape.tsv
    │   ├── Misiones_10_landscape.tsv
    │   ├── Misiones_11_landscape.tsv
    │   ├── Misiones_12_landscape.tsv
    │   ├── Misiones_13_landscape.tsv
    │   ├── Misiones_14_landscape.tsv
    │   ├── Misiones_16_landscape.tsv
    │   ├── Misiones_19_landscape.tsv
    │   ├── Misiones_1_landscape.tsv
    │   ├── Misiones_20_landscape.tsv
    │   ├── Misiones_21_landscape.tsv
    │   ├── Misiones_2_landscape.tsv
    │   ├── Misiones_3_landscape.tsv
    │   ├── Misiones_4_landscape.tsv
    │   ├── Misiones_5_landscape.tsv
    │   ├── Misiones_6_landscape.tsv
    │   ├── Misiones_7_landscape.tsv
    │   ├── Misiones_8_landscape.tsv
    │   ├── Misiones_9_landscape.tsv
    │   ├── Moju_10_landscape.tsv
    │   ├── Moju_11_landscape.tsv
    │   ├── Moju_12_landscape.tsv
    │   ├── Moju_13_landscape.tsv
    │   ├── Moju_14_landscape.tsv
    │   ├── Moju_15_landscape.tsv
    │   ├── Moju_16_landscape.tsv
    │   ├── Moju_17_landscape.tsv
    │   ├── Moju_18_landscape.tsv
    │   ├── Moju_19_landscape.tsv
    │   ├── Moju_1_landscape.tsv
    │   ├── Moju_20_landscape.tsv
    │   ├── Moju_21_landscape.tsv
    │   ├── Moju_22_landscape.tsv
    │   ├── Moju_2_landscape.tsv
    │   ├── Moju_3_landscape.tsv
    │   ├── Moju_4_landscape.tsv
    │   ├── Moju_5_landscape.tsv
    │   ├── Moju_6_landscape.tsv
    │   ├── Moju_7_landscape.tsv
    │   ├── Moju_8_landscape.tsv
    │   ├── Moju_9_landscape.tsv
    │   ├── Montagne_tortue_P17_exploitee_1_landscape.tsv
    │   ├── Montagne_tortue_P17_exploitee_2_landscape.tsv
    │   ├── Montagne_tortue_P17_temoin_landscape.tsv
    │   ├── Paracou_10_landscape.tsv
    │   ├── Paracou_11_landscape.tsv
    │   ├── Paracou_12_landscape.tsv
    │   ├── Paracou_13_landscape.tsv
    │   ├── Paracou_14_landscape.tsv
    │   ├── Paracou_15_landscape.tsv
    │   ├── Paracou_1_landscape.tsv
    │   ├── Paracou_2_landscape.tsv
    │   ├── Paracou_3_landscape.tsv
    │   ├── Paracou_4_landscape.tsv
    │   ├── Paracou_5_landscape.tsv
    │   ├── Paracou_6_landscape.tsv
    │   ├── Paracou_7_landscape.tsv
    │   ├── Paracou_8_landscape.tsv
    │   ├── Paracou_9_landscape.tsv
    │   ├── Peteco_10_landscape.tsv
    │   ├── Peteco_11_landscape.tsv
    │   ├── Peteco_12_landscape.tsv
    │   ├── Peteco_13_landscape.tsv
    │   ├── Peteco_14_landscape.tsv
    │   ├── Peteco_15_landscape.tsv
    │   ├── Peteco_16_landscape.tsv
    │   ├── Peteco_17_landscape.tsv
    │   ├── Peteco_18_landscape.tsv
    │   ├── Peteco_1_landscape.tsv
    │   ├── Peteco_20_landscape.tsv
    │   ├── Peteco_21_landscape.tsv
    │   ├── Peteco_22_landscape.tsv
    │   ├── Peteco_23_landscape.tsv
    │   ├── Peteco_24_landscape.tsv
    │   ├── Peteco_25_landscape.tsv
    │   ├── Peteco_26_landscape.tsv
    │   ├── Peteco_27_landscape.tsv
    │   ├── Peteco_28_landscape.tsv
    │   ├── Peteco_29_landscape.tsv
    │   ├── Peteco_2_landscape.tsv
    │   ├── Peteco_30_landscape.tsv
    │   ├── Peteco_31_landscape.tsv
    │   ├── Peteco_32_landscape.tsv
    │   ├── Peteco_33_landscape.tsv
    │   ├── Peteco_34_landscape.tsv
    │   ├── Peteco_35_landscape.tsv
    │   ├── Peteco_36_landscape.tsv
    │   ├── Peteco_3_landscape.tsv
    │   ├── Peteco_4_landscape.tsv
    │   ├── Peteco_5_landscape.tsv
    │   ├── Peteco_6_landscape.tsv
    │   ├── Peteco_7_landscape.tsv
    │   ├── Peteco_8_landscape.tsv
    │   ├── Peteco_9_landscape.tsv
    │   ├── Sungai Lalang_13_landscape.tsv
    │   ├── Sungai Lalang_14_landscape.tsv
    │   ├── Sungai Lalang_15_landscape.tsv
    │   ├── Sungai Lalang_16_landscape.tsv
    │   ├── Sungai Lalang_17_landscape.tsv
    │   ├── Sungai Lalang_18_landscape.tsv
    │   ├── Sungai Lalang_19_landscape.tsv
    │   ├── Sungai Lalang_20_landscape.tsv
    │   ├── Sungai Lalang_21_landscape.tsv
    │   ├── Tapajos km 114_101_landscape.tsv
    │   ├── Tapajos km 114_102_landscape.tsv
    │   ├── Tapajos km 114_103_landscape.tsv
    │   ├── Tapajos km 114_104_landscape.tsv
    │   ├── Tapajos km 114_105_landscape.tsv
    │   ├── Tapajos km 114_106_landscape.tsv
    │   ├── Tapajos km 114_107_landscape.tsv
    │   ├── Tapajos km 114_108_landscape.tsv
    │   ├── Tapajos km 114_109_landscape.tsv
    │   ├── Tapajos km 114_110_landscape.tsv
    │   ├── Tapajos km 114_111_landscape.tsv
    │   ├── Tapajos km 114_112_landscape.tsv
    │   ├── Tapajos km 114_201_landscape.tsv
    │   ├── Tapajos km 114_202_landscape.tsv
    │   ├── Tapajos km 114_203_landscape.tsv
    │   ├── Tapajos km 114_204_landscape.tsv
    │   ├── Tapajos km 114_205_landscape.tsv
    │   ├── Tapajos km 114_206_landscape.tsv
    │   ├── Tapajos km 114_207_landscape.tsv
    │   ├── Tapajos km 114_208_landscape.tsv
    │   ├── Tapajos km 114_209_landscape.tsv
    │   ├── Tapajos km 114_210_landscape.tsv
    │   ├── Tapajos km 114_211_landscape.tsv
    │   ├── Tapajos km 114_212_landscape.tsv
    │   ├── Tapajos km 114_301_landscape.tsv
    │   ├── Tapajos km 114_302_landscape.tsv
    │   ├── Tapajos km 114_303_landscape.tsv
    │   ├── Tapajos km 114_304_landscape.tsv
    │   ├── Tapajos km 114_305_landscape.tsv
    │   ├── Tapajos km 114_306_landscape.tsv
    │   ├── Tapajos km 114_307_landscape.tsv
    │   ├── Tapajos km 114_308_landscape.tsv
    │   ├── Tapajos km 114_309_landscape.tsv
    │   ├── Tapajos km 114_310_landscape.tsv
    │   ├── Tapajos km 114_311_landscape.tsv
    │   ├── Tapajos km 114_312_landscape.tsv
    │   ├── Tapajos km 114_401_landscape.tsv
    │   ├── Tapajos km 114_402_landscape.tsv
    │   ├── Tapajos km 114_403_landscape.tsv
    │   ├── Tapajos km 114_404_landscape.tsv
    │   ├── Tapajos km 114_405_landscape.tsv
    │   ├── Tapajos km 114_406_landscape.tsv
    │   ├── Tapajos km 114_407_landscape.tsv
    │   ├── Tapajos km 114_408_landscape.tsv
    │   ├── Tapajos km 114_409_landscape.tsv
    │   ├── Tapajos km 114_410_landscape.tsv
    │   ├── Tapajos km 114_411_landscape.tsv
    │   ├── Tapajos km 114_412_landscape.tsv
    │   ├── Tapajos km 114_501_landscape.tsv
    │   ├── Tapajos km 114_502_landscape.tsv
    │   ├── Tapajos km 114_503_landscape.tsv
    │   ├── Tapajos km 114_504_landscape.tsv
    │   ├── Tapajos km 114_505_landscape.tsv
    │   ├── Tapajos km 114_506_landscape.tsv
    │   ├── Tapajos km 114_507_landscape.tsv
    │   ├── Tapajos km 114_508_landscape.tsv
    │   ├── Tapajos km 114_509_landscape.tsv
    │   ├── Tapajos km 114_510_landscape.tsv
    │   ├── Tapajos km 114_511_landscape.tsv
    │   ├── Tapajos km 114_512_landscape.tsv
    │   ├── Tapajós km 67_01E_landscape.tsv
    │   ├── Tapajós km 67_01T_landscape.tsv
    │   ├── Tapajós km 67_02E_landscape.tsv
    │   ├── Tapajós km 67_02T_landscape.tsv
    │   ├── Tapajós km 67_03E_landscape.tsv
    │   ├── Tapajós km 67_03T_landscape.tsv
    │   ├── Tapajós km 67_04E_landscape.tsv
    │   ├── Tapajós km 67_04T_landscape.tsv
    │   ├── Tapajós km 67_05E_landscape.tsv
    │   ├── Tapajós km 67_05T_landscape.tsv
    │   ├── Tapajós km 67_06E_landscape.tsv
    │   ├── Tapajós km 67_06T_landscape.tsv
    │   ├── Tapajós km 67_07E_landscape.tsv
    │   ├── Tapajós km 67_07T_landscape.tsv
    │   ├── Tapajós km 67_08E_landscape.tsv
    │   ├── Tapajós km 67_08T_landscape.tsv
    │   ├── Tapajós km 67_09E_landscape.tsv
    │   ├── Tapajós km 67_09T_landscape.tsv
    │   ├── Tapajós km 67_10E_landscape.tsv
    │   ├── Tapajós km 67_10T_landscape.tsv
    │   ├── Tapajós km 67_11E_landscape.tsv
    │   ├── Tapajós km 67_11T_landscape.tsv
    │   ├── Tapajós km 67_12E_landscape.tsv
    │   ├── Tapajós km 67_12T_landscape.tsv
    │   ├── Tapajós km 67_13E_landscape.tsv
    │   ├── Tapajós km 67_13T_landscape.tsv
    │   ├── Tapajós km 67_14E_landscape.tsv
    │   ├── Tapajós km 67_14T_landscape.tsv
    │   ├── Tapajós km 67_15E_landscape.tsv
    │   ├── Tapajós km 67_15T_landscape.tsv
    │   ├── Tapajós km 67_16E_landscape.tsv
    │   ├── Tapajós km 67_16T_landscape.tsv
    │   ├── Tapajós km 67_17E_landscape.tsv
    │   ├── Tapajós km 67_17T_landscape.tsv
    │   ├── Tapajós km 67_18E_landscape.tsv
    │   ├── Tapajós km 67_18T_landscape.tsv
    │   ├── Tapajós km 67_19E_landscape.tsv
    │   ├── Tapajós km 67_20E_landscape.tsv
    │   ├── Tapajós km 67_21E_landscape.tsv
    │   ├── Tapajós km 67_22E_landscape.tsv
    │   ├── Tapajós km 67_23E_landscape.tsv
    │   ├── Tapajós km 67_24E_landscape.tsv
    │   ├── Tapajós km 67_25E_landscape.tsv
    │   ├── Tapajós km 67_26E_landscape.tsv
    │   ├── Tapajós km 67_27E_landscape.tsv
    │   ├── Tapajós km 67_28E_landscape.tsv
    │   ├── Tapajós km 67_29E_landscape.tsv
    │   ├── Tapajós km 67_30E_landscape.tsv
    │   ├── Tapajós km 67_31E_landscape.tsv
    │   ├── Tapajós km 67_32E_landscape.tsv
    │   ├── Tapajós km 67_33E_landscape.tsv
    │   ├── Tapajós km 67_34E_landscape.tsv
    │   ├── Tapajós km 67_35E_landscape.tsv
    │   ├── Tapajós km 67_36E_landscape.tsv
    │   ├── Tene_Subplot_10_landscape.tsv
    │   ├── Tene_Subplot_11_landscape.tsv
    │   ├── Tene_Subplot_12_landscape.tsv
    │   ├── Tene_Subplot_13_landscape.tsv
    │   ├── Tene_Subplot_14_landscape.tsv
    │   ├── Tene_Subplot_15_landscape.tsv
    │   ├── Tene_Subplot_16_landscape.tsv
    │   ├── Tene_Subplot_17_landscape.tsv
    │   ├── Tene_Subplot_18_landscape.tsv
    │   ├── Tene_Subplot_19_landscape.tsv
    │   ├── Tene_Subplot_1_landscape.tsv
    │   ├── Tene_Subplot_20_landscape.tsv
    │   ├── Tene_Subplot_21_landscape.tsv
    │   ├── Tene_Subplot_22_landscape.tsv
    │   ├── Tene_Subplot_23_landscape.tsv
    │   ├── Tene_Subplot_24_landscape.tsv
    │   ├── Tene_Subplot_25_landscape.tsv
    │   ├── Tene_Subplot_2_landscape.tsv
    │   ├── Tene_Subplot_3_landscape.tsv
    │   ├── Tene_Subplot_4_landscape.tsv
    │   ├── Tene_Subplot_5_landscape.tsv
    │   ├── Tene_Subplot_6_landscape.tsv
    │   ├── Tene_Subplot_7_landscape.tsv
    │   ├── Tene_Subplot_8_landscape.tsv
    │   ├── Tene_Subplot_9_landscape.tsv
    │   ├── Ulu Muda_22_landscape.tsv
    │   ├── Ulu Muda_23_landscape.tsv
    │   ├── Ulu Muda_24_landscape.tsv
    │   ├── Ulu Muda_25_landscape.tsv
    │   ├── Ulu Muda_26_landscape.tsv
    │   ├── Ulu Muda_27_landscape.tsv
    │   ├── Ulu Muda_28_landscape.tsv
    │   ├── Ulu Muda_29_landscape.tsv
    │   ├── Ulu Muda_30_landscape.tsv
    │   ├── Uppangala_LP1_landscape.tsv
    │   ├── Uppangala_LP2_landscape.tsv
    │   ├── Uppangala_LP3_landscape.tsv
    │   ├── Uppangala_LP4_landscape.tsv
    │   ├── Uppangala_UP1_landscape.tsv
    │   ├── Uppangala_UP2_landscape.tsv
    │   ├── sao_nicolau_1_landscape.tsv
    │   ├── sao_nicolau_2_landscape.tsv
    │   ├── sao_nicolau_3_landscape.tsv
    │   ├── sao_nicolau_4_landscape.tsv
    │   ├── sao_nicolau_5_landscape.tsv
    │   └── sao_nicolau_6_landscape.tsv
    ├── logs
    │   ├── BAFOG_III_climate.log
    │   ├── BAFOG_III_landscape.log
    │   ├── BAFOG_III_soil.log
    │   ├── BAFOG_II_climate.log
    │   ├── BAFOG_II_landscape.log
    │   ├── BAFOG_II_soil.log
    │   ├── BAFOG_IV_climate.log
    │   ├── BAFOG_IV_landscape.log
    │   ├── BAFOG_IV_soil.log
    │   ├── BAFOG_I_climate.log
    │   ├── BAFOG_I_landscape.log
    │   ├── BAFOG_I_soil.log
    │   ├── BAFOG_VII_climate.log
    │   ├── BAFOG_VII_landscape.log
    │   ├── BAFOG_VII_soil.log
    │   ├── BAFOG_VI_climate.log
    │   ├── BAFOG_VI_landscape.log
    │   ├── BAFOG_VI_soil.log
    │   ├── BAFOG_V_climate.log
    │   ├── BAFOG_V_landscape.log
    │   ├── BAFOG_V_soil.log
    │   ├── Ecosilva_10_climate.log
    │   ├── Ecosilva_10_landscape.log
    │   ├── Ecosilva_10_soil.log
    │   ├── Ecosilva_11_climate.log
    │   ├── Ecosilva_11_landscape.log
    │   ├── Ecosilva_11_soil.log
    │   ├── Ecosilva_12_climate.log
    │   ├── Ecosilva_12_landscape.log
    │   ├── Ecosilva_12_soil.log
    │   ├── Ecosilva_13_climate.log
    │   ├── Ecosilva_13_landscape.log
    │   ├── Ecosilva_13_soil.log
    │   ├── Ecosilva_14_climate.log
    │   ├── Ecosilva_14_landscape.log
    │   ├── Ecosilva_14_soil.log
    │   ├── Ecosilva_15_climate.log
    │   ├── Ecosilva_15_landscape.log
    │   ├── Ecosilva_15_soil.log
    │   ├── Ecosilva_16_climate.log
    │   ├── Ecosilva_16_landscape.log
    │   ├── Ecosilva_16_soil.log
    │   ├── Ecosilva_17_climate.log
    │   ├── Ecosilva_17_landscape.log
    │   ├── Ecosilva_17_soil.log
    │   ├── Ecosilva_18_climate.log
    │   ├── Ecosilva_18_landscape.log
    │   ├── Ecosilva_18_soil.log
    │   ├── Ecosilva_1_climate.log
    │   ├── Ecosilva_1_landscape.log
    │   ├── Ecosilva_1_soil.log
    │   ├── Ecosilva_2_climate.log
    │   ├── Ecosilva_2_landscape.log
    │   ├── Ecosilva_2_soil.log
    │   ├── Ecosilva_3_climate.log
    │   ├── Ecosilva_3_landscape.log
    │   ├── Ecosilva_3_soil.log
    │   ├── Ecosilva_4_climate.log
    │   ├── Ecosilva_4_landscape.log
    │   ├── Ecosilva_4_soil.log
    │   ├── Ecosilva_5_climate.log
    │   ├── Ecosilva_5_landscape.log
    │   ├── Ecosilva_5_soil.log
    │   ├── Ecosilva_6_climate.log
    │   ├── Ecosilva_6_landscape.log
    │   ├── Ecosilva_6_soil.log
    │   ├── Ecosilva_7_climate.log
    │   ├── Ecosilva_7_landscape.log
    │   ├── Ecosilva_7_soil.log
    │   ├── Ecosilva_8_climate.log
    │   ├── Ecosilva_8_landscape.log
    │   ├── Ecosilva_8_soil.log
    │   ├── Ecosilva_9_climate.log
    │   ├── Ecosilva_9_landscape.log
    │   ├── Ecosilva_9_soil.log
    │   ├── Iwokrama_IWO-01_climate.log
    │   ├── Iwokrama_IWO-01_landscape.log
    │   ├── Iwokrama_IWO-01_soil.log
    │   ├── Iwokrama_IWO-02_climate.log
    │   ├── Iwokrama_IWO-02_landscape.log
    │   ├── Iwokrama_IWO-02_soil.log
    │   ├── Iwokrama_IWO-03_climate.log
    │   ├── Iwokrama_IWO-03_landscape.log
    │   ├── Iwokrama_IWO-03_soil.log
    │   ├── Iwokrama_IWO-04_climate.log
    │   ├── Iwokrama_IWO-04_landscape.log
    │   ├── Iwokrama_IWO-04_soil.log
    │   ├── Iwokrama_IWO-05_climate.log
    │   ├── Iwokrama_IWO-05_landscape.log
    │   ├── Iwokrama_IWO-05_soil.log
    │   ├── Iwokrama_IWO-06_climate.log
    │   ├── Iwokrama_IWO-06_landscape.log
    │   ├── Iwokrama_IWO-06_soil.log
    │   ├── Iwokrama_IWO-07_climate.log
    │   ├── Iwokrama_IWO-07_landscape.log
    │   ├── Iwokrama_IWO-07_soil.log
    │   ├── Iwokrama_IWO-08_climate.log
    │   ├── Iwokrama_IWO-08_landscape.log
    │   ├── Iwokrama_IWO-08_soil.log
    │   ├── Iwokrama_IWO-09_climate.log
    │   ├── Iwokrama_IWO-09_landscape.log
    │   ├── Iwokrama_IWO-09_soil.log
    │   ├── Iwokrama_IWO-10_climate.log
    │   ├── Iwokrama_IWO-10_landscape.log
    │   ├── Iwokrama_IWO-10_soil.log
    │   ├── Iwokrama_IWO-11_climate.log
    │   ├── Iwokrama_IWO-11_landscape.log
    │   ├── Iwokrama_IWO-11_soil.log
    │   ├── Iwokrama_IWO-12_climate.log
    │   ├── Iwokrama_IWO-12_landscape.log
    │   ├── Iwokrama_IWO-12_soil.log
    │   ├── Iwokrama_IWO-13_climate.log
    │   ├── Iwokrama_IWO-13_landscape.log
    │   ├── Iwokrama_IWO-13_soil.log
    │   ├── Iwokrama_IWO-14_climate.log
    │   ├── Iwokrama_IWO-14_landscape.log
    │   ├── Iwokrama_IWO-14_soil.log
    │   ├── Iwokrama_IWO-15_climate.log
    │   ├── Iwokrama_IWO-15_landscape.log
    │   ├── Iwokrama_IWO-15_soil.log
    │   ├── Iwokrama_IWO-16_climate.log
    │   ├── Iwokrama_IWO-16_landscape.log
    │   ├── Iwokrama_IWO-16_soil.log
    │   ├── Iwokrama_IWO-17_climate.log
    │   ├── Iwokrama_IWO-17_landscape.log
    │   ├── Iwokrama_IWO-17_soil.log
    │   ├── Iwokrama_IWO-21_climate.log
    │   ├── Iwokrama_IWO-21_landscape.log
    │   ├── Iwokrama_IWO-21_soil.log
    │   ├── Iwokrama_IWO-22_climate.log
    │   ├── Iwokrama_IWO-22_landscape.log
    │   ├── Iwokrama_IWO-22_soil.log
    │   ├── Jari_101_climate.log
    │   ├── Jari_101_landscape.log
    │   ├── Jari_101_soil.log
    │   ├── Jari_102_climate.log
    │   ├── Jari_102_landscape.log
    │   ├── Jari_102_soil.log
    │   ├── Jari_103_climate.log
    │   ├── Jari_103_landscape.log
    │   ├── Jari_103_soil.log
    │   ├── Jari_104_climate.log
    │   ├── Jari_104_landscape.log
    │   ├── Jari_104_soil.log
    │   ├── Jari_105_climate.log
    │   ├── Jari_105_landscape.log
    │   ├── Jari_105_soil.log
    │   ├── Jari_106_climate.log
    │   ├── Jari_106_landscape.log
    │   ├── Jari_106_soil.log
    │   ├── Jari_107_climate.log
    │   ├── Jari_107_landscape.log
    │   ├── Jari_107_soil.log
    │   ├── Jari_108_climate.log
    │   ├── Jari_108_landscape.log
    │   ├── Jari_108_soil.log
    │   ├── Jari_109_climate.log
    │   ├── Jari_109_landscape.log
    │   ├── Jari_109_soil.log
    │   ├── Jari_110_climate.log
    │   ├── Jari_110_landscape.log
    │   ├── Jari_110_soil.log
    │   ├── Jari_111_climate.log
    │   ├── Jari_111_landscape.log
    │   ├── Jari_111_soil.log
    │   ├── Jari_112_climate.log
    │   ├── Jari_112_landscape.log
    │   ├── Jari_112_soil.log
    │   ├── Jari_1_climate.log
    │   ├── Jari_1_landscape.log
    │   ├── Jari_1_soil.log
    │   ├── Jari_201_climate.log
    │   ├── Jari_201_landscape.log
    │   ├── Jari_201_soil.log
    │   ├── Jari_202_climate.log
    │   ├── Jari_202_landscape.log
    │   ├── Jari_202_soil.log
    │   ├── Jari_203_climate.log
    │   ├── Jari_203_landscape.log
    │   ├── Jari_203_soil.log
    │   ├── Jari_204_climate.log
    │   ├── Jari_204_landscape.log
    │   ├── Jari_204_soil.log
    │   ├── Jari_205_climate.log
    │   ├── Jari_205_landscape.log
    │   ├── Jari_205_soil.log
    │   ├── Jari_206_climate.log
    │   ├── Jari_206_landscape.log
    │   ├── Jari_206_soil.log
    │   ├── Jari_207_climate.log
    │   ├── Jari_207_landscape.log
    │   ├── Jari_207_soil.log
    │   ├── Jari_208_climate.log
    │   ├── Jari_208_landscape.log
    │   ├── Jari_208_soil.log
    │   ├── Jari_209_climate.log
    │   ├── Jari_209_landscape.log
    │   ├── Jari_209_soil.log
    │   ├── Jari_210_climate.log
    │   ├── Jari_210_landscape.log
    │   ├── Jari_210_soil.log
    │   ├── Jari_211_climate.log
    │   ├── Jari_211_landscape.log
    │   ├── Jari_211_soil.log
    │   ├── Jari_212_climate.log
    │   ├── Jari_212_landscape.log
    │   ├── Jari_212_soil.log
    │   ├── Jari_2_climate.log
    │   ├── Jari_2_landscape.log
    │   ├── Jari_2_soil.log
    │   ├── Jari_301_climate.log
    │   ├── Jari_301_landscape.log
    │   ├── Jari_301_soil.log
    │   ├── Jari_302_climate.log
    │   ├── Jari_302_landscape.log
    │   ├── Jari_302_soil.log
    │   ├── Jari_303_climate.log
    │   ├── Jari_303_landscape.log
    │   ├── Jari_303_soil.log
    │   ├── Jari_304_climate.log
    │   ├── Jari_304_landscape.log
    │   ├── Jari_304_soil.log
    │   ├── Jari_305_climate.log
    │   ├── Jari_305_landscape.log
    │   ├── Jari_305_soil.log
    │   ├── Jari_306_climate.log
    │   ├── Jari_306_landscape.log
    │   ├── Jari_306_soil.log
    │   ├── Jari_307_climate.log
    │   ├── Jari_307_landscape.log
    │   ├── Jari_307_soil.log
    │   ├── Jari_308_climate.log
    │   ├── Jari_308_landscape.log
    │   ├── Jari_308_soil.log
    │   ├── Jari_309_climate.log
    │   ├── Jari_309_landscape.log
    │   ├── Jari_309_soil.log
    │   ├── Jari_310_climate.log
    │   ├── Jari_310_landscape.log
    │   ├── Jari_310_soil.log
    │   ├── Jari_311_climate.log
    │   ├── Jari_311_landscape.log
    │   ├── Jari_311_soil.log
    │   ├── Jari_312_climate.log
    │   ├── Jari_312_landscape.log
    │   ├── Jari_312_soil.log
    │   ├── Jari_3_climate.log
    │   ├── Jari_3_landscape.log
    │   ├── Jari_3_soil.log
    │   ├── Jari_4_climate.log
    │   ├── Jari_4_landscape.log
    │   ├── Jari_4_soil.log
    │   ├── Kabo_KAB-12_climate.log
    │   ├── Kabo_KAB-12_landscape.log
    │   ├── Kabo_KAB-12_soil.log
    │   ├── Kabo_KAB-14_climate.log
    │   ├── Kabo_KAB-14_landscape.log
    │   ├── Kabo_KAB-14_soil.log
    │   ├── Kabo_KAB-19_climate.log
    │   ├── Kabo_KAB-19_landscape.log
    │   ├── Kabo_KAB-19_soil.log
    │   ├── Kabo_KAB-22_climate.log
    │   ├── Kabo_KAB-22_landscape.log
    │   ├── Kabo_KAB-22_soil.log
    │   ├── Kabo_KAB-26_climate.log
    │   ├── Kabo_KAB-26_landscape.log
    │   ├── Kabo_KAB-26_soil.log
    │   ├── Kabo_KAB-28_climate.log
    │   ├── Kabo_KAB-28_landscape.log
    │   ├── Kabo_KAB-28_soil.log
    │   ├── Kabo_KAB-32_climate.log
    │   ├── Kabo_KAB-32_landscape.log
    │   ├── Kabo_KAB-32_soil.log
    │   ├── Kabo_KAB-34_climate.log
    │   ├── Kabo_KAB-34_landscape.log
    │   ├── Kabo_KAB-34_soil.log
    │   ├── Kabo_KAB-38_climate.log
    │   ├── Kabo_KAB-38_landscape.log
    │   ├── Kabo_KAB-38_soil.log
    │   ├── Kabo_KAB-41_climate.log
    │   ├── Kabo_KAB-41_landscape.log
    │   ├── Kabo_KAB-41_soil.log
    │   ├── Kabo_KAB-42_climate.log
    │   ├── Kabo_KAB-42_landscape.log
    │   ├── Kabo_KAB-42_soil.log
    │   ├── Kabo_KAB-43_climate.log
    │   ├── Kabo_KAB-43_landscape.log
    │   ├── Kabo_KAB-43_soil.log
    │   ├── Lesong_10_climate.log
    │   ├── Lesong_10_landscape.log
    │   ├── Lesong_10_soil.log
    │   ├── Lesong_11_climate.log
    │   ├── Lesong_11_landscape.log
    │   ├── Lesong_11_soil.log
    │   ├── Lesong_12_climate.log
    │   ├── Lesong_12_landscape.log
    │   ├── Lesong_12_soil.log
    │   ├── Lesong_1_climate.log
    │   ├── Lesong_1_landscape.log
    │   ├── Lesong_1_soil.log
    │   ├── Lesong_2_climate.log
    │   ├── Lesong_2_landscape.log
    │   ├── Lesong_2_soil.log
    │   ├── Lesong_3_climate.log
    │   ├── Lesong_3_landscape.log
    │   ├── Lesong_3_soil.log
    │   ├── Lesong_4_climate.log
    │   ├── Lesong_4_landscape.log
    │   ├── Lesong_4_soil.log
    │   ├── Lesong_5_climate.log
    │   ├── Lesong_5_landscape.log
    │   ├── Lesong_5_soil.log
    │   ├── Lesong_6_climate.log
    │   ├── Lesong_6_landscape.log
    │   ├── Lesong_6_soil.log
    │   ├── Lesong_7_climate.log
    │   ├── Lesong_7_landscape.log
    │   ├── Lesong_7_soil.log
    │   ├── Lesong_8_climate.log
    │   ├── Lesong_8_landscape.log
    │   ├── Lesong_8_soil.log
    │   ├── Lesong_9_climate.log
    │   ├── Lesong_9_landscape.log
    │   ├── Lesong_9_soil.log
    │   ├── Malinau_CNV01_climate.log
    │   ├── Malinau_CNV01_landscape.log
    │   ├── Malinau_CNV01_soil.log
    │   ├── Malinau_CNV02_climate.log
    │   ├── Malinau_CNV02_landscape.log
    │   ├── Malinau_CNV02_soil.log
    │   ├── Malinau_CNV03_climate.log
    │   ├── Malinau_CNV03_landscape.log
    │   ├── Malinau_CNV03_soil.log
    │   ├── Malinau_CNV04_climate.log
    │   ├── Malinau_CNV04_landscape.log
    │   ├── Malinau_CNV04_soil.log
    │   ├── Malinau_CNV05_climate.log
    │   ├── Malinau_CNV05_landscape.log
    │   ├── Malinau_CNV05_soil.log
    │   ├── Malinau_CNV06_climate.log
    │   ├── Malinau_CNV06_landscape.log
    │   ├── Malinau_CNV06_soil.log
    │   ├── Malinau_CNV07_climate.log
    │   ├── Malinau_CNV07_landscape.log
    │   ├── Malinau_CNV07_soil.log
    │   ├── Malinau_CNV08_climate.log
    │   ├── Malinau_CNV08_landscape.log
    │   ├── Malinau_CNV08_soil.log
    │   ├── Malinau_CNV09_climate.log
    │   ├── Malinau_CNV09_landscape.log
    │   ├── Malinau_CNV09_soil.log
    │   ├── Malinau_CNV10_climate.log
    │   ├── Malinau_CNV10_landscape.log
    │   ├── Malinau_CNV10_soil.log
    │   ├── Malinau_CNV11_climate.log
    │   ├── Malinau_CNV11_landscape.log
    │   ├── Malinau_CNV11_soil.log
    │   ├── Malinau_CNV12_climate.log
    │   ├── Malinau_CNV12_landscape.log
    │   ├── Malinau_CNV12_soil.log
    │   ├── Malinau_RIL01_climate.log
    │   ├── Malinau_RIL01_landscape.log
    │   ├── Malinau_RIL01_soil.log
    │   ├── Malinau_RIL02_climate.log
    │   ├── Malinau_RIL02_landscape.log
    │   ├── Malinau_RIL02_soil.log
    │   ├── Malinau_RIL03_climate.log
    │   ├── Malinau_RIL03_landscape.log
    │   ├── Malinau_RIL03_soil.log
    │   ├── Malinau_RIL04_climate.log
    │   ├── Malinau_RIL04_landscape.log
    │   ├── Malinau_RIL04_soil.log
    │   ├── Malinau_RIL05_climate.log
    │   ├── Malinau_RIL05_landscape.log
    │   ├── Malinau_RIL05_soil.log
    │   ├── Malinau_RIL06_climate.log
    │   ├── Malinau_RIL06_landscape.log
    │   ├── Malinau_RIL06_soil.log
    │   ├── Malinau_RIL07_climate.log
    │   ├── Malinau_RIL07_landscape.log
    │   ├── Malinau_RIL07_soil.log
    │   ├── Malinau_RIL08_climate.log
    │   ├── Malinau_RIL08_landscape.log
    │   ├── Malinau_RIL08_soil.log
    │   ├── Malinau_RIL09_climate.log
    │   ├── Malinau_RIL09_landscape.log
    │   ├── Malinau_RIL09_soil.log
    │   ├── Malinau_RIL10_climate.log
    │   ├── Malinau_RIL10_landscape.log
    │   ├── Malinau_RIL10_soil.log
    │   ├── Malinau_RIL11_climate.log
    │   ├── Malinau_RIL11_landscape.log
    │   ├── Malinau_RIL11_soil.log
    │   ├── Malinau_RIL12_climate.log
    │   ├── Malinau_RIL12_landscape.log
    │   ├── Malinau_RIL12_soil.log
    │   ├── Manare_Manare_II_climate.log
    │   ├── Manare_Manare_II_landscape.log
    │   ├── Manare_Manare_II_soil.log
    │   ├── Manare_Manare_I_climate.log
    │   ├── Manare_Manare_I_landscape.log
    │   ├── Manare_Manare_I_soil.log
    │   ├── Manare_Saut_Lavilette_climate.log
    │   ├── Manare_Saut_Lavilette_landscape.log
    │   ├── Manare_Saut_Lavilette_soil.log
    │   ├── Misiones_10_climate.log
    │   ├── Misiones_10_landscape.log
    │   ├── Misiones_10_soil.log
    │   ├── Misiones_11_climate.log
    │   ├── Misiones_11_landscape.log
    │   ├── Misiones_11_soil.log
    │   ├── Misiones_12_climate.log
    │   ├── Misiones_12_landscape.log
    │   ├── Misiones_12_soil.log
    │   ├── Misiones_13_climate.log
    │   ├── Misiones_13_landscape.log
    │   ├── Misiones_13_soil.log
    │   ├── Misiones_14_climate.log
    │   ├── Misiones_14_landscape.log
    │   ├── Misiones_14_soil.log
    │   ├── Misiones_16_climate.log
    │   ├── Misiones_16_landscape.log
    │   ├── Misiones_16_soil.log
    │   ├── Misiones_19_climate.log
    │   ├── Misiones_19_landscape.log
    │   ├── Misiones_19_soil.log
    │   ├── Misiones_1_climate.log
    │   ├── Misiones_1_landscape.log
    │   ├── Misiones_1_soil.log
    │   ├── Misiones_20_climate.log
    │   ├── Misiones_20_landscape.log
    │   ├── Misiones_20_soil.log
    │   ├── Misiones_21_climate.log
    │   ├── Misiones_21_landscape.log
    │   ├── Misiones_21_soil.log
    │   ├── Misiones_2_climate.log
    │   ├── Misiones_2_landscape.log
    │   ├── Misiones_2_soil.log
    │   ├── Misiones_3_climate.log
    │   ├── Misiones_3_landscape.log
    │   ├── Misiones_3_soil.log
    │   ├── Misiones_4_climate.log
    │   ├── Misiones_4_landscape.log
    │   ├── Misiones_4_soil.log
    │   ├── Misiones_5_climate.log
    │   ├── Misiones_5_landscape.log
    │   ├── Misiones_5_soil.log
    │   ├── Misiones_6_climate.log
    │   ├── Misiones_6_landscape.log
    │   ├── Misiones_6_soil.log
    │   ├── Misiones_7_climate.log
    │   ├── Misiones_7_landscape.log
    │   ├── Misiones_7_soil.log
    │   ├── Misiones_8_climate.log
    │   ├── Misiones_8_landscape.log
    │   ├── Misiones_8_soil.log
    │   ├── Misiones_9_climate.log
    │   ├── Misiones_9_landscape.log
    │   ├── Misiones_9_soil.log
    │   ├── Moju_10_climate.log
    │   ├── Moju_10_landscape.log
    │   ├── Moju_10_soil.log
    │   ├── Moju_11_climate.log
    │   ├── Moju_11_landscape.log
    │   ├── Moju_11_soil.log
    │   ├── Moju_12_climate.log
    │   ├── Moju_12_landscape.log
    │   ├── Moju_12_soil.log
    │   ├── Moju_13_climate.log
    │   ├── Moju_13_landscape.log
    │   ├── Moju_13_soil.log
    │   ├── Moju_14_climate.log
    │   ├── Moju_14_landscape.log
    │   ├── Moju_14_soil.log
    │   ├── Moju_15_climate.log
    │   ├── Moju_15_landscape.log
    │   ├── Moju_15_soil.log
    │   ├── Moju_16_climate.log
    │   ├── Moju_16_landscape.log
    │   ├── Moju_16_soil.log
    │   ├── Moju_17_climate.log
    │   ├── Moju_17_landscape.log
    │   ├── Moju_17_soil.log
    │   ├── Moju_18_climate.log
    │   ├── Moju_18_landscape.log
    │   ├── Moju_18_soil.log
    │   ├── Moju_19_climate.log
    │   ├── Moju_19_landscape.log
    │   ├── Moju_19_soil.log
    │   ├── Moju_1_climate.log
    │   ├── Moju_1_landscape.log
    │   ├── Moju_1_soil.log
    │   ├── Moju_20_climate.log
    │   ├── Moju_20_landscape.log
    │   ├── Moju_20_soil.log
    │   ├── Moju_21_climate.log
    │   ├── Moju_21_landscape.log
    │   ├── Moju_21_soil.log
    │   ├── Moju_22_climate.log
    │   ├── Moju_22_landscape.log
    │   ├── Moju_22_soil.log
    │   ├── Moju_2_climate.log
    │   ├── Moju_2_landscape.log
    │   ├── Moju_2_soil.log
    │   ├── Moju_3_climate.log
    │   ├── Moju_3_landscape.log
    │   ├── Moju_3_soil.log
    │   ├── Moju_4_climate.log
    │   ├── Moju_4_landscape.log
    │   ├── Moju_4_soil.log
    │   ├── Moju_5_climate.log
    │   ├── Moju_5_landscape.log
    │   ├── Moju_5_soil.log
    │   ├── Moju_6_climate.log
    │   ├── Moju_6_landscape.log
    │   ├── Moju_6_soil.log
    │   ├── Moju_7_climate.log
    │   ├── Moju_7_landscape.log
    │   ├── Moju_7_soil.log
    │   ├── Moju_8_climate.log
    │   ├── Moju_8_landscape.log
    │   ├── Moju_8_soil.log
    │   ├── Moju_9_climate.log
    │   ├── Moju_9_landscape.log
    │   ├── Moju_9_soil.log
    │   ├── Montagne_tortue_P17_exploitee_1_climate.log
    │   ├── Montagne_tortue_P17_exploitee_1_landscape.log
    │   ├── Montagne_tortue_P17_exploitee_1_soil.log
    │   ├── Montagne_tortue_P17_exploitee_2_climate.log
    │   ├── Montagne_tortue_P17_exploitee_2_landscape.log
    │   ├── Montagne_tortue_P17_exploitee_2_soil.log
    │   ├── Montagne_tortue_P17_temoin_climate.log
    │   ├── Montagne_tortue_P17_temoin_landscape.log
    │   ├── Montagne_tortue_P17_temoin_soil.log
    │   ├── Paracou_10_climate.log
    │   ├── Paracou_10_landscape.log
    │   ├── Paracou_10_soil.log
    │   ├── Paracou_11_climate.log
    │   ├── Paracou_11_landscape.log
    │   ├── Paracou_11_soil.log
    │   ├── Paracou_12_climate.log
    │   ├── Paracou_12_landscape.log
    │   ├── Paracou_12_soil.log
    │   ├── Paracou_13_climate.log
    │   ├── Paracou_13_landscape.log
    │   ├── Paracou_13_soil.log
    │   ├── Paracou_14_climate.log
    │   ├── Paracou_14_landscape.log
    │   ├── Paracou_14_soil.log
    │   ├── Paracou_15_climate.log
    │   ├── Paracou_15_landscape.log
    │   ├── Paracou_15_soil.log
    │   ├── Paracou_1_climate.log
    │   ├── Paracou_1_landscape.log
    │   ├── Paracou_1_soil.log
    │   ├── Paracou_2_climate.log
    │   ├── Paracou_2_landscape.log
    │   ├── Paracou_2_soil.log
    │   ├── Paracou_3_climate.log
    │   ├── Paracou_3_landscape.log
    │   ├── Paracou_3_soil.log
    │   ├── Paracou_4_climate.log
    │   ├── Paracou_4_landscape.log
    │   ├── Paracou_4_soil.log
    │   ├── Paracou_5_climate.log
    │   ├── Paracou_5_landscape.log
    │   ├── Paracou_5_soil.log
    │   ├── Paracou_6_climate.log
    │   ├── Paracou_6_landscape.log
    │   ├── Paracou_6_soil.log
    │   ├── Paracou_7_climate.log
    │   ├── Paracou_7_landscape.log
    │   ├── Paracou_7_soil.log
    │   ├── Paracou_8_climate.log
    │   ├── Paracou_8_landscape.log
    │   ├── Paracou_8_soil.log
    │   ├── Paracou_9_climate.log
    │   ├── Paracou_9_landscape.log
    │   ├── Paracou_9_soil.log
    │   ├── Peteco_10_climate.log
    │   ├── Peteco_10_landscape.log
    │   ├── Peteco_10_soil.log
    │   ├── Peteco_11_climate.log
    │   ├── Peteco_11_landscape.log
    │   ├── Peteco_11_soil.log
    │   ├── Peteco_12_climate.log
    │   ├── Peteco_12_landscape.log
    │   ├── Peteco_12_soil.log
    │   ├── Peteco_13_climate.log
    │   ├── Peteco_13_landscape.log
    │   ├── Peteco_13_soil.log
    │   ├── Peteco_14_climate.log
    │   ├── Peteco_14_landscape.log
    │   ├── Peteco_14_soil.log
    │   ├── Peteco_15_climate.log
    │   ├── Peteco_15_landscape.log
    │   ├── Peteco_15_soil.log
    │   ├── Peteco_16_climate.log
    │   ├── Peteco_16_landscape.log
    │   ├── Peteco_16_soil.log
    │   ├── Peteco_17_climate.log
    │   ├── Peteco_17_landscape.log
    │   ├── Peteco_17_soil.log
    │   ├── Peteco_18_climate.log
    │   ├── Peteco_18_landscape.log
    │   ├── Peteco_18_soil.log
    │   ├── Peteco_1_climate.log
    │   ├── Peteco_1_landscape.log
    │   ├── Peteco_1_soil.log
    │   ├── Peteco_20_climate.log
    │   ├── Peteco_20_landscape.log
    │   ├── Peteco_20_soil.log
    │   ├── Peteco_21_climate.log
    │   ├── Peteco_21_landscape.log
    │   ├── Peteco_21_soil.log
    │   ├── Peteco_22_climate.log
    │   ├── Peteco_22_landscape.log
    │   ├── Peteco_22_soil.log
    │   ├── Peteco_23_climate.log
    │   ├── Peteco_23_landscape.log
    │   ├── Peteco_23_soil.log
    │   ├── Peteco_24_climate.log
    │   ├── Peteco_24_landscape.log
    │   ├── Peteco_24_soil.log
    │   ├── Peteco_25_climate.log
    │   ├── Peteco_25_landscape.log
    │   ├── Peteco_25_soil.log
    │   ├── Peteco_26_climate.log
    │   ├── Peteco_26_landscape.log
    │   ├── Peteco_26_soil.log
    │   ├── Peteco_27_climate.log
    │   ├── Peteco_27_landscape.log
    │   ├── Peteco_27_soil.log
    │   ├── Peteco_28_climate.log
    │   ├── Peteco_28_landscape.log
    │   ├── Peteco_28_soil.log
    │   ├── Peteco_29_climate.log
    │   ├── Peteco_29_landscape.log
    │   ├── Peteco_29_soil.log
    │   ├── Peteco_2_climate.log
    │   ├── Peteco_2_landscape.log
    │   ├── Peteco_2_soil.log
    │   ├── Peteco_30_climate.log
    │   ├── Peteco_30_landscape.log
    │   ├── Peteco_30_soil.log
    │   ├── Peteco_31_climate.log
    │   ├── Peteco_31_landscape.log
    │   ├── Peteco_31_soil.log
    │   ├── Peteco_32_climate.log
    │   ├── Peteco_32_landscape.log
    │   ├── Peteco_32_soil.log
    │   ├── Peteco_33_climate.log
    │   ├── Peteco_33_landscape.log
    │   ├── Peteco_33_soil.log
    │   ├── Peteco_34_climate.log
    │   ├── Peteco_34_landscape.log
    │   ├── Peteco_34_soil.log
    │   ├── Peteco_35_climate.log
    │   ├── Peteco_35_landscape.log
    │   ├── Peteco_35_soil.log
    │   ├── Peteco_36_climate.log
    │   ├── Peteco_36_landscape.log
    │   ├── Peteco_36_soil.log
    │   ├── Peteco_3_climate.log
    │   ├── Peteco_3_landscape.log
    │   ├── Peteco_3_soil.log
    │   ├── Peteco_4_climate.log
    │   ├── Peteco_4_landscape.log
    │   ├── Peteco_4_soil.log
    │   ├── Peteco_5_climate.log
    │   ├── Peteco_5_landscape.log
    │   ├── Peteco_5_soil.log
    │   ├── Peteco_6_climate.log
    │   ├── Peteco_6_landscape.log
    │   ├── Peteco_6_soil.log
    │   ├── Peteco_7_climate.log
    │   ├── Peteco_7_landscape.log
    │   ├── Peteco_7_soil.log
    │   ├── Peteco_8_climate.log
    │   ├── Peteco_8_landscape.log
    │   ├── Peteco_8_soil.log
    │   ├── Peteco_9_climate.log
    │   ├── Peteco_9_landscape.log
    │   ├── Peteco_9_soil.log
    │   ├── Sungai Lalang_13_climate.log
    │   ├── Sungai Lalang_13_landscape.log
    │   ├── Sungai Lalang_13_soil.log
    │   ├── Sungai Lalang_14_climate.log
    │   ├── Sungai Lalang_14_landscape.log
    │   ├── Sungai Lalang_14_soil.log
    │   ├── Sungai Lalang_15_climate.log
    │   ├── Sungai Lalang_15_landscape.log
    │   ├── Sungai Lalang_15_soil.log
    │   ├── Sungai Lalang_16_climate.log
    │   ├── Sungai Lalang_16_landscape.log
    │   ├── Sungai Lalang_16_soil.log
    │   ├── Sungai Lalang_17_climate.log
    │   ├── Sungai Lalang_17_landscape.log
    │   ├── Sungai Lalang_17_soil.log
    │   ├── Sungai Lalang_18_climate.log
    │   ├── Sungai Lalang_18_landscape.log
    │   ├── Sungai Lalang_18_soil.log
    │   ├── Sungai Lalang_19_climate.log
    │   ├── Sungai Lalang_19_landscape.log
    │   ├── Sungai Lalang_19_soil.log
    │   ├── Sungai Lalang_20_climate.log
    │   ├── Sungai Lalang_20_landscape.log
    │   ├── Sungai Lalang_20_soil.log
    │   ├── Sungai Lalang_21_climate.log
    │   ├── Sungai Lalang_21_landscape.log
    │   ├── Sungai Lalang_21_soil.log
    │   ├── Tapajos km 114_101_climate.log
    │   ├── Tapajos km 114_101_landscape.log
    │   ├── Tapajos km 114_101_soil.log
    │   ├── Tapajos km 114_102_climate.log
    │   ├── Tapajos km 114_102_landscape.log
    │   ├── Tapajos km 114_102_soil.log
    │   ├── Tapajos km 114_103_climate.log
    │   ├── Tapajos km 114_103_landscape.log
    │   ├── Tapajos km 114_103_soil.log
    │   ├── Tapajos km 114_104_climate.log
    │   ├── Tapajos km 114_104_landscape.log
    │   ├── Tapajos km 114_104_soil.log
    │   ├── Tapajos km 114_105_climate.log
    │   ├── Tapajos km 114_105_landscape.log
    │   ├── Tapajos km 114_105_soil.log
    │   ├── Tapajos km 114_106_climate.log
    │   ├── Tapajos km 114_106_landscape.log
    │   ├── Tapajos km 114_106_soil.log
    │   ├── Tapajos km 114_107_climate.log
    │   ├── Tapajos km 114_107_landscape.log
    │   ├── Tapajos km 114_107_soil.log
    │   ├── Tapajos km 114_108_climate.log
    │   ├── Tapajos km 114_108_landscape.log
    │   ├── Tapajos km 114_108_soil.log
    │   ├── Tapajos km 114_109_climate.log
    │   ├── Tapajos km 114_109_landscape.log
    │   ├── Tapajos km 114_109_soil.log
    │   ├── Tapajos km 114_110_climate.log
    │   ├── Tapajos km 114_110_landscape.log
    │   ├── Tapajos km 114_110_soil.log
    │   ├── Tapajos km 114_111_climate.log
    │   ├── Tapajos km 114_111_landscape.log
    │   ├── Tapajos km 114_111_soil.log
    │   ├── Tapajos km 114_112_climate.log
    │   ├── Tapajos km 114_112_landscape.log
    │   ├── Tapajos km 114_112_soil.log
    │   ├── Tapajos km 114_201_climate.log
    │   ├── Tapajos km 114_201_landscape.log
    │   ├── Tapajos km 114_201_soil.log
    │   ├── Tapajos km 114_202_climate.log
    │   ├── Tapajos km 114_202_landscape.log
    │   ├── Tapajos km 114_202_soil.log
    │   ├── Tapajos km 114_203_climate.log
    │   ├── Tapajos km 114_203_landscape.log
    │   ├── Tapajos km 114_203_soil.log
    │   ├── Tapajos km 114_204_climate.log
    │   ├── Tapajos km 114_204_landscape.log
    │   ├── Tapajos km 114_204_soil.log
    │   ├── Tapajos km 114_205_climate.log
    │   ├── Tapajos km 114_205_landscape.log
    │   ├── Tapajos km 114_205_soil.log
    │   ├── Tapajos km 114_206_climate.log
    │   ├── Tapajos km 114_206_landscape.log
    │   ├── Tapajos km 114_206_soil.log
    │   ├── Tapajos km 114_207_climate.log
    │   ├── Tapajos km 114_207_landscape.log
    │   ├── Tapajos km 114_207_soil.log
    │   ├── Tapajos km 114_208_climate.log
    │   ├── Tapajos km 114_208_landscape.log
    │   ├── Tapajos km 114_208_soil.log
    │   ├── Tapajos km 114_209_climate.log
    │   ├── Tapajos km 114_209_landscape.log
    │   ├── Tapajos km 114_209_soil.log
    │   ├── Tapajos km 114_210_climate.log
    │   ├── Tapajos km 114_210_landscape.log
    │   ├── Tapajos km 114_210_soil.log
    │   ├── Tapajos km 114_211_climate.log
    │   ├── Tapajos km 114_211_landscape.log
    │   ├── Tapajos km 114_211_soil.log
    │   ├── Tapajos km 114_212_climate.log
    │   ├── Tapajos km 114_212_landscape.log
    │   ├── Tapajos km 114_212_soil.log
    │   ├── Tapajos km 114_301_climate.log
    │   ├── Tapajos km 114_301_landscape.log
    │   ├── Tapajos km 114_301_soil.log
    │   ├── Tapajos km 114_302_climate.log
    │   ├── Tapajos km 114_302_landscape.log
    │   ├── Tapajos km 114_302_soil.log
    │   ├── Tapajos km 114_303_climate.log
    │   ├── Tapajos km 114_303_landscape.log
    │   ├── Tapajos km 114_303_soil.log
    │   ├── Tapajos km 114_304_climate.log
    │   ├── Tapajos km 114_304_landscape.log
    │   ├── Tapajos km 114_304_soil.log
    │   ├── Tapajos km 114_305_climate.log
    │   ├── Tapajos km 114_305_landscape.log
    │   ├── Tapajos km 114_305_soil.log
    │   ├── Tapajos km 114_306_climate.log
    │   ├── Tapajos km 114_306_landscape.log
    │   ├── Tapajos km 114_306_soil.log
    │   ├── Tapajos km 114_307_climate.log
    │   ├── Tapajos km 114_307_landscape.log
    │   ├── Tapajos km 114_307_soil.log
    │   ├── Tapajos km 114_308_climate.log
    │   ├── Tapajos km 114_308_landscape.log
    │   ├── Tapajos km 114_308_soil.log
    │   ├── Tapajos km 114_309_climate.log
    │   ├── Tapajos km 114_309_landscape.log
    │   ├── Tapajos km 114_309_soil.log
    │   ├── Tapajos km 114_310_climate.log
    │   ├── Tapajos km 114_310_landscape.log
    │   ├── Tapajos km 114_310_soil.log
    │   ├── Tapajos km 114_311_climate.log
    │   ├── Tapajos km 114_311_landscape.log
    │   ├── Tapajos km 114_311_soil.log
    │   ├── Tapajos km 114_312_climate.log
    │   ├── Tapajos km 114_312_landscape.log
    │   ├── Tapajos km 114_312_soil.log
    │   ├── Tapajos km 114_401_climate.log
    │   ├── Tapajos km 114_401_landscape.log
    │   ├── Tapajos km 114_401_soil.log
    │   ├── Tapajos km 114_402_climate.log
    │   ├── Tapajos km 114_402_landscape.log
    │   ├── Tapajos km 114_402_soil.log
    │   ├── Tapajos km 114_403_climate.log
    │   ├── Tapajos km 114_403_landscape.log
    │   ├── Tapajos km 114_403_soil.log
    │   ├── Tapajos km 114_404_climate.log
    │   ├── Tapajos km 114_404_landscape.log
    │   ├── Tapajos km 114_404_soil.log
    │   ├── Tapajos km 114_405_climate.log
    │   ├── Tapajos km 114_405_landscape.log
    │   ├── Tapajos km 114_405_soil.log
    │   ├── Tapajos km 114_406_climate.log
    │   ├── Tapajos km 114_406_landscape.log
    │   ├── Tapajos km 114_406_soil.log
    │   ├── Tapajos km 114_407_climate.log
    │   ├── Tapajos km 114_407_landscape.log
    │   ├── Tapajos km 114_407_soil.log
    │   ├── Tapajos km 114_408_climate.log
    │   ├── Tapajos km 114_408_landscape.log
    │   ├── Tapajos km 114_408_soil.log
    │   ├── Tapajos km 114_409_climate.log
    │   ├── Tapajos km 114_409_landscape.log
    │   ├── Tapajos km 114_409_soil.log
    │   ├── Tapajos km 114_410_climate.log
    │   ├── Tapajos km 114_410_landscape.log
    │   ├── Tapajos km 114_410_soil.log
    │   ├── Tapajos km 114_411_climate.log
    │   ├── Tapajos km 114_411_landscape.log
    │   ├── Tapajos km 114_411_soil.log
    │   ├── Tapajos km 114_412_climate.log
    │   ├── Tapajos km 114_412_landscape.log
    │   ├── Tapajos km 114_412_soil.log
    │   ├── Tapajos km 114_501_climate.log
    │   ├── Tapajos km 114_501_landscape.log
    │   ├── Tapajos km 114_501_soil.log
    │   ├── Tapajos km 114_502_climate.log
    │   ├── Tapajos km 114_502_landscape.log
    │   ├── Tapajos km 114_502_soil.log
    │   ├── Tapajos km 114_503_climate.log
    │   ├── Tapajos km 114_503_landscape.log
    │   ├── Tapajos km 114_503_soil.log
    │   ├── Tapajos km 114_504_climate.log
    │   ├── Tapajos km 114_504_landscape.log
    │   ├── Tapajos km 114_504_soil.log
    │   ├── Tapajos km 114_505_climate.log
    │   ├── Tapajos km 114_505_landscape.log
    │   ├── Tapajos km 114_505_soil.log
    │   ├── Tapajos km 114_506_climate.log
    │   ├── Tapajos km 114_506_landscape.log
    │   ├── Tapajos km 114_506_soil.log
    │   ├── Tapajos km 114_507_climate.log
    │   ├── Tapajos km 114_507_landscape.log
    │   ├── Tapajos km 114_507_soil.log
    │   ├── Tapajos km 114_508_climate.log
    │   ├── Tapajos km 114_508_landscape.log
    │   ├── Tapajos km 114_508_soil.log
    │   ├── Tapajos km 114_509_climate.log
    │   ├── Tapajos km 114_509_landscape.log
    │   ├── Tapajos km 114_509_soil.log
    │   ├── Tapajos km 114_510_climate.log
    │   ├── Tapajos km 114_510_landscape.log
    │   ├── Tapajos km 114_510_soil.log
    │   ├── Tapajos km 114_511_climate.log
    │   ├── Tapajos km 114_511_landscape.log
    │   ├── Tapajos km 114_511_soil.log
    │   ├── Tapajos km 114_512_climate.log
    │   ├── Tapajos km 114_512_landscape.log
    │   ├── Tapajos km 114_512_soil.log
    │   ├── Tapajós km 67_01E_climate.log
    │   ├── Tapajós km 67_01E_landscape.log
    │   ├── Tapajós km 67_01E_soil.log
    │   ├── Tapajós km 67_01T_climate.log
    │   ├── Tapajós km 67_01T_landscape.log
    │   ├── Tapajós km 67_01T_soil.log
    │   ├── Tapajós km 67_02E_climate.log
    │   ├── Tapajós km 67_02E_landscape.log
    │   ├── Tapajós km 67_02E_soil.log
    │   ├── Tapajós km 67_02T_climate.log
    │   ├── Tapajós km 67_02T_landscape.log
    │   ├── Tapajós km 67_02T_soil.log
    │   ├── Tapajós km 67_03E_climate.log
    │   ├── Tapajós km 67_03E_landscape.log
    │   ├── Tapajós km 67_03E_soil.log
    │   ├── Tapajós km 67_03T_climate.log
    │   ├── Tapajós km 67_03T_landscape.log
    │   ├── Tapajós km 67_03T_soil.log
    │   ├── Tapajós km 67_04E_climate.log
    │   ├── Tapajós km 67_04E_landscape.log
    │   ├── Tapajós km 67_04E_soil.log
    │   ├── Tapajós km 67_04T_climate.log
    │   ├── Tapajós km 67_04T_landscape.log
    │   ├── Tapajós km 67_04T_soil.log
    │   ├── Tapajós km 67_05E_climate.log
    │   ├── Tapajós km 67_05E_landscape.log
    │   ├── Tapajós km 67_05E_soil.log
    │   ├── Tapajós km 67_05T_climate.log
    │   ├── Tapajós km 67_05T_landscape.log
    │   ├── Tapajós km 67_05T_soil.log
    │   ├── Tapajós km 67_06E_climate.log
    │   ├── Tapajós km 67_06E_landscape.log
    │   ├── Tapajós km 67_06E_soil.log
    │   ├── Tapajós km 67_06T_climate.log
    │   ├── Tapajós km 67_06T_landscape.log
    │   ├── Tapajós km 67_06T_soil.log
    │   ├── Tapajós km 67_07E_climate.log
    │   ├── Tapajós km 67_07E_landscape.log
    │   ├── Tapajós km 67_07E_soil.log
    │   ├── Tapajós km 67_07T_climate.log
    │   ├── Tapajós km 67_07T_landscape.log
    │   ├── Tapajós km 67_07T_soil.log
    │   ├── Tapajós km 67_08E_climate.log
    │   ├── Tapajós km 67_08E_landscape.log
    │   ├── Tapajós km 67_08E_soil.log
    │   ├── Tapajós km 67_08T_climate.log
    │   ├── Tapajós km 67_08T_landscape.log
    │   ├── Tapajós km 67_08T_soil.log
    │   ├── Tapajós km 67_09E_climate.log
    │   ├── Tapajós km 67_09E_landscape.log
    │   ├── Tapajós km 67_09E_soil.log
    │   ├── Tapajós km 67_09T_climate.log
    │   ├── Tapajós km 67_09T_landscape.log
    │   ├── Tapajós km 67_09T_soil.log
    │   ├── Tapajós km 67_10E_climate.log
    │   ├── Tapajós km 67_10E_landscape.log
    │   ├── Tapajós km 67_10E_soil.log
    │   ├── Tapajós km 67_10T_climate.log
    │   ├── Tapajós km 67_10T_landscape.log
    │   ├── Tapajós km 67_10T_soil.log
    │   ├── Tapajós km 67_11E_climate.log
    │   ├── Tapajós km 67_11E_landscape.log
    │   ├── Tapajós km 67_11E_soil.log
    │   ├── Tapajós km 67_11T_climate.log
    │   ├── Tapajós km 67_11T_landscape.log
    │   ├── Tapajós km 67_11T_soil.log
    │   ├── Tapajós km 67_12E_climate.log
    │   ├── Tapajós km 67_12E_landscape.log
    │   ├── Tapajós km 67_12E_soil.log
    │   ├── Tapajós km 67_12T_climate.log
    │   ├── Tapajós km 67_12T_landscape.log
    │   ├── Tapajós km 67_12T_soil.log
    │   ├── Tapajós km 67_13E_climate.log
    │   ├── Tapajós km 67_13E_landscape.log
    │   ├── Tapajós km 67_13E_soil.log
    │   ├── Tapajós km 67_13T_climate.log
    │   ├── Tapajós km 67_13T_landscape.log
    │   ├── Tapajós km 67_13T_soil.log
    │   ├── Tapajós km 67_14E_climate.log
    │   ├── Tapajós km 67_14E_landscape.log
    │   ├── Tapajós km 67_14E_soil.log
    │   ├── Tapajós km 67_14T_climate.log
    │   ├── Tapajós km 67_14T_landscape.log
    │   ├── Tapajós km 67_14T_soil.log
    │   ├── Tapajós km 67_15E_climate.log
    │   ├── Tapajós km 67_15E_landscape.log
    │   ├── Tapajós km 67_15E_soil.log
    │   ├── Tapajós km 67_15T_climate.log
    │   ├── Tapajós km 67_15T_landscape.log
    │   ├── Tapajós km 67_15T_soil.log
    │   ├── Tapajós km 67_16E_climate.log
    │   ├── Tapajós km 67_16E_landscape.log
    │   ├── Tapajós km 67_16E_soil.log
    │   ├── Tapajós km 67_16T_climate.log
    │   ├── Tapajós km 67_16T_landscape.log
    │   ├── Tapajós km 67_16T_soil.log
    │   ├── Tapajós km 67_17E_climate.log
    │   ├── Tapajós km 67_17E_landscape.log
    │   ├── Tapajós km 67_17E_soil.log
    │   ├── Tapajós km 67_17T_climate.log
    │   ├── Tapajós km 67_17T_landscape.log
    │   ├── Tapajós km 67_17T_soil.log
    │   ├── Tapajós km 67_18E_climate.log
    │   ├── Tapajós km 67_18E_landscape.log
    │   ├── Tapajós km 67_18E_soil.log
    │   ├── Tapajós km 67_18T_climate.log
    │   ├── Tapajós km 67_18T_landscape.log
    │   ├── Tapajós km 67_18T_soil.log
    │   ├── Tapajós km 67_19E_climate.log
    │   ├── Tapajós km 67_19E_landscape.log
    │   ├── Tapajós km 67_19E_soil.log
    │   ├── Tapajós km 67_20E_climate.log
    │   ├── Tapajós km 67_20E_landscape.log
    │   ├── Tapajós km 67_20E_soil.log
    │   ├── Tapajós km 67_21E_climate.log
    │   ├── Tapajós km 67_21E_landscape.log
    │   ├── Tapajós km 67_21E_soil.log
    │   ├── Tapajós km 67_22E_climate.log
    │   ├── Tapajós km 67_22E_landscape.log
    │   ├── Tapajós km 67_22E_soil.log
    │   ├── Tapajós km 67_23E_climate.log
    │   ├── Tapajós km 67_23E_landscape.log
    │   ├── Tapajós km 67_23E_soil.log
    │   ├── Tapajós km 67_24E_climate.log
    │   ├── Tapajós km 67_24E_landscape.log
    │   ├── Tapajós km 67_24E_soil.log
    │   ├── Tapajós km 67_25E_climate.log
    │   ├── Tapajós km 67_25E_landscape.log
    │   ├── Tapajós km 67_25E_soil.log
    │   ├── Tapajós km 67_26E_climate.log
    │   ├── Tapajós km 67_26E_landscape.log
    │   ├── Tapajós km 67_26E_soil.log
    │   ├── Tapajós km 67_27E_climate.log
    │   ├── Tapajós km 67_27E_landscape.log
    │   ├── Tapajós km 67_27E_soil.log
    │   ├── Tapajós km 67_28E_climate.log
    │   ├── Tapajós km 67_28E_landscape.log
    │   ├── Tapajós km 67_28E_soil.log
    │   ├── Tapajós km 67_29E_climate.log
    │   ├── Tapajós km 67_29E_landscape.log
    │   ├── Tapajós km 67_29E_soil.log
    │   ├── Tapajós km 67_30E_climate.log
    │   ├── Tapajós km 67_30E_landscape.log
    │   ├── Tapajós km 67_30E_soil.log
    │   ├── Tapajós km 67_31E_climate.log
    │   ├── Tapajós km 67_31E_landscape.log
    │   ├── Tapajós km 67_31E_soil.log
    │   ├── Tapajós km 67_32E_climate.log
    │   ├── Tapajós km 67_32E_landscape.log
    │   ├── Tapajós km 67_32E_soil.log
    │   ├── Tapajós km 67_33E_climate.log
    │   ├── Tapajós km 67_33E_landscape.log
    │   ├── Tapajós km 67_33E_soil.log
    │   ├── Tapajós km 67_34E_climate.log
    │   ├── Tapajós km 67_34E_landscape.log
    │   ├── Tapajós km 67_34E_soil.log
    │   ├── Tapajós km 67_35E_climate.log
    │   ├── Tapajós km 67_35E_landscape.log
    │   ├── Tapajós km 67_35E_soil.log
    │   ├── Tapajós km 67_36E_climate.log
    │   ├── Tapajós km 67_36E_landscape.log
    │   ├── Tapajós km 67_36E_soil.log
    │   ├── Tene_Subplot_10_climate.log
    │   ├── Tene_Subplot_10_landscape.log
    │   ├── Tene_Subplot_10_soil.log
    │   ├── Tene_Subplot_11_climate.log
    │   ├── Tene_Subplot_11_landscape.log
    │   ├── Tene_Subplot_11_soil.log
    │   ├── Tene_Subplot_12_climate.log
    │   ├── Tene_Subplot_12_landscape.log
    │   ├── Tene_Subplot_12_soil.log
    │   ├── Tene_Subplot_13_climate.log
    │   ├── Tene_Subplot_13_landscape.log
    │   ├── Tene_Subplot_13_soil.log
    │   ├── Tene_Subplot_14_climate.log
    │   ├── Tene_Subplot_14_landscape.log
    │   ├── Tene_Subplot_14_soil.log
    │   ├── Tene_Subplot_15_climate.log
    │   ├── Tene_Subplot_15_landscape.log
    │   ├── Tene_Subplot_15_soil.log
    │   ├── Tene_Subplot_16_climate.log
    │   ├── Tene_Subplot_16_landscape.log
    │   ├── Tene_Subplot_16_soil.log
    │   ├── Tene_Subplot_17_climate.log
    │   ├── Tene_Subplot_17_landscape.log
    │   ├── Tene_Subplot_17_soil.log
    │   ├── Tene_Subplot_18_climate.log
    │   ├── Tene_Subplot_18_landscape.log
    │   ├── Tene_Subplot_18_soil.log
    │   ├── Tene_Subplot_19_climate.log
    │   ├── Tene_Subplot_19_landscape.log
    │   ├── Tene_Subplot_19_soil.log
    │   ├── Tene_Subplot_1_climate.log
    │   ├── Tene_Subplot_1_landscape.log
    │   ├── Tene_Subplot_1_soil.log
    │   ├── Tene_Subplot_20_climate.log
    │   ├── Tene_Subplot_20_landscape.log
    │   ├── Tene_Subplot_20_soil.log
    │   ├── Tene_Subplot_21_climate.log
    │   ├── Tene_Subplot_21_landscape.log
    │   ├── Tene_Subplot_21_soil.log
    │   ├── Tene_Subplot_22_climate.log
    │   ├── Tene_Subplot_22_landscape.log
    │   ├── Tene_Subplot_22_soil.log
    │   ├── Tene_Subplot_23_climate.log
    │   ├── Tene_Subplot_23_landscape.log
    │   ├── Tene_Subplot_23_soil.log
    │   ├── Tene_Subplot_24_climate.log
    │   ├── Tene_Subplot_24_landscape.log
    │   ├── Tene_Subplot_24_soil.log
    │   ├── Tene_Subplot_25_climate.log
    │   ├── Tene_Subplot_25_landscape.log
    │   ├── Tene_Subplot_25_soil.log
    │   ├── Tene_Subplot_2_climate.log
    │   ├── Tene_Subplot_2_landscape.log
    │   ├── Tene_Subplot_2_soil.log
    │   ├── Tene_Subplot_3_climate.log
    │   ├── Tene_Subplot_3_landscape.log
    │   ├── Tene_Subplot_3_soil.log
    │   ├── Tene_Subplot_4_climate.log
    │   ├── Tene_Subplot_4_landscape.log
    │   ├── Tene_Subplot_4_soil.log
    │   ├── Tene_Subplot_5_climate.log
    │   ├── Tene_Subplot_5_landscape.log
    │   ├── Tene_Subplot_5_soil.log
    │   ├── Tene_Subplot_6_climate.log
    │   ├── Tene_Subplot_6_landscape.log
    │   ├── Tene_Subplot_6_soil.log
    │   ├── Tene_Subplot_7_climate.log
    │   ├── Tene_Subplot_7_landscape.log
    │   ├── Tene_Subplot_7_soil.log
    │   ├── Tene_Subplot_8_climate.log
    │   ├── Tene_Subplot_8_landscape.log
    │   ├── Tene_Subplot_8_soil.log
    │   ├── Tene_Subplot_9_climate.log
    │   ├── Tene_Subplot_9_landscape.log
    │   ├── Tene_Subplot_9_soil.log
    │   ├── Ulu Muda_22_climate.log
    │   ├── Ulu Muda_22_landscape.log
    │   ├── Ulu Muda_22_soil.log
    │   ├── Ulu Muda_23_climate.log
    │   ├── Ulu Muda_23_landscape.log
    │   ├── Ulu Muda_23_soil.log
    │   ├── Ulu Muda_24_climate.log
    │   ├── Ulu Muda_24_landscape.log
    │   ├── Ulu Muda_24_soil.log
    │   ├── Ulu Muda_25_climate.log
    │   ├── Ulu Muda_25_landscape.log
    │   ├── Ulu Muda_25_soil.log
    │   ├── Ulu Muda_26_climate.log
    │   ├── Ulu Muda_26_landscape.log
    │   ├── Ulu Muda_26_soil.log
    │   ├── Ulu Muda_27_climate.log
    │   ├── Ulu Muda_27_landscape.log
    │   ├── Ulu Muda_27_soil.log
    │   ├── Ulu Muda_28_climate.log
    │   ├── Ulu Muda_28_landscape.log
    │   ├── Ulu Muda_28_soil.log
    │   ├── Ulu Muda_29_climate.log
    │   ├── Ulu Muda_29_landscape.log
    │   ├── Ulu Muda_29_soil.log
    │   ├── Ulu Muda_30_climate.log
    │   ├── Ulu Muda_30_landscape.log
    │   ├── Ulu Muda_30_soil.log
    │   ├── Uppangala_LP1_climate.log
    │   ├── Uppangala_LP1_landscape.log
    │   ├── Uppangala_LP1_soil.log
    │   ├── Uppangala_LP2_climate.log
    │   ├── Uppangala_LP2_landscape.log
    │   ├── Uppangala_LP2_soil.log
    │   ├── Uppangala_LP3_climate.log
    │   ├── Uppangala_LP3_landscape.log
    │   ├── Uppangala_LP3_soil.log
    │   ├── Uppangala_LP4_climate.log
    │   ├── Uppangala_LP4_landscape.log
    │   ├── Uppangala_LP4_soil.log
    │   ├── Uppangala_UP1_climate.log
    │   ├── Uppangala_UP1_landscape.log
    │   ├── Uppangala_UP1_soil.log
    │   ├── Uppangala_UP2_climate.log
    │   ├── Uppangala_UP2_landscape.log
    │   ├── Uppangala_UP2_soil.log
    │   ├── sao_nicolau_1_climate.log
    │   ├── sao_nicolau_1_landscape.log
    │   ├── sao_nicolau_1_soil.log
    │   ├── sao_nicolau_2_climate.log
    │   ├── sao_nicolau_2_landscape.log
    │   ├── sao_nicolau_2_soil.log
    │   ├── sao_nicolau_3_climate.log
    │   ├── sao_nicolau_3_landscape.log
    │   ├── sao_nicolau_3_soil.log
    │   ├── sao_nicolau_4_climate.log
    │   ├── sao_nicolau_4_landscape.log
    │   ├── sao_nicolau_4_soil.log
    │   ├── sao_nicolau_5_climate.log
    │   ├── sao_nicolau_5_landscape.log
    │   ├── sao_nicolau_5_soil.log
    │   ├── sao_nicolau_6_climate.log
    │   ├── sao_nicolau_6_landscape.log
    │   └── sao_nicolau_6_soil.log
    └── soil
        ├── BAFOG_III_soil.tsv
        ├── BAFOG_II_soil.tsv
        ├── BAFOG_IV_soil.tsv
        ├── BAFOG_I_soil.tsv
        ├── BAFOG_VII_soil.tsv
        ├── BAFOG_VI_soil.tsv
        ├── BAFOG_V_soil.tsv
        ├── Ecosilva_10_soil.tsv
        ├── Ecosilva_11_soil.tsv
        ├── Ecosilva_12_soil.tsv
        ├── Ecosilva_13_soil.tsv
        ├── Ecosilva_14_soil.tsv
        ├── Ecosilva_15_soil.tsv
        ├── Ecosilva_16_soil.tsv
        ├── Ecosilva_17_soil.tsv
        ├── Ecosilva_18_soil.tsv
        ├── Ecosilva_1_soil.tsv
        ├── Ecosilva_2_soil.tsv
        ├── Ecosilva_3_soil.tsv
        ├── Ecosilva_4_soil.tsv
        ├── Ecosilva_5_soil.tsv
        ├── Ecosilva_6_soil.tsv
        ├── Ecosilva_7_soil.tsv
        ├── Ecosilva_8_soil.tsv
        ├── Ecosilva_9_soil.tsv
        ├── Iwokrama_IWO-01_soil.tsv
        ├── Iwokrama_IWO-02_soil.tsv
        ├── Iwokrama_IWO-03_soil.tsv
        ├── Iwokrama_IWO-04_soil.tsv
        ├── Iwokrama_IWO-05_soil.tsv
        ├── Iwokrama_IWO-06_soil.tsv
        ├── Iwokrama_IWO-07_soil.tsv
        ├── Iwokrama_IWO-08_soil.tsv
        ├── Iwokrama_IWO-09_soil.tsv
        ├── Iwokrama_IWO-10_soil.tsv
        ├── Iwokrama_IWO-11_soil.tsv
        ├── Iwokrama_IWO-12_soil.tsv
        ├── Iwokrama_IWO-13_soil.tsv
        ├── Iwokrama_IWO-14_soil.tsv
        ├── Iwokrama_IWO-15_soil.tsv
        ├── Iwokrama_IWO-16_soil.tsv
        ├── Iwokrama_IWO-17_soil.tsv
        ├── Iwokrama_IWO-21_soil.tsv
        ├── Iwokrama_IWO-22_soil.tsv
        ├── Jari_101_soil.tsv
        ├── Jari_102_soil.tsv
        ├── Jari_103_soil.tsv
        ├── Jari_104_soil.tsv
        ├── Jari_105_soil.tsv
        ├── Jari_106_soil.tsv
        ├── Jari_107_soil.tsv
        ├── Jari_108_soil.tsv
        ├── Jari_109_soil.tsv
        ├── Jari_110_soil.tsv
        ├── Jari_111_soil.tsv
        ├── Jari_112_soil.tsv
        ├── Jari_1_soil.tsv
        ├── Jari_201_soil.tsv
        ├── Jari_202_soil.tsv
        ├── Jari_203_soil.tsv
        ├── Jari_204_soil.tsv
        ├── Jari_205_soil.tsv
        ├── Jari_206_soil.tsv
        ├── Jari_207_soil.tsv
        ├── Jari_208_soil.tsv
        ├── Jari_209_soil.tsv
        ├── Jari_210_soil.tsv
        ├── Jari_211_soil.tsv
        ├── Jari_212_soil.tsv
        ├── Jari_2_soil.tsv
        ├── Jari_301_soil.tsv
        ├── Jari_302_soil.tsv
        ├── Jari_303_soil.tsv
        ├── Jari_304_soil.tsv
        ├── Jari_305_soil.tsv
        ├── Jari_306_soil.tsv
        ├── Jari_307_soil.tsv
        ├── Jari_308_soil.tsv
        ├── Jari_309_soil.tsv
        ├── Jari_310_soil.tsv
        ├── Jari_311_soil.tsv
        ├── Jari_312_soil.tsv
        ├── Jari_3_soil.tsv
        ├── Jari_4_soil.tsv
        ├── Kabo_KAB-12_soil.tsv
        ├── Kabo_KAB-14_soil.tsv
        ├── Kabo_KAB-19_soil.tsv
        ├── Kabo_KAB-22_soil.tsv
        ├── Kabo_KAB-26_soil.tsv
        ├── Kabo_KAB-28_soil.tsv
        ├── Kabo_KAB-32_soil.tsv
        ├── Kabo_KAB-34_soil.tsv
        ├── Kabo_KAB-38_soil.tsv
        ├── Kabo_KAB-41_soil.tsv
        ├── Kabo_KAB-42_soil.tsv
        ├── Kabo_KAB-43_soil.tsv
        ├── Lesong_10_soil.tsv
        ├── Lesong_11_soil.tsv
        ├── Lesong_12_soil.tsv
        ├── Lesong_1_soil.tsv
        ├── Lesong_2_soil.tsv
        ├── Lesong_3_soil.tsv
        ├── Lesong_4_soil.tsv
        ├── Lesong_5_soil.tsv
        ├── Lesong_6_soil.tsv
        ├── Lesong_7_soil.tsv
        ├── Lesong_8_soil.tsv
        ├── Lesong_9_soil.tsv
        ├── Malinau_CNV01_soil.tsv
        ├── Malinau_CNV02_soil.tsv
        ├── Malinau_CNV03_soil.tsv
        ├── Malinau_CNV04_soil.tsv
        ├── Malinau_CNV05_soil.tsv
        ├── Malinau_CNV06_soil.tsv
        ├── Malinau_CNV07_soil.tsv
        ├── Malinau_CNV08_soil.tsv
        ├── Malinau_CNV09_soil.tsv
        ├── Malinau_CNV10_soil.tsv
        ├── Malinau_CNV11_soil.tsv
        ├── Malinau_CNV12_soil.tsv
        ├── Malinau_RIL01_soil.tsv
        ├── Malinau_RIL02_soil.tsv
        ├── Malinau_RIL03_soil.tsv
        ├── Malinau_RIL04_soil.tsv
        ├── Malinau_RIL05_soil.tsv
        ├── Malinau_RIL06_soil.tsv
        ├── Malinau_RIL07_soil.tsv
        ├── Malinau_RIL08_soil.tsv
        ├── Malinau_RIL09_soil.tsv
        ├── Malinau_RIL10_soil.tsv
        ├── Malinau_RIL11_soil.tsv
        ├── Malinau_RIL12_soil.tsv
        ├── Manare_Manare_II_soil.tsv
        ├── Manare_Manare_I_soil.tsv
        ├── Manare_Saut_Lavilette_soil.tsv
        ├── Misiones_10_soil.tsv
        ├── Misiones_11_soil.tsv
        ├── Misiones_12_soil.tsv
        ├── Misiones_13_soil.tsv
        ├── Misiones_14_soil.tsv
        ├── Misiones_16_soil.tsv
        ├── Misiones_19_soil.tsv
        ├── Misiones_1_soil.tsv
        ├── Misiones_20_soil.tsv
        ├── Misiones_21_soil.tsv
        ├── Misiones_2_soil.tsv
        ├── Misiones_3_soil.tsv
        ├── Misiones_4_soil.tsv
        ├── Misiones_5_soil.tsv
        ├── Misiones_6_soil.tsv
        ├── Misiones_7_soil.tsv
        ├── Misiones_8_soil.tsv
        ├── Misiones_9_soil.tsv
        ├── Moju_10_soil.tsv
        ├── Moju_11_soil.tsv
        ├── Moju_12_soil.tsv
        ├── Moju_13_soil.tsv
        ├── Moju_14_soil.tsv
        ├── Moju_15_soil.tsv
        ├── Moju_16_soil.tsv
        ├── Moju_17_soil.tsv
        ├── Moju_18_soil.tsv
        ├── Moju_19_soil.tsv
        ├── Moju_1_soil.tsv
        ├── Moju_20_soil.tsv
        ├── Moju_21_soil.tsv
        ├── Moju_22_soil.tsv
        ├── Moju_2_soil.tsv
        ├── Moju_3_soil.tsv
        ├── Moju_4_soil.tsv
        ├── Moju_5_soil.tsv
        ├── Moju_6_soil.tsv
        ├── Moju_7_soil.tsv
        ├── Moju_8_soil.tsv
        ├── Moju_9_soil.tsv
        ├── Montagne_tortue_P17_exploitee_1_soil.tsv
        ├── Montagne_tortue_P17_exploitee_2_soil.tsv
        ├── Montagne_tortue_P17_temoin_soil.tsv
        ├── Paracou_10_soil.tsv
        ├── Paracou_11_soil.tsv
        ├── Paracou_12_soil.tsv
        ├── Paracou_13_soil.tsv
        ├── Paracou_14_soil.tsv
        ├── Paracou_15_soil.tsv
        ├── Paracou_1_soil.tsv
        ├── Paracou_2_soil.tsv
        ├── Paracou_3_soil.tsv
        ├── Paracou_4_soil.tsv
        ├── Paracou_5_soil.tsv
        ├── Paracou_6_soil.tsv
        ├── Paracou_7_soil.tsv
        ├── Paracou_8_soil.tsv
        ├── Paracou_9_soil.tsv
        ├── Peteco_10_soil.tsv
        ├── Peteco_11_soil.tsv
        ├── Peteco_12_soil.tsv
        ├── Peteco_13_soil.tsv
        ├── Peteco_14_soil.tsv
        ├── Peteco_15_soil.tsv
        ├── Peteco_16_soil.tsv
        ├── Peteco_17_soil.tsv
        ├── Peteco_18_soil.tsv
        ├── Peteco_1_soil.tsv
        ├── Peteco_20_soil.tsv
        ├── Peteco_21_soil.tsv
        ├── Peteco_22_soil.tsv
        ├── Peteco_23_soil.tsv
        ├── Peteco_24_soil.tsv
        ├── Peteco_25_soil.tsv
        ├── Peteco_26_soil.tsv
        ├── Peteco_27_soil.tsv
        ├── Peteco_28_soil.tsv
        ├── Peteco_29_soil.tsv
        ├── Peteco_2_soil.tsv
        ├── Peteco_30_soil.tsv
        ├── Peteco_31_soil.tsv
        ├── Peteco_32_soil.tsv
        ├── Peteco_33_soil.tsv
        ├── Peteco_34_soil.tsv
        ├── Peteco_35_soil.tsv
        ├── Peteco_36_soil.tsv
        ├── Peteco_3_soil.tsv
        ├── Peteco_4_soil.tsv
        ├── Peteco_5_soil.tsv
        ├── Peteco_6_soil.tsv
        ├── Peteco_7_soil.tsv
        ├── Peteco_8_soil.tsv
        ├── Peteco_9_soil.tsv
        ├── Sungai Lalang_13_soil.tsv
        ├── Sungai Lalang_14_soil.tsv
        ├── Sungai Lalang_15_soil.tsv
        ├── Sungai Lalang_16_soil.tsv
        ├── Sungai Lalang_17_soil.tsv
        ├── Sungai Lalang_18_soil.tsv
        ├── Sungai Lalang_19_soil.tsv
        ├── Sungai Lalang_20_soil.tsv
        ├── Sungai Lalang_21_soil.tsv
        ├── Tapajos km 114_101_soil.tsv
        ├── Tapajos km 114_102_soil.tsv
        ├── Tapajos km 114_103_soil.tsv
        ├── Tapajos km 114_104_soil.tsv
        ├── Tapajos km 114_105_soil.tsv
        ├── Tapajos km 114_106_soil.tsv
        ├── Tapajos km 114_107_soil.tsv
        ├── Tapajos km 114_108_soil.tsv
        ├── Tapajos km 114_109_soil.tsv
        ├── Tapajos km 114_110_soil.tsv
        ├── Tapajos km 114_111_soil.tsv
        ├── Tapajos km 114_112_soil.tsv
        ├── Tapajos km 114_201_soil.tsv
        ├── Tapajos km 114_202_soil.tsv
        ├── Tapajos km 114_203_soil.tsv
        ├── Tapajos km 114_204_soil.tsv
        ├── Tapajos km 114_205_soil.tsv
        ├── Tapajos km 114_206_soil.tsv
        ├── Tapajos km 114_207_soil.tsv
        ├── Tapajos km 114_208_soil.tsv
        ├── Tapajos km 114_209_soil.tsv
        ├── Tapajos km 114_210_soil.tsv
        ├── Tapajos km 114_211_soil.tsv
        ├── Tapajos km 114_212_soil.tsv
        ├── Tapajos km 114_301_soil.tsv
        ├── Tapajos km 114_302_soil.tsv
        ├── Tapajos km 114_303_soil.tsv
        ├── Tapajos km 114_304_soil.tsv
        ├── Tapajos km 114_305_soil.tsv
        ├── Tapajos km 114_306_soil.tsv
        ├── Tapajos km 114_307_soil.tsv
        ├── Tapajos km 114_308_soil.tsv
        ├── Tapajos km 114_309_soil.tsv
        ├── Tapajos km 114_310_soil.tsv
        ├── Tapajos km 114_311_soil.tsv
        ├── Tapajos km 114_312_soil.tsv
        ├── Tapajos km 114_401_soil.tsv
        ├── Tapajos km 114_402_soil.tsv
        ├── Tapajos km 114_403_soil.tsv
        ├── Tapajos km 114_404_soil.tsv
        ├── Tapajos km 114_405_soil.tsv
        ├── Tapajos km 114_406_soil.tsv
        ├── Tapajos km 114_407_soil.tsv
        ├── Tapajos km 114_408_soil.tsv
        ├── Tapajos km 114_409_soil.tsv
        ├── Tapajos km 114_410_soil.tsv
        ├── Tapajos km 114_411_soil.tsv
        ├── Tapajos km 114_412_soil.tsv
        ├── Tapajos km 114_501_soil.tsv
        ├── Tapajos km 114_502_soil.tsv
        ├── Tapajos km 114_503_soil.tsv
        ├── Tapajos km 114_504_soil.tsv
        ├── Tapajos km 114_505_soil.tsv
        ├── Tapajos km 114_506_soil.tsv
        ├── Tapajos km 114_507_soil.tsv
        ├── Tapajos km 114_508_soil.tsv
        ├── Tapajos km 114_509_soil.tsv
        ├── Tapajos km 114_510_soil.tsv
        ├── Tapajos km 114_511_soil.tsv
        ├── Tapajos km 114_512_soil.tsv
        ├── Tapajós km 67_01E_soil.tsv
        ├── Tapajós km 67_01T_soil.tsv
        ├── Tapajós km 67_02E_soil.tsv
        ├── Tapajós km 67_02T_soil.tsv
        ├── Tapajós km 67_03E_soil.tsv
        ├── Tapajós km 67_03T_soil.tsv
        ├── Tapajós km 67_04E_soil.tsv
        ├── Tapajós km 67_04T_soil.tsv
        ├── Tapajós km 67_05E_soil.tsv
        ├── Tapajós km 67_05T_soil.tsv
        ├── Tapajós km 67_06E_soil.tsv
        ├── Tapajós km 67_06T_soil.tsv
        ├── Tapajós km 67_07E_soil.tsv
        ├── Tapajós km 67_07T_soil.tsv
        ├── Tapajós km 67_08E_soil.tsv
        ├── Tapajós km 67_08T_soil.tsv
        ├── Tapajós km 67_09E_soil.tsv
        ├── Tapajós km 67_09T_soil.tsv
        ├── Tapajós km 67_10E_soil.tsv
        ├── Tapajós km 67_10T_soil.tsv
        ├── Tapajós km 67_11E_soil.tsv
        ├── Tapajós km 67_11T_soil.tsv
        ├── Tapajós km 67_12E_soil.tsv
        ├── Tapajós km 67_12T_soil.tsv
        ├── Tapajós km 67_13E_soil.tsv
        ├── Tapajós km 67_13T_soil.tsv
        ├── Tapajós km 67_14E_soil.tsv
        ├── Tapajós km 67_14T_soil.tsv
        ├── Tapajós km 67_15E_soil.tsv
        ├── Tapajós km 67_15T_soil.tsv
        ├── Tapajós km 67_16E_soil.tsv
        ├── Tapajós km 67_16T_soil.tsv
        ├── Tapajós km 67_17E_soil.tsv
        ├── Tapajós km 67_17T_soil.tsv
        ├── Tapajós km 67_18E_soil.tsv
        ├── Tapajós km 67_18T_soil.tsv
        ├── Tapajós km 67_19E_soil.tsv
        ├── Tapajós km 67_20E_soil.tsv
        ├── Tapajós km 67_21E_soil.tsv
        ├── Tapajós km 67_22E_soil.tsv
        ├── Tapajós km 67_23E_soil.tsv
        ├── Tapajós km 67_24E_soil.tsv
        ├── Tapajós km 67_25E_soil.tsv
        ├── Tapajós km 67_26E_soil.tsv
        ├── Tapajós km 67_27E_soil.tsv
        ├── Tapajós km 67_28E_soil.tsv
        ├── Tapajós km 67_29E_soil.tsv
        ├── Tapajós km 67_30E_soil.tsv
        ├── Tapajós km 67_31E_soil.tsv
        ├── Tapajós km 67_32E_soil.tsv
        ├── Tapajós km 67_33E_soil.tsv
        ├── Tapajós km 67_34E_soil.tsv
        ├── Tapajós km 67_35E_soil.tsv
        ├── Tapajós km 67_36E_soil.tsv
        ├── Tene_Subplot_10_soil.tsv
        ├── Tene_Subplot_11_soil.tsv
        ├── Tene_Subplot_12_soil.tsv
        ├── Tene_Subplot_13_soil.tsv
        ├── Tene_Subplot_14_soil.tsv
        ├── Tene_Subplot_15_soil.tsv
        ├── Tene_Subplot_16_soil.tsv
        ├── Tene_Subplot_17_soil.tsv
        ├── Tene_Subplot_18_soil.tsv
        ├── Tene_Subplot_19_soil.tsv
        ├── Tene_Subplot_1_soil.tsv
        ├── Tene_Subplot_20_soil.tsv
        ├── Tene_Subplot_21_soil.tsv
        ├── Tene_Subplot_22_soil.tsv
        ├── Tene_Subplot_23_soil.tsv
        ├── Tene_Subplot_24_soil.tsv
        ├── Tene_Subplot_25_soil.tsv
        ├── Tene_Subplot_2_soil.tsv
        ├── Tene_Subplot_3_soil.tsv
        ├── Tene_Subplot_4_soil.tsv
        ├── Tene_Subplot_5_soil.tsv
        ├── Tene_Subplot_6_soil.tsv
        ├── Tene_Subplot_7_soil.tsv
        ├── Tene_Subplot_8_soil.tsv
        ├── Tene_Subplot_9_soil.tsv
        ├── Ulu Muda_22_soil.tsv
        ├── Ulu Muda_23_soil.tsv
        ├── Ulu Muda_24_soil.tsv
        ├── Ulu Muda_25_soil.tsv
        ├── Ulu Muda_26_soil.tsv
        ├── Ulu Muda_27_soil.tsv
        ├── Ulu Muda_28_soil.tsv
        ├── Ulu Muda_29_soil.tsv
        ├── Ulu Muda_30_soil.tsv
        ├── Uppangala_LP1_soil.tsv
        ├── Uppangala_LP2_soil.tsv
        ├── Uppangala_LP3_soil.tsv
        ├── Uppangala_LP4_soil.tsv
        ├── Uppangala_UP1_soil.tsv
        ├── Uppangala_UP2_soil.tsv
        ├── sao_nicolau_1_soil.tsv
        ├── sao_nicolau_2_soil.tsv
        ├── sao_nicolau_3_soil.tsv
        ├── sao_nicolau_4_soil.tsv
        ├── sao_nicolau_5_soil.tsv
        └── sao_nicolau_6_soil.tsv
