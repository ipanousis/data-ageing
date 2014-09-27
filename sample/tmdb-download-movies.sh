#!/bin/bash

YEARS=`seq 1900 2020`
./tmdb-download.py $YEARS downloads
