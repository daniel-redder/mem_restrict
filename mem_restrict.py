import psutil
import resource


#https://www.geeksforgeeks.org/python-how-to-put-limits-on-memory-and-cpu-usage/

PERCENTAGE_MEMORY_ALLOWED = 0.8

# Calculate the maximum memory limit (80% of available memory)
virtual_memory = psutil.virtual_memory()
available_memory = virtual_memory.available
memory_limit = int(available_memory * PERCENTAGE_MEMORY_ALLOWED)

print(f'{memory_limit} memory limit, available: {available_memory}')

# Set the memory limit
resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))
