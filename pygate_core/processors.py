##########################################################
# manage all the dynamically loaded modules of the gateway.
# a module manages devices and or assets

__author__ = 'Jan Bogaerts'
__copyright__ = "Copyright 2015, AllThingsTalk"
__credits__ = []
__maintainer__ = "Jan Bogaerts"
__email__ = "jb@allthingstalk.com"
__status__ = "Prototype"  # "Development", or "Production"

import logging

from core import assetStateCache as cache

processors = {}


def load(processorNames):
    """Loads all the gateway modules"""
    if processorNames and len(processorNames) > 0:
        global processors
        logging.info("loading processors")
        processors = dict(zip(processorNames, map(__import__, processorNames)))       # load the modules and put them in a dictionary, key = the name of the module.
    else:
        logging.info("no processors to load")


def onAssetValueChanged(module, device, asset, value):
    cache.tryUpdateValue(device, asset, value)              # before calling any processors update the casche, so that processors that rely on the cache also get the latest value
    for key, mod in processors.iteritems():
        if hasattr(mod, 'onAssetValueChanged'):
            logging.info("running processor " + key)
            try:
                mod.onAssetValueChanged(module, device, asset, value)
            except:
                logging.exception('failed to run procesor ' + key + ' to gateway.')

def syncGatewayAssets():
    for key, mod in processors.iteritems():
        if hasattr(mod, 'syncGatewayAssets'):
            logging.info("syncing gateway assets for " + key)
            try:
                mod.syncGatewayAssets()
            except:
                logging.exception('failed to sync gateway assets for processor {}.'.format(key))