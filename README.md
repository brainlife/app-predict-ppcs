<h1 align="center">Clairvoy</h1>

<p align="center">
  A low- or high-risk prediction of persisting post-concussion symptoms (PPCS) from white matter FA tract profiles, with a pretrained logistic regression classifier.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.793"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.793-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Predicts the risk of persisting post-concussion symptoms (PPCS) from mean FA tract profiles with a pretrained logistic regression classifier and reports low or high risk.**

Takes the FA tract profiles, keeps the tracts listed in significant_tracts.txt, averages each profile, and applies a pretrained logistic regression model; the result (low or high risk of PPCS) is shown as a message on brainlife.io and no data are written. The model was trained for concussion data; results on other populations are not meaningful.

| | |
|---|---|
| **Inputs** | `neuro/tractmeasures` |
| **Container** | `brainlife/dipy:1.4.1` |
| **Resources** | 4 CPUs · 4 GB memory · 0.17 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.793](https://doi.org/10.25663/brainlife.app.793) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/tractmeasures` (profiles) | yes | Tract Profiles. Must include FA profiles for the tracts the classifier was trained on. |

<!-- brainlife-app:end -->

## About

Clairvoy predicts time to return to play after a concussion, framed as the risk of persisting post-concussion symptoms (PPCS). It averages the fractional anisotropy (FA) profiles of a set of white matter tracts and applies a pretrained logistic regression classifier. The model was trained on concussion data; its predictions are not meaningful for other populations. The approach is summarised in the poster [`poster_nns2023.pdf`](poster_nns2023.pdf).

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.793](https://doi.org/10.25663/brainlife.app.793), choose a `neuro/tractmeasures` dataset tagged `profiles` (tract profiles) and press **Execute**. The result, "This injury is at low risk of developing PPCS" or "This injury is at high risk of developing PPCS", is shown as a message on the results page. The App does not write any data to your project.

### How it works

1. The FA profiles of the 16 tracts listed in [`significant_tracts.txt`](significant_tracts.txt) are read from the tract profiles table (column `fa`, matched on `structureID`).
2. Each profile, which must have 100 nodes, is averaged over its central nodes (nodes 10–89).
3. The pretrained classifier `clf_LR_16` (scikit-learn logistic regression) predicts low (0) or high (1) PPCS risk from the 16 mean FA values.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) and [`jq`](https://jqlang.github.io/jq/). The App runs in the `brainlife/dipy:1.4.1` container.

1. Clone this repository.
2. Create `config.json` with the path to your tract profiles:

   ```json
   {
       "profiles": "./input/tractmeasures.csv"
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## Outputs

The prediction is printed to the log and written to `product.json` as a brainlife.io message. No datasets are produced.

## Troubleshooting

- **The App fails while extracting the FA profiles**: the tract profiles must contain an `fa` column, 100 nodes per tract, and every tract named in `significant_tracts.txt` (as `structureID`).

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Clairvoy. brainlife.io App. [doi:10.25663/brainlife.app.793](https://doi.org/10.25663/brainlife.app.793)
- Hayashi S, Caron BA, et al. brainlife.io: A decentralized and open source cloud platform to support neuroscience research. Nature Methods, in press.
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- [Giulia Bertò](https://github.com/giulia-berto)

**Contributors:** Franco Pestilli (project director), Nicholas Port

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

[MIT](LICENSE).
