from mylog import logger

#INFO
#WARNING
#DEBUG
#CRITICA'
#Error


def div(x, y):
    try:
        c = x / y
        print("value of :", c)
    except Exception as e:
        logger.info(e)
    finally:
        print("finally completed")

#print("*"*20 + "another" + "*"*20)

div(3, 0)
