import pynvml

# 初始化NVML
pynvml.nvmlInit()

# 获取GPU数量
device_count = pynvml.nvmlDeviceGetCount()

# 遍历每个GPU并获取使用情况
for i in range(device_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    gpu_info = pynvml.nvmlDeviceGetMemoryInfo(handle)

    # 打印GPU的使用情况
    print(f"GPU {i+1}:")
    print(f"  Total memory: {gpu_info.total / 1024**2} MB")
    print(f"  Used memory: {gpu_info.used / 1024**2} MB")
    print(f"  Free memory: {gpu_info.free / 1024**2} MB")
    print(f"  GPU utilization: {pynvml.nvmlDeviceGetUtilizationRates(handle).gpu} %")

# 关闭NVML
pynvml.nvmlShutdown()


