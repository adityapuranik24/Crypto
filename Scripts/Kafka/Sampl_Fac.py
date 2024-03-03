import faust

app=faust.App('demo-streaming',broker='kafka://3.17.23.28:9092')

class Greeting(faust.Record,serializer='json'):
    name:str
    age:int

input_topic = app.topic('crypto', value_type=Greeting)
aged_table = app.Table("major-count",key_type=str,value_type=str,partitions=1,default=int)


@app.agent(input_topic)
async def processor(stream):
    async for message in stream:
        # if(message.age>30):
        aged_table[str(message.name)] = message.age
        print(aged_table.as_ansitable(title='Aged Tabled'))
        # print(aged_table)
        