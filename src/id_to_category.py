categoriesImagenet = {
  "540":"arma", #Rifle
  "541":"arma", #Rifle 2
  "370":"arma", #Cutelo
  "369":"arma", #Machado
  "787":"arma", #Coldre
  "371":"arma", #Canivete
  "542":"arma", #Municao
  "219":"arma", #Revolver  
  "879":"documento", #Envelope
  "546":"droga", #Isqueiro
  "984":"droga", #Fosforo
  "901":"droga", #Remedio
  "521":"droga", #Balanca
  "531":"droga", #Seringa
  "557":"roubo", #Cacaniquel
  "522":"roubo", #Relogio
  "528":"roubo", #Cronometro
  "548":"roubo", #Caixa eletronico
  "583":"roubo", #Senha cofre
  "971":"roubo", #Mascara
  "375":"roubo", #Martelo
  "753":"roubo", #Cofre
  "920":"veiculo", #Minionibus
  "271":"veiculo", #Minivan
  "277":"veiculo", #Motoneta
  "260":"veiculo", #Scooter
  "281":"veiculo", #Pickup
  "285":"veiculo", #Policia
  "286":"veiculo", #RV
  "282":"veiculo", #Caminhao
  "283":"veiculo" #Trailer
}

def getCategoryImagenet (id):
  if id in categoriesImagenet:
    return categoriesImagenet[id]
  else:
    return None
