[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/brainlife.io-app.793-blue.svg)](https://doi.org/10.25663/brainlife.app.793)

# app-Clairevoy

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Predicts the risk of persisting post-concussion symptoms (PPCS) from mean FA tract profiles with a pretrained logistic regression classifier and reports low or high risk.**

Takes the FA tract profiles, keeps the tracts listed in significant_tracts.txt, averages each profile, and applies a pretrained logistic regression model; the result (low or high risk of PPCS) is shown as a message on brainlife.io and no data are written. The model was trained for concussion data; results on other populations are not meaningful.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.793](https://doi.org/10.25663/brainlife.app.793)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `0` | `neuro/tractmeasures` (profiles) | yes | Tract Profiles. Must include FA profiles for the tracts the classifier was trained on. |

Runtime: container `brainlife/dipy:1.4.1`; 4 CPUs; 4 GB memory; 0.17 h walltime.

Please cite:
- Hayashi S, Caron BA, et al. brainlife.io: A decentralized and open source cloud platform to support neuroscience research. Nature Methods, in press.

<!-- brainlife-app:end -->

App to predict time to return to play (a.k.a., Persisting Post Concussion Symptoms).

### Authors
- [Giulia Bertò](giulia.berto.4@gmail.com)

### Contributor
- [Franco Pestilli](pestilli@utexas.edu)
- [Nicholas Port](nport@iu.edu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project, it is helpful to Acknowledge the use of the platform. Please acknowledge the funding below in your publications, presentations, and code, that uses this code.

[![DoD-W81XWH-2010717](https://img.shields.io/badge/DoD-W81XWH_2010717-blue.svg)](https://brainlife.io/ezbids)

### Citations
We ask that you cite the following articles when publishing papers and code using this code. 

Hayashi, Caron, et al., brainlife.io: A decentralized and open source cloud platform to support neuroscience research *Nature Methods, In Press*.

### Running the App
### On [Brainlife.io](http://brainlife.io/) 
You can submit this App online at https://brainlife.io/app/64d62738e4d2e9108d7ab094 via the “Execute” tab.

Input: \
Tract Profiles.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something, like the following content with paths to your input files.

```json
{
  "profiles": "./input/tractmeasures.csv"
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Dependencies
This App only requires [singularity](https://sylabs.io/singularity/) to run. 

#### MIT Copyright (C) 2024 brainlife.io The University of Texas at Austin.
