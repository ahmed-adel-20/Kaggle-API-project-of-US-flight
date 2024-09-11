import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('usdot/flight-delays',path='.',unzip=True)
