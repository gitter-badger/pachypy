#!/bin/bash

if [ -n "${CODECOV_TOKEN}" ]; then
    bash <(curl -s https://codecov.io/bash) -t "${CODECOV_TOKEN}";
fi