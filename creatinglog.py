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

div(3, 0)
