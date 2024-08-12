# import requests

# responce = requests.get('https://jsonplaceholder.typicode.com/todos')
# # print(responce.status_code)

# if responce.status_code == 200:
#     data = responce.json()

#     for i, j in enumerate(data):
#         file_name = f"todos_{i+1}.txt"
#         with open(file_name, "w") as file:
#             file.write(str(j))

#     print('Сохранение завершено')

# else:
#     print("Ошибка")





# import aiohttp
# import asyncio

# async def fetch_and_save(session, url, index):
#     async with session.get(url) as response:
#         if response.status == 200:
#             data = await response.json()
#             file_name = f"post_{index+1}.txt"
            
#             with open(file_name, "w") as file:
#                 file.write(str(data))

# async def main():
#     url = "https://jsonplaceholder.typicode.com/posts"
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for i in range(100):
#             task = fetch_and_save(session, url + f"/{i+1}", i)
#             tasks.append(task)
#         await asyncio.gather(*tasks)


# asyncio.run(main())