from manim import *
import numpy as np


class EntropiaMicroestados(Scene):

    def construct(self):

        # ============================================================
        # CONFIGURACIÓN
        # ============================================================

        self.camera.background_color = "#07080A"

        # ============================================================
        # TÍTULO
        # ============================================================

        titulo = Text(
            "¿Qué es realmente la entropía?",
            font_size=34,
            weight=BOLD
        )

        titulo.to_edge(UP, buff=0.35)

        self.play(
            Write(titulo),
            run_time=1.2
        )

        self.wait(1)

        # ============================================================
        # RECIPIENTE DEL SISTEMA
        # ============================================================

        caja = RoundedRectangle(
            width=5.0,
            height=4.6,
            corner_radius=0.15,
            stroke_color=WHITE,
            stroke_width=2
        )

        caja.shift(
            LEFT * 2.8 + DOWN * 0.25
        )

        etiqueta = Text(
            "Hielo sólido",
            font_size=25,
            color=BLUE_B
        )

        etiqueta.next_to(
            caja,
            UP,
            buff=0.25
        )

        self.play(
            Create(caja),
            Write(etiqueta),
            run_time=1
        )

        # ============================================================
        # FUNCIÓN PARA CREAR UNA MOLÉCULA DE AGUA
        # ============================================================

        def crear_molecula(pos, escala=1.0):

            oxigeno = Dot(
                pos,
                radius=0.105 * escala,
                color=RED_C
            )

            hidrogeno1 = Dot(
                pos + np.array([
                    -0.12 * escala,
                    -0.10 * escala,
                    0
                ]),
                radius=0.065 * escala,
                color=WHITE
            )

            hidrogeno2 = Dot(
                pos + np.array([
                    0.12 * escala,
                    -0.10 * escala,
                    0
                ]),
                radius=0.065 * escala,
                color=WHITE
            )

            enlace1 = Line(
                oxigeno.get_center(),
                hidrogeno1.get_center(),
                stroke_width=2,
                color=GRAY_B
            )

            enlace2 = Line(
                oxigeno.get_center(),
                hidrogeno2.get_center(),
                stroke_width=2,
                color=GRAY_B
            )

            return VGroup(
                enlace1,
                enlace2,
                oxigeno,
                hidrogeno1,
                hidrogeno2
            )

        # ============================================================
        # CREAR RED CRISTALINA DEL HIELO
        # ============================================================

        moleculas = VGroup()

        filas = 4
        columnas = 4

        posiciones = []

        for fila in range(filas):

            for columna in range(columnas):

                x = -1.75 + columna * 1.15
                y = -1.55 + fila * 1.0

                posicion = (
                    caja.get_center()
                    + np.array([x, y, 0])
                )

                posiciones.append(posicion)

                molecula = crear_molecula(
                    posicion,
                    0.9
                )

                moleculas.add(molecula)

        # ============================================================
        # APARICIÓN DE LAS MOLÉCULAS
        # ============================================================

        self.play(
            LaggedStart(
                *[
                    FadeIn(molecula)
                    for molecula in moleculas
                ],
                lag_ratio=0.06
            ),
            run_time=1.8
        )

        # ============================================================
        # ENLACES DE LA RED CRISTALINA
        # ============================================================

        enlaces_cristal = VGroup()

        # Enlaces horizontales
        for fila in range(filas):

            for columna in range(columnas - 1):

                indice1 = fila * columnas + columna
                indice2 = indice1 + 1

                linea = Line(
                    posiciones[indice1],
                    posiciones[indice2],
                    stroke_width=1,
                    color=BLUE_D
                )

                linea.set_opacity(0.45)

                enlaces_cristal.add(linea)

        # Enlaces verticales
        for fila in range(filas - 1):

            for columna in range(columnas):

                indice1 = fila * columnas + columna
                indice2 = (fila + 1) * columnas + columna

                linea = Line(
                    posiciones[indice1],
                    posiciones[indice2],
                    stroke_width=1,
                    color=BLUE_D
                )

                linea.set_opacity(0.45)

                enlaces_cristal.add(linea)

        self.play(
            Create(enlaces_cristal),
            run_time=1.5
        )

        # ============================================================
        # EXPLICACIÓN DEL HIELO
        # ============================================================

        texto = Text(
            "Las moléculas están restringidas\n"
            "a posiciones de equilibrio.",
            font_size=19,
            color=GRAY_A
        )

        texto.to_corner(
            DL,
            buff=0.45
        )

        self.play(
            FadeIn(texto),
            run_time=0.8
        )

        self.wait(1)

        # ============================================================
        # VIBRACIÓN DE LAS MOLÉCULAS
        # ============================================================

        for _ in range(3):

            animaciones = []

            for molecula in moleculas:

                desplazamiento = np.array([
                    np.random.uniform(-0.045, 0.045),
                    np.random.uniform(-0.045, 0.045),
                    0
                ])

                animaciones.append(
                    molecula.animate.shift(
                        desplazamiento
                    )
                )

            self.play(
                *animaciones,
                run_time=0.25
            )

            # Regresar a la posición anterior
            regreso = []

            for molecula in moleculas:

                regreso.append(
                    molecula.animate.shift(
                        -desplazamiento
                    )
                )

            self.play(
                *regreso,
                run_time=0.25
            )

        self.wait(0.8)

        # ============================================================
        # PANEL DE MICROESTADOS
        # ============================================================

        panel = RoundedRectangle(
            width=4.4,
            height=3.7,
            corner_radius=0.15,
            stroke_color=GRAY_B,
            stroke_width=2
        )

        panel.shift(
            RIGHT * 3.0 + DOWN * 0.3
        )

        titulo_panel = Text(
            "Microestados posibles",
            font_size=22,
            weight=BOLD
        )

        titulo_panel.next_to(
            panel,
            UP,
            buff=0.25
        )

        numero = Integer(
            16,
            font_size=42,
            color=YELLOW
        )

        numero.move_to(
            panel.get_center() + UP * 0.45
        )

        descripcion = Text(
            "formas microscópicas\n"
            "de acomodarse",
            font_size=18,
            color=GRAY_A
        )

        descripcion.next_to(
            numero,
            DOWN,
            buff=0.25
        )

        self.play(
            Create(panel),
            Write(titulo_panel),
            Write(numero),
            FadeIn(descripcion),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # DERRETIMIENTO
        # ============================================================

        texto_derretir = Text(
            "El hielo se derrite...",
            font_size=25,
            color=TEAL_B
        )

        texto_derretir.to_edge(
            DOWN,
            buff=0.45
        )

        self.play(
            FadeOut(texto),
            FadeIn(texto_derretir),
            run_time=0.8
        )

        # Desaparece la red rígida

        self.play(
            FadeOut(enlaces_cristal),
            run_time=1.3
        )

        # ============================================================
        # CAMBIO DE ETIQUETA
        # ============================================================

        nueva_etiqueta = Text(
            "Agua líquida",
            font_size=25,
            color=TEAL_B
        )

        nueva_etiqueta.next_to(
            caja,
            UP,
            buff=0.25
        )

        self.play(
            Transform(
                etiqueta,
                nueva_etiqueta
            ),
            run_time=1
        )

        # ============================================================
        # REDISTRIBUCIÓN DE LAS MOLÉCULAS
        # ============================================================

        posiciones_finales = []

        for i in range(len(moleculas)):

            nueva_posicion = (
                caja.get_center()
                + np.array([
                    np.random.uniform(-1.85, 1.85),
                    np.random.uniform(-1.75, 1.75),
                    0
                ])
            )

            posiciones_finales.append(
                nueva_posicion
            )

        animaciones = []

        for molecula, destino in zip(
            moleculas,
            posiciones_finales
        ):

            animaciones.append(
                molecula.animate.move_to(
                    destino
                )
            )

        self.play(
            LaggedStart(
                *animaciones,
                lag_ratio=0.05
            ),
            run_time=3
        )

        # ============================================================
        # MOVIMIENTO DE LAS MOLÉCULAS EN EL LÍQUIDO
        # ============================================================

        for _ in range(4):

            animaciones = []

            for molecula in moleculas:

                desplazamiento = np.array([
                    np.random.uniform(-0.14, 0.14),
                    np.random.uniform(-0.14, 0.14),
                    0
                ])

                animaciones.append(
                    molecula.animate.shift(
                        desplazamiento
                    )
                )

            self.play(
                *animaciones,
                run_time=0.45,
                rate_func=there_and_back
            )

        self.wait(1)

        # ============================================================
        # AUMENTO DE MICROESTADOS
        # ============================================================

        nuevo_numero = Integer(
            1000000,
            font_size=42,
            color=YELLOW
        )

        nuevo_numero.move_to(
            numero.get_center()
        )

        self.play(
            Transform(
                numero,
                nuevo_numero
            ),
            run_time=1.5
        )

        texto_muchos = Text(
            "Muchísimas más configuraciones\n"
            "microscópicas son posibles.",
            font_size=18,
            color=GRAY_A
        )

        texto_muchos.next_to(
            numero,
            DOWN,
            buff=0.25
        )

        self.play(
            Transform(
                descripcion,
                texto_muchos
            ),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # IDEA CENTRAL
        # ============================================================

        self.play(
            FadeOut(caja),
            FadeOut(moleculas),
            FadeOut(panel),
            FadeOut(titulo_panel),
            FadeOut(numero),
            FadeOut(descripcion),
            FadeOut(etiqueta),
            FadeOut(texto_derretir),
            FadeOut(titulo),
            run_time=1
        )

        idea = Text(
            "Más microestados  →  mayor probabilidad",
            font_size=31,
            weight=BOLD,
            color=YELLOW
        )

        self.play(
            Write(idea),
            run_time=1.5
        )

        self.wait(1.5)

        # ============================================================
        # EXPLICACIÓN CONCEPTUAL
        # ============================================================

        explicacion = Text(
            "No es que el universo 'quiera' desordenarse.\n"
            "Simplemente existen muchas más formas de estar\n"
            "en un estado con alta multiplicidad de microestados.",
            font_size=21,
            line_spacing=1.2
        )

        explicacion.next_to(
            idea,
            DOWN,
            buff=0.5
        )

        self.play(
            FadeIn(explicacion),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # ECUACIÓN DE BOLTZMANN
        # ============================================================

        self.play(
            FadeOut(idea),
            FadeOut(explicacion),
            run_time=1
        )

        formula = MathTex(
            "S = k_B \\ln W",
            font_size=55
        )

        formula.set_color_by_tex(
            "S",
            BLUE_B
        )

        formula.set_color_by_tex(
            "W",
            YELLOW
        )

        self.play(
            Write(formula),
            run_time=1.5
        )

        self.wait(1)

        # ============================================================
        # EXPLICACIÓN DE LA ECUACIÓN
        # ============================================================

        explicacion_formula = VGroup(

            Text(
                "S = entropía",
                font_size=21,
                color=BLUE_B
            ),

            Text(
                "k_B = constante de Boltzmann",
                font_size=21,
                color=GRAY_A
            ),

            Text(
                "W = número de microestados",
                font_size=21,
                color=YELLOW
            )

        )

        explicacion_formula.arrange(
            DOWN,
            buff=0.25
        )

        explicacion_formula.next_to(
            formula,
            DOWN,
            buff=0.6
        )

        self.play(
            FadeIn(explicacion_formula),
            run_time=1
        )

        self.wait(3)