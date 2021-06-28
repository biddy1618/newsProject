import logging

logging.basicConfig(
    format='{levelname} {name} {asctime}: {message}', 
    level=logging.INFO, 
    datefmt='%m/%d/%Y %H:%M:%S',
    style='{',
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
        ]
    )
