from GPUtil import showUtilization as gpu_usage
gpu_usage()       
import torch
torch.cuda.empty_cache()

# from numba import cuda
# cuda.select_device(0)
# cuda.close()
# cuda.select_device(0)