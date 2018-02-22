# IPND 2nd project

import random

easy = 'Cuando yo quiero comer, tengo ___1___.  Cuando yo quiero beber, tengo ___2___.  Cuando yo llevo un abrigo, es porque tengo ___3___.  Cuando quiero saltar en una piscina, es porque tengo ___4___.'
med = 'Estoy en la playa y quiero visitar una isla.  La isla esta muy lejos de la playa y no puedo nadar hasta la isla.  Por eso necesito conseguir un ___1___. Primero, busco a mi dinero.  Tengo $100 dolares y no puedo comprar el ___1___.  Pero lo voy a poder ___2___.  Hace sol y no quiero quemarme, por eso pongo el ___3___ en mi piel.  Ya estoy listo entonces subo al ___1___.  Pero no tiene motor sino tiene  ___4___.  Yo izo la ___4___ y navego a la isla.'
hard = 'Hoy el abogado demando al politico por causa de difamacion de parte de su cliente, Juan Gonzalez.  El Sr. Gonzalez es el ___1___ en el procedimiento.  La presunta ___2___ ocurrio en un discurso dado por el politico.  Por falta de evidencia, el juez  ___3___ el procedimiento y ___4___ el permiso de contrademanda al politico.'

vocab = ["hambre", "sed", "frio", "calor", "barco", "alquilar", "bronceador", "vela", "querellante", "difamacion", "desestimo", "otorgo"]

easy_vocab = vocab[:4]
med_vocab = vocab[4:8]
hard_vocab = vocab[8:]

print "Spanish Vocabulary Test"

# Instructions for quiz

print "\n" + "In the following quiz, fill in the blanks with the proper words from our vocabulary list." + "\n"

# Prompt users to enter in their desired difficulty level.

dif_level = raw_input("Choose your difficulty level.  Please type easy, medium, or hard: ")
dif_options = ["easy", "medium", "hard"]

while dif_level not in dif_options: # Prompt user to reenter difficulty level if they haven't typed the correct word.
	print "Please check your spelling, and try again."
	dif_level = raw_input("Choose your difficulty level.  Please type easy, medium, or hard: ")

def vocab(): #Specify the proper list that corresponds to the difficulty level
	if dif_level == "easy":
		vocab = easy_vocab
	if dif_level == "medium":
		vocab = med_vocab
	if dif_level == "hard":
		vocab = hard_vocab
	return vocab

def paragraph():
	if dif_level == "easy": # Specify paragraph that corresponds to difficulty level.
		paragraph = easy
	elif dif_level == "medium":
		paragraph = med
	elif dif_level == "hard":
		paragraph = hard
	return paragraph

scramble = vocab()[:] # Copy the list to adjust it without breaking the logic below.
random.shuffle(scramble) # Use the shuffle function to reorder the list randomly.

print "\n" + str(paragraph()) # Print all the prompts so user can take the quiz.
print "\n" + "Word Bank: " + str(scramble) + "\n"

blanks = [] # Create a blank list to be populated with the inputs.

def answers():
	par = paragraph()
	i = 1
	while i <= 4:
		answer = raw_input("Type your answer for Number " + str(i) + ": ") # User inputs answers.
		if answer == vocab()[i-1]: # Check input to the corresponding answer in the list.
			print "\n" + "Correct!"
			blanks.append(answer) # Adds answer to the blank list
			par = par.replace("___" + str(i) + "___", blanks[i-1]) # Replaces blank in paragraph with the correct answer.
			print "\n" + par + "\n"
			i += 1
		else:
			print "\n" +  "Try again!" + "\n"
		if i > 4:
			print "Way to go! All finished!" # Finishes the quiz.

print answers()