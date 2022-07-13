pages = [
    "Este lugar es muy oscuro y extraño. Veo una pradera un tanto peligrosa, \n escucho cuervos y muchos lobos. \n Debo elegir rápidamente o moriré \n 1) Ir al camino de la izquierda \n 2) Huir por la pradera \n 3) Ir a la derecha",
    "-Corriste hacia la izquierda- \nGenial. Al parecer estoy a salvo. \n ¿Qué es eso? ¡ES UN LOBO! NOOOO \n\n *HAZ MUERTO* \n FIN DEL JUEGO",
    "-Huyes por la pradera- \n se acerca un brujo y te convierte en su ayudante \n Observas un lobo, este intenta atacarte a ti y al brujo, pero logran matarlo entre ambos. \n \n Felicidades, ganaste el juego \n FIN",
    "-Corriste hacia la derecha- \n Una manada de lobos te atacan \n Pero tranquilo, unos cuervos se hicieron un festín con tus restos. \n \n PERDISTE \n FIN DEL JUEGO",
]

def showPage(pageNumber):
    text = pages[pageNumber]
    print(text)
    response = input()
    showPage(int(response))

showPage(0)
