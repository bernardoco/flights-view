'''Download data from ANAC and save in a '/data' folder.'''

import requests
import zipfile
import io
import logging

# There is data available since 2000.
# We'll only use the most recent years
START_YEAR = 2020
END_YEAR = 2021

months = [str(month).zfill(2) for month in range(1, 12+1)]
years = [str(year) for year in range(START_YEAR, END_YEAR+1)]

BASE_URL = 'https://www.gov.br/anac/pt-br/assuntos/regulados/empresas-aereas/Instrucoes-para-a-elaboracao-e-apresentacao-das-demonstracoes-contabeis/microdados/'


logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s', 
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

# Download zip file from ANAC and extract files to the '/data' folder
for year in years:
    logging.info('Downloading ' + str(year) + ' data...')

    for month in months:

        url = BASE_URL + 'basica{year}-{month}.zip'
        r = requests.get(url.format(year=year, month=month), stream=True)

        with zipfile.ZipFile(io.BytesIO(r.content), 'r') as zip_ref:
            zip_ref.extractall('src/data/' + year)