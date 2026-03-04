import shodan 
api = shodan.Shodan('IgMAesboTd0OZxAQu4WhdVGatI1CSJlR')
try:
    with open('shodan.txt',"w", encoding= 'UTF-8') as fichier:
        query=('apache')
        resultat= api.search(query)
        
        for ligne in resultat['matches']:
            fichier.write('\n')
            fichier.write(str(ligne['ip_str']))
            fichier.write('\n')
            fichier.write('\n')
            fichier.write(str(ligne['port']))
            fichier.write('\n')
            fichier.write('\n')
            fichier.write(str(ligne['org']))
            fichier.write('\n')
            fichier.write('\n')
            fichier.write(str(ligne['latitude']))
            fichier.write('\n')
            fichier.write('\n')
            fichier.write(str(ligne['location']['longitude']))
            fichier.write('\n')
    
except shodan.APIError as err:
    print("Impossible de se connecter à l'API")
    
    
finally: 
    print("Vive le Hacking et le fichier est crée")