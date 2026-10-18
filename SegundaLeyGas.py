from manim import *
import numpy as np


class SegundaLeyGas(Scene):

    def construct(self):

        # ============================================================
        # CONFIGURACIÓN
        # ============================================================

        self.camera.background_color = "#05070A"

        # ============================================================
        # TÍTULO
        # ============================================================

        titulo = Text(
            "Segunda Ley de la Termodinámica",
            font_size=34
        )

        subtitulo = Text(
            "Un gas tiende a distribuirse por todo el espacio disponible",
            font_size=20
        )

        titulo.to_edge(UP, buff=0.35)
        subtitulo.next_to(titulo, DOWN, buff=0.15)

        self.play(
            Write(titulo),
            FadeIn(subtitulo, shift=DOWN),
            run_time=1.5
        )

        # ============================================================
        # CAJA DEL GAS
        # ============================================================

        caja = Rectangle(
            width=10.5,
            height=5.2,
            stroke_width=3,
            color=WHITE
        )

        # Bajamos la caja para dejar espacio al título
        caja.shift(DOWN * 0.55)

        self.play(
            Create(caja),
            run_time=1
        )

        # ============================================================
        # ETIQUETA DEL ESTADO INICIAL
        # ============================================================

        estado = Text(
            "ESTADO INICIAL",
            font_size=22
        )

        estado.next_to(caja, DOWN, buff=0.35)

        self.play(
            FadeIn(estado),
            run_time=0.6
        )

        # ============================================================
        # PARÁMETROS DE LA CAJA
        # ============================================================

        x_min = -4.9
        x_max = 4.9

        y_min = -2.85
        y_max = 2.0

        # ============================================================
        # PARTÍCULAS
        # ============================================================

        numero_particulas = 70

        particulas = VGroup()

        posiciones = []
        velocidades = []

        np.random.seed(10)

        # ------------------------------------------------------------
        # TODAS LAS PARTÍCULAS COMIENZAN AGRUPADAS
        # ------------------------------------------------------------

        for i in range(numero_particulas):

            # Grupo inicial en la esquina superior izquierda
            x = np.random.uniform(
                x_min + 0.35,
                x_min + 2.1
            )

            y = np.random.uniform(
                y_max - 1.7,
                y_max - 0.25
            )

            posiciones.append(
                np.array([x, y, 0])
            )

            # Velocidades fuertes hacia diferentes direcciones
            angulo = np.random.uniform(
                0,
                2 * np.pi
            )

            velocidad = np.array([
                np.cos(angulo),
                np.sin(angulo),
                0
            ])

            velocidad *= np.random.uniform(
                2.0,
                3.2
            )

            velocidades.append(velocidad)

            particula = Dot(
                point=np.array([x, y, 0]),
                radius=0.055
            )

            particulas.add(particula)

        self.play(
            FadeIn(particulas),
            run_time=1
        )

        # ============================================================
        # INFORMACIÓN INICIAL
        # ============================================================

        texto_inicial = Text(
            "Muchas partículas ocupan una pequeña región",
            font_size=18
        )

        texto_inicial.next_to(
            estado,
            DOWN,
            buff=0.18
        )

        self.play(
            FadeIn(texto_inicial),
            run_time=0.7
        )

        self.wait(1)

        # ============================================================
        # QUITAMOS TEXTO INICIAL
        # ============================================================

        self.play(
            FadeOut(texto_inicial),
            FadeOut(estado),
            run_time=0.6
        )

        # ============================================================
        # NUEVA ETIQUETA
        # ============================================================

        estado_final = Text(
            "EXPANSIÓN DEL GAS",
            font_size=22
        )

        estado_final.next_to(
            caja,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(estado_final),
            run_time=0.6
        )

        # ============================================================
        # CONTADOR DE TIEMPO
        # ============================================================

        tiempo = ValueTracker(0)

        contador = always_redraw(
            lambda: Text(
                f"Tiempo: {tiempo.get_value():.1f} s",
                font_size=20
            ).to_corner(
                UR,
                buff=0.3
            )
        )

        self.add(contador)

        # ============================================================
        # FUNCIÓN DE MOVIMIENTO
        # ============================================================

        def mover_particulas(mob, dt):

            for i, particula in enumerate(mob):

                posicion = particula.get_center()

                velocidad = velocidades[i]

                nueva_posicion = (
                    posicion + velocidad * dt
                )

                # ----------------------------------------------------
                # PARED IZQUIERDA
                # ----------------------------------------------------

                if nueva_posicion[0] < x_min:

                    nueva_posicion[0] = x_min

                    velocidades[i][0] *= -1

                # ----------------------------------------------------
                # PARED DERECHA
                # ----------------------------------------------------

                if nueva_posicion[0] > x_max:

                    nueva_posicion[0] = x_max

                    velocidades[i][0] *= -1

                # ----------------------------------------------------
                # PARED INFERIOR
                # ----------------------------------------------------

                if nueva_posicion[1] < y_min:

                    nueva_posicion[1] = y_min

                    velocidades[i][1] *= -1

                # ----------------------------------------------------
                # PARED SUPERIOR
                # ----------------------------------------------------

                if nueva_posicion[1] > y_max:

                    nueva_posicion[1] = y_max

                    velocidades[i][1] *= -1

                particula.move_to(
                    nueva_posicion
                )

        particulas.add_updater(
            mover_particulas
        )

        # ============================================================
        # PRIMERA ETAPA:
        # EXPLOSIÓN / EXPANSIÓN VISIBLE
        # ============================================================

        self.play(
            tiempo.animate.set_value(3),
            run_time=3,
            rate_func=linear
        )

        # ============================================================
        # SEGUNDA ETAPA
        # ============================================================

        self.play(
            tiempo.animate.set_value(7),
            run_time=4,
            rate_func=linear
        )

        # ============================================================
        # TERCERA ETAPA
        # ============================================================

        self.play(
            tiempo.animate.set_value(12),
            run_time=5,
            rate_func=linear
        )

        # ============================================================
        # DETENER PARTÍCULAS
        # ============================================================

        particulas.remove_updater(
            mover_particulas
        )

        # ============================================================
        # MENSAJE FINAL
        # ============================================================

        self.play(
            FadeOut(estado_final),
            run_time=0.5
        )

        mensaje = Text(
            "El gas termina distribuido por todo el recipiente",
            font_size=22
        )

        mensaje.next_to(
            caja,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(mensaje),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # EXPLICACIÓN DE ENTROPÍA
        # ============================================================

        self.play(
            FadeOut(mensaje),
            run_time=0.5
        )

        explicacion = VGroup(
            Text(
                "Más configuraciones posibles",
                font_size=21
            ),
            Text(
                "→ mayor entropía",
                font_size=21
            )
        )

        explicacion.arrange(
            DOWN,
            buff=0.15
        )

        explicacion.next_to(
            caja,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(explicacion),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # ECUACIÓN
        # ============================================================

        ecuacion = MathTex(
            r"S = k_B \ln(W)",
            font_size=38
        )

        ecuacion.to_edge(
            DOWN,
            buff=0.25
        )

        self.play(
            Write(ecuacion),
            run_time=1
        )

        self.wait(3)