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
    # sound dictionary
    sounds = func.obtainingSound()

    startThread = func.playSound(sounds, "sonidoEmpezar.wav", 0.8, 1.5, [0, 0, -1], 3.5, False, "static")
    if startThread.is_alive(): sounds["sonidoEmpezar.wav"].stop() and startThread.join()
    # Loading screen
    func.loadingScreen()
    menuThread = func.playSound(sounds, "sonidoInicioMenu.wav", 0.8, 1, [0, 0, 0], 0, True, "static")
    if menuThread.is_alive():
        try:
            input("\n                         Presiona enter para continuar...                            \n\n")
        finally:
            sounds["sonidoInicioMenu.wav"].stop() and menuThread.join()
    # Console Cleaning
    os.system('cls')

    tiene_pechera = False
    text = "Dios - Frederic es un aventurero común y corriente que hace parte de un grupo de mercenarios, donde él despierta después de una exploración que salió mal y con un fuerte dolor de cabeza."
    WindThread = func.playSound(sounds, "sonidoViento.wav", 1, 2, [0, 1, 0], 0, False, "static")
    func.playerInteraction(sounds, "continue", text, WindThread, "sonidoViento.wav", 1)

    text = "Frederic - Ahg que.. que paso? ¿Dónde estoy? No veo absolutamente nada, hay un olor a humo, estoy mojado y repleto de lodo."
    waterdropsThread = func.playSound(sounds, "sonidoGotasCueva.wav", 0.3, 1, [1, 0, 0], 1, True, "static")
    waterdropsThread2 = func.playSound(sounds, "sonidoGotasCueva2.wav", 0.05, 1, [-1, 0, 0], 1, True, "static")
    func.printText(text, 0)
    
    cont = 0
    while cont < 1:
        print("¿Qué quieres hacer? \n1. Levantarse \n2. Mirar a tu alrededor")
        decision = func.playerInteraction(sounds, "selection", "", "", "", 0)
        
        if decision == "1":
            text = "Frederic - ¿Qué es esto? ¿una herida? Mierda tengo una cortada infectada en el abdomen."
            hurtThread = func.playSound(sounds, "sonidoHeridaFrederic.wav", 1, 1, [0, 0, 0], 0, False, "static")
            func.playerInteraction(sounds, "continue", text, hurtThread, "sonidoHeridaFrederic.wav", 0)

            print("¿Qué quieres hacer? \n1. Inspeccionar cuerpo \n2. Caminar")
            decision = func.playerInteraction(sounds, "selection", "", "", "", 0)
            if decision == "1":
                text = "Frederic - Qué carajo, no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo, mejor voy para allá."
                doubtThread = func.playSound(sounds, "sonidoDudaFrederic.wav", 0.8, 1, [0, 0, 0], 0, False, "static")
                func.playerInteraction(sounds, "continue", text, doubtThread, "sonidoDudaFrederic.wav",  0)
                cont += 1
            else:
                cont +=1

        elif decision == "2":
            text = "Frederic - Qué carajo no se ve nada alrededor, ¿Uh?… ¿Qué es eso? Algo brilla al fondo."
            doubtThread = func.playSound(sounds, "sonidoDudaFrederic.wav", 0.8, 1, [0, 0, 0], 0, False, "static")
            func.playerInteraction(sounds, "continue", text, doubtThread, "sonidoDudaFrederic.wav", 0)

            print("¿Qué quieres hacer? \n1. Levantarse \n2. Caminar")
            decision = func.playerInteraction(sounds, "selection", "", "", "", 0)
            if decision == "1":
                text = "Frederic - ¿Qué es esto? ¿una herida? Mierda tengo una cortada en el abdomen, mejor me muevo de acá."
                hurtThread = func.playSound(sounds, "sonidoHeridaFrederic.wav", 1, 1, [0, 0, 0], 0, False, "static")
                func.playerInteraction(sounds, "continue", text, hurtThread, "sonidoHeridaFrederic.wav", 0)
                cont += 1
            else:
                cont +=1

    humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1, 1, [0, -3, 0], 2, False, "static")
    bonfireStop = func.threading.Event()
    bonfireThread = func.playSound(sounds, "sonidoFogata.wav", 4, 1, [0, 0, 5], 0, True, "move", bonfireStop)
    text = "Frederic - Parece que estoy en una especie de cueva. ¿Dónde demonios está mi equipo? Demonios, esa espada me costó tanto \
            como una semana en el burdel. Me acercaré a esa luz; puede que encuentre algo de utilidad o ver algo.\n\n \
            Dios - Frederic, confundido y sin saber dónde está, se acerca a la luz con cautela.\n\n \
            Frederic - ¿Una fogata? ¿Qué hace una fogata aquí?, No veo nada de relevancia excepto este palo seco."
    func.playerInteraction(sounds, "continue", text, humanStepsThread, "sonidoPasosHumano.wav", 0)
    
    cont = 0
    while cont < 1:
        print("¿Qué quieres hacer? \n1. Hacer una antorcha \n2. Arrojar el palo al fuego")
        decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

        if decision == "1":
            craftThread = func.playSound(sounds, "sonidoCrafteo.wav", 1, 1, [0, 0, 1], 1, False, "static")
            if craftThread.is_alive(): sounds["sonidoCrafteo.wav"].stop() and craftThread.join()
            text = "Dios - Frederic, ahora con antorcha en mano, se dispuso a explorar las inmediaciones de la cueva"
            humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1, 1, [0, -3, 0], 2, False, "static")
            func.playerInteraction(sounds, "continue", text, humanStepsThread, "sonidoPasosHumano.wav", 0)
            slimeThread = func.playSound(sounds, "sonidoBaba.wav", 1, 1, [0, 0, 0], 5, False, "static")
            if slimeThread.is_alive(): sounds["sonidoBaba.wav"].stop() and slimeThread.join()
            text = "Frederic - Ojalá ahora encuentre esa maldita espada. Pero, ¿qué carajo...? Toda la cueva está llena de arañazos y de un extraño líquido verde... \
                    ¿Eso es un derrumbe? Veo algo de luz del otro lado... ¿Qué mierda pasó aquí? Este camino está bloqueado... ¿Qué fue eso? Mierda mi antorcha, ¿Quién está ahí? ¡Sal y pelea, cobarde!"
            func.printText(text, 0)
            screamThread = func.playSound(sounds, "sonidoMujerGritando.wav", 0.5, 1, [-2, 0, 0], 6, False, "static")
            roarThread = func.playSound(sounds, "sonidoMonstruoRugido.wav", 0.7, 1, [-2, 0, 0], 8, False, "static")
            if screamThread.is_alive(): sounds["sonidoMujerGritando.wav"].stop() and screamThread.join()
            if roarThread.is_alive(): sounds["sonidoMonstruoRugido.wav"].stop() and roarThread.join()
            
            # Stop bonfire
            if bonfireThread.is_alive():bonfireStop.set() and bonfireThread.join()
    
            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Avanzar por el unico camino \n2. Despejar el camino bloqueado")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, -3, 0], 4, False, "static")
                    if humanRunThread.is_alive(): sounds["sonidoCorrerHumano.wav"].stop() and humanRunThread.join()
                    armorThread = func.playSound(sounds, "sonidoArmadura.wav", 1, 1, [0, -3, 0], 1, False, "static")
                    text = "Frederic - No sé qué fue eso, mejor me preparo para luchar.\n\n \
                            Frederic - Aquí está la pechera que compré en rebaja, qué porquería de pechera, casi me cuesta la vida, tiene una gran \
                            abertura en el abdomen. ¿Por qué estaba aquí? Las correas están intactas.\n\n \
                            Frederic - ¿Quién me la habrá quitado? Bueno, eso no importa, me la pondré, de algo debe servir, esto es mejor que nada."
                    func.playerInteraction(sounds, "continue", text, armorThread, "sonidoArmadura.wav", 1)
                    tiene_pechera = True
                    cont += 1

                elif decision == "2":
                    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
                    humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1, 1, [0, -3, 0], 2, False, "static")
                    func.playerInteraction(sounds, "continue", text, humanStepsThread, "sonidoPasosHumano.wav", 0)
                    batThread = func.playSound(sounds, "sonidoMurcielagos.wav", 1, 1, [0, 5, 5], 1, False, "static")
                    if batThread.is_alive(): sounds["sonidoMurcielagos.wav"].stop() and batThread.join()
                    text = "Frederic - Supongo que puedo intentar salir por donde entré.\n\n \
                            Frederic - Carajo llevo varios minutos y estas piedras no se mueven lo suficiente.\n\n \
                            Frederic - Esta cueva es más grande de lo que pensaba, está llena de estalagmitas y de estalactitas, sin quitar \
                            de lado esta asquerosa cantidad de murciélagos.\n\n \
                            Frederic - Mejor me preparo para avanzar por el otro camino."
                    rocksThread = func.playSound(sounds, "sonidoRocasCayendo.wav", 1, 1, [0, 0, 0], 2, False, "static")
                    func.playerInteraction(sounds, "continue", text, rocksThread, "sonidoRocasCayendo.wav", 1)
                    tiene_pechera = False
                    cont += 1

        elif decision == "2":
            fireThread = func.playSound(sounds, "sonidoFuegoIncremento.wav", 1.2, 1, [0, -3, 0], 1, False, "static")
            if fireThread.is_alive(): sounds["sonidoFuegoIncremento.wav"].stop() and fireThread.join()
            text = "Frederic - Mierda casi me quemo, el fuego creció demasiado, por lo menos ahora puedo ver lo que está en la cercanía.\n\n" \
                    "Dios - Frederic sin nada de luz para explorar, se sienta a ver la fogata, mientras recuerdos llegan a su mente, luego de eso la fogata se extingue por completo.\n\n" \
                    "Frederic - Ahora solo tengo dos opciones, avanzar por esta cueva o morir de viejo esperando a que pase algo interesante… avanzare."
            barThread = func.playSound(sounds, "sonidoBar.wav", 1, 1, [0, 0, -10], 1, False, "static")
            func.playerInteraction(sounds, "continue", text, barThread, "sonidoBar.wav", 1)
            # Stop bonfire
            if bonfireThread.is_alive():bonfireStop.set() and bonfireThread.join()
            cont += 1
            tiene_pechera = False

    # Stop WaterDrops
    if waterdropsThread.is_alive() and waterdropsThread2.is_alive(): sounds["sonidoGotasCueva.wav"].stop() and sounds["sonidoGotasCueva2.wav"].stop() and waterdropsThread.join() and waterdropsThread2.join()

    humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1, 1, [0, -3, 0], 2, True, "static")
    riverThread = func.playSound(sounds, "sonidoRio.wav", 0.8, 1, [0, -5, 0], 1, True, "static")
    text = "Frederic - Llevo quince minutos caminando, ¿Dónde está la salida?, esta cueva es enorme, al menos veo el camino con este " \
            "río fosforescente color verde vómito.\n\n" \
            "Frederic - Qué suerte la mía, esta cueva será mi tumba y este río apesta a cadáver de grifo.\n\n" \
            "Frederic - ¿Qué es eso?… Bien!!!! mi espada, pensé que no te encontraría, ven aquí preciosa, te besaría, pero no quiero hacerme otra herida.\n\n" \
            "Frederic - Aún manchada de verde tienes tanto filo como las palabras de verónica.\n\n" \
            "Frederic - ¿Qué!!!!!? Veronica, maldición, ¿Dónde está esa sexy clérigo de ojos morados? Mierda dónde están el Jefe y Axcel, Vinimos aquí buscando algo pero… ¿Qué era?\n\n" \
            "Frederic - Céntrate, ahora estoy solo, por lo menos ahora tengo algo para defenderme."
    takeThread = func.playSound(sounds, "sonidoRecoger.wav", 0.8, 1, [0, -5, 0], 6, False, "static")
    func.playerInteraction(sounds, "continue", text, takeThread, "sonidoRecoger.wav", 1)

    laughterThread = func.playSound(sounds, "sonidoRisaFrederic.wav", 0.8, 1, [0, -5, 0], 5, False, "static")
    text = "Dios - Frederic camino otros cinco minutos sin parar de hacerse la misma pregunta, ¿Que paso en la cueva?\n\n \
            Frederic - ¿Ah? ¿Qué es eso? Una puerta de madera rota madera, es gigante, parece que llegue al final de este maldito camino, \
            pensé que no saldría de aquí, espero que allí esté Veronica esperándome con algun hechizo para recuperarme de esta herida, no puedo esperar para poner mis manos sobre esas curvas…"
    func.playerInteraction(sounds, "continue", text, laughterThread, "sonidoRisaFrederic.wav", 1)
    # Stop human Steps
    if humanStepsThread.is_alive(): sounds["sonidoPasosHumano.wav"].stop() and humanStepsThread.join()
    spiderThread = func.playSound(sounds, "sonidoAraña.wav", 0.7, 1, [2, 0, 0], 2, False, "static")
    text = "Frederic - Pero que carajo, ¿Una araña? esta cosa es tan grande como un lobo blanco."
    func.playerInteraction(sounds, "continue", text, spiderThread, "sonidoAraña.wav", 0)

    if tiene_pechera:
        spiderThread = func.playSound(sounds, "sonidoAraña.wav", 0.7, 1, [0, 0, 0], 2, False, "static")
        text = "Frederic - Uh… ¿La pechera? Fue directo al hombro.\n\n" \
                "Frederic - Buen ataque idiota, no falles el próximo, pero espera tu turno, ahora me toca a mí."
        func.playerInteraction(sounds, "continue", text, spiderThread, "sonidoAraña.wav", 0)
    else:
        hurtThread = func.playSound(sounds, "sonidoDolorHombre.wav", 1, 1, [0, 0, 0], 1, False, "static")
        if hurtThread.is_alive(): sounds["sonidoDolorHombre.wav"].stop() and hurtThread.join()
        text = "Frederic - Ahhh!!! maldición, me diste en el hombro izquierdo ¿eso es ácido?, idiota eso va a dejar cicatriz, ven aquí estúpida arañita, vamos a jugar."
        sighThread = func.playSound(sounds, "sonidoSuspiro.wav", 1, 1, [0, 0, 0], 2, False, "static")
        func.playerInteraction(sounds, "continue", text, sighThread, "sonidoSuspiro.wav", 0)

    cont = 0
    while cont < 1:
        print("¿Qué quieres hacer? \n1. Atacar \n2. Bloquear y contraatacar \n3. Engañar a la araña")
        decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

        if decision == "1":
            cont += 1
            attackThread = func.playSound(sounds, "sonidoEspada.wav", 1, 1, [0, 0, 0], 1, False, "static")
            if attackThread.is_alive(): sounds["sonidoEspada.wav"].stop() and attackThread.join()
            text = "Frederic - Toma esto idiota ¿Te gustó? ¿Quieres una segunda cita?, Ahg!!!! quédate quieta de una vez"
            attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
            func.playerInteraction(sounds, "continue", text, attackSpiderThread, "sonidoAtaqueAraña.wav", 0)

        elif decision == "2":
            cont += 1
            spiderThread = func.playSound(sounds, "sonidoAraña.wav", 0.7, 1, [2, 0, 0], 2, False, "static")
            if hurtThread.is_alive(): sounds["sonidoAraña.wav"].stop() and hurtThread.join()
            text = "Frederic - ¿Crees que ese ataque podría hacerme algo? No en esta vida, Ahg!!! Eso estuvo cerca, déjame mostrarte cómo se hace."
            attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
            func.playerInteraction(sounds, "continue", text, attackSpiderThread, "sonidoAtaqueAraña.wav", 0)

        elif decision == "3":
            cont += 1
            humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, -3, 0], 4, False, "static")
            if humanRunThread.is_alive(): sounds["sonidoCorrerHumano.wav"].stop() and humanRunThread.join()
            text = "Frederic - Ven aquí, sígueme. \n\n \
                    Dios - Frederic espero pacientemente en una esquina a que la araña llegara, para hacerla caer en su plan.\n\n \
                    Frederic - Vamos ¿Qué haces ahí descansando? ¿No tenías ganas de darme un buen mordisco?... Ven!!! \n\n \
                    Dios - Al atacar la araña, Frederic la ataco directamente lo que la hizo retroceder y caer en el río verde."
            attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
            func.playerInteraction(sounds, "continue", text, attackSpiderThread, "sonidoAtaqueAraña.wav", 0)
            SplashThread = func.playSound(sounds, "sonidoSplashAgua.wav", 1, 1, [0, -5, 0], 3, False, "static")
            if SplashThread.is_alive(): sounds["sonidoSplashAgua.wav"].stop() and SplashThread.join()

    attackThread = func.playSound(sounds, "sonidoEspada.wav", 1, 1, [0, 0, 0], 1, False, "static")
    if attackThread.is_alive(): sounds["sonidoEspada.wav"].stop() and attackThread.join()        
    text = "Frederic - Puff, espero no encontrarme con más de una al mismo tiempo… Ahora debo centrarme en avanzar y encontrar a los demás."
    sighThread = func.playSound(sounds, "sonidoSuspiro.wav", 1, 1, [0, 0, 0], 2, False, "static")
    func.playerInteraction(sounds, "continue", text, sighThread, "sonidoSuspiro.wav", 1)

    # Stop River
    if riverThread.is_alive(): sounds["sonidoRio.wav"].stop() and riverThread.join()

    # func.playSound(sounds, "sonidoPasosHumano.wav", 1, [0, -1, 0], [0, -1, 0], 1, 0, False)
    text = "Dios - Frederic despues de atravezar el marco de puerta, se encontro con una dura decision.\n\n \
            Frederic - ¿Nogh ahora qué? ¿2 caminos? ¿Esto es un laberinto o es una cueva? A este paso tendré que pensar en quedarme aquí y vender araña asada en un palo.\n\n \
            Dios - Frederic vacilante pensó cuál camino tomar."
    doubtThread = func.playSound(sounds, "sonidoDudaFrederic.wav", 0.8, 1, [0, 0, 0], 1, False, "static")
    func.playerInteraction(sounds, "continue", text, doubtThread, "sonidoDudaFrederic.wav", 0)
    
    cont = 0
    while cont < 1:
        if not tiene_pechera:
            cont += 1
            humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1, 1, [0, -3, 0], 2, True, "static")
            text = "Frederic - Por el segundo camino veo cráneos, demasiadas telarañas y sangre verde por todos lados, definitivamente no voy a ir ahí a morir, mejor me voy por el primer camino.\n\n \
                    Frederic - ¿Qué es eso? Que bien, hay luz al final del túnel, estoy cerca de una salida, pero antes de eso, dónde están mis compañeros, pensándolo bien…?"
            func.playerInteraction(sounds, "continue", text, humanStepsThread, "sonidoPasosHumano.wav", 0)
            cont = 0

            while cont < 1:
                print("¿Qué quieres hacer? \n1. Enfocarse en el pensamiento \n2. Ignorar este pensamiento y seguir avanzando")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    barThread = func.playSound(sounds, "sonidoBar.wav", 1, 1, [0, 0, -10], 1, False, "static")
                    text = "Frederic - Mierda…, ya recorde, vinimos buscando una estupida mazmorra para encontrar un huevo de araña matriarca, nos pagarian una buena cantidad en el mercado negro, demonios chicos, Veronica…, Chef… Axel… Dónde están? Creo que peleamos con algo y eso nos separó… ¿Qué era esa cosa?"
                    func.playerInteraction(sounds, "continue", text, barThread, "sonidoBar.wav", 1)

                elif decision == "2":
                    cont += 1
                    WindThread = func.playSound(sounds, "sonidoViento.wav", 1, 2, [0, 1, 0], 0, False, "static")
                    text = "Frederic - Nada, no recuerdo que paso, no tiene sentido tener pensamientos intrusivos ahora, tengo que seguir avanzando."
                    func.playerInteraction(sounds, "continue", text, WindThread, "sonidoViento.wav", 1)

            humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 1, 1, [0, -3, 0], 2, True, "static")
            text = "Dios - Frederic continúa avanzando hasta que ve a lo lejos una sala de la cueva muy diferente a lo que ya ha visto antes.\n\n \
                    Frederic - Que maldito  asco, ¿Que pise? ¿Qué es eso?, son cientos de huevos y telarañas… parece la casa de otra asquerosa araña… ENORME!!!, mierda, mierda, puta madre, ya se donde estoy…"
            slimeThread = func.playSound(sounds, "sonidoBaba.wav", 1.5, 1, [0, 0, 0], 5, False, "static")
            if slimeThread.is_alive(): sounds["sonidoBaba.wav"].stop() and slimeThread.join()
            func.playerInteraction(sounds, "continue", text, humanStepsThread, "sonidoPasosHumano.wav", 0)

            spiderStepsThread = func.playSound(sounds, "sonidoPasosJefe.wav", 1.5, 1, [0, 0, 3], 5, False, "static")
            text = "Frederic - El nido de la matriarca!!!\n\n \
                    Dios - Frédéric derrepente esucho unas pisadas cerca de el, donde inmediatamente se esconde detrás de unos huevos."
            func.playerInteraction(sounds, "continue", text, spiderStepsThread, "sonidoPasosJefe.wav", 0)
            
            spiderStepsThread = func.playSound(sounds, "sonidoPasosJefe.wav", 1.5, 1, [0, 0, 3], 5, False, "static")
            text = "Frederic - Ahora que, piensa, piensa, que se supone que haga?, ya no la esucho, pero eso no significa que no este, Yo solo no soy capaz de matar a esa cosa, debo escapar de aquí de inmediato, pero como?,\
                    parece que esa mamá araña quiere comida para sus horribles bebés, carajo. Me tengo que ir rápido, este asqueroso huevo podrido huele horrible… oh… mierda"
            func.playerInteraction(sounds, "continue", text, spiderStepsThread, "sonidoPasosJefe.wav", 0)

            roarThread = func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.2, 1, [0, 0, 3], 3, False, "static")
            text  = "Dios - Frederic sin decir una palabra, observa como entra a la habitación con un gran sigilo una enorme, horripilante, tenebrosa araña matriarca negra con manchas verdes y con unos grandes colmillos altamente venenosos."
            func.playerInteraction(sounds, "continue", text, spiderStepsThread, "sonidoMonstruoRugido.wav", 0)
            
            helpThread = func.playSound(sounds, "sonidoAyudaM.wav", 0.8, 1, [0, -2, 0], 3, False, "static")
            text = "Frederic - Qué demonios come esa araña en una cueva como esta para estar así, si me enfrento a esa cosa estaré muerto. Fue ella la que causó todo este maldito infierno, fuimos emboscados y nos atrapó, supongo que fui el \
                    único que no se llevó por alguna razón, la bastarda me dejo para morir o simplemente no quiso comerme, maldita, todos deben estar aquíFrederic - Demonios… siento algo en la espalda… Esto picha, es un bigote, color blanco, pegado a un enano calvo con cara de enojado, mmm… me parece familiar, OH JEFE! Chef!, esperame ya te voy a sacar de ahí.\n\n \
                    Dios - Fue entonces que Frederic se dio cuenta que además de haber cientos de huevos a su alrededor, también había docenas de criaturas de diferentes especies atrapadas en capullos de telaraña esperando ser alimento para las crías de arañas."
            func.playerInteraction(sounds, "continue", text, helpThread, "sonidoAyudaM.wav", 0)

            coughThread = func.playSound(sounds, "sonidoToserM.wav", 0.7, 1, [0, 1, 0], 0, False, "static")
            text = "Chef - Qu…Qué es esto? ¿Dónde estoy? Frede…ric? Dónde estamos, informarme de la situación actual, donde están los demás? \n\n \
                    Frederic - Jefecito pensé que lo perdería, los demás están atrapados pero eso no importa, primero voy a sacarte de este capullo, solo deja que te quite esto de encima. \n\n \
                    Chef - Gracias Frede…"
            func.playerInteraction(sounds, "continue", text, coughThread, "sonidoToserM.wav", 0)
            attackThread = func.playSound(sounds, "sonidoEspada.wav", 1, 1, [0, 0, 0], 1, False, "static")
            if attackThread.is_alive(): sounds["sonidoEspada.wav"].stop() and attackThread.join()

            behindThread = func.playSound(sounds, "sonidoAtrasTuyo.wav", 1, 1, [0, 0, 0], 4, False, "static")
            if behindThread.is_alive(): sounds["sonidoAtrasTuyo.wav"].stop() and behindThread.join()
            crushThread = func.playSound(sounds, "sonidoAplastado.wav", 1, 1, [0, 0, 0], 6, False, "static")
            if crushThread.is_alive(): sounds["sonidoAplastado.wav"].stop() and crushThread.join()

            shoutThread = func.playSound(sounds, "sonidoGritoMuerte.wav", 1, 1, [0, 0, 0], 7, False, "static")
            text = "Dios - Fue en ese entonces que Frederic bañado en la sangre de su amigo se da cuenta que la araña los había escuchado e inmediatamente mató a Chef para darle sus entrañas a sus crías prontas a nacer.\n\n \
                    Frederic - JEFEEEEE!!! NOOOOO!!!, MIERDA!; MIERDA!, Maldita puta araña,quieres comer, ven aquí idiota!!!, esa es…, a quien está apunto de comerse, no, no, NOOOO ESPERA!!!"
            func.playerInteraction(sounds, "continue", text, shoutThread, "sonidoGritoMuerte.wav", 1) 

            attackThread = func.playSound(sounds, "sonidoEspada.wav", 1, 1, [0, 0, 0], 1, False, "static")
            text = "Dios - En ese momento Frederic visualizo como la matriarca tenia entre su boca tiene a Veronica a punto de ser masticada por el monstruo.\n\n \
                    Frederic - NOOOO MALDITA ARAÑAS, PELEA COBARDE, SUELA A VERONICA AHHHHH"
            func.playerInteraction(sounds, "continue", text, attackThread, "sonidoEspada.wav", 0) 
        
            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Atacar a las patas. \n2. Atacar a la mandibula")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
                    if attackSpiderThread.is_alive(): sounds["sonidoAtaqueAraña.wav"].stop() and attackSpiderThread.join()
                    roarThread = func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.5, 1.5, [0, 0, 0], 3, False, "static")
                    text = "Dios - Después de un golpe certero, Frederic logra cortar 2 de sus 8 patas donde el monstruo grita del dolor cayendo al suelo momentáneamente."
                    func.playerInteraction(sounds, "continue", text, roarThread, "sonidoMonstruoRugido.wav", 0) 
                    
                    humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, -3, 0], 4, False, "static")
                    text = "Frederic - voy por ti hermosura, espero que después de esta salvada épica me des por fin una cita.\n\n \
                            Dios - Frederic inmediatamente al inmovilizar a la araña matriarca abre su mandíbula y entra ligeramente.\n\n \
                            Frederic - Ya casi te saco, ah!!! vamos.\n\n \
                            Dios - Sin embargo en ese momento la araña matriarca despierta y de un solo acto reflejo…"
                    func.playerInteraction(sounds, "continue", text, humanRunThread, "sonidoCorrerHumano.wav", 0) 
                
                elif decision == "2":
                    cont += 1
                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
                    text = "Frederic - Es todo o nada, voy a lanzar la espada, ten cuidado Veronica, Sueltala!!!\n\n \
                            Dios - Derrepente Frederic logra herirla en la mandíbula, la matriarca enojada inmediatamente de un solo acto reflejo..."
                    func.playerInteraction(sounds, "continue", text, attackSpiderThread, "sonidoAtaqueAraña.wav", 0) 

            crushThread = func.playSound(sounds, "sonidoAplastado.wav", 1, 1, [0, 0, 0], 6, False, "static")
            text = "Dios - Aunque se encontraba motivado por el auge de la batalla, Frederic recordó sus anteriores palabras, “Yo solo no soy capaz de matar a esa cosa”, las cuales lo condenaron."
            func.playerInteraction(sounds, "continue", text, crushThread, "sonidoAplastado.wav", 0) 
                
            defeatThread = func.playSound(sounds, "sonidoDerrota.wav", 1, 1, [0, 0, 0], 0, False, "static")
            text = "Dios - Completamente machacado, lamentablemente Frederic y Verónica son comidos por la araña matriarcado, esparciendo sangre y tripas por toda la sala para que sus hijos se alimenten.\n\n \
                    Final Malo(#1) - 1/2 finales)"
            func.playerInteraction(sounds, "continue", text, defeatThread, "sonidoDerrota.wav", 0) 
        
        else:
            cont += 1
            sighThread = func.playSound(sounds, "sonidoSuspiro.wav", 1, 1, [0, 0, 0], 2, False, "static")
            text = "Frederic - Ahg hay que descartar… bueno, no voy a entrar al primer camino, está demasiado oscuro y algo me dice que alguna cosa me esperaría del otro lado, voy a ir por la segunda ruta.\n\n \
                    Frederic - Mmm, esto parece un precipicio, está demasiado alto, no veo ninguna otra salida por alguna dirección, solo hacia abajo."
            func.playerInteraction(sounds, "continue", text, sighThread, "sonidoSuspiro.wav", 0)
            cont = 0

            while cont < 1:
                print("¿Qué quieres hacer? \n1. Regresar. \n2. Saltar \n:")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    spiderThread = func.playSound(sounds, "sonidoAraña.wav", 0.8, 1, [0, 0, -1], 2, False, "static")
                    if spiderThread.is_alive(): sounds["sonidoAraña.wav"].stop() and spiderThread.join()
                    text = "Frederic - Mejor me devuelvo no hay salida por este lado, tal vez por otro camino, yo pueda, AH! otra araña!!!.\n\n \
                            Dios - Inmediatamente Frederic fue atacado por una araña que lo vio entrar al lugar, logrando empujarlo hacia el precipicio, donde ambos cayeron varios metros."
                    # func.playSound(sounds, "sonidoGritoMuerte.wav", 0.8, [0, 0, 1], [0, 0, 1], 1, 0, False)
                    
                    shoutThread = func.playSound(sounds, "sonidoGritoMuerte.wav", 1, 1, [0, 0, 0], 7, False, "static")
                    text = "Frederic - Ahhhh, ¿Que hago?, ahora estoy cayendo, Carajo muerete ya. "
                    func.playerInteraction(sounds, "continue", text, shoutThread, "sonidoGritoMuerte.wav", 0) 
                    
                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
                    if spiderThread.is_alive(): sounds["sonidoAraña.wav"].stop() and spiderThread.join()
                    
                    fallThread = func.playSound(sounds, "sonidoCaida.wav", 1.2, 1, [0, 0, 0], 2, False, "static")
                    text = "Dios - Frederic rápidamente usa el cuerpo de la araña muerta para usarla como cuerpo de soporte para aguantar un poco la caída y que él no sufra lesiones graves."
                    func.playerInteraction(sounds, "continue", text, fallThread, "sonidoCaida.wav", 0) 
                    
                elif decision == "2":
                    cont += 1
                    fallThread = func.playSound(sounds, "sonidoCaida.wav", 1.2, 1, [0, 0, 0], 2, False, "static")
                    text = "Frederic - Supongo que solo queda ir hacia abajo y rogar para no morir.\n\n \
                            Dios - Fue en ese entonces que Frederic, cae un par de metros hasta que choca con varias telarañas rompiendolas unas tras otras pero logrando reducir su velocidad lo suficiente hasta caer al fondo sin daños graves."
                    func.playerInteraction(sounds, "continue", text, fallThread, "sonidoCaida.wav", 0) 
        
            humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, -3, 0], 0, False, "static")
            text = "Frederic - ¿dónde estoy?, un momento… Huevos… telarañas… demonios, esto es… un nido de arañas, entonces debe haber una matriarca cerca, debe ser la misma que causó todo este problema\n\n \
                    Frederic - Parece que cuando entramos fuimos emboscados y nos atrapó, sin embargo me debió dejar atrás por estar en ese líquido asqueroso y cubierto de lodo, todos deben estar aquí, espero que estén vivos.\n\n \
                    Dios - Rápidamente Frederic busco entre los cuerpos enredados para encontrar a sus amigos"
            func.playerInteraction(sounds, "continue", text, humanRunThread, "sonidoCorrerHumano.wav", 1) 

            attackThread = func.playSound(sounds, "sonidoEspada.wav", 1, 1, [0, 0, 0], 1, False, "static")
            text = "Frederic - Esa es?…VERONICA!, Esperame, ya te saco."
            func.playerInteraction(sounds, "continue", text, attackThread, "sonidoEspada.wav", 0) 
            
            kissThread = func.playSound(sounds, "sonidoBeso.wav", 1, 1, [0, 0, 0], 4, False, "static")
            text = "Veronica - … Freder…ic? ¿Eres tu?\n\n \
                    Frederic - Si, me alegra que estés con vida, estás un poco herida según veo, pero así solo te ves más sexy.\n\n \
                    Veronica - Quítate!!!, ni en esta situación puedes estar serio?, como sea, no tengo heridas graves, ¿vez mi mochila por algún lado?\n\n \
                    Frederic - Si, está al lado de dos hombres bestia que no lo lograron, qué pasa con ella?\n\n \
                    Veronica - Necesita que la traigas, ahi tengo una botella de maná, necesito recuperar energía para usar algún hechizo de curación."
            func.playerInteraction(sounds, "continue", text, kissThread, "sonidoBeso.wav", 0) 
            
            humanStepsThread = func.playSound(sounds, "sonidoPasosHumano.wav", 0.7, 1, [0, -3, 0], 2, False, "static")
            text = "Dios - Frederic camino hasta la mochila con cuidado de no despertar ninguna cría y llevarle la poción a Veronica."
            func.playerInteraction(sounds, "continue", text, humanStepsThread, "sonidoBeso.wav", 0)

            bottleThread = func.playSound(sounds, "sonidoBotella.wav", 1, 1, [0, 0, 0], 2, False, "static")
            text = "Frederic - Toma, bébetela toda, no dejes ni una gota, así crecerás grande y fuerte.\n\n \
                    Veronica - Callate!!! Aún estoy herida pero creo tener la suficiente energía para hacer algunos hechizos."
            func.playerInteraction(sounds, "continue", text, bottleThread, "sonidoBotella.wav", 0)
            
            healingThread = func.playSound(sounds, "sonidoHealing.wav", 1, 1, [0, 0, 0], 3, False, "static")
            text = "Dios - Inmediatamente Verónica cura a Frederic y a ella misma.\n\n \
                    Frederic - Excelente, Ahora me siento mejor, gracias preciosa, busquemos a los otros y larguémonos de aquí."
            func.playerInteraction(sounds, "continue", text, healingThread, "sonidoHealing.wav", 0)

            spiderStepsThread = func.playSound(sounds, "sonidoPasosJefe.wav", 1.5, 1, [0, 0, 3], 5, False, "static")
            if spiderStepsThread.is_alive(): sounds["sonidoPasosJefe.wav"].stop() and spiderStepsThread.join()
            
            roarThread = func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.5, 1, [0, 0, 5], 8, False, "static")
            text = "Dios - Fue en ese preciso momento que vieron a la distancia en lugares opuestos a Axel y Chef, uno entre varios huevos de araña herido y el \
                    otro atrapado en un capullo de telaraña, sin embargo, justamente en ese momento llega la araña matriarca.\n\n \
                    Veronica - Debemos salvar a ambos, pero ahora solo podemos sacar a uno… que… que hacemos Frederic?"
            func.playerInteraction(sounds, "continue", text, roarThread, "sonidoMonstruoRugido.wav", 1)
            
            doubtThread = func.playSound(sounds, "sonidoDudaFrederic.wav", 0.8, 1, [0, 0, 0], 0, False, "static")
            text = "Dios - Frederic estaba en una situación terrible donde solo tenían suficiente tiempo para sacar a uno momentáneamente.\n\n \
                    Frederic - Que hago? Chef es nuestro tranque, cocinero, jefe y maestro, puede ser de gran ayuda pero no sé si necesitamos fuerza bruta o \
                    las extrañas habilidades de Axel, al ser un asesino especializado en sigilo, puede enfocarse en ataques vitales… ¿Qué carajo hago?"
            func.playerInteraction(sounds, "continue", text, doubtThread, "sonidoDudaFrederic.wav",  0)
            
            cont = 0
            while cont < 1:
                print("¿Qué quieres hacer? \n1. Salvar a Chef. \n2. Salvar a Axel")
                decision = func.playerInteraction(sounds, "selection", "", "", "", 0)

                if decision == "1":
                    cont += 1
                    humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, 0, 0], 4, False, "static")
                    text = "Frederic - Rapido Verónica, ve por Chef, nos será de más utilidad ahora, curalo y prepárense para luchar, yo lo distraigo por ahora.\n\n \
                            Veronica - Entendido\n\n \
                            Frederic - Eh!!! Asquerosa araña ves esto¿Te gustó?."
                    func.playerInteraction(sounds, "continue", text, humanRunThread, "sonidoCorrerHumano.wav",  0)

                    roarThread = func.playSound(sounds, "sonidoMonstruoRugido.wav", 1.5, 1, [0, 0, 0], 3, False, "static")
                    if roarThread.is_alive(): sounds["sonidoMonstruoRugido.wav"].stop() and roarThread.join()
                    
                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
                    text = "Dios - En ese momento, Frederic ya recuperado y con su fuerza al máximo comienza el ataque enfocándose en sus patas y dándole el mayor tiempo posible a Verónica."
                    func.playerInteraction(sounds, "continue", text, attackSpiderThread, "sonidoAtaqueAraña.wav", 0)
                    
                    coughThread = func.playSound(sounds, "sonidoToserM.wav", 0.7, 1, [0, 1, 0], 0, False, "static")
                    text = "Chef - Ho…Hola? Veronica, vaya <sonidos de gritos>, que agradable sorpresa, puedo ver la situación, vamos hay que acabar con esa araña matriarca, está demasiado agresiva por la temporada de apareamiento. "
                    func.playerInteraction(sounds, "continue", text, coughThread, "sonidoToserM.wav", 0)

                    humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, 0, 0], 4, False, "static")
                    text = "Frederic - jajajaja Chef, te veo bien anciano, mejor ven y dame una mano antes de que lo mate yo ah!!!.\n\n \
                            Chef - Silencio Frederic, ahora te enseño cómo acabar con un monstruo de esa calidad, rápido, Veronica sigue a Frederic mientras van por atrás.\n\n \
                            Dios - Chef lider del grupo, ya recuperado utiliza un hechizo de encantamiento para atraer la atención de la araña matriarca y absorber daño para desencadenarlo en un fuerte impacto en su punto débil el abdomen mientras los demás la atacan por detrás sin preocuparse en ser objetivo de daño."
                    func.playerInteraction(sounds, "continue", text, humanRunThread, "sonidoCorrerHumano.wav",  0)
                    enchanterThread = func.playSound(sounds, "sonidoEnchanter.wav", 1.2, 1, [0, 0, 6], 1, False, "static")
                    if enchanterThread.is_alive(): sounds["sonidoEnchanter.wav"].stop() and enchanterThread.join()
                    healingThread = func.playSound(sounds, "sonidoHealing.wav", 1.2, 1, [0, 0, 0], 1, False, "static")
                    if healingThread.is_alive(): sounds["sonidoHealing.wav"].stop() and healingThread.join()
                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1.2, 1, [0, 0, 0], 1, False, "static")
                    if attackSpiderThread.is_alive(): sounds["sonidoAtaqueAraña.wav"].stop() and attackSpiderThread.join()

                elif decision == "2":
                    cont += 1
                    humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, 0, 0], 4, False, "static")
                    text = "Frederic - Rapido Verónica, ve por Chef, nos será de más utilidad ahora, curalo y prepárense para luchar, yo lo distraigo por ahora.\n\n \
                            Veronica - Entendido\n\n \
                            Frederic - Eh!!! Asquerosa araña ves esto¿Te gustó?."
                    func.playerInteraction(sounds, "continue", text, humanRunThread, "sonidoCorrerHumano.wav",  0)

                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1, 1, [0, 0, 0], 2, False, "static")
                    text = "Dios - En ese momento, Frederic ya recuperado y con su fuerza al máximo comienza el ataque enfocándose en sus patas y dándole el mayor tiempo posible a Verónica."
                    func.playerInteraction(sounds, "continue", text, attackSpiderThread, "sonidoAtaqueAraña.wav", 0)
                    
                    slimeThread = func.playSound(sounds, "sonidoBaba.wav", 1, 1, [0, 0, 0], 5, False, "static")
                    text = "Axel - Ughhh!!!, maldita sea que asco, puaj, vaya, Veronica eres tu, gracias, ¿Como te lograste liberar?\n\n \
                            Veronica - No, me salvo Frederic, pero ahora lo más importante es acabar con esa cosa."
                    func.playerInteraction(sounds, "continue", text, slimeThread, "sonidoBaba.wav", 0)
                    
                    maniacThread = func.playSound(sounds, "sonidoManiatico.wav", 1, 1, [0, 0, 0], 1.25, False, "static")
                    text = "Axel - jejejejeje ya veo, interesante, muy divertido, hagámoslo VAMOS!, OYEEE FREDERIC!"
                    func.playerInteraction(sounds, "continue", text, maniacThread, "sonidoManiatico.wav", 0)
                    
                    humanRunThread = func.playSound(sounds, "sonidoCorrerHumano.wav", 1, 1, [0, 0, 0], 4, False, "static")
                    text = "Frederic - jajajaja hijo de perra, ya estás bien, muévete ya, dame una mano.\n\n \
                            Axel - Claro, no te voy a dejar toda esta diversión, jejejejeje, ahora escuchen, Veronica, apoyanos desde atrás, Frederic la distrae mientras yo la apuñalo, el jefe dijo que en el abdomen es débil, JEJEJE.\n\n \
                            Dios - Axel psicomaniatico del grupo, enfocó su daño en el abdomen mientras Veronica golpeaba en la cabeza a la araña y engañándole con un encantamiento de espejismo, mientras Frederic golpea con gran fuerza desde el otro extremo, con la ayuda de un potenciador de Veronica.\n\n \
                            Frederic - No te emociones demasiado Axel.\n\n \
                            Axel - jejejeje!"
                    func.playerInteraction(sounds, "continue", text, humanRunThread, "sonidoCorrerHumano.wav",  0)
                    healingThread = func.playSound(sounds, "sonidoHealing.wav", 1.2, 1, [0, 0, 0], 1, False, "static")
                    if healingThread.is_alive(): sounds["sonidoHealing.wav"].stop() and healingThread.join()
                    maniacThread = func.playSound(sounds, "sonidoManiatico.wav", 1, 1, [0, 0, 0], 1.25, False, "static")
                    if maniacThread.is_alive(): sounds["sonidoManiatico.wav"].stop() and maniacThread.join()
                    attackSpiderThread = func.playSound(sounds, "sonidoAtaqueAraña.wav", 1.2, 1, [0, 0, 0], 1, False, "static")
                    if attackSpiderThread.is_alive(): sounds["sonidoAtaqueAraña.wav"].stop() and attackSpiderThread.join()

            vicgtoryThread = func.playSound(sounds, "sonidoVictoria.wav", 1, 1, [0, 0, 0], 4, False, "static")
            text = "Dios - Después de una gran lucha, logran salir con vida del encuentro, salvando de paso al otro compañero atrapado, tomando como recompensa un huevo de araña matriarcal y equipo de aventureros caídos, eliminando el resto de arañas para así lograr salir de la tumba de la seda, una de las \
                    mazmorras más engañosas por la que han pasado este grupo de mercenarios.\n\n \
                    Final Bueno(#2) - 1/2 finales"
            func.playerInteraction(sounds, "continue", text, vicgtoryThread, "sonidoVictoria.wav",  0)
    
    print("FIN")
    # Clean and close openAL
    oalQuit()

# start the game
main()
