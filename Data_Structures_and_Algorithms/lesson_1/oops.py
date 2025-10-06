
class Phone():
    camera = 3
    thickness = "2mm"
    charging_port = 1
    headphone_jack = 1
    speakers = 10
    
    def taking_pics(self):
     print("camera is clicking pics")
    def msgs(self):
       print ("sending msgs")


pixel = Phone()
motorola = Phone()
nokia = Phone()


pixel.taking_pics()
print(nokia.camera)
print("the thickness of the phone is" ,motorola.thickness)

