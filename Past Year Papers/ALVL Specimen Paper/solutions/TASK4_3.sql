select Device.SerialNumber, Device.Model, Device.Location, Monitor.DateCleaned 
from Device, Monitor where Device.SerialNumber = Monitor.SerialNumber