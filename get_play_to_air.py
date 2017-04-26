import os
import urllib.request, json
print("Sync_Pautas_play_to_air")
asigment_data = []

snapshot_path = ""

snap_name = "snap_"
snap1_exist = False

if(os.path.exists(snapshot_path+snap_name+"1.json")):
	print("Existe el Snapshot")
	snap1_exist = True
else:
	print("No existe el Snapshot")


snapshot_1 = []
snapshot_2 = []
with urllib.request.urlopen("http://192.168.196.73:8080/data/data_assigment_list.json") as url:
	asigment_data = json.loads(url.read().decode())
    
print(len(asigment_data))
if(snap1_exist == False):
	print("creando el snap 1...")
	snap_file = open(snapshot_path+snap_name+"1.json","w")
	snap_file.write(json.dumps(asigment_data))
	# print("Snap creado")
	if(os.path.exists(snapshot_path+snap_name+"1.json")):
		print("Snap1 Creado Exitosamente")
		snap1_exist = True
else:
	with open(snapshot_path+snap_name+"1.json","r") as snap_1:
		snapshot_1 = json.loads(snap_1.read())
	last_pautas_total = len(snapshot_1)
	curent_pautas_total = len(asigment_data)
	print("Snapshot 1 Pautas:",last_pautas_total)
	print("Current snap Pautas:",curent_pautas_total)

	pauta_mos_movements = False
	#Detect Pauta MOS Movements(+,-)
	if(last_pautas_total > curent_pautas_total):
		print("- Pautas")
		pauta_mos_movements = True
	elif(last_pautas_total < curent_pautas_total):
		print("+ Pautas")
		pauta_mos_movements = True
	elif(last_pautas_total == curent_pautas_total):
		print("none movements")

	#Detect Nota MOS Movements
	for pauta in asigment_data:
		if(pauta_mos_movements):
			print(pauta["name"],"\n\n")

		else:
			print("\nAnalizando Pauta:",pauta["name"])
			for pauta_snap in snapshot_1:
					if(pauta['guid'] ==  pauta_snap['guid']):
						nota_movements = False
						total_notas_old = len(pauta_snap['mos_table'])
						total_notas_now = len(pauta['mos_table'])
						print("Now: ",total_notas_now," - Old:",total_notas_old, " = ",(total_notas_now - total_notas_old ) )
						# print("\n\n Coincide la Pauta \n")

						if(total_notas_old == total_notas_now):
							print("No Nota Movements")
						elif(total_notas_old < total_notas_now):
							print(" + Nota")
							nota_movements = True
						elif(total_notas_old > total_notas_now):
							print(" - Nota")
							nota_movements = True

						notaAdd_counter = 0
						for nota in pauta["mos_table"]:
							if(nota_movements):
								# print("Find Nota: ",nota)
								nota_exists = False

								for nota_snap in pauta_snap["mos_table"]:
									#if(mos_name)
									
									# print(" # ",nota_snap)
									if(nota['mos_name'] == nota_snap['mos_name']):
										# print("-------------------Existe")

										nota_exists = True
										break
								if(nota_exists):
									# print(" ---- Pasa")

									pass
								else:
									# print("verify rename...")
									mos_name_e = nota['mos_name'][:23]
									mos_name_id = nota['mos_name'][23:]
									if(len(mos_name_id) < 8):
										print("No completa:",mos_name_id)
										if(len(nota['mos_name'].split("_")[1]) == 8):
										 	mos_name_id = nota['mos_name'].split("_")[1]

									if(mos_name_e in nota_snap['mos_name']):
										print("----- Nota Rename ---------")
										print(mos_name_e ," - ", nota_snap['mos_name'])
									elif(mos_name_id in nota_snap['mos_name']):
										print("----- Nota Rename ---------")
										print(mos_name_id ," - ", nota_snap['mos_name'])

									print(" ++ Nota: ",nota)
									notaAdd_counter += 1
						print("    Notas add: ", notaAdd_counter, " Pauta:", pauta["name"])
						# 	print(" # ",nota)
						# 	# print(pauta['guid'] ," - ",  pauta_snap['guid'])
						# 	nota_ok = False
							# for nota_snap in pauta_snap["mos_table"]:
							# 	if(nota['mos_name'] == nota_snap['mos_name']):
							# 		print("Coincide Nota")
							# 		nota_ok = True
							# 	if(nota_ok == True):
							# 		print("Nota normal")
							# 	else:
							# 		print("Add Nota")


		
				
					# print("\n \n  - ",pauta_snap)


# print(asigment_data)