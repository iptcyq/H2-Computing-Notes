SELECT  Device.SerialNumber, 
Device.Model, 
Device.Location, 
Monitor.DateCleaned 
FROM Device 
INNER JOIN Monitor O
N Device.SerialNumber = Monitor.SerialNumber