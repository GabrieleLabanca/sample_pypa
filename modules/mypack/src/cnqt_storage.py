import importlib.util

import tqdm

if importlib.util.find_spec("numpy") is not None:
    import numpy as np
