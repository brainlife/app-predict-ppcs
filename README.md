[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/brainlife.app.793-blue.svg)](https://doi.org/10.25663/brainlife.app.793)

# app-Clairevoy
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

Hayashi, Caron et al., brainlife.io: A decentralized and open source cloud platform to support neuroscience research Nature Methods, In Press.

### Running the App
### On [Brainlife.io](http://brainlife.io/) 
You can submit this App online at https://brainlife.io/app/64d62738e4d2e9108d7ab094 via the “Execute” tab.

Input: \
Tract Profiles.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

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

#### MIT Copyright (c) 2023 brainlife.io The University of Texas at Austin.
