

def save_weather_forecast(self, uid):
    print(self.weather_data);
    sql = "UPDATE weather_data SET temperature = "+ str(self.weather_data["temperature"]) + ", " 
    +"temperature_feels = "+ str(self.weather_data["temperature_feels"]) +", " 
    +"humidity = "+ str(self.weather_data["humidity"]) +", " 
    +"weather_status = ""+ str(self.weather_data["type"]) +"", " 
    +"precipitation = "+ str(self.weather_data["precipitation"]) +"" 
    +" WHERE UID = ""+ str(uid) +"""

print(sql)
c = self._db.cursor()
c.execute(sql)
c.close()
