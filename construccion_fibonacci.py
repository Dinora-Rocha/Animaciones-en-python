from manim import *


class ConstruccionFibonacci(Scene):
    def construct(self):
        self.camera.background_color = "#07080A"

        # -------------------------------------------------------------
        # 1. TÍTULO E INTRODUCCIÓN
        # -------------------------------------------------------------
        titulo = Text("La Sucesión de Fibonacci", font_size=34, color=WHITE)
        titulo.to_edge(UP, buff=0.4)

        regla = Text(
            "Cada número nuevo nace de sumar los dos que lo preceden",
            font_size=20,
            color=GRAY_A,
        )
        regla.next_to(titulo, DOWN, buff=0.2)

        self.play(Write(titulo), FadeIn(regla), run_time=1.8)
        self.wait(0.5)

        # -------------------------------------------------------------
        # 2. CONSTRUCCIÓN ANIMADA PASO A PASO
        # -------------------------------------------------------------
        # Valores de la secuencia
        valores = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

        # Contenedor para las casillas con números
        casillas = VGroup()

        def crear_casilla(valor):
            caja = Square(
                side_length=0.9,
                stroke_color=BLUE_D,
                fill_color="#121824",
                fill_opacity=0.8,
            )
            numero = MathTex(str(valor), font_size=32, color=GOLD)
            return VGroup(caja, numero)

        # Muestra inicial: Cero y Uno
        casillas.add(crear_casilla(valores[0]))
        casillas.add(crear_casilla(valores[1]))
        casillas.arrange(RIGHT, buff=0.15)
        casillas.move_to(UP * 0.2)

        self.play(
            LaggedStart(
                FadeIn(casillas[0], shift=DOWN * 0.3),
                FadeIn(casillas[1], shift=DOWN * 0.3),
                lag_ratio=0.5,
            ),
            run_time=1.5,
        )
        self.wait(0.5)

        # Iteración sumando los elementos paso a paso
        for i in range(2, len(valores)):
            # Nueva casilla
            nueva_caja = crear_casilla(valores[i])

            # Reorganizar casillas para que queden centradas en la pantalla
            grupo_temporal = VGroup(*casillas, nueva_caja).arrange(
                RIGHT, buff=0.15
            )

            # Ajuste de escala si hay muchos elementos
            if len(grupo_temporal) > 8:
                grupo_temporal.scale_to_fit_width(12)

            grupo_temporal.move_to(UP * 0.2)

            # Marcos amarillos para señalar los dos números que se suman
            marco1 = SurroundingRectangle(casillas[i - 2], color=YELLOW, buff=0.05)
            marco2 = SurroundingRectangle(casillas[i - 1], color=YELLOW, buff=0.05)

            # Texto de la operación (ej: "0 + 1 = 1")
            v1, v2, v_suma = valores[i - 2], valores[i - 1], valores[i]
            texto_op = MathTex(
                f"{v1}",
                "+",
                f"{v2}",
                "=",
                f"{v_suma}",
                font_size=32,
                color=GREEN_B,
            ).next_to(grupo_temporal, DOWN, buff=0.6)

            self.play(Create(marco1), Create(marco2), run_time=0.4)
            self.play(Write(texto_op), run_time=0.6)

            # Aparece el nuevo número
            casillas.add(nueva_caja)
            self.play(
                Transform(
                    VGroup(*casillas[:-1]),
                    grupo_temporal[:-1],
                ),
                FadeIn(nueva_caja, shift=LEFT * 0.2),
                run_time=0.6,
            )

            self.wait(0.4)
            self.play(
                Uncreate(marco1),
                Uncreate(marco2),
                FadeOut(texto_op),
                run_time=0.3,
            )

        # -------------------------------------------------------------
        # 3. CONCLUSIÓN
        # -------------------------------------------------------------
        texto_final = Text(
            "Cero, uno, uno, dos, tres, cinco, ocho, trece, veintiuno...",
            font_size=22,
            color=GOLD,
        ).next_to(casillas, DOWN, buff=0.7)

        secuencia_infinita = Text(
            "Esa es la secuencia de Fibonacci. Y continúa indefinidamente.",
            font_size=20,
            color=WHITE,
        ).next_to(texto_final, DOWN, buff=0.3)

        self.play(Write(texto_final), run_time=2.0)
        self.play(FadeIn(secuencia_infinita), run_time=1.2)
        self.wait(3)