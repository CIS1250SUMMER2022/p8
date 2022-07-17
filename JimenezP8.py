# JimenezP8
# Programmer: Mark Jimenez
# EMail: mjimenez43@cnm.edu
# Purpose: demonstrate exception handling

import math



class GeoPoint():
	def __init__(self):
		
		self.lat = 0
		self.lon = 0
		self.description = ""

	def SetPoint(self, lat, lon):
		self.lat = lat
		self.lon = lon

	def GetPoint(self):
		return (self.lat, self.lon)

	def Distance(self, lat, lon):
		R = 6371

		A = (math.sin((self.lat - lat)/2))**2 + math.cos(self.lat) * math.cos(lat) * (math.sin((self.lon - lon/2)))**2
		C = 2 * math.atan2(math.sqrt(A),math.sqrt(1-A))
		D = R * C
		return D

	def SetDescription(self, new_description):
		self.description = new_description

	def GetDescription(self):
		return self.description



geo_one = GeoPoint()
geo_one.SetPoint(100, 120)
geo_one.SetDescription("point one")

geo_two = GeoPoint()
geo_two.SetPoint(10, 12)
geo_two.SetDescription("point two")

while True:
	while True:
		try:
			user_points = input("What is your location? Please be comma seperated: ")
			points = user_points.split(',')
			points[0] = int(points[0])
			points[1] = int(points[1])
			
		except TypeError:
			print("That is not a number!")
			
		except ValueError:
			print("Please enter a number!")
			
		except Exception as e:
			print(f"Someting went wrong: {e}")
			
		else:
			break
			
	distance_from_one = geo_one.Distance(points[0], points[1])
	distance_from_two = geo_two.Distance(*points)
		
	if distance_from_one < distance_from_two:
		print(f"you are closest to {geo_one.GetDescription()} which is located at {geo_one.GetPoint()}")
	else:
		print(f"you are closest to {geo_two.GetDescription()} which is located at {geo_two.GetPoint()}")
		
	if input("Do another (y/n)?") == 'n':
		break
			
print("Have a great day!")
