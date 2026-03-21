import time
import asyncio

import httpx
import requests

### Sync\Async sleep


# def sync_sleep(task_name: str, delay: str):
#     print(f"Задача {task_name} - запущена")
#     time.sleep(int(delay))
#     print(f"Задача {task_name} - завершена")
#
# def run_sync_sleep():
#     start_time = time.time()
#
#     task1 = sync_sleep(task_name="Task A", delay="2")
#     task2 = sync_sleep(task_name="Task B", delay="1")
#     task3 = sync_sleep(task_name="Task C", delay="3")
#
#     total_time = time.time() - start_time
#
#     print(f"Общее время выполнения - {total_time}")
#     return [task1, task2, task3]
#
# sync_sleep_result = run_sync_sleep()
# print(f"Результат sync: {sync_sleep_result}")
# #=================================================================================================
# #=================================================================================================
# #=================================================================================================
#
# async def async_sleep(task_name: str, delay: str):
#     print(f"Задача {task_name} - запущена")
#     await asyncio.sleep(int(delay))
#     print(f"Задача {task_name} - завершена")
#
#     return task_name
#
#
# async def run_async_sleep():
#     start_time = time.time()
#
#     tasks = [
#         async_sleep(task_name="Task A", delay="2"),
#         async_sleep(task_name="Task B", delay="1"),
#         async_sleep(task_name="Task C", delay="3")
#         ]
#
#     results = await asyncio.gather(*tasks)
#
#     total_time = time.time() - start_time
#
#     print(f"Общее время выполнения - {total_time}")
#     return results
#
# async_sleep_result = asyncio.run(run_async_sleep())
# print(async_sleep_result)


### Sync\Async HTTP


#
# def sync_http(url: str) -> str:
#     print(f"Запрос к {url}")
#     start = time.time()
#
#     response = requests.get(url)
#
#     total_time = time.time() - start
#
#     print(f"Ответ от {url} за {total_time} секунд")
#
#     return response.json()
#
# def run_sync_http():
#     urls = [
#         "https://httpbin.org/delay/3",
#         "https://httpbin.org/delay/1",
#         "https://httpbin.org/delay/2",
#
#     ]
#
#     start = time.time()
#     results = []
#     for url in urls:
#         results.append(sync_http(url))
#     total_time = time.time() - start
#
#     print(f"Общее время выполнения - {total_time}")
#     return results
#
# sync_http_res = run_sync_http()
# print(sync_http_res)
#
#
async def async_http(url: str, client) -> str:
    print(f"Запрос к {url}")
    start = time.time()

    response = await client.get(url)

    total_time = time.time() - start

    print(f"Ответ от {url} за {total_time} секунд")

    return response.json()


async def run_async_http():
    urls = [
        "https://httpbin.org/delay/3",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
    ]

    start = time.time()

    async with httpx.AsyncClient() as client:
        tasks = [async_http(url, client) for url in urls]
        results = await asyncio.gather(*tasks)

    total_time = time.time() - start
#
    print(f"Общее время выполнения - {total_time}")
    return results
#
# async_http_res = asyncio.run(run_async_http())



def cpu_task(task_name: str, n: int):
    print(f"{task_name} n={n}")
    start = time.time()

    result = sum(i*i for i in range(n))

    total = time.time() - start
    print(f"{task_name} result={result//100000} total={total}")
    return result

def run_cpu_tasks():
    tasks = [
        ("Task A", 40000000),
        ("Task B", 40000000),
        ("Task C", 40000000)
    ]

    start = time.time()

    results = []
    for task in tasks:
        results.append(cpu_task(task[0], task[1]))

    total = time.time() - start
    print(f"Total time={total}")
    print(results)

run_cpu_tasks()

async def async_cpu_task(task_name: str, n: int):
    print(f"{task_name} n={n}")
    start = time.time()

    result = sum(i*i for i in range(n))

    total = time.time() - start
    print(f"{task_name} result={result//100000} total={total}")
    return result

async def run_async_cpu_tasks():
    tasks = [
        async_cpu_task("Task A", 40000000),
        async_cpu_task("Task B", 40000000),
        async_cpu_task("Task C", 40000000)
    ]

    start = time.time()

    results = asyncio.gather(*tasks)

    total = time.time() - start
    print(f"Total time={total}")
    print(results)

run_cpu_tasks()


