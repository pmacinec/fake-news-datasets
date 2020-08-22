# Fake News Datasets

## Introduction

This project was created to show basic analysis of public datasets of **fake news**. Main idea is to make each analysis replicable, so everyone can add his own analysis and use it for his experiments and data mining. Every dataset has its own *python jupyter notebook* with simple analysis, which can help to choose appropriate dataset.

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
