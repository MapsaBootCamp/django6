LOG_LEVEL_NAME = ("ERROR", "WARNING", "INFO", "DEBUG", "A")
LOG_LEVEL_CODE = (40, 30, 20, 10)


for elm in zip(LOG_LEVEL_NAME, LOG_LEVEL_CODE, LOG_LEVEL_CODE):
    print(elm)
	


LOG_CONFIG = {
    "format" : ['date', "message"],
    "level" : "DEBUG"
}