#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 2019

@author: kristjan
"""

import os
import yaml
from shutil import copyfile

class YamlManager():
    
    def save(file_name, yaml_data):
        with open(file_name, 'w') as yaml_file:
            yaml.dump(yaml_data, yaml_file)
            
    def load(file_name):
        with open(file_name, 'r') as yaml_file:
            return yaml.load(yaml_file)
        
class ImageManager():
    
    def replace(src, dst):
        i = 0
        for path, subdirs, files in os.walk(src):
            for name in files:
                file_name = os.path.join(path, name)
                new_name = '{}/{}_{}'.format(dst, path.split('/')[1], name)
                copyfile(file_name, new_name)
                i += 1
        print('\ncopied {} images from: {} to: {}'.format(i, src, dst))
        
class DataCleaner():
    
    def parse_killer_data():
        pass
    
    def parse_usw():
        pass

if __name__ == '__main__':
    
    file_name = 'test_data.yml'
    data = YamlManager.load(file_name)
    print(data)
    ImageManager.replace('serial_killers', 'serial_killers_replace')
