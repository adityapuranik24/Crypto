import faust
import pandas as pd
app=faust.App('demo-streaming',broker='kafka://3.17.23.28:9092')


input_topic = app.topic('crypto', value_serializer='json')
# aged_table = app.Table("major-count",key_type=str, value_type=str, partitions=1, default=int)


@app.agent(input_topic)
async def processor(stream):
    async for message in stream:
        rem_list = ['symbol', 'rank', 'color', 'png32', 'png64','webp32', 'webp64', 'pairs', 'categories', 'links', 'delta']
        for key in rem_list:
            del message[key]
        values =pd.DataFrame.from_dict(message, orient='index')
        print(values)



