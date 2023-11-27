# Data Analytics
import cvxpy as cp
import datetime
import geopandas as gpd
import numpy as np
import networkx as nx
import osmnx as ox
import pandas as pd
import scipy.io as sio
import shapely.geometry as sg
import time

from shapely.ops import split, snap
from shapely.geometry import Point, LineString
from sodapy import Socrata


# Data Visualization
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import random

# Admin
import os
import pdb
import sys 

from base64 import b64decode
from IPython import display
from tqdm.notebook import tqdm
from dotenv import load_dotenv

tqdm.pandas()
pd.set_option("display.max_columns", 1000)
load_dotenv()