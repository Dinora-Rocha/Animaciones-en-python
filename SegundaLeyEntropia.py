from manim import *
import numpy as np


class SegundaLeyEntropia(Scene):

    def construct(self):

        self.camera.background_color = "#05070A"

        # ============================================================
        # ESCENA 1 - SEGUNDA LEY
        # ============================================================

        titulo = Text(
            "La segunda ley de la termodinámica",
            font_size=32,
            weight=BOLD
        )
        titulo.to_edge(UP, buff=0.35)

        self.play(
            Write(titulo),
            run_time=1.2
        )

        formula = MathTex(
            r"\Delta S \geq 0",
            font_size=58
        )
        formula.set_color_by_tex("S", YELLOW)
        formula.move_to(UP * 0.7)

        explicacion = Text(
            "En un sistema aislado,\n"
            "la entropía total no disminuye.",
            font_size=24,
            line_spacing=1.15
        )
        explicacion.next_to(
            formula,
            DOWN,
            buff=0.45
        )

        self.play(
            Write(formula),
            run_time=1
        )

        self.play(
            FadeIn(explicacion),
            run_time=0.8
        )

        self.wait(2)

        self.play(
            FadeOut(titulo),
            FadeOut(formula),
            FadeOut(explicacion),
            run_time=0.8
        )

        # ============================================================
        # ESCENA 2 - GAS
        # ============================================================

        titulo_gas = Text(
            "Un gas se dispersa espontáneamente",
            font_size=30,
            weight=BOLD
        )
        titulo_gas.to_edge(UP, buff=0.35)

        self.play(
            Write(titulo_gas),
            run_time=1
        )

        # Recipiente
        caja = Rectangle(
            width=9.4,
            height=5.0,
            stroke_color=WHITE,
            stroke_width=2
        )
        caja.move_to(DOWN * 0.25)

        self.play(
            Create(caja),
            run_time=1
        )

        # ============================================================
        # PARTÍCULAS
        # ============================================================

        num_particulas = 50
        particulas = VGroup()

        for _ in range(num_particulas):

            x = np.random.uniform(-4.15, -2.6)
            y = np.random.uniform(-1.75, 1.3)

            particula = Dot(
                np.array([x, y, 0]),
                radius=0.045,
                color=TEAL_A
            )

            particulas.add(particula)

        self.play(
            LaggedStart(
                *[
                    FadeIn(p, scale=0.5)
                    for p in particulas
                ],
                lag_ratio=0.02
            ),
            run_time=1
        )

        # Texto inicial
        estado_inicial = Text(
            "Inicialmente, las moléculas están concentradas.",
            font_size=19,
            color=GRAY_A
        )

        estado_inicial.next_to(
            caja,
            DOWN,
            buff=0.25
        )

        self.play(
            FadeIn(estado_inicial),
            run_time=0.7
        )

        self.wait(1)

        # ============================================================
        # VELOCIDADES
        # ============================================================

        velocidades = []

        for _ in range(num_particulas):

            velocidad = np.array([
                np.random.uniform(0.35, 0.85),
                np.random.uniform(-0.65, 0.65),
                0
            ])

            velocidades.append(velocidad)

        # ============================================================
        # ACTUALIZADOR DE MOVIMIENTO
        # ============================================================

        def mover_gas(mob, dt):

            for i, particula in enumerate(mob):

                posicion = particula.get_center()

                nueva_posicion = (
                    posicion
                    + velocidades[i] * dt
                )

                # Pared izquierda
                if nueva_posicion[0] <= -4.55:
                    nueva_posicion[0] = -4.55
                    velocidades[i][0] = abs(
                        velocidades[i][0]
                    )

                # Pared derecha
                if nueva_posicion[0] >= 4.55:
                    nueva_posicion[0] = 4.55
                    velocidades[i][0] = -abs(
                        velocidades[i][0]
                    )

                # Pared inferior
                if nueva_posicion[1] <= -2.7:
                    nueva_posicion[1] = -2.7
                    velocidades[i][1] = abs(
                        velocidades[i][1]
                    )

                # Pared superior
                if nueva_posicion[1] >= 2.2:
                    nueva_posicion[1] = 2.2
                    velocidades[i][1] = -abs(
                        velocidades[i][1]
                    )

                particula.move_to(
                    nueva_posicion
                )

        particulas.add_updater(
            mover_gas
        )

        # ============================================================
        # CONTADOR
        # ============================================================

        tiempo = ValueTracker(0)

        contador = always_redraw(
            lambda: Text(
                f"Tiempo: {tiempo.get_value():.1f}",
                font_size=19,
                color=GRAY_A
            ).to_corner(
                UR,
                buff=0.3
            )
        )

        self.add(contador)

        # ============================================================
        # DISPERSIÓN
        # ============================================================

        self.play(
            tiempo.animate.set_value(10),
            run_time=10,
            rate_func=linear
        )

        particulas.remove_updater(
            mover_gas
        )

        self.wait(1)

        # ============================================================
        # TEXTO FINAL DEL GAS
        # ============================================================

        estado_final = Text(
            "Después de un tiempo, las moléculas ocupan todo el espacio.",
            font_size=19,
            color=GRAY_A
        )

        estado_final.next_to(
            caja,
            DOWN,
            buff=0.25
        )

        self.play(
            FadeOut(estado_inicial),
            FadeIn(estado_final),
            run_time=0.8
        )

        self.wait(2)

        explicacion_gas = Text(
            "Hay muchas más configuraciones dispersas\n"
            "que configuraciones completamente concentradas.",
            font_size=20,
            line_spacing=1.15,
            color=YELLOW
        )

        explicacion_gas.move_to(
            DOWN * 3.0
        )

        self.play(
            FadeIn(explicacion_gas),
            run_time=0.8
        )

        self.wait(2)

        # Limpiar
        self.play(
            FadeOut(caja),
            FadeOut(particulas),
            FadeOut(contador),
            FadeOut(estado_final),
            FadeOut(explicacion_gas),
            FadeOut(titulo_gas),
            run_time=1
        )

        # ============================================================
        # ESCENA 3 - FLECHA DEL TIEMPO
        # ============================================================

        titulo_tiempo = Text(
            "¿Por qué el tiempo parece tener una dirección?",
            font_size=29,
            weight=BOLD
        )
        titulo_tiempo.to_edge(UP, buff=0.35)

        self.play(
            Write(titulo_tiempo),
            run_time=1
        )

        # Línea temporal
        linea = Arrow(
            LEFT * 4.5,
            RIGHT * 4.5,
            buff=0,
            stroke_width=5
        )
        linea.move_to(DOWN * 1.2)

        pasado = Text(
            "PASADO",
            font_size=19,
            color=BLUE_B
        )
        pasado.next_to(
            linea.get_start(),
            DOWN,
            buff=0.25
        )

        futuro = Text(
            "FUTURO",
            font_size=19,
            color=YELLOW
        )
        futuro.next_to(
            linea.get_end(),
            DOWN,
            buff=0.25
        )

        self.play(
            Create(linea),
            FadeIn(pasado),
            FadeIn(futuro),
            run_time=1.2
        )

        # ============================================================
        # HUEVO INTACTO
        # ============================================================

        huevo = Ellipse(
            width=1.25,
            height=1.65,
            color=WHITE,
            stroke_width=3
        )

        huevo.move_to(
            LEFT * 3.2 + UP * 0.45
        )

        etiqueta_huevo = Text(
            "Estado ordenado",
            font_size=19,
            color=BLUE_B
        )

        etiqueta_huevo.next_to(
            huevo,
            UP,
            buff=0.25
        )

        self.play(
            Create(huevo),
            FadeIn(etiqueta_huevo),
            run_time=1
        )

        self.wait(1.5)

        # ============================================================
        # TRANSICIÓN
        # ============================================================

        self.play(
            FadeOut(huevo),
            FadeOut(etiqueta_huevo),
            run_time=0.7
        )

        # ============================================================
        # HUEVO ROTO
        # ============================================================

        fragmentos = VGroup()

        posiciones_fragmentos = [
            [2.6, 0.7, 0],
            [3.2, 0.2, 0],
            [3.8, 0.65, 0],
            [4.4, 0.05, 0],
            [3.0, -0.55, 0],
            [3.9, -0.65, 0]
        ]

        for posicion in posiciones_fragmentos:

            fragmento = Arc(
                start_angle=0,
                angle=PI * 0.65,
                radius=0.22,
                color=WHITE,
                stroke_width=3
            )

            fragmento.move_to(
                np.array(posicion)
            )

            fragmentos.add(fragmento)

        self.play(
            LaggedStart(
                *[
                    FadeIn(f, scale=0.4)
                    for f in fragmentos
                ],
                lag_ratio=0.08
            ),
            run_time=1.2
        )

        etiqueta_roto = Text(
            "Muchas configuraciones posibles",
            font_size=18,
            color=YELLOW
        )

        etiqueta_roto.next_to(
            fragmentos,
            UP,
            buff=0.25
        )

        self.play(
            FadeIn(etiqueta_roto),
            run_time=0.7
        )

        # ============================================================
        # CURVA DE ENTROPÍA
        # ============================================================

        curva = VMobject(
            color=YELLOW,
            stroke_width=4
        )

        puntos = [
            LEFT * 3.2 + DOWN * 0.45,
            LEFT * 1.7 + DOWN * 0.2,
            ORIGIN + UP * 0.1,
            RIGHT * 1.7 + UP * 0.5,
            RIGHT * 3.4 + UP * 0.9
        ]

        curva.set_points_smoothly(
            [
                np.array(p)
                for p in puntos
            ]
        )

        self.play(
            Create(curva),
            run_time=2
        )

        etiqueta_s = MathTex(
            "S",
            font_size=38,
            color=YELLOW
        )

        etiqueta_s.next_to(
            curva,
            UP,
            buff=0.15
        )

        self.play(
            FadeIn(etiqueta_s),
            run_time=0.5
        )

        explicacion_tiempo = Text(
            "La entropía aumenta estadísticamente hacia el futuro.",
            font_size=20,
            color=GRAY_A
        )

        explicacion_tiempo.to_edge(
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(explicacion_tiempo),
            run_time=0.8
        )

        self.wait(3)

        # Limpiar
        self.play(
            FadeOut(titulo_tiempo),
            FadeOut(linea),
            FadeOut(pasado),
            FadeOut(futuro),
            FadeOut(fragmentos),
            FadeOut(etiqueta_roto),
            FadeOut(curva),
            FadeOut(etiqueta_s),
            FadeOut(explicacion_tiempo),
            run_time=1
        )

        # ============================================================
        # ESCENA 4 - MUERTE TÉRMICA
        # ============================================================

        titulo_final = Text(
            "El destino final del universo",
            font_size=31,
            weight=BOLD
        )
        titulo_final.to_edge(
            UP,
            buff=0.35
        )

        self.play(
            Write(titulo_final),
            run_time=1
        )

        # ============================================================
        # UNIVERSO CON ESTRELLAS
        # ============================================================

        estrellas = VGroup()

        posiciones_estrellas = [
            [-4.0, 1.5, 0],
            [-2.0, 0.7, 0],
            [0.0, 1.6, 0],
            [2.0, 0.8, 0],
            [4.0, 1.5, 0],
            [-3.0, -1.1, 0],
            [-0.5, -0.8, 0],
            [2.0, -1.4, 0],
            [4.0, -0.7, 0]
        ]

        for posicion in posiciones_estrellas:

            estrella = Star(
                n=5,
                outer_radius=0.23,
                inner_radius=0.10,
                color=YELLOW
            )

            estrella.move_to(
                np.array(posicion)
            )

            estrellas.add(estrella)

        self.play(
            LaggedStart(
                *[
                    FadeIn(e, scale=0.5)
                    for e in estrellas
                ],
                lag_ratio=0.1
            ),
            run_time=1.5
        )

        texto_universo = Text(
            "Un universo con estructuras y fuentes de energía",
            font_size=20,
            color=GRAY_A
        )

        texto_universo.to_edge(
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(texto_universo),
            run_time=0.8
        )

        self.wait(2)

        # ============================================================
        # DISPERSIÓN
        # ============================================================

        destinos = []

        for _ in estrellas:

            destinos.append(
                np.array([
                    np.random.uniform(-5, 5),
                    np.random.uniform(-2.4, 2.3),
                    0
                ])
            )

        animaciones = []

        for estrella, destino in zip(
            estrellas,
            destinos
        ):

            animaciones.append(
                estrella.animate
                .scale(0.45)
                .move_to(destino)
            )

        self.play(
            *animaciones,
            run_time=4,
            rate_func=smooth
        )

        # ============================================================
        # EQUILIBRIO
        # ============================================================

        self.play(
            FadeOut(texto_universo),
            run_time=0.7
        )

        equilibrio = Text(
            "Equilibrio térmico",
            font_size=27,
            color=TEAL_B,
            weight=BOLD
        )

        equilibrio.move_to(
            UP * 0.45
        )

        self.play(
            FadeIn(equilibrio),
            run_time=1
        )

        descripcion_equilibrio = Text(
            "La energía estaría distribuida de manera muy uniforme.",
            font_size=20,
            color=GRAY_A
        )

        descripcion_equilibrio.next_to(
            equilibrio,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(descripcion_equilibrio),
            run_time=0.8
        )

        self.wait(2)

        # ============================================================
        # MUERTE TÉRMICA
        # ============================================================

        muerte = Text(
            "Muerte térmica del universo",
            font_size=30,
            weight=BOLD,
            color=YELLOW
        )

        muerte.move_to(
            UP * 0.45
        )

        descripcion_muerte = Text(
            "Un escenario teórico de máxima entropía.\n"
            "Ya no habría energía disponible para realizar trabajo útil.",
            font_size=19,
            color=GRAY_A,
            line_spacing=1.15
        )

        descripcion_muerte.next_to(
            muerte,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeOut(equilibrio),
            FadeOut(descripcion_equilibrio),
            FadeIn(muerte),
            FadeIn(descripcion_muerte),
            run_time=1.2
        )

        self.wait(3)

        # ============================================================
        # ACLARACIÓN CIENTÍFICA
        # ============================================================

        aclaracion = Text(
            "Es una extrapolación teórica a escalas de tiempo extremas.",
            font_size=18,
            color=GRAY_B
        )

        aclaracion.to_edge(
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(aclaracion),
            run_time=0.8
        )

        self.wait(3)

        # ============================================================
        # FINAL
        # ============================================================

        frase_final = Text(
            "La entropía marca una dirección estadística del cambio.",
            font_size=24,
            color=WHITE,
            weight=BOLD
        )

        self.play(
            FadeOut(estrellas),
            FadeOut(titulo_final),
            FadeOut(muerte),
            FadeOut(descripcion_muerte),
            FadeOut(aclaracion),
            run_time=1
        )

        self.play(
            FadeIn(frase_final),
            run_time=1.2
        )

        self.wait(3)