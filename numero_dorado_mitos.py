from manim import *
import numpy as np


class NumeroDoradoYMitos(Scene):

    def construct(self):

        # ============================================================
        # CONFIGURACIÓN
        # ============================================================

        self.camera.background_color = "#07080A"

        DORADO = "#D9A441"
        DORADO_CLARO = "#F5D06F"
        AMARILLO = "#FFD95A"
        AZUL = "#65BCEB"
        VERDE = "#75B978"
        ROJO = "#E57373"
        ROSA = "#E7A5B8"
        BLANCO = "#F5F5F5"
        GRIS = "#A8A8A8"

        # Margen de seguridad para que nada toque los bordes
        MARGEN = 0.65

        # ============================================================
        # FUNCIONES AUXILIARES
        # ============================================================

        def titulo_seccion(texto, color=BLANCO):

            t = Text(
                texto,
                font_size=28,
                color=color
            )

            # Nunca permitir que el título sea demasiado ancho
            if t.width > 11.5:
                t.scale_to_fit_width(11.5)

            t.to_edge(
                UP,
                buff=0.45
            )

            return t

        def texto_seguro(
            texto,
            font_size=20,
            color=WHITE,
            max_width=10.5
        ):

            t = Text(
                texto,
                font_size=font_size,
                color=color
            )

            if t.width > max_width:
                t.scale_to_fit_width(max_width)

            return t

        # ============================================================
        # 1. TÍTULO
        # ============================================================

        titulo = titulo_seccion(
            "La Conexión con el Número Dorado"
        )

        linea = Line(
            LEFT * 3.4,
            RIGHT * 3.4,
            color=DORADO,
            stroke_width=2
        )

        linea.next_to(
            titulo,
            DOWN,
            buff=0.22
        )

        self.play(
            Write(titulo),
            Create(linea),
            run_time=1.4
        )

        self.wait(0.5)

        # ============================================================
        # 2. FIBONACCI
        # ============================================================

        texto_div = texto_seguro(
            "Dividir un número de Fibonacci entre el anterior",
            font_size=21,
            color=GRIS,
            max_width=9.5
        )

        texto_div.next_to(
            linea,
            DOWN,
            buff=0.38
        )

        self.play(
            FadeIn(texto_div),
            run_time=0.8
        )

        # Números Fibonacci
        fib_text = MathTex(
            r"1,\;1,\;2,\;3,\;5,\;8,\;13,\;21,\;34,\;55,\;89",
            font_size=29,
            color=WHITE
        )

        fib_text.next_to(
            texto_div,
            DOWN,
            buff=0.42
        )

        self.play(
            Write(fib_text),
            run_time=1.2
        )

        # ============================================================
        # CAJA
        # ============================================================

        caja = RoundedRectangle(
            corner_radius=0.15,
            width=4.8,
            height=1.35,
            stroke_color=DORADO,
            stroke_width=2,
            fill_color="#15100A",
            fill_opacity=0.8
        )

        caja.next_to(
            fib_text,
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(caja),
            run_time=0.6
        )

        # ============================================================
        # DIVISIONES
        # ============================================================

        divisiones = [
            (r"\frac{5}{3}", "1.666..."),
            (r"\frac{8}{5}", "1.600"),
            (r"\frac{13}{8}", "1.625"),
            (r"\frac{21}{13}", "1.615"),
            (r"\frac{34}{21}", "1.619"),
            (r"\frac{55}{34}", "1.617"),
            (r"\frac{89}{55}", "1.61818...")
        ]

        eq = MathTex(
            r"\frac{5}{3}\approx1.666...",
            font_size=37,
            color=DORADO_CLARO
        )

        eq.move_to(
            caja.get_center()
        )

        self.play(
            Write(eq),
            run_time=1
        )

        self.wait(0.4)

        for fraccion, resultado in divisiones[1:]:

            nueva = MathTex(
                fraccion + rf"\approx {resultado}",
                font_size=37,
                color=DORADO_CLARO
            )

            nueva.move_to(
                eq.get_center()
            )

            self.play(
                Transform(eq, nueva),
                run_time=0.55
            )

            self.wait(0.15)

        # ============================================================
        # PHI
        # ============================================================

        flecha = Arrow(
            caja.get_bottom(),
            caja.get_bottom() + DOWN * 0.65,
            color=DORADO,
            buff=0.08,
            stroke_width=3
        )

        self.play(
            GrowArrow(flecha),
            run_time=0.7
        )

        phi = MathTex(
            r"\phi \approx 1.6180339887\ldots",
            font_size=39,
            color=AMARILLO
        )

        phi.next_to(
            flecha,
            DOWN,
            buff=0.18
        )

        marco_phi = SurroundingRectangle(
            phi,
            color=DORADO,
            buff=0.14,
            corner_radius=0.1
        )

        nombre_phi = texto_seguro(
            "Número Áureo / Número Dorado",
            font_size=19,
            color=ROSA,
            max_width=7
        )

        nombre_phi.next_to(
            phi,
            DOWN,
            buff=0.18
        )

        self.play(
            Write(phi),
            Create(marco_phi),
            run_time=1
        )

        self.play(
            FadeIn(nombre_phi),
            run_time=0.8
        )

        self.wait(2)

        # ============================================================
        # 3. DEFINICIÓN
        # ============================================================

        self.play(
            FadeOut(
                titulo,
                linea,
                texto_div,
                fib_text,
                caja,
                eq,
                flecha,
                phi,
                marco_phi,
                nombre_phi
            ),
            run_time=0.8
        )

        titulo2 = titulo_seccion(
            "¿De dónde aparece el Número Dorado?",
            DORADO_CLARO
        )

        self.play(
            Write(titulo2),
            run_time=1
        )

        ecuacion = MathTex(
            r"\phi = \frac{1+\sqrt{5}}{2}",
            font_size=47,
            color=AMARILLO
        )

        ecuacion.move_to(
            UP * 0.45
        )

        self.play(
            Write(ecuacion),
            run_time=1.3
        )

        explicacion = texto_seguro(
            "La razón entre términos consecutivos de Fibonacci\n"
            "se aproxima cada vez más a este valor.",
            font_size=21,
            color=WHITE,
            max_width=9.5
        )

        explicacion.next_to(
            ecuacion,
            DOWN,
            buff=0.5
        )

        self.play(
            FadeIn(explicacion),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # 4. ESPIRAL ÁUREA
        # ============================================================

        self.play(
            FadeOut(
                titulo2,
                ecuacion,
                explicacion
            ),
            run_time=0.8
        )

        titulo3 = titulo_seccion(
            "La Espiral Áurea",
            AZUL
        )

        self.play(
            Write(titulo3),
            run_time=1
        )

        # ------------------------------------------------------------
        # ESPIRAL
        # ------------------------------------------------------------

        centro = DOWN * 0.35

        b = np.log(1.61803398875) / (np.pi / 2)

        puntos = []

        total = 220

        for i in range(total):

            t = (
                i / (total - 1)
            ) * 3.3 * 2 * PI

            r = (
                0.12 *
                np.exp(b * t)
            )

            x = r * np.cos(t)
            y = r * np.sin(t)

            puntos.append(
                centro +
                np.array([x, y, 0])
            )

        espiral = VMobject()

        espiral.set_points_smoothly(
            puntos
        )

        espiral.set_stroke(
            color=DORADO_CLARO,
            width=4
        )

        punto = Dot(
            centro,
            radius=0.07,
            color=AMARILLO
        )

        # La espiral queda en el centro,
        # sin tocar título ni bordes.
        self.play(
            FadeIn(punto),
            Create(espiral),
            run_time=3.5
        )

        # ============================================================
        # ECUACIÓN A LA DERECHA
        # ============================================================

        ecuacion_espiral = MathTex(
            r"r = ae^{b\theta}",
            font_size=31,
            color=AZUL
        )

        ecuacion_espiral.to_edge(
            RIGHT,
            buff=0.75
        )

        ecuacion_espiral.shift(
            UP * 0.25
        )

        texto_log = texto_seguro(
            "Espiral logarítmica",
            font_size=18,
            color=GRIS,
            max_width=3.5
        )

        texto_log.next_to(
            ecuacion_espiral,
            DOWN,
            buff=0.25
        )

        self.play(
            Write(ecuacion_espiral),
            FadeIn(texto_log),
            run_time=1
        )

        self.wait(1.5)

        # ============================================================
        # 5. NÁUTILUS
        # ============================================================

        # ------------------------------------------------------------
        # CONCHA
        # ------------------------------------------------------------

        concha_centro = LEFT * 3.0 + DOWN * 0.35

        exterior = Circle(
            radius=1.65,
            fill_color="#B77A45",
            fill_opacity=0.9,
            stroke_color="#E3B47C",
            stroke_width=3
        )

        exterior.move_to(
            concha_centro
        )

        puntos_concha = []

        for i in range(180):

            t = (
                i / 179
            ) * 2.7 * 2 * PI

            r = (
                0.10 *
                np.exp(b * t)
            )

            x = r * np.cos(t)
            y = r * np.sin(t)

            puntos_concha.append(
                concha_centro +
                np.array([x, y, 0])
            )

        espiral_concha = VMobject()

        espiral_concha.set_points_smoothly(
            puntos_concha
        )

        espiral_concha.set_stroke(
            color="#5B351F",
            width=4
        )

        concha = VGroup(
            exterior,
            espiral_concha
        )

        self.play(
            FadeIn(
                concha,
                scale=0.85
            ),
            run_time=1.3
        )

        # ------------------------------------------------------------
        # TEXTO A LA DERECHA
        # ------------------------------------------------------------

        texto_nautilus = texto_seguro(
            "El caracol náutilus presenta\n"
            "una concha con crecimiento espiral.",
            font_size=19,
            color=WHITE,
            max_width=5
        )

        texto_nautilus.to_edge(
            RIGHT,
            buff=0.65
        )

        texto_nautilus.shift(
            UP * 0.45
        )

        self.play(
            FadeIn(
                texto_nautilus,
                shift=LEFT * 0.2
            ),
            run_time=1
        )

        aclaracion = texto_seguro(
            "Se parece a una espiral áurea,\n"
            "pero no es una copia matemática exacta.",
            font_size=17,
            color=DORADO_CLARO,
            max_width=5
        )

        aclaracion.next_to(
            texto_nautilus,
            DOWN,
            buff=0.35
        )

        self.play(
            FadeIn(aclaracion),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # 6. MITOS
        # ============================================================

        self.play(
            FadeOut(
                titulo3,
                espiral,
                punto,
                ecuacion_espiral,
                texto_log,
                concha,
                texto_nautilus,
                aclaracion
            ),
            run_time=0.9
        )

        titulo_mitos = titulo_seccion(
            "Mitos y exageraciones",
            ROJO
        )

        self.play(
            Write(titulo_mitos),
            run_time=1
        )

        advertencia = texto_seguro(
            "No todo lo que tiene proporciones parecidas contiene φ.",
            font_size=20,
            color=GRIS,
            max_width=9.5
        )

        advertencia.next_to(
            titulo_mitos,
            DOWN,
            buff=0.4
        )

        self.play(
            FadeIn(advertencia),
            run_time=0.8
        )

        # ============================================================
        # LISTA DE MITOS
        # ============================================================

        mito1 = texto_seguro(
            "La Mona Lisa de Leonardo da Vinci",
            font_size=21,
            color=WHITE,
            max_width=8
        )

        mito2 = texto_seguro(
            "La arquitectura de la antigua Grecia",
            font_size=21,
            color=WHITE,
            max_width=8
        )

        mito3 = texto_seguro(
            "Proporciones \"perfectas\" del cuerpo humano",
            font_size=21,
            color=WHITE,
            max_width=8
        )

        fila1 = VGroup(
            Text("X", font_size=28, color=ROJO),
            mito1
        ).arrange(
            RIGHT,
            buff=0.3
        )

        fila2 = VGroup(
            Text("X", font_size=28, color=ROJO),
            mito2
        ).arrange(
            RIGHT,
            buff=0.3
        )

        fila3 = VGroup(
            Text("X", font_size=28, color=ROJO),
            mito3
        ).arrange(
            RIGHT,
            buff=0.3
        )

        lista = VGroup(
            fila1,
            fila2,
            fila3
        ).arrange(
            DOWN,
            buff=0.42
        )

        lista.move_to(
            DOWN * 0.25
        )

        self.play(
            LaggedStart(
                *[
                    Write(x)
                    for x in lista
                ],
                lag_ratio=0.3
            ),
            run_time=2.5
        )

        self.wait(2)

        # ============================================================
        # 7. IDEA IMPORTANTE
        # ============================================================

        self.play(
            FadeOut(
                titulo_mitos,
                advertencia,
                lista
            ),
            run_time=0.8
        )

        titulo_realidad = titulo_seccion(
            "La idea importante",
            VERDE
        )

        self.play(
            Write(titulo_realidad),
            run_time=1
        )

        realidad1 = texto_seguro(
            "Fibonacci y el Número Dorado son fenómenos matemáticos reales.",
            font_size=21,
            color=WHITE,
            max_width=10
        )

        realidad1.move_to(
            UP * 0.55
        )

        realidad2 = texto_seguro(
            "Pero no necesitamos atribuirlos a todo lo que parece bonito o proporcionado.",
            font_size=19,
            color=WHITE,
            max_width=10
        )

        realidad2.next_to(
            realidad1,
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(realidad1),
            run_time=1
        )

        self.play(
            FadeIn(realidad2),
            run_time=1
        )

        self.wait(2)

        # ============================================================
        # 8. CONCLUSIÓN
        # ============================================================

        self.play(
            FadeOut(
                titulo_realidad,
                realidad1,
                realidad2
            ),
            run_time=0.8
        )

        phi_final = MathTex(
            r"\phi \approx 1.6180339887\ldots",
            font_size=46,
            color=AMARILLO
        )

        phi_final.move_to(
            UP * 0.75
        )

        self.play(
            Write(phi_final),
            run_time=1.3
        )

        conclusion = texto_seguro(
            "La Sucesión de Fibonacci y el Número Dorado\n"
            "son fascinantes por sí mismos.",
            font_size=22,
            color=WHITE,
            max_width=9.5
        )

        conclusion.next_to(
            phi_final,
            DOWN,
            buff=0.45
        )

        self.play(
            FadeIn(conclusion),
            run_time=1.2
        )

        frase_final = texto_seguro(
            "¡No necesitan que les inventemos apariciones donde no las hay!",
            font_size=20,
            color=DORADO_CLARO,
            max_width=10
        )

        # En lugar de ponerlo pegado al borde,
        # queda separado de la parte inferior.
        frase_final.next_to(
            conclusion,
            DOWN,
            buff=0.55
        )

        self.play(
            Write(frase_final),
            run_time=1.8
        )

        self.wait(3)