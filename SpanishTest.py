# IPND 2nd project

easy = 'Cuando yo quiero comer, tengo ___1___.  Cuando yo quiero beber, tengo ___2___.  Cuando yo llevo un abrigo, es porque tengo ___3___.  Cuando quiero saltar en una piscina, es porque tengo ___4___.'
med = 'Estoy en la playa y quiero visitar una isla.  La isla esta muy lejos de la playa y no puedo nadar hasta la isla.  Por eso necesito conseguir un ___1___. Primero, busco a mi dinero.  Tengo $100 dolares y no puedo comprar el ___1___.  Pero lo voy a poder ___2___.  Hace sol y no quiero quemarme, por eso pongo el ___3___ en mi piel.  Ya estoy listo entonces subo al ___1___.  Pero no tiene motor sino tiene  ___4___.  Yo izo la ___4___ y navego a la isla.'
hard = 'Hoy el abogado demando al politico por causa de difamacion de parte de su cliente, Juan Gonzalez.  El Sr. Gonzalez es el ___1___ en el procedimiento.  La presunta ___2___ ocurrio en un discurso dado por el politico.  Por falta de evidencia, el juez  ___3___ el procedimiento y ___4___ el permiso de contrademanda al politico.'

vocab = ["hambre", "sed", "frio", "calor", "barco", "alquilar", "bronceador", "vela", "querellante", "difamacion", "desestimo", "otorgo"]

easy_vocab = ["hambre", "sed", "frio", "calor"]
med_vocab = vocab[4:8]
hard_vocab = vocab[8:]

print "Spanish Vocabulary Test"

# Instructions for quiz

print "\n" + "In the following quiz, fill in the blanks with the proper words from our vocabulary list." + "\n"

# Prompt users to enter in their desired difficulty level.


dif_level = raw_input("Choose your difficulty level.  Please type easy, medium, or hard: ")

def par():
	dif_options = ["easy", "medium", "hard"]
	while dif_level in dif_options: # Print paragraph that corresponds to difficulty level.
		if dif_level == "easy":
			par = easy
			return par
		if dif_level == "medium":
			par = med
			return par
		if dif_level == "hard":
			par = hard
			return par
	else:
		print "Please check your spelling, and try again."


def word_bank():
	if dif_level == "easy":
		print "\n" + "Word Bank: frio, hambre, calor, sed" + "\n"
	if dif_level == "medium":
		print "\n" + "Word Bank: alquilar, barco, bronceador, vela" + "\n"
	if dif_level == "hard":
		print "\n" + "Word Bank: desestimo, difamacion, otorgo, querellante" + "\n"

print par()
print word_bank()

# Function to verify correctness

'''def correct_answer(word):
		if difficulty == "easy":
			if word == easy_vocab[i]:
				i += 1
				return True
		elif difficulty == "medium":
			if word == med_vocab[i]:
				i += 1
				return True
		elif difficulty == "hard":
			if word == hard_vocab[i]:
				i += 1
				return True
		else:
			print "Try again!"
			return False'''

# Get input, verify it is correct, return list of answers

num_answers = ["___1___", "___2___", "___3___", "___4___"]

def fill_par(string_par, num_answers):
	replaced = []
	string_par = string_par.split()
	i = 1
	while i <= 4:
		answer = raw_input("Type your answer for Number " + str(i) + ": ")
		if correct_answer(answer) = True:
			string_par = string_par.replace("___" + str(i) + "___", answer)
			i += 1
		else:
			print "Try again!"	
	return string_par

def answers():
	blanks = []
	i = 1
	while i <= 4:
		
		blanks.append(answer)
		
		#print fill_par(answer)
	return blanks

print answers()
print fill_par(answer)

