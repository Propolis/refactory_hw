import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

print("Всем привет")
def cpu_task_process(task_name: str, n: int):
    result = sum(i*i for i in range(n))
    print(f"Task {task_name} finished with result {result}")
    return task_name, result

async def async_task_process():
    tasks = [
        ("Task A", 60000000),
        ("Task B", 40000000),
        ("Task C", 50000000)
    ]
    start = time.time()

    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        feature = [loop.run_in_executor(executor, cpu_task_process, task[0], task[1]) for task in tasks]
        results = await asyncio.gather(*feature)

    total_time = time.time() - start
    print(f"Total time: {total_time}")
    return results

if __name__ == "__main__":
    results = asyncio.run(async_task_process())
    print(results)
