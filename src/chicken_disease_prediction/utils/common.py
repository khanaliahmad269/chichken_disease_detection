import os
from box.exceptions import BoxValueError
import yaml
from chicken_disease_prediction import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''reads yaml file and returns 
    Args: 
        path_to_yaml (str): path like input
    
    Raises:
    
        value_error: if yaml file is empty
        e: empty file
    Returns:
    
        ComfigBox: ConfigBox Type

    '''
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded Successfully")
            return ConfigBox(content)   
    except BoxvalueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''create list of directories:
    Args:
    path_to_directories (list): list of path to directories
    ignore_log(bool, optional): ignore if  multiple dirs is to be created. Default to False'''
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")


@ensure_annotations
def save_jason(path: Path, data: dict):
    ''' save json data
    
    Args: 
    path(Path): path to json file
    data(dict): data to be saved in json file
    
    '''

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file saved at {path}")

@ensure_annotations
def load_jason(path: Path) -> ConfigBox:
    ''' load json file
    Args:
    paths(Path): path to jason files
    
    Returns:
    ConfigBox: data as class atributes  istead of dict
    '''
    with open(path) as f:
        content= json.load(f)
    logger.info(f"jason file loaded successfully from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    ''' Save binary file
    Args:
    data (Any): Data to be stored in the binary file
    path(Path): path to binary file
    '''
    joblib.dump(value = data, filename=path)
    logger.info(f"Binary file saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    ''' load binary file
    Args:
    path(Path): path to binary file
    Returns:
    Any: any data stored in binary file'''

    data= joblib.load(path)
    logger.info(f"Binary file loaded successfully from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    ''' get size in kb
    Args:
        path(Path): path of the file
    Returns:
        str: size of file in kb 
    '''
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} kb"

@ensure_annotations
def decodeImage(imgstring, filename):
    imgdata=base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

@ensure_annotations
def encodeImageIntoBase64(cropppedImagePath):
    with open(cropppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())

