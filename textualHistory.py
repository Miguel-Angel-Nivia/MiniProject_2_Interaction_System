from openal import *
import functions as func
import os, time

# Principal code
# By: Miguel Angel Nivia Y Daniel Vasquez

def main():
    # open OpenAl
    oalInit()

    # Player
    player = Listener()
    player.set_position((0, 0, 0))

    sounds = func.obtainingSound()
    startThread = func.playSound(sounds, "sonidoEmpezar.wav", 1, 1.5, [0, 0, -1], [0, 0, -1], 3.5, False, "static")
    if startThread.is_alive(): sounds["sonidoEmpezar.wav"].stop() and startThread.join()
    # Loading screen
    func.loadingScreen()
    menuThread = func.playSound(sounds, "sonidoInicioMenu.wav", 1, 1, [0, 0, 0], [0, 0, 0], 0, True, "static")
    if menuThread.is_alive():
        try:
            input("\n                         Presiona enter para continuar...                            \n\n")
        finally:
            sounds["sonidoInicioMenu.wav"].stop() and menuThread.join()
    # Console Cleaning
    os.system('cls')

    tiene_pechera = False

    text = "Dios - Frederic es un aventurero común y corriente que hace parte de un grupo de mercenarios, donde él despierta después de una exploración que salió mal y con un fuerte dolor de cabeza."
    WindThread = func.playSound(sounds, "sonidoViento.wav", 1, 2, [0, 1, 0], [0, 1, 0], 0, False, "static")
    func.playerInteraction(sounds, "continue", text, WindThread, "sonidoViento.wav", 1)

    text = "Frederic - Ahg que.. que paso? ¿Dónde estoy? No veo absolutamente nada, hay un olor a humo, estoy mojado y repleto de lodo."
    waterdropsThread = func.playSound(sounds, "sonidoGotasCueva.wav", 0.6, 1, [1, 0, 0], [0, 0, 0], 1, True, "static")
    waterdropsThread2 = func.playSound(sounds, "sonidoGotasCueva2.wav", 0.2, 1, [-1, 0, 0], [0, 0, 0], 1, True, "static")
    func.printText(text, 0)
    
    cont = 0
    while cont < 1:
        print("¿Qué quieres hacer? \n1. Levantarse \n2. Mirar a tu alrededor")
        decision = func.playerInteraction(sounds, "selection", "", "", "", 0)
        
        if decision == "1":
            text = "Frederic - ¿Qué es esto? ¿una herida? Mierda tengo una cortada infectada en el abdomen."
            hurtThread = func.playSound(sounds, "sonidoHeridaFrederic.wav", 1, 1, [0, 0, 0], [0, 0, 0], 0, False, "static")
            func.playerInteraction(sounds, "continue", text, hurtThread, "sonidoHeridaFrederic.wav", 0)

            print("¿Qué quieres hacer? \n1. Inspeccionar cuerpo \n2. Caminar")
            decision = func.playerInteraction(sounds, "selection", "", "", "", 0)
            if decision == "1":
                text = "Frederic - Qué carajo, no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo, mejor voy para allá."
                doubtThread = func.playSound(sounds, "sonidoDudaFrederic.wav", 0.8, 1, [0, 0, 0], [0, 0, 0], 0, False, "static")
                func.playerInteraction(sounds, "continue", text, doubtThread, "sonidoDudaFrederic.wav",  0)
                cont += 1
            else:
                cont +=1

        elif decision == "2":
            text = "Frederic - Qué carajo no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo."
            doubtThread = func.playSound(sounds, "sonidoDudaFrederic.wav", 0.8, 1, [0, 0, 0], [0, 0, 0], 0, False, "static")
            func.playerInteraction(sounds, "continue", text, doubtThread, "sonidoDudaFrederic.wav", 0)

            print("¿Qué quieres hacer? \n1. Levantarse \n2. Caminar")
            decision = func.playerInteraction(sounds, "selection", "", "", "", 0)
            if decision == "1":
                text = "Frederic - ¿Qué es esto? ¿una herida? Mierda tengo una cortada en el abdomen, mejor me muevo de acá."
                hurtThread = func.playSound(sounds, "sonidoHeridaFrederic.wav", 1, 1, [0, 0, 0], [0, 0, 0], 0, False, "static")
                func.playerInteraction(sounds, "continue", text, hurtThread, "sonidoHeridaFrederic.wav", 0)
                cont += 1
            else:
                cont +=1

    humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1.5, 1, [0, -3, 0], [0, -1, 0], 2, True, "static")
    # bonfireThread = func.playSound(sounds, "sonidoFogata.wav", 1, 1, [12, 0, 12], [0, 0, 0], 1, True, "move")
    text = "Frederic - Parece que estoy en una especie de cueva. ¿Dónde demonios está mi equipo? Demonios, esa espada me costó tanto \
            como una semana en el burdel. Me acercaré a esa luz; puede que encuentre algo de utilidad o ver algo.\n\n \
            Dios - Frederic, confundido y sin saber dónde está, se acerca a la luz con cautela.\n\n \
            Frederic - ¿Una fogata? ¿Qué hace una fogata aquí?\n\n \
            Frederic - No veo nada de relevancia excepto este palo seco."
    func.printText(text, 0)
    # player movement
    """
    for i in range(13):
        player.set_position((12 - i, 0, 12))
        if i == 12 and bonfireThread.is_alive():
            sounds["sonidoFogata.wav"].stop()
            bonfireThread.join()
        time.sleep(1)
    """
    if waterdropsThread.is_alive() and waterdropsThread2.is_alive and humanStepsThread.is_alive():
        sounds["sonidoGotasCueva.wav"].stop()
        sounds["sonidoGotasCueva2.wav"].stop()
        sounds["sonidoPasosHumano.wav"].stop()
        waterdropsThread.join()
        waterdropsThread2.join()
        humanStepsThread.join()
    """
    cont = 0
    while cont < 1:
        print("¿Qué quieres hacer? \n1. Hacer una antorcha \n2. Arrojar el palo al fuego")
        decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

        if decision == "1":
            text = "Frederic - Parece que este palo puede servir para hacer una antorcha.\n\n" \
                    "Dios - Frederic, ahora con antorcha en mano, se dispuso a explorar las inmediaciones de la cueva.\n\n" \
                    "Frederic - Ojalá ahora encuentre esa maldita espada. Pero, ¿qué carajo...? Toda la cueva está llena de arañazos y de un extraño líquido verde...\n\n" \
                    "Frederic - ¿Eso es un derrumbe? Veo algo de luz del otro lado... ¿Qué mierda pasó aquí? Este camino está bloqueado...\n\n" \
                    "Frederic - ¿Qué fue eso? ¿Quién está ahí? ¡Sal y pelea, cobarde!"
            func.printText(text, 1)
            # func.playSound(sounds, "sonidoCrafteo.wav", 1, [0, 0, 1], [0, 0, 0], 1, 0, False)
            # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            # func.playSound(sounds, "sonidoRocasCayendo.wav", 0.8, [0, 1, 0], [0, 1, 0], 1, 0, False)
            # func.playSound(sounds, "sonidoMujerGritando.wav", 0.8, [0, 0, -8], [0, 0, -8], 1, 0, False)
            # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.2, [0, 0, -10], [0, 0, 0], 1, 1, False)

            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Devolverse y func.avanzar por el camino de la fogata \n2. Despejar el camino bloqueado")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    text = "Frederic - No sé qué fue eso, mejor me muevo rápido, me devuelvo a la fogata y me preparo para luchar.\n\n" \
                            "Frederic - Aquí está la pechera que compré en rebaja, qué porquería de pechera, casi me cuesta la vida, tiene una gran " \
                            "abertura en el abdomen. ¿Por qué estaba aquí? Las correas están intactas.\n\n" \
                            "Frederic - ¿Quién me la habrá quitado? Bueno, eso no importa, me la pondré, de algo debe servir, esto es mejor que nada."
                    func.printText(text, 1)
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    # func.playSound(sounds, "sonidoBrillo.wav", 1, [0, 0, 1], [0, 0, 1], 1, 0, False)
                    # func.playSound(sounds, "sonidoArmadura.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    cont += 1
                    tiene_pechera = True

                elif decision == "2":
                    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    text = "Frederic - Supongo que puedo intentar salir por donde entré.\n\n" \
                            "Frederic - Carajo llevo varios minutos y estas piedras no se mueven ni un centímetro, maldita sea.\n\n" \
                            "Frederic - Esta cueva es más grande de lo que pensaba, está llena de estalagmitas y de estalactitas, sin quitar " \
                            "de lado esta asquerosa cantidad de murciélagos.\n\n" \
                            "Frederic - Mejor me devuelvo hacia la fogata y me preparo para avanzar."
                    func.printText(text, 1)
                    # func.playSound(sounds, "sonidoRocasCayendo.wav", 1.3, [0, 0, 0], [0, 0, 0], 0.8, 0, False)
                    # func.playSound(sounds, "sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    # func.playSound(sounds, "sonidoMurcielagos.wav", 1.2, [0, 1, 5], [0, 1, 5], 1, 0, False)
                    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    # func.playSound(sounds, "sonidoFogata.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    cont += 1
                    tiene_pechera = False

        elif decision == "2":
            # func.playSound(sounds, "sonidoFuegoIncremento.wav", 1.2, [0, -3, 0], [0, -3, 0], 1, 0, False)
            text = "Frederic - Mierda casi me quemo, el fuego creció demasiado, por lo menos ahora puedo ver lo que está en la cercanía.\n\n" \
                    "Dios - Frederic sin nada de luz para explorar, se sienta a ver la fogata, mientras recuerdos llegan a su mente, luego de eso la fogata se extingue por completo.\n\n" \
                    "Frederic - Ahora solo tengo dos opciones, avanzar por esta cueva o morir de viejo esperando a que pase algo interesante…"
            func.printText(text, 1)
            # func.playSound(sounds, "sonidoFogata.wav", 1, [0, 0, -1], [0, 0, 0], 1, 0, False)
            # func.playSound(sounds, "sonidoBar.wav", 1, [0, 0, -10], [0, 0, -10], 1, 0, False)
            # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            cont += 1
            tiene_pechera = False

    text = "Frederic - Llevo quince minutos caminando, ¿Dónde está la salida?, esta cueva es enorme, al menos veo el camino con este " \
            "río fosforescente color verde vómito.\n\n" \
            "Frederic - Qué suerte la mía, esta cueva será mi tumba y este río apesta a cadáver de grifo.\n\n" \
            "Frederic - ¿Qué es eso?… Bien!!!! mi espada, pensé que no te encontraría, ven aquí preciosa, te besaría, pero no quiero hacerme otra herida.\n\n" \
            "Frederic - Aún manchada de verde tienes tanto filo como las palabras de verónica.\n\n" \
            "Frederic - ¿Qué!!!!!? Veronica, maldición, ¿Dónde está esa sexy clérigo de ojos morados? Mierda dónde están el Jefe y Axcel, Vinimos aquí buscando algo pero… ¿Qué era?\n\n" \
            "Frederic - Céntrate, ahora estoy solo, por lo menos ahora tengo algo para defenderme."
    func.printText(text, 1)
    # func.playSound(sounds, "sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoRecoger.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoDudaFrederic.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

    text = "Dios - Frederic camino otros cinco minutos sin parar de hacerse la misma pregunta, ¿Que paso en la cueva?\n\n" \
            "Frederic - ¿Ah? ¿Qué es eso? Una puerta de madera rota madera, es gigante, parece que llegue al final de este maldito camino, " \
            "pensé que no saldría de aquí, espero que allí esté Veronica esperándome con algun hechizo para recuperarme de esta herida, no puedo esperar para poner mis manos sobre esas curvas…\n\n" \
            "Frederic - Pero que carajo, ¿Una araña? esta cosa es tan grande como un lobo blanco."

    func.printText(text, 1)
    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    # func.playSound(sounds, "sonidoRisaFrederic.wav", 0.8, [0, 0, 0], [0, 0, 0], 1, 2.5, False)
    # func.playSound(sounds, "sonidoAraña.wav", 0.7, [0, 0, 0], [0, 0, 0], 1, 0, False)

    if tiene_pechera:
        # func.playSound(sounds, "sonidoAraña.wav", 0.7, [0, 0, 0], [0, 0, 0], 1, 0, False)
        text = "Frederic - Uh… ¿La pechera? Fue directo al hombro.\n\n" \
                "Frederic - Buen ataque idiota, no falles el próximo, pero espera tu turno, ahora me toca a mí."
        func.printText(text, 0)
        # func.playSound(sounds, "sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 2, 0, False)
        
    else:
        # func.playSound(sounds, "sonidoDolorHombre.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
        text = "Frederic - Ahhh!!! maldición, me diste en el hombro izquierdo ¿eso es ácido?, idiota eso va a dejar cicatriz, ven aquí estúpida arañita, vamos a jugar."
        func.printText(text, 0)
        # func.playSound(sounds, "sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)

    cont = 0
    while cont < 1:
        print("¿Qué quieres hacer? \n1. Atacar \n2. Bloquear y contraatacar \n3. Engañar a la araña")
        decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

        if decision == "1":
            cont += 1
            # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            text = "Frederic - Toma esto idiota ¿Te gustó? ¿Quieres una segunda cita?, Ahg!!!! quédate quieta de una vez"
            func.printText(text, 0)
            # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)

        elif decision == "2":
            cont += 1
            # func.playSound(sounds, "sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 1, 0, False)
            text = "Frederic - ¿Crees que ese ataque podría hacerme algo? No en esta vida, Ahg!!! Eso estuvo cerca, déjame mostrarte cómo se hace."
            func.printText(text, 0)
            # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)

        elif decision == "3":
            cont += 1
            # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            text = "Frederic - Ven aquí, sígueme. \n\n" \
                   "Dios - Frederic para en seco justo después de dar vuelta en una esquina, esperando a que la araña llegara, velozmente " \
                   "utilizó su espada logrando cortarle dos patas lo que la desestabiliza.\n\n" \
                   "Frederic - que se siente eso idiota, vamos ¿Qué haces ahí descansando? ¿No tenías ganas de darme un buen mordisco?.\n\n" \
                   "Frederic - Bueno uno, dos, tres!!!! Toma!!!!! \n\n" \
                   "Dios - Frederic empujó a la araña con una embestida lo que la hizo retroceder y caer en el río verde."
            func.printText(text, 0)
            # func.playSound(sounds, "sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 2, 0, False)

            # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            # func.playSound(sounds, "sonidoRisaFrederic.wav", 0.9, [0, 0, 0], [0, 0, 0], 1, 0, False) 
            # func.playSound(sounds, "sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 2, 0, False)
            # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            # func.playSound(sounds, "sonidoRio.wav", 0.8, [0, -5, 0], [0, -5, 0], 2, 0, False)
            # func.playSound(sounds, "sonidoSplashAgua.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
    """
    """
    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
    print("Frederic - Puff, espero no encontrarme con más de una al mismo tiempo… Ahora debo centrarme en func.avanzar y encontrar a los demás.")
    # func.playSound(sounds, "sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    print("Frederic - ¿Nogh ahora qué? ¿Tres caminos? ¿Esto es un laberinto o es una cueva? A este paso tendré que pensar en quedarme aquí y vender araña asada en un palo.")
    print("Dios - Frederic vacilante pensó cuál camino tomar.")

    if not tiene_pechera:
        # func.playSound(sounds, "sonidoRocasCayendo.wav", 0.8, [0, 1, 0], [0, 1, 0], 1, 0, False)
        print("Frederic - Por el segundo camino veo cráneos, demasiadas telarañas y sangre verde por todos lados, definitivamente no voy a ir ahí a morir.")
        # func.playSound(sounds, "sonidoMurcielagos.wav", 1.2, [-1, 1, 3], [-1, 1, 3], 1, 0, False)

    else:
        print("Frederic - Ahg hay que descartar… bueno, no voy a entrar al primer camino, está demasiado oscuro y algo me dice que alguna cosa me esperaría del otro lado.")
        # func.playSound(sounds, "sonidoViento.wav", 1, [0, 1, 0], [0, 1, 0], 1, 0, False)
    
    cont = 0
    while cont < 1:
        if not tiene_pechera:
            print("¿Qué quieres hacer? \n1. Primer camino(Se ve muy oscuro, pero hay un luz al final) \n3. Tercer camino(Parece el mas seguro, esta muy limpio)")
            decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

        else: 
            print("¿Qué quieres hacer? \n2. Segundo camino(Tiene manchas de sangre y huesos, pero tambien tiene un aroma familiar) \n3. Tercer camino(Parece el mas seguro, esta muy limpio)")
            decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

        print("Frederic - Bueno en marcha, no saldré si no me muevo.")
        # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

        print("Dios - Frederic avanza por la cueva hasta que…")
        # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

        if decision == "1" and not tiene_pechera:
            cont += 1

            # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
            print("Frederic - ¿Qué es eso? Que bien, hay luz al final del túnel, estoy cerca de una salida, pero antes de eso, dónde están mis compañeros, pensándolo bien…")
            # func.playSound(sounds, "sonidoBar.wav", 1, [0, 0, -10], [0, 0, -10], 1, 0, False)

            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Enfocarse en el pensamiento \n2. Ignorar este pensamiento y seguir avanzando")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1

                    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    print("Frederic - Mierda…, ya recorde, vinimos buscando una estupida mazmorra para encontrar un huevo de araña matriarca, nos pagarian una buena cantidad en el mercado negro, demonios chicos, Veronica…, Chef… Axel… Dónde están? Creo que peleamos con algo y eso nos separó… ¿Qué era esa cosa?")
                    # func.playSound(sounds, "sonidoSplashAgua.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)

                elif decision == "2":
                    cont += 1

                    print("Frederic - Nada, no recuerdo que paso, no tiene sentido tener pensamientos intrusivos ahora, tengo que seguir avanzando.")
                    # func.playSound(sounds, "sonidoViento.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Dios - Frederic continúa avanzando hasta que ve a lo lejos una sala de la cueva muy diferente a lo que ya ha visto antes.")
            # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

            print("Frederic - Que maldito  asco, ¿Que pise? ¿Qué es eso?, son cientos de huevos y telarañas… parece la casa de otra asquerosa araña… ENORME!!!, mierda, mierda, puta madre, ya se donde estoy…")
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

            print("Frederic - El nido de la matriarca!!!")
            # func.playSound(sounds, "sonidoPasosJefe.wav", 0.8, [0, 0, -5], [0, 0, -5], 1, 0, False)

            print("Dios - Frédéric al escuchar las fuertes pisadas aproximándose se esconde detrás de unos huevos.")
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, -1, 0], [0, -1, 0], 1.5, 0, False)

            # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.2, [0, 0, -5], [0, 0, -5], 1, 0, False)
            print("Frederic - Ahora que, piensa, piensa, que se supone que haga? Yo solo no soy capaz de matar a esa cosa, debo escapar de aquí de inmediato, pero como?, parece que esa mamá araña quiere comida para sus horribles bebés, carajo.")
            print("Frederic - Me tengo que ir rápido, este asqueroso huevo podrido huele horrible… oh… mierda")
            print("Dios - Frederic sin decir una palabra, observa como entra a la habitación una enorme, horripilante, tenebrosa araña matriarca negra con manchas verdes y con unos grandes colmillos altamente venenosos.")

            # func.playSound(sounds, "sonidoPasosJefe.wav", 1, [0, 0, -3], [0, 0, -3], 1, 0, False)
            print("Frederic - Qué demonios come esa araña en una cueva como esta para estar así, si me enfrento a esa cosa estaré muerto. Fue ella la que causó todo este maldito infierno, fuimos emboscados y nos atrapó, supongo que fui el único que no se llevó por alguna razón, la bastarda me dejo para morir o simplemente no quiso comerme, maldita, todos deben estar aquí.")
            # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Frederic - Demonios… siento algo en la espalda… Esto picha, es un bigote, color blanco, pegado a un enano calvo con cara de enojado, mmm… me parece familiar, OH JEFE! Chef!, esperame ya te voy a sacar de ahí.")
            # func.playSound(sounds, "sonidoAyudaM.wav", 0.8, [1, 0, 0], [1, 0, 0], 1, 0, False)

            print("Dios - Fue entonces que Frederic se dio cuenta que además de haber cientos de huevos a su alrededor, también había docenas de criaturas de diferentes especies atrapadas en capullos de telaraña esperando ser alimento para las crías de arañas.")
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

            print("Chef - Qu…Qué es esto? ¿Dónde estoy? Frede…ric? Dónde estamos, informarme de la situación actual, donde están los demás?")
            # func.playSound(sounds, "sonidoToserM.wav", 0.7, [0, 0, 1], [0, 0, 1], 2, 0, False)

            print("Frederic - Jefecito pensé que lo perdería, los demás están atrapados pero eso no importa, primero voy a sacarte de este capullo, solo deja que te quite esto de encima.")
            # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            # func.playSound(sounds, "sonidoAtrasTuyo.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Chef - Gracias Frede…")
            # func.playSound(sounds, "sonidoAplastado.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Dios - Fue en ese entonces que Frederic bañado en la sangre de su amigo se da cuenta que la araña los había escuchado e inmediatamente mató a Chef para darle sus entrañas a sus crías prontas a nacer.")
            # func.playSound(sounds, "sonidoDudaFrederic.wav", 0.7, [0, 0, 0], [0, 0, 0], 1, 3, False)

            print("Frederic - JEFEEEEE!!! NOOOOO!!!, MIERDA!; MIERDA!, Maldita puta araña,quieres comer, ven aquí idiota!!!, esa es…, a quien está apunto de comerse, no, no, NOOOO ESPERA!!!")
            # func.playSound(sounds, "sonidoGritoMuerte.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Dios - En ese momento Frederic visualizo como entre su boca tiene a Veronica a punto de ser masticada por el monstruo.")
            # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1, [0, 0, 0], [0, 0, 0], 1.75, 0, False)

            print("Frederic - NOOOO MALDITA ARAÑAS, PELEA COBARDE, SUELA A VERONICA AHHHHH")
            # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
        
            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Atacar a las patas. \n2. Atacar a la mandibula")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1

                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 1, 0], [0, 1, 0], 1, 0, False)
                    print("Dios - Después de un golpe certero, hace que la araña se descuide y choque con una roca que le cae en la cabeza, el monstruo grita del dolor cayendo al suelo momentáneamente.")
                    # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1, [0, 1, 0], [0, 1, 0], 2, 0, False)

                    print("Frederic - voy por ti hermosura, espero que después de esta salvada épica me des por fin una cita.")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

                    print("Dios - Frederic inmediatamente al inmovilizar a la araña matriarca abre su mandíbula y entra ligeramente. ")
                    # func.playSound(sounds, "sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
                    
                    print("Frederic - Ya casi te saco, ah!!! vamos.")
                    print("Dios - Sin embargo en ese momento la araña matriarca despierta y de un solo acto reflejo…")
                    # func.playSound(sounds, "sonidoHeridaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                
                elif decision == "2":
                    cont += 1

                    print("Frederic - Es todo o nada, voy a lanzar la espada, ten cuidado Veronica, Sueltala!!!")
                    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    print("Dios - Derrepente Frederic logra herir a la araña en su mandíbula, la araña enojada empezó a acercarse a Frederic ahora sin un arma en sus manos…")
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 1, 0], [0, 1, 0], 1, 0, False)

                    print("Frederic - Quieres un poco mas idiota? ven, acercate viejo. ")
                    print("Dios - Aunque se encontraba motivado por el auge de la batalla, Frederic recordó sus anteriores palabras, “Yo solo no soy capaz de matar a esa cosa”, palabras que lo condenaron, pues al ver a los ojos a esa araña se dio cuenta de que no podía ganar.")
            
            print("Frederic - Con un demonio, lo que faltaba…")
            # func.playSound(sounds, "sonidoAplastado.wav", 1, [0, 0, 0], [0, 0, 0], 1, 3, False)
            
            # func.playSound(sounds, "sonidoAraña.wav", 0.8, [0, 0, 0], [0, 0, 0], 2, 0, False)
            print("Dios - Completamente machacado, lamentablemente Frederic y Verónica son comidos por la araña matriarcado, esparciendo sangre y tripas por toda la sala para que sus hijos se alimenten. ")
            # func.playSound(sounds, "sonidoDerrota.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Final Malo(#1)")
        
        elif decision == "2" and tiene_pechera:
            cont += 1
            print("Frederic - Mmm, esto parece un precipicio, está demasiado alto, no veo ninguna otra salida por alguna dirección, solo hacia abajo.")
            # func.playSound(sounds, "sonidoSuspiro.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Regresar. \n2. Saltar \n:")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    # func.playSound(sounds, "sonidoRocasCayendo.wav", 0.8, [0, 1, 0], [0, 1, 0], 1, 0, False)
                    print("Frederic - Mejor me devuelvo no hay salida por este lado, tal vez por otro camino, yo pueda, AH! otra araña!!!.")
                    # func.playSound(sounds, "sonidoAraña.wav", 0.8, [0, 0, -1], [0, 0, -1], 2, 0, False)
                    
                    print("Dios - Inmediatamente Frederic fue atacado por una araña que lo vio entrar al lugar, logrando empujarlo hacia el precipicio, donde ambos cayeron varios metros.")
                    # func.playSound(sounds, "sonidoGritoMuerte.wav", 0.8, [0, 0, 1], [0, 0, 1], 1, 0, False)
                    
                    print("Frederic - Ahhhh, ¿Que hago?, ahora estoy cayendo, Carajo muerete ya. ")
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 1, 0], [0, 1, 0], 2, 0, False)
                    
                    print("Dios - Frederic rápidamente usa el cuerpo de la araña muerta para usarla como cuerpo de soporte para aguantar un poco la caída y que él no sufra lesiones graves.")
                    # func.playSound(sounds, "sonidoCaida.wav", 1.2, [0, 0, 0], [0, 0, 0], 1, 3, False)
                    
                elif decision == "2":
                    cont += 1
                    print("Frederic - Supongo que solo queda ir hacia abajo y rogar para no morir.")
                    
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    print("Dios - Fue en ese entonces que Frederic, cae un par de metros hasta que choca con varias telarañas rompiendolas unas tras otras pero logrando reducir su velocidad lo suficiente hasta caer al fondo sin daños graves.")
                    # func.playSound(sounds, "sonidoRocasCayendo.wav", 1.2, [0, 0, 0], [0, 0, 0], 2, 0, False)
        
            print("Frederic - Ahg, Mierda pense que no la contaba, estoy en una pieza aunque siento que me he roto algo, como sea, ¿dónde estoy?, un momento… ")
            # func.playSound(sounds, "sonidoHeridaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Frederic - Huevos… telarañas… demonios, esto es… un nido de arañas, entonces debe haber una matriarca cerca, debe ser la misma que causó todo este problema, ")
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)

            print("Frederic - Parece que cuando entramos fuimos emboscados y nos atrapó, sin embargo me debió dejar atrás por estar en ese líquido asqueroso y cubierto de lodo, todos deben estar aquí, espero que estén vivos.")
            print("Dios - Rápidamente Frederic busco entre los cuerpos enredados para encontrar a sus amigos")
            # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Frederic - Esa es?…VERONICA!, Esperame, ya te saco.")
            # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            
            print("Veronica - … Freder…ic? ¿Eres tu?")
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 2, 0, False)
            
            print("Frederic - Si, me alegra que estés con vida, estás un poco herida según veo, pero así solo te ves más sexy. ")
            # func.playSound(sounds, "sonidoBeso.wav", 1, [0, 0, 0], [0, 0, 0], 1, 3, False)
        
            print("Veronica - Quítate!!!, ni en esta situación puedes estar serio?, como sea, no tengo heridas graves, ¿vez mi mochila por algún lado?")
            # func.playSound(sounds, "sonidoCaida.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            
            print("Frederic - Si, está al lado de dos hombres bestia que no lo lograron, qué pasa con ella?")
            print("Veronica - Necesita que la traigas, ahi tengo una botella de maná, necesito recuperar energía para usar algún hechizo de curación.")
            print("Dios - Frederic camino hasta la mochila con cuidado de no despertar ninguna cría y llevarle la poción a Veronica.")
            # func.playSound(sounds, "sonidoRecoger.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

            print("Frederic - Toma, bébetela toda, no dejes ni una gota, así crecerás grande y fuerte.")
            # func.playSound(sounds, "sonidoRisaFrederic.wav", 0.9, [0, 0, 0], [0, 0, 0], 1.5, 0, False) 

            print("Veronica - Callate.")

            # func.playSound(sounds, "sonidoBotella.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            print("Veronica - Aún estoy herida pero creo tener la suficiente energía para hacer algunos hechizos.")
            
            print("Dios - Inmediatamente Verónica cura a Frederic y a ella misma.")
            # func.playSound(sounds, "sonidoHealing.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            
            print("Frederic - Excelente, Ahora me siento mejor, gracias preciosa, busquemos a los otros y larguémonos de aquí.")
            
            # func.playSound(sounds, "sonidoPasosJefe.wav", 1, [0, 0, -3], [0, 0, -3], 1, 0, False)
            print("Veronica - Esa araña va a ser un problema.")
            
            print("Dios - Fue en ese preciso momento que vieron a la distancia en lugares opuestos a Axel y Chef, uno entre varios huevos de araña herido y el otro atrapado en un capullo de telaraña, sin embargo, justamente en ese momento llega la araña matriarca.")
            # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.2, [0, 0, -10], [0, 0, 0], 1.5, 1, False)
            
            print("Veronica - Debemos salvar a ambos, pero ahora solo podemos sacar a uno… que… que hacemos Frederic?")
            # func.playSound(sounds, "sonidoPasosJefe.wav", 1, [0, 0, -2], [0, 0, -2], 1.5, 0, False)
            
            print("Dios - Frederic estaba en una situación terrible donde solo tenían suficiente tiempo para sacar a uno momentáneamente.")
            print("Frederic - Que hago? Chef es nuestro tranque, cocinero, jefe y maestro, puede ser de gran ayuda pero no sé si necesitamos fuerza bruta o las extrañas habilidades de Axel, al ser un asesino especializado en sigilo, puede enfocarse en ataques vitales… ¿Qué carajo hago? ")
            # func.playSound(sounds, "sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            
            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Salvar a Chef. \n2. Salvar a Axel")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    print("Frederic - Rapido Verónica, ve por Chef, nos será de más utilidad ahora, curalo y prepárense para luchar, yo lo distraigo por ahora.")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

                    print("Veronica - Entendido")
                    print("Frederic - Eh!!! Asquerosa araña ves esto¿Te gustó?.")
                    # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.5, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    
                    print("Dios - En ese momento, Frederic ya recuperado y con su fuerza al máximo comienza el ataque enfocándose en sus patas, corriendo por todos lados y dándole el mayor tiempo posible a Verónica.")
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Chef - Ho…Hola? Veronica, vaya <sonidos de gritos>, que agradable sorpresa, puedo ver la situación, vamos hay que acabar con esa araña matriarca, está demasiado agresiva por la temporada de apareamiento. ")
                    # func.playSound(sounds, "sonidoToserM.wav", 0.7, [0, 0, 1], [0, 0, 1], 2, 0, False)
                    
                    print("Frederic - jajajaja Chef, te veo bien anciano, mejor ven y dame una mano antes de que lo mate yo ah!!!.")
                    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Chef - Silencio Frederic, ahora te enseño cómo acabar con un monstruo de esa calidad, rápido, Veronica quédate atrás de Frederic, Frederic ve por atrás.")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Dios - Chef lider del grupo, ya recuperado utiliza un hechizo de encantamiento para atraer la atención de la araña matriarca y absorber daño para desencadenarlo en un fuerte impacto en su punto débil el abdomen mientras los demás la atacan por detrás sin preocuparse en ser objetivo de daño.")
                    # func.playSound(sounds, "sonidoEnchanter.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    # func.playSound(sounds, "sonidoHealing.wav", 1, [0, 0, 0], [0, 0, 0], 1, 1, False)
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    
                    print("Frederic - Vamos Veronica prendele fuego, haz que brille. ")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Veronica - Entendido ")
            
                elif decision == "2":
                    cont += 1
                    print("Frederic - Rapido Verónica, ve por Axel, nos será de más utilidad tener el mayor daño posible, curalo y prepárense para luchar, yo lo distraigo por ahora.")

                    print("Veronica - Entendido")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

                    # func.playSound(sounds, "sonidoPasosJefe.wav", 1, [0, 0, -2], [0, 0, -2], 1.5, 0, False)
                    print("Frederic - Eh!!! Asquerosa araña ves esto ¿Te gustó? ")
                    # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.5, [0, 0, 0], [0, 0, 0], 1.5, 0, False)

                    print("Dios - En ese momento, Frederic ya recuperado y con su fuerza al máximo comienza el ataque enfocándose en sus patas, corriendo por todos lados y dándole el mayor tiempo posible a Verónica.")
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Axel - Ughhh!!!, maldita sea que asco, puaj, vaya, Veronica eres tu, gracias, ¿Como te lograste liberar? ")
                    # func.playSound(sounds, "sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    
                    print("Veronica - No, me salvo Frederic, pero ahora lo más importante es acabar con esa cosa.")
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Axel - jejejejeje ya veo, interesante, muy divertido, hagámoslo VAMOS!, OYEEE FREDERIC!")
                    # func.playSound(sounds, "sonidoManiatico.wav", 1, [0, 0, 0], [0, 0, 0], 1.25, 0, False)
                    
                    print("Frederic - jajajaja hijo de perra, ya estás bien, muévete ya, dame una mano.")
                    # func.playSound(sounds, "sonidoRisaFrederic.wav", 0.9, [0, 0, 0], [0, 0, 0], 1.5, 0, False) 
                    
                    print("Axel - Claro, no te voy a dejar toda esta diversión, jejejejeje, ahora escuchen, Veronica, apoyanos desde atrás, Frederic la distrae mientras yo la apuñalo, el jefe dijo que en el abdomen es débil, JEJEJE.")
                    print("Dios - Axel psicomaniatico del grupo, enfocó su daño en el abdomen mientras Veronica golpeaba en la cabeza a la araña y engañándole con un encantamiento de espejismo, mientras Frederic golpea con gran fuerza desde el otro extremo, con la ayuda de un potenciador de Veronica.")
                    # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)

                    print("Frederic - No te emociones demasiado Axel.")
                    # func.playSound(sounds, "sonidoHealing.wav", 1, [0, 0, 0], [0, 0, 0], 1, 1, False)
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)

                    print("Axel - jejejeje!")
                    # func.playSound(sounds, "sonidoManiatico.wav", 1, [0, 0, 0], [0, 0, 0], 1.25, 0, False)

            print("Dios - Después de una gran lucha, logran salir con vida del encuentro, salvando de paso al otro compañero atrapado, tomando como recompensa un huevo de araña matriarcal y equipo de aventureros caídos, eliminando el resto de arañas para así lograr salir de la tumba de la seda, una de las mazmorras más engañosas por la que han pasado este grupo de mercenarios.")
            # func.playSound(sounds, "sonidoVictoria.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Final Bueno(#2)")
    
        elif decision == "3":
            cont += 1
            print("Frederic - Vaya, al parecer es un camino bastante seguro, me parece extraño que no vea rastro de monstruos o humanos.")
            # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)

            print("Frederic - ¿Dónde estarán los chicos? Carajo.")
            # func.playSound(sounds, "sonidoDudaFrederic.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Dios - Fue en ese entonces que a través de unos agujeros naturales logró ver al otro lado una gran sala muy diferente a las otras, llena de huevos y telaraña.")
            # func.playSound(sounds, "sonidoRocasCayendo.wav", 1.2, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Frederic - Pero que carajo, eso es un nido de araña matriarca, seguramente la madre de las arañas, Mejor sigo moviendome antes de que algo me vea…")
            # func.playSound(sounds, "sonidoPasosJefe.wav", 1, [0, 0, -3], [0, 0, -3], 1, 0, False)

            print("Dios - Frederic justo antes de seguir avanzando observa como entra a la habitación una enorme, horripilante, tenebrosa araña matriarca negra con manchas verdes y con unos grandes colmillos altamente venenosos . ")
            # func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)

            print("Frederic - Parece que cuando entramos fuimos emboscados y nos atrapó, sin embargo me debió dejar atrás por estar en ese líquido asqueroso y cubierto de lodo, todos deben estar aquí, espero que estén vivos.")
            print("Dios - Fue entonces que Frederic se dio cuenta que estaba atrapado Axel ahí, envuelto como capullo en telaraña, además de haber huevos a su alrededor, también había criaturas de diferentes especies atrapadas esperando ser alimento para las crías de arañas.")
            # func.playSound(sounds, "sonidoBaba.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
            
            print("Frederic - AXEL!, espera, si el esta ahi y no he visto ningún rastro de los demás, entonces ahí estarán los otros, MIERDA!")
            print("Axel - Con que hasta allí estás… TE LOGRO VER FEDERIC SACAME HIJO DE PERRA…")
            # func.playSound(sounds, "sonidoToserM.wav", 0.7, [0, 0, 4], [0, 0, 4], 1, 0, False)
            
            print("Frederic - AXEL!!! NO TE MUERAS; YA VOY POR USTEDES!!!")
            
            # func.playSound(sounds, "sonidoToserM.wav", 0.7, [0, 0, 4], [0, 0, 4], 2, 0, False)
            print("Axel - jajajaja, lo siento hermano, pero eso no va a ser posible, no hay forma sencilla de atravesar los muros, ya lo intente… lo siento… pero debes irte, escapa co… co… con… vida.")
            # func.playSound(sounds, "sonidoGritoMuerte.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
            
            print("Frederic - AXEL!!! IDIOTA!!! AXEL!!! AXEEEEEL!!!")
            
            # func.playSound(sounds, "sonidoPasosJefe.wav", 1, [0, 0, 3], [0, 0, 3], 1, 0, False)
            print("Dios - Fue entonces que la araña matriarca, saca entre varios montículos de cuerpos a Verónica para comérsela.")
            print("Frederic - Veronica!!!, que hago, no tengo suficiente tiempo para volver y no creo ser capaz de abrir este agujero lo suficientemente para pasar, Mierda!.")
            # func.playSound(sounds, "sonidoEspada.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
            
            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Gritar. \n2. Rendirse \n:")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    # func.playSound(sounds, "sonidoAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    print("Dios - En ese momento Frederic grita logrando atraer a la araña matriarca, la cual de un grito mucho mayor al de él, hace que despierten todas sus crías las cuales salen corriendo hacia él.")
                    # func.playSound(sounds, "sonidoAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    
                    print("Frederic - Mierda, son demasiadas, debo salir rápido o voy a morir, ATRÁS MALDITOS BICHOS!! AHHHHHHHH!!!!.")
                    # func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, [0, 0, 0], [0, 0, 0], 1, 2, False)
                    
                    print("Dios - Después de una gran pelea contra las crías de araña, Frederic logra salir vivo de la cueva.")
                    # func.playSound(sounds, "sonidoPasosHumano.wav", 0.8, [0, -1, 0], [0, -1, 0], 0.8, 0, False)

                    print("Frederic - Maldición, estoy vivo, gracias a Rumania, esos malditos me quitaron el brazo, tengo que curarme rápido… mierda mis amigos…... no los pude salvar, ya deben estar muertos, MIERDAAAAAAAA!!!!.")

                elif decision == "2":
                    print("Frederic - Carajo… tal vez si yo… solamente yo… fuera capaz de hacer algo lo haría, pero… no soy capaz, perdonenme <Sonido de Correr>.")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)
                    
                    print("Dios - Frederic ante la situación y el miedo que le recorría todo el cuerpo decidió abandonar a sus amigos a la suerte, llegando hasta esa luz que vio anteriormente que era la salida de la cueva.")
                    # func.playSound(sounds, "sonidoCorrerHumano.wav", 1, [0, 0, 0], [0, 0, 0], 1.5, 0, False)

                    print("Frederic - yo….")
                    # func.playSound(sounds, "sonidoGritoMuerte.wav", 1.5, [0, 0, 0], [0, 0, 0], 1, 0, False)
                    cont += 1

            print("Dios - Después de salir con vida de la cueva, Frederic herido logra llegar hasta el pueblo más cercano para pedir ayuda, enterrando esta historia de su vida como un recordatorio del día que perdió a sus amigos, su brazo y su vida como aventurero.")
            # func.playSound(sounds, "sonidoNeutral.wav", 1, [0, 0, 0], [0, 0, 0], 1, 0, False)
    
    print("FIN")
        """
    # Clean and close openAL
    oalQuit()

# start the game
main()
