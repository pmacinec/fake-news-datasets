# Fake News Datasets

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)


## Introduction

This project was created to show basic analysis of public datasets of **fake news**. Main idea is to make each analysis replicable, so everyone can add his own analysis and use it for his experiments and data mining. Every dataset has its own *python jupyter notebook* with simple analysis, which can help to choose appropriate dataset.

## Prerequisites

* [Docker](https://www.docker.com/)
* [GIT LFS](https://git-lfs.github.com/)

## Installation and running

To run all jupyter notebooks with appropriate libraries installed, we refer to use [Docker](https://www.docker.com/).

With installed Docker, run the following command to build docker image and start container:
```bash
./scripts/run.sh -b
```
**Note:** Next time, when no build is needed (because image has been already built), you can just run container by skipping `-b` argument.

## Datasets

List of all processed datasets with simple comparison is stored in [datasets/README.md](./datasets/README.md) file.

All datasets analyses are stored in [datasets/](./datasets/) folder. Each dataset has its own folder with simple description in README file and jupyter notebook (also can include different files, e.g. data itself).

Dataset files (e.g. `.csv` or `.tsv` files) are stored using Git LFS (see [Git LFS](https://git-lfs.github.com/) for more information).

### Adding new dataset

When adding new dataset, please follow these steps:

1. Call `./scripts/create_structure.sh {name}` script with name argument supplied in `snake_case` format (e.g. `fake_news_detection_kaggle`). This script will create needed folders and files in `datasets/{name}` folder.
1. Add data into `datasets/{name}/data` directory.
1. Update `datasets/{name}/README.md` file to provide link, potential tasks, description and attributes descriptions. Please, follow template file structure.
1. Update `datasets/{name}/{name}.ipynb` file with analysis of the dataset. Please, follow template file structure.
1. Add dataset and details into table of datasets in `datasets/README.md` file (please, follow the alphabetical order).


## TODO

Finish datasets:
* fake_news_vs_satire
* news_credibility
* fever